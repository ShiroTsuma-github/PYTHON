from enum import Enum, auto
from dataclasses import dataclass


class TokenTypes(Enum):
    plus = auto()
    minus = auto()
    multiply = auto()
    divide = auto()
    sqrt = auto()
    number = auto()


@dataclass
class Token:
    token_type: TokenTypes
    value: any


class Tokenizer:

    @classmethod
    def tokenize(self, string):
        tokens = []
        to_skip = 0

        for i, char in enumerate(string):
            if to_skip > 0:
                to_skip -= 1
                continue
            if char == '+':
                tokens.append(Token(TokenTypes.plus, '+'))
            elif char == '-':
                tokens.append(Token(TokenTypes.minus, '-'))
            elif char == '/':
                tokens.append(Token(TokenTypes.divide, '/'))
            elif char == '*':
                tokens.append(Token(TokenTypes.multiply, '*'))
            elif char == '_':
                tokens.append(Token(TokenTypes.sqrt, '_'))
            else:
                item = ''
                for j in range(i, len(string)):
                    if string[j] in '0123456789.':
                        item += string[j]
                    else:
                        break
                to_skip = len(item) - 1
                if '.' in item:
                    tokens.append(Token(TokenTypes.number, float(item)))
                else:
                    if len(item) > 0:
                        tokens.append(Token(TokenTypes.number, int(item)))
        return tokens


class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.stack_size = 0

    def pop(self):
        self.stack_size -= 1
        return self.stack.pop()

    def push(self, val):
        self.stack_size += 1
        self.stack.append(val)

    def add(self):
        if not self.stack_size >= 2:
            raise ArithmeticError(
                f"Add takes 2 parameters. {self.stack_size} on stack")
        a = self.pop()
        b = self.pop()
        self.push(a + b)

    def sub(self):
        if not self.stack_size >= 2:
            raise ArithmeticError(
                f"Sub takes 2 parameters. {self.stack_size} on stack")
        a = self.pop()
        b = self.pop()
        self.push(b - a)

    def mul(self):
        if not self.stack_size >= 2:
            raise ArithmeticError(
                f"Mul takes 2 parameters. {self.stack_size} on stack")
        a = self.pop()
        b = self.pop()
        self.push(b * a)

    def div(self):
        if not self.stack_size >= 2:
            raise ArithmeticError(
                f"Div takes 2 parameters. {self.stack_size} on stack")
        a = self.pop()
        b = self.pop()
        self.push(b / a)

    def sqrt(self):
        if not self.stack_size >= 1:
            raise ArithmeticError(
                f"Sqrt takes 1 parameters. {self.stack_size} on stack")
        a = self.pop()
        self.push(a ** 0.5)

    def peek_top(self):
        print(self.stack[self.stack_size - 1])

    def parse(self, str):
        for item in Tokenizer.tokenize(str):
            if item.token_type == TokenTypes.number:
                self.push(item.value)
            elif item.token_type == TokenTypes.plus:
                self.add()
                print("Add: ")
                self.peek_top()
            elif item.token_type == TokenTypes.minus:
                self.sub()
                print("Sub: ")
                self.peek_top()
            elif item.token_type == TokenTypes.divide:
                self.div()
                print("Div: ")
                self.peek_top()
            elif item.token_type == TokenTypes.multiply:
                self.mul()
                print("Mul: ")
                self.peek_top()
            elif item.token_type == TokenTypes.sqrt:
                self.sqrt()
                print("Sqrt: ")
                self.peek_top()


if __name__ == '__main__':
    stack = Stack()
    stack.parse("3^10^5+*12+4_/18-")
