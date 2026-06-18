#!/usr/bin/python3
def generate_invitations(template_file, data_list):
    try:
        # Check if data list is valid
        if not isinstance(data_list, list):
            print("Error: data_list must be a list.")
            return

        # Read template
        with open(template_file, "r", encoding="utf-8") as file:
            template = file.read()

        # Check if template is empty
        if not template.strip():
            print("Error: Template file is empty.")
            return

        # Generate invitation files
        for index, data in enumerate(data_list, start=1):
            try:
                if not isinstance(data, dict):
                    print(f"Warning: Entry {index} is not a dictionary. Skipping.")
                    continue

                invitation = template.format(**data)

                output_filename = f"output_{index}.txt"

                with open(output_filename, "w", encoding="utf-8") as output_file:
                    output_file.write(invitation)

            except KeyError as missing_key:
                print(
                    f"Warning: Missing placeholder value "
                    f"'{missing_key.args[0]}' in entry {index}. Skipping."
                )

    except FileNotFoundError:
        print(f"Error: Template file '{template_file}' not found.")

    except Exception as e:
        print(f"Unexpected error: {e}")