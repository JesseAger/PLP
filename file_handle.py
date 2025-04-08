def read_and_modify_file():
    filename = input("Enter the filename to read from: ")

    try:
        # Try opening and reading the file
        with open(filename, 'r') as file:
            contents = file.read()
        
        # Convert to uppercase
        modified_contents = contents.upper()

        # Create a new file
        new_filename = "modified_" + filename

        with open(new_filename, 'w') as new_file:
            new_file.write(modified_contents)

        print(f"Success! Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except IOError:
        print("Error: File could not be read or written. Please check permissions or file status.")

# Call function
read_and_modify_file()
