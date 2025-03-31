# START

def modify_content(content):
    """Modify the content"""
    return content.upper()

def read_and_write_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
        
        modified_content = modify_content(content)

        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}' successfully!")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_write_file()

# THE END
