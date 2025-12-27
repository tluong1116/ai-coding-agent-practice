import os
import subprocess

from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute a python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path of the python script to run (e.g., 'main.py' or 'script/helper.py').",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="The list of command line argument (optional) to pass to the function to run"
            )
        },
        required=["file_path"] # Tells the AI it MUST provide this
    ),
)

def run_python_file(working_directory, file_path, args=None):
    try:    
        abs_working_directory = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_directory, file_path))

        valid_file_path = os.path.commonpath([abs_working_directory,abs_file_path]) == abs_working_directory
        # check
        if not valid_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not abs_file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", abs_file_path,]
        if args:
            command.extend(args)

        output = subprocess.run(command,
                       text=True,
                       capture_output=True,
                       timeout=30,
                       cwd=abs_working_directory)
        
        if output.returncode != 0:
            output_string = f"Process exited with code {output.returncode}"
        elif output.stdout is None or output.stderr is None:
            output_string = "No output produced"
        else:
            output_string = f"STDOUT: {output.stdout}\nSTDERR: {output.stderr}"

        return output_string     

    except Exception as e:
        return(f"Error: executing Python file: {e}")
