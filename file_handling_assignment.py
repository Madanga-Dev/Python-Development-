# File Creation
def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line of text\n")
    except PermissionError:
        print("Permission denied. Unable to create file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("File created successfully.")

# File Reading and Display
def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Content of my_file.txt:")
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File Appending
def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("Appending line 2\n")
            file.write("Appending line 3\n")
    except PermissionError:
        print("Permission denied. Unable to append to file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("Content appended to file successfully.")

# Error Handling
try:
    create_file()
    read_file()
    append_file()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Script execution completed.")
