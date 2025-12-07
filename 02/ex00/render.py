#!/bin/python3

import sys, os, re, settings


def main():
    if len(sys.argv) != 2:
        sys.stderr.write("Error: Wrong number of arguments.\n")
        sys.stderr.write("Usage: python3 render.py <file.template>\n")
        sys.exit(1)
    template_path = sys.argv[1]
    if not template_path.endswith(".template"):
        sys.stderr.write(f"Error: The file '{template_path}' does not have a .template extention.\n")
        sys.exit(1)
    
    if not os.path.isfile(template_path):
        sys.stderr.write(f"Error: the file '{template_path}' does not exit.\n")
        sys.exit(1)
    context = {key: value for key, value in vars(settings).items() if not key.startswith('__')}
    try:
        with open(template_path, 'r') as f:
            content = f.read()
        for key, value in context.items():
            pattern = '{' + key + '}'
            content = content.replace(pattern, str(value))

        output_path = template_path.replace(".template", ".html")
        with open(output_path, 'w') as f:
            f.write(content)
        print(f"success! rendred to {output_path}")
    except Exception as e:
        sys.stderr.write(f"Error : {e}")
        sys.exit(1)



if __name__ == "__main__":
    main()