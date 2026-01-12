# python clean_rst.py /path/to/folder


import os
import sys

def clean_rst_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cleaned_lines = []
    empty_count = 0

    for line in lines:
        stripped_line = line.rstrip()

        if stripped_line == "":
            empty_count += 1
            if empty_count <= 1:
                cleaned_lines.append("\n")
        else:
            empty_count = 0
            cleaned_lines.append(stripped_line + "\n")

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(cleaned_lines)

    print(f"Cleaned: {file_path}")


def clean_rst_in_folder(root_folder):
    for root, _, files in os.walk(root_folder):
        for file in files:
            if file.lower().endswith(".rst"):
                clean_rst_file(os.path.join(root, file))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python clean_rst.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]

    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid folder")
        sys.exit(1)

    clean_rst_in_folder(folder_path)
