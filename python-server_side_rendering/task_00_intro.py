#!/usr/bin/python3
"""Module for generating invitation files from a template."""


def generate_invitations(template, attendees):
    """Generate personalized invitation files."""

    # Validate template type
    if not isinstance(template, str):
        print("Error: template must be a string")
        return

    # Validate attendees type
    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees
    ):
        print("Error: attendees must be a list of dictionaries")
        return

    # Check if template is empty
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        output = template

        # Replace placeholders with attendee data
        placeholders = [
            "name",
            "event_title",
            "event_date",
            "event_location"
        ]

        for key in placeholders:
            value = attendee.get(key)

            if value is None:
                value = "N/A"

            output = output.replace("{" + key + "}", str(value))

        # Write output to file
        filename = "output_{}.txt".format(index)

        try:
            with open(filename, "w") as file:
                file.write(output)
        except Exception as e:
            print("Error writing file {}: {}".format(filename, e))