import operator as op
import ast
from numbers import NumberService


class SimpleMathService(object):
    """
    Service to perform basic arithmetic derived from English expressions. Use
    the ast module to evaluate the string form of expression.
    """

    def __init__(self):
        # map abstract arithmetic constructs to operators from 'operator'
        # module
        self.supported_ops = {
            ast.Add: op.add,
            ast.Sub: op.sub,
            ast.Mult: op.mul,
            ast.Div: op.truediv,
            ast.Pow: op.pow,
            ast.BitXor: op.xor,
            ast.USub: op.neg
        }
        # map english expression to operator object
        self.single_word_ops = {
            'plus': op.add,
            'minus': op.sub,
            'times': op.mul,
            'xor': op.xor,
            'XOR': op.xor,
            'to': op.pow,
        }
        self.double_word_ops = {
            'divided by': op.div,
            'raised to': op.pow,
        }
        # map operator object to string form
        self.op_to_str = {
            op.add: '+',
            op.sub: '-',
            op.mul: '*',
            op.div: '/',
            op.pow: '**',
            op.xor: '^',
        }
        self.number_service = NumberService()

    def parse_basic_formula(self, input):
        lacks_operator = True
        running_number = ""
        expression = []  # store expression as list of operators and operands
        remaining_operator_words = 0  # number of words left from last operator
        xor_operator = False  # if there is an XOR somewhere in the expression

        for s_i, string in enumerate(input.split(" ")):
            # print string

            # moved forward through input split, so if there is a running
            # operator string, decrement remaining words
            if remaining_operator_words > 0:
                remaining_operator_words -= 1

            # only process if we're not still consuming a string operator
            if remaining_operator_words is 0:
                # if a single word expression is found, append the running
                # number to the expression and then the operator
                if string in self.single_word_ops:
                    expression.append(running_number.strip())
                    expression.append(self.single_word_ops.get(string, None))
                    if string == 'xor' or string == 'XOR':
                        xor_operator = True
                    running_number = ""
                    lacks_operator = False
                    remaining_operator_words = 1
                # if a double word expression is found, append the running
                # number to the expression and then the operator
                elif (s_i + 1 < len(input.split(" ")) and
                      string + " " + input.split(" ")[s_i + 1] in
                      self.double_word_ops):
                    expression.append(running_number.strip())
                    expression.append(self.double_word_ops.get(
                        string + " " + input.split(" ")[s_i + 1], None))
                    running_number = ""
                    lacks_operator = False
                    remaining_operator_words = 2
                # substring is not an operator, number is still running
                else:
                    running_number += string + " "

        # append last remaining running number if any
        if len(running_number) > 0:
            expression.append(running_number.strip())

        # if the expression seems valid with at least one operator, convert
        # its operands and operators to reduced number/primitive form
        if not lacks_operator:
            print "expression list: " + str(expression)
            expr_to_eval = ""
            ns = NumberService()
            for substr in expression:
                if type(substr) == str:
                    if not xor_operator:
                        expr_to_eval += str(float(ns.parse_english(substr))) + " "
                    # XOR requires integers, not floats
                    else:
                        expr_to_eval += str(int(ns.parse_english(substr))) + " "
                # map operator.function to its sign form
                else:
                    print "operator"
                    expr_to_eval += str(self.op_to_str.get(substr, None)) + " "
            print "expression to evaluate: " + expr_to_eval
            return self._eval_str_expr(expr_to_eval)
        else:
            raise Exception("You did not include an operator")

    def _eval_str_expr(self, expr):
        """Evaluate the reduced string form of a mathematical expression"""
        return self._eval_helper(ast.parse(expr, mode='eval').body)

    def _eval_helper(self, node):
        """Recursive expression evaluation"""
        # <number>
        if isinstance(node, ast.Num):
            return node.n
        # <left> <operator> <right>: binary operator operates on two operands
        elif isinstance(node, ast.BinOp):
            return self.supported_ops[type(node.op)](
                self._eval_helper(node.left), self._eval_helper(node.right))
        # <operator> <operand> e.g., -1: unary operator operates on one operand
        elif isinstance(node, ast.UnaryOp):
            return self.supported_ops[type(node.op)](
                self._eval_helper(node.operand))
        else:
            raise TypeError(node)
