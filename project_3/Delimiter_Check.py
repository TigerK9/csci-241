import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
    charStack = Stack()
    with open(filename) as text:
        content = text.read() # this is a string datatype
    for char in content:
        if char in {"(","{","["}:
            charStack.push(char)
        elif char in {")", "}", "]"}:
            popped = charStack.pop()
            if char == "]" and popped != "[":
                print("Doesn't work")
                return False
            elif char == ")" and popped != "(":
                return False
            elif char == "}" and popped != "{":
                return False
    if len(charStack) == 0:
        return True
    return False

    # TODO replace pass with an implementation that returns True
    # if the delimiters (), [], and {} are balanced and False otherwise.
    pass

if __name__ == '__main__':
    # The list sys.argv contains everything the user typed on the command 
    # line after the word python. For example, if the user types
    # python Delimiter_Check.py file_to_check.py
    # then printing the contents of sys.argv shows
    # ['Delimiter_Check.py', 'file_to_check.py']
    if len(sys.argv) < 2:
        # This means the user did not provide the filename to check.
        # Show the correct usage.
        print('Usage: python Delimiter_Check.py file_to_check.py')
    else:
        if delimiter_check(sys.argv[1]):
            print('The file contains balanced delimiters.')
        else:
            print('The file contains IMBALANCED DELIMITERS.')


