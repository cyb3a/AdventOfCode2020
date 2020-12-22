import re

input = open('data/18.txt').read().splitlines()


class NewMathNumber(int):
    def __add__(self, other):
        return NewMathNumber(int(self) * int(other))

    def __mul__(self, other):
        return NewMathNumber(int(self) + int(other))

    @staticmethod
    def eval(expr):
        return eval(re.sub(r'\d+', lambda match: f'NewMathNumber({match.group(0)})',
                           expr.replace('*', 'x').replace('+', '*').replace('x', '+')))


print(sum(map(NewMathNumber.eval, input)))
