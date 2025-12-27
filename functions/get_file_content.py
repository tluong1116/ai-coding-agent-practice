import os
from config import MAX_CHARS
#MAX_CHARS = 10_000

def get_file_content(working_directory, file_path):
    try:    
        abs_working_directory = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_directory, file_path))

        valid_file_path = os.path.commonpath([abs_working_directory,abs_file_path]) == abs_working_directory

        if not valid_file_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(abs_file_path) as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            
        return content
    except Exception as e:
        return(f"Error: An unexpected error occurred: {e}")




