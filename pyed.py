import os
from os import system as sh


manual = '''cmds:
    ~ man(m): display the manual
    ~ shell($): access the system shell prompt
    ~ load(l): load a file into the buffer. creates a new buffer if valid file not found
    ~ show(s): displays the entire buffer
    ~ insert(i): takes a number of lines and appends them to the end of the document
    ~ replace(r): replaces a line by index
    ~ delete(d): deletes a line
    ~ clear(c): deletes all the lines in the buffer
    ~ write(w): saves the current buffer
    ~ quit(q): quits pyed
'''


def load(filename):
    buffer = list()
    if not os.path.exists(filename): return buffer
    with open(f'{filename}', 'r') as f:
        line = f.readline()
        while line:
            buffer.append(line.rstrip('\n'))
            line = f.readline()
    return buffer


filename = 'home.txt'
buffer = load(filename)
print('enter "manual" or "m" to see all commands')
while True:
    prompt = f'"{filename}" @{os.getcwd()} : '
    match input(prompt):
        case 'manual'|'m': print(manual)
        case 'shell'|'$': sh(input('$ '))
        case 'load'|'l':
            filename = input('name? : ')
            buffer = load(filename)
        case 'show'|'s':
            for i in range(len(buffer)):
                print(str(i + 1) + " | " + buffer[i])
        case 'insert'|'i':
            quantity = int(input('how many lines? : '))
            [buffer.append(input()) for i in range(quantity)]
        case 'replace'|'r':
            linenum = int(input('what line? : '))
            print(f'replacing line {linenum}: "{buffer[linenum - 1].strip()}" . . .')
            buffer[linenum - 1] = input()
        case 'delete'|'d':
            linenum = int(input('what line? : '))
            del buffer[linenum - 1]
        case 'clear'|'c': buffer.clear()
        case 'write'|'w':
            with open(f'{filename}', 'w') as f:
                f.write('\n'.join(buffer))
        case 'quit'|'q': quit()
        case _: print('cmd not recognized. please enter a valid cmd.')