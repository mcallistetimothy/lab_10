class AppointmentLookup:
    """Look up available lash appointment times."""

    def __init__(self, availability):
        self.availability = availability

    def find_day(self, text):
        """Return the first known day mentioned in the text."""
        text = text.lower()

        for day in self.availability:
            if day.lower() in text:
                return day

        return None

    def times_for(self, day):
        """Return the available times for a day."""
        return self.availability.get(day)
