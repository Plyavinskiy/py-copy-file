import os


def copy_file(command: str) -> None:
    command_parts = command.strip().split()

    if len(command_parts) != 3 or command_parts[0] != "cp":
        return

    source_path, dest_path = command_parts[1].strip(), command_parts[2].strip()

    if not source_path or not dest_path:
        return

    if os.path.isdir(source_path) or os.path.isdir(dest_path):
        return

    if source_path == dest_path or not os.path.isfile(source_path):
        return

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    try:
        with open(source_path, "r", encoding="utf-8") as source, \
             open(dest_path, "w", encoding="utf-8") as destination:
            destination.writelines(source)
    except (FileNotFoundError, PermissionError, OSError):
        return
