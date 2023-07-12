
#!/usr/bin/python3
"""write_file module.

Contains a function that writes a text file.
"""

def write_file(filename="", text=""):
    """function that writes a string to a text file and return the number
    of characters written"""

    with open(filename, 'w') as f:
        return f.write(text)
