import os


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template.

    Args:
        template (str): Path to template file.
        attendees (list): List of dictionaries with values.

    Returns:
        None
    """

    # ---- Error handling ----
    if not isinstance(template, str):
        print("Error: template must be a string")
        return

    if not isinstance(attendees, list):
        print("Error: attendees must be a list")
        return

    if not attendees:
        print("No data provided")
        return

    try:
        with open(template, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: template file '{template}' not found")
        return
    except Exception as e:
        print(f"Error: cannot read template - {e}")
        return

    # ---- Generate files ----
    for i, person in enumerate(attendees, start=1):
        if not isinstance(person, dict):
            print(f"Skipping invalid entry at index {i}")
            continue

        output = content

        for key, value in person.items():
            placeholder = "{{" + key + "}}"
            output = output.replace(placeholder, str(value))

        filename = f"output_{i}.txt"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(output)
        except Exception as e:
            print(f"Error writing {filename}: {e}")
