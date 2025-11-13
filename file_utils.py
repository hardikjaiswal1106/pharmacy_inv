import json
import os

def load_data(filename):

    try:
        if not os.path.exists(filename):
            return []  

        with open(filename, 'r') as f:
            content = f.read().strip()
            if not content:
                return [] 

            return json.loads(content)

    except json.JSONDecodeError:
        print(f"\033[1;91m❌ Warning: {filename} was corrupted or invalid. Recreating file.\033[0m\n")
        save_data(filename, [])
        return []

    except Exception as e:
        print(f"\033[1;91m❌ Error while reading {filename}: {e}\033[0m\n")
        return []


def save_data(filename, data):
   
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"\033[1;91m❌ Error saving {filename}: {e}\033[0m\n")