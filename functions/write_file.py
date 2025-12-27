import os

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.normpath(os.path.join(abs_working_directory, file_path))

    valid_file_path = os.path.commonpath([abs_working_directory,abs_file_path]) == abs_working_directory

    if not valid_file_path:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'