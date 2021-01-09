from Gorithms import *
from GUIHandler import *

init()

closed = False
while not closed:
    user_input = input('Please enter a command: ')

    if user_input in ['close', 'exit', 'end', 'stop']:
        closed = True

    if user_input.startswith('test '):
        args = user_input.split(' ')

        if (len(args) < 2):
            continue
        while (len(args) > 2):
            args.__delitem__(2)
        
        print(test_commons(args[1]))
