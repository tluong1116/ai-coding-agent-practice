import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    try:
        full_wd = os.path.abspath(working_directory)
        #print(full_wd)
        target_dir = os.path.normpath(os.path.join(full_wd, directory))
        #print(target_dir)
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        # Will be True or False
        valid_target_dir = os.path.commonpath([full_wd,target_dir]) == full_wd
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        result_list = []
        for item in os.scandir(path = target_dir):
            item_path = os.path.normpath(os.path.join(target_dir,item))
            item_name = os.path.basename(item_path)
            is_dir = os.path.isdir(item_path)
            file_size = os.path.getsize(item_path)
            result_list.append(f"- {item_name} file_size={file_size}, is_dir={os.path.isdir(item_path)}")

        return '\n'.join(result_list)
    except Exception as e:
        return(f"An unexpected error occurred: {e}")



#get_files_info('Videos','lectures')

# my_path = '/home/tluong/Videos/lectures'
# for item in os.scandir(path = my_path):
#     item_path = os.path.normpath(os.path.join(my_path,item))
#     item_name = os.path.basename(item_path)
#     file_size = os.path.getsize(item_path)
#     print(f"{item_name} file_size={file_size}, is_dir={os.path.isdir(item_path)}")