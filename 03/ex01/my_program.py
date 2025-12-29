import sys

sys.path.insert(0, './local_lib')
from path import Path

def main():
    try:
        Path('directory').mkdir_p()
    except FileExistsError as e:
        print(e)
    f = Path('directory/file')
    f.write_lines(['hello', 'ggg!'])
    print(f.read_text())


if __name__ == '__main__':
    main()