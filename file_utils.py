import json
import os

def load_data(filename):
    """
    Loads JSON data safely from a file.
    Returns an empty list if file doesn't exist, is empty, or corrupted.
    """
    try:
        if not os.path.exists(filename):
            return []  # File not present — start fresh

        with open(filename, 'r') as f:
            content = f.read().strip()
            if not content:
                return []  # Empty file — just return []

            return json.loads(content)

    except json.JSONDecodeError:
        print(f"\033[1;91m❌ Warning: {filename} was corrupted or invalid. Recreating file.\033[0m\n")
        save_data(filename, [])
        return []

    except Exception as e:
        print(f"\033[1;91m❌ Error while reading {filename}: {e}\033[0m\n")
        return []


def save_data(filename, data):
    """
    Saves data safely into a JSON file with proper formatting.
    """
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"\033[1;91m❌ Error saving {filename}: {e}\033[0m\n")