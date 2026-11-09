# my_main.py
# Author: Maliyah Timothy

from my_assistant import LashAssistant
from my_tool import AppointmentLookup
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are Lumi, a helpful lash appointment assistant.
Answer in one short sentence.
Clients should arrive with clean lashes and no eye makeup.
Hybrid sets combine classic lashes with volume fans.
Only state facts that appear in these instructions.
If you do not know, say you do not know and offer to pass the customer to a person."""

availability = {
    "monday": ["4:00 PM"],
    "wednesday": ["10:00 AM"],
    "friday": ["10:00 AM", "4:00 PM"],
}

tool = AppointmentLookup(availability)
model = OllamaModel(MODEL_NAME)
assistant = LashAssistant("Lumi", INSTRUCTIONS, tool, model)

print("Type a message, or type quit to stop.")

while True:
    message = input("You: ")

    if message.lower() == "quit":
        break

    reply = assistant.respond(message)
    print(f"{assistant.name}: {reply}")

print(f"Messages in this conversation: {len(assistant.history)}")
