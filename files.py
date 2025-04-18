#read and write file code
def read_and_write_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
        
        modified_content = content.upper()  #  modification: Converting the text to uppercase

        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"Modified content written to {output_filename}")

    except Exception as e:
        print(f"Error: {e}")

# Example 
input_filename = "input.txt"
output_filename = "output.txt"
read_and_write_file(input_filename, output_filename)

#Error handling
def handle_file_errors():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:\n", content)

    except FileNotFoundError:
        print(f"Error: {filename} does not exist.")
    except IOError:
        print(f"Error: Unable to read {filename}.")
    except Exception as e:
        print(f"Unexpected error: {e}")

handle_file_errors()

