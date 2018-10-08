from test_framework import generic_test

# So obviously use some kind of operands (recursive or the data structure)
# I think we can do this by splitting the string by commas and then pushing values
# onto a operands until we hit a +, -, x, or / expression. When that happens, we can
# pop off the values on the operands (should be two) and then apply the operator on
# those numbers. We would then push the result back onto the operands. The question
# specifies that the expression is in RPN so we don't have to worry about invalid
# inputs. When we reach the end of the expressions, we return the top of the operands.

# This solution takes O(n) time, where n is the amount of expressions that are contained in the input.
# We know that our operands will only hold two values at a time so we can say that our space complexity is constant.

def evaluate(expression):
    op_map = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b
    }
    operands = []
    for exp in expression.split(','):
        if exp in op_map:
            second, first = operands.pop(), operands.pop()
            result = op_map[exp](first, second)
            operands.append(result)
        else:
            operands.append(int(exp))
    return operands.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
