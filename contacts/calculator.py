class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

if __name__ == '__main__':
    calc = Calculator(6, 2)

    sumResult = calc.sum()                      # 덧셈
    print(f'덧셈 결과 {sumResult}')

    subResult = calc.sub()                      # 뺄셈
    print(f'뺄셈 결과 {subResult}')

    mulResult = calc.mul()                      # 곱셈
    print(f'곱셈 결과 {mulResult}')

    divResult = calc.div()                      # 나눗셈
    print(f'나눗셈 결과 {divResult}')    
