#!/usr/bin/python3
import re

def generate_invitations(template, attendees):
    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    if not isinstance(attendees, list):
        print("Invalid data format.")
        return

    placeholders = re.findall(r"\{(\w+)\}", template)

    for i, attendee in enumerate(attendees, start=1):
        content = template

        for field in placeholders:
            value = attendee.get(field, "N/A")

            if value is None:
                value = "N/A"

            content = content.replace(f"{{{field}}}", str(value))

        with open(f"output_{i}.txt", "w", encoding="utf-8") as file:
            file.write(content)
