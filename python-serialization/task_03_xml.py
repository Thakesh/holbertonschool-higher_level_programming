#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): Dictionary to serialize.
        filename (str): Output XML filename.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): Input XML filename.

    Returns:
        dict: Dictionary reconstructed from the XML file.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}

    for child in root:
        value = child.text

        # Attempt basic type conversion
        if value == "True":
            value = True
        elif value == "False":
            value = False
        else:
            try:
                value = int(value)
            except (ValueError, TypeError):
                try:
                    value = float(value)
                except (ValueError, TypeError):
                    pass

        result[child.tag] = value

    return result