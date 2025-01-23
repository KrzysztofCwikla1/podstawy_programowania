import queue

def brackets_ok(expression):
    """
    Checks if the brackets in the expression are used correctly.
    :param expression: The input string containing the expression.
    :return: True if brackets are correct, False otherwise.
    """
    stack = queue.LifoQueue()
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.put(char)
        elif char in ')}]':
            if stack.empty() or stack.get() != bracket_pairs[char]:
                return False

    return stack.empty()

# Test expressions
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # brackets ok
expression2 = "[(2+3]/4)"                   # brackets not correct
expression3 = "(2-3*4+(5/6)"                # brackets not correct

# Check and print results
if brackets_ok(expression1):
    print("Expression 1: Brackets are correct")
else:
    print("Expression 1: Brackets are not correct")

if brackets_ok(expression2):
    print("Expression 2: Brackets are correct")
else:
    print("Expression 2: Brackets are not correct")

if brackets_ok(expression3):
    print("Expression 3: Brackets are correct")
else:
    print("Expression 3: Brackets are not correct")
