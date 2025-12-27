import os

def write_file(working_directory, file_path, content):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_directory, file_path))

        valid_file_path = os.path.commonpath([abs_working_directory,abs_file_path]) == abs_working_directory

        # Check
        if not valid_file_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(abs_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        # Extract the Parent Directory and create it if needed
        parent_dir = os.path.dirname(abs_file_path)
        os.makedirs(parent_dir, exist_ok=True)

        # Write to file
        with open(abs_file_path,'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return(f"Error: An unexpected error occurred: {e}")


write_file('temp','test.txt','abcxyz this is a test')

write_file('temp','test2/test2.txt','abcxyz this is a test2')

