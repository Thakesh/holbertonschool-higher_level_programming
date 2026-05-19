#!/usr/bin/python3
import importlib.util
import os

if __name__ == "__main__":
    path = os.path.join(os.path.dirname(__file__), "hidden_4.pyc")

    spec = importlib.util.spec_from_file_location("hidden_4", path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)