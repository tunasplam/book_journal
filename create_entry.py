import os
from pathlib import Path

def prompt_user_for_info() -> dict:
    return {
        'Title': input("Enter in title of work:\n"),
        'Author': input("Enter in author name:\n"),
        'Edition': input("Enter in enough edition info to make sure readers can reference page numbers correctly:\n")
    }

def create_stub(info: dict):

    os.makedirs(info['Author'], exist_ok=True)
    with open('template.txt', 'r') as f:
        txt = f.read()

    fp = Path(info['Author']) / Path(info['Title'] + '.md')
    fp.touch()
    with open(fp, 'w') as f:
        f.write(txt.format_map(info))

if __name__ == '__main__':
    create_stub(prompt_user_for_info())
