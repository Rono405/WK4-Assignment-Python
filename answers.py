# Question 1
# Readsa nd writes a  modifed verson of a file
def modify_file(input_filename, output_filename):
    try:
        # Read from the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File has been successfully modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = input("Enter the name of the file to read from: ")
output_file = input("Enter the name of the file to write to: ")
modify_file(input_file, output_file)

# Question 2
# asks the user for a filename and handle errors if it doesn’t exist or can’t be read
def read_user_file():
    filename = input("Enter the filename you want to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile content:\n")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_user_file()

# END OF ASSIGNMENT