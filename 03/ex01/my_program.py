
import sys

sys.path.insert(0, './local_lib')
from path import Path

def main():
    try:
        Path('my_folder').mkdir_p()
    except FileExistsError as e:
        print(f"Error: {e}")
    
    f = Path('my_folder/my_file.txt')
    f.write_lines(['Hello from path.py library!', 'This is a test file.', 'Created using the Path object.'])
    print(f.read_text())


if __name__ == '__main__':
    main()