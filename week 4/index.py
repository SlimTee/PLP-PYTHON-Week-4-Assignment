def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            # Read the content of the file
            content = infile.readlines()
        
        # Modify the content (for example, convert to uppercase)
        modified_content = [line.upper() for line in content]

        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"Modified content written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read or write to the file.")

# Ask the user for the input filename and output filename
input_file = input("Enter the name of the file to read from: ")
output_file = input("Enter the name of the file to write to: ")

# Call the function with user-provided filenames
read_and_modify_file(input_file, output_file)
