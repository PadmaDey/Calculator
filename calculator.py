class Calculator:
    def __init__(self):
        while True:
            try:
                self.num1 = float(input("Enter the first number: "))
                break
            except Exception as e:
                print(f"{e} \nInvalid input. Please enter a valid integer...")
                
        while True:
            try:
                self.num2 = float(input("Enter the second number: "))
                break
            except Exception as e:
                print(f"{e} \nInvalid input. Please enter a valid integer...")   

    def display(self):
        print(f"The first number is {self.num1} and the second number is {self.num2}")

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        try:
            return round(self.num1 / self.num2,4)
        except Exception as e:
            return f"{e} \nError: Division by zero is not allowed."
        
if __name__ == '__main__':
    cal = Calculator()
    operator = ['+', '-', '*', '/']
    while True:
        op = input(f'Choose the operator among these - {operator}: ')

        try:
            if op == '+':
                print(f"Result: {cal.add()}")
            elif op == '-':
                print(f"Result: {cal.sub()}")
            elif op == '*':
                print(f"Result: {cal.mul()}")
            elif op == '/':
                result = cal.div()
                if result is not None: 
                    print(f"Result: {result}")
            else:
                print("Invalid operator. Please choose from the available operators.")
                
        except Exception as e:
            print(e)
            
        condition = input("Do you want to continue? Enter 'X' to exit: ")
        if condition.strip().upper() == 'X':
            break

