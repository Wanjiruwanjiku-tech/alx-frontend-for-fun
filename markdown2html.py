#!/usr/bin/python3
"""Module that converts markdown txt to html"""
import sys
import os

def markdown2html():
    """A function that starts a script
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    if len(sys.argv) < 3:
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
        exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        sys.stderr.write('Missing ' + markdown_file + '\n')
        exit(1)

    with open(markdown_file, 'r') as f:
        lines = f.readlines()

    html_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#'):
            level = stripped.count('#')
            html_lines.append('<h{}>'.format(level) + stripped[level:].strip() + '</h{}>\n'.format(level))
        elif stripped.startswith('- '):
            html_lines.append('<ul>\n')
            html_lines.append('<li>' + stripped[2:] + '</li>\n')
            html_lines.append('</ul>\n')
        elif stripped.startswith('* '):
            html_lines.append('<ol>\n')
            html_lines.append('<li>' + stripped[2:] + '</li>\n')
            html_lines.append('</ol>\n')
        else:
            html_lines.append('<p>\n')
            html_lines.append(stripped.replace('\n', '<br />\n'))
            html_lines.append('</p>\n')

    with open(html_file, 'w') as f:
        f.writelines(html_lines)

    exit(0)

if __name__ == "__main__":
    markdown2html()
