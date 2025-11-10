import os

from config import MAX_CHARS
#from wsgiref import types
from google.genai import types

def get_files_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'error: "{file_path}" is not in the working directory'
    if not os.path.isfile(abs_file_path):
        return f'error: "{file_path}" is not a file'
    
    file_content_string = ""
    try:
            
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string += (
                    f'[...file "{file_path}" truncated at 10000 characters]'
                )
        return file_content_string
    except Exception as e:
        return f'exception reading file: {e}'
    
    
schema_get_files_content = types.FunctionDeclaration(
    name="get_files_content",
    description="Gets the contents of the given file as a string, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path to get content from, relative to the working directory. If not provided, gets content from the working directory itself.",
            ),
        },
    ),
)