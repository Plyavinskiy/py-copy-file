import os


def copy_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source, target = parts[1], parts[2]

    if source == target or not os.path.isfile(source):
        return

    target_dir = os.path.dirname(target)
    if target_dir:
        os.makedirs(target_dir, exist_ok=True)

    try:
        with open(source, "r", encoding="utf-8") as file_in:
            content = file_in.read()
        with open(target, "w", encoding="utf-8") as file_out:
            file_out.write(content)
    except (PermissionError, OSError, IsADirectoryError):
        return
