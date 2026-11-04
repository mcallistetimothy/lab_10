from my_assistant import LashAssistant
from my_tool import AppointmentLookup

availability = {
    "monday": ["4:00 PM"],
    "wednesday": ["10:00 AM"],
    "friday": ["10:00 AM", "4:00 PM"],
}

tool = AppointmentLookup(availability)
assistant = LashAssistant("Lumi", tool)

print("Type a message, or type quit to stop.")

while True:
    message = input("You: ")

    if message.lower() == "quit":
        break

    reply = assistant.respond(message)
    print(f"{assistant.name}: {reply}")

print(f"Messages in this conversation: {len(assistant.history)}")
