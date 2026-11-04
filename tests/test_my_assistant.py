from my_assistant import LashAssistant
from my_tool import AppointmentLookup


def make_assistant():
    availability = {
        "monday": ["4:00 PM"],
        "wednesday": ["10:00 AM"],
        "friday": ["10:00 AM", "4:00 PM"],
    }

    tool = AppointmentLookup(availability)
    return LashAssistant("Lumi", tool)


def test_tool_finds_day():
    assistant = make_assistant()

    assert assistant.tool.find_day("What is open on Friday?") == "friday"


def test_availability_question_uses_tool():
    assistant = make_assistant()

    reply = assistant.respond("What is available on Monday?")

    assert "4:00 PM" in reply


def test_missing_day_gets_helpful_reply():
    assistant = make_assistant()

    reply = assistant.respond("What appointments are available?")

    assert "Which day" in reply


def test_booking_request_goes_to_person():
    assistant = make_assistant()

    reply = assistant.respond("Please book me for Monday")

    assert "person" in reply


def test_unknown_request_gets_safe_reply():
    assistant = make_assistant()

    reply = assistant.respond("What is the weather?")

    assert "not sure" in reply


def test_history_records_both_messages():
    assistant = make_assistant()

    assistant.respond("hello")

    assert len(assistant.history) == 2
    assert assistant.history[0]["role"] == "user"
    assert assistant.history[1]["role"] == "assistant"
