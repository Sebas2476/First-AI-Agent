import os

def get_files_info(working_directory: str, directory: str = "."):
    working_directory_abs = os.path.abspath(working_directory)
    trg_directory = os.path.normpath(os.path.join(working_directory_abs, directory))
    valid_target_dir = os.path.commonpath([working_directory_abs, trg_directory]) == working_directory_abs
    try:
        if not valid_target_dir: 
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(trg_directory):
            return f'Error: "{directory}" is not a directory'
        else:
            file_contents = []
            for items in os.listdir(trg_directory):
                full_path = os.path.join(trg_directory, items)
                file_size = os.path.getsize(full_path)
                dir_check = os.path.isdir(full_path)
                file_contents.append(f"- {items}: file_size={file_size} bytes, is_dir={dir_check}")
            return "\n".join(file_contents)

    except Exception as e:
        return f"Error: {e}"
    
    