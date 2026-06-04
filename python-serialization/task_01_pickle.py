#!/usr/bin/python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object and save it to a file.
        Returns None if an error occurs.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file and return it.
        Returns None if the file does not exist or is malformed.
        """
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                return obj
        except (FileNotFoundError, OSError, pickle.PickleError, EOFError):
            return None
