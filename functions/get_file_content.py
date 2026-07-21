import os 

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads and returns the content of a specified file relative to the working directory, truncated if it exceeds the maximum character limit",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to read, relative to the working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}

def get_file_content(working_directory: str, file_path: str) -> str:
    abs_path_for_dir = os.path.abspath(working_directory) #as var implies, this line gets us the absulute path for a directory
    abs_file_path = os.path.normpath(os.path.join(abs_path_for_dir, file_path)) #this allows us to join the file and the directory together Ex: home/sebas/main.py
    try:
        if not abs_file_path.startswith(abs_path_for_dir): #if the path of the directory is outside of the scope of the abs_path then return error
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        else:
            MAX_CHARS = 10000
            with open(abs_file_path, "r") as f:
                file_content_string = f.read(MAX_CHARS)
                if f.read(1):
                        file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                return file_content_string
             
    except Exception as e:
        return f"Error: {e}" 