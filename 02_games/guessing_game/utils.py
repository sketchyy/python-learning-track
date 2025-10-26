import os

def read_highscore(file_path):
    """Reads the current highscore if available."""
    if not os.path.exists(file_path):
        return None, None
    with open(file_path, "r") as file:
        content = file.read().strip()
        if ":" in content:
            name, value = content.split(":")
            return name, int(value)
    return None, None

def write_highscore(file_path, name, score):
    """Writes a new highscore to file."""
    with open(file_path, "w") as file:
        file.write(f"{name}:{score}")

def clear_highscore(file_path):
    """Deletes the highscore file if it exists."""
    if os.path.exists(file_path):
        os.remove(file_path)

def clear_screen():
    """Clears the terminal screen."""
    os.system("clear" if os.name == "posix" else "cls")
