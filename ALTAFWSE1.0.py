import os

# Строки, которые нужно добавить
add_lines = [
    "<h1>Example Text</h1>",
    "<p>Hello World!</p>"
]

def process_your_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    if any(add_lines[0] in line for line in content) and any(add_lines[1] in line for line in content):
        return

    new_content = [line + '\n' for line in add_lines] + ['\n'] + content

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_content)

def find_and_process_your_files(root_folder):
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.html'): # Формат файла который надо искать
                full_path = os.path.join(root, file)
                process_your_file(full_path)

if __name__ == '__main__':
    current_directory = os.path.dirname(os.path.abspath(__file__))
    find_and_process_your_files(current_directory)
