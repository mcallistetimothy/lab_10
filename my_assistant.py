from email.mime import text


HANDOFF_WORDS = ["book", "cancel", "reschedule", "change"]


class LashAssistant:
    """A mock assistant that answers lash appointment availability questions."""

    def __init__(self, name, instructions, tool, model):
        """Set up the assistant with instructions, an availability tool, and a model."""
        self.name = name
        self.instructions = instructions
        self.tool = tool
        self.model = model
        self.history = []

    def respond(self, user_message):
        """Record the conversation and return a reply."""
        self.history.append({"role": "user", "content": user_message})

        reply = self.choose_reply(user_message)

        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a response based on simple rules."""
        text = user_message.lower()

        for word in HANDOFF_WORDS:
            if word in text:
                return (
                    "I can't book or change appointments. "
                    "I'm passing you to a person who can update the schedule."
                )

        if "available" in text or "open" in text or "appointment" in text:
            return self.availability_reply(user_message)

        return self.model_reply()

    def model_reply(self):
        """Ask the model for a reply and provide a safe fallback."""
        reply = self.model.reply(self.instructions, self.history)

        if reply is None:
            return "Sorry, I can't answer that right now. Please try again in a moment."

        return reply

    def availability_reply(self, user_message):
        """Use the tool to answer an availability question."""
        day = self.tool.find_day(user_message)

        if day is None:
            return "Which day would you like me to check?"

        times = self.tool.times_for(day)

        if not times:
            return f"There are no available appointments on {day}."

        return f"Available times on {day}: {', '.join(times)}."
