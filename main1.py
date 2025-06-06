from src.logger import logging

class Calculator:
    def __init__(self):
        self.__num1 = 0
        self.__num2 = 0

    def input_numbers(self):
        while True:
            try:
                return float(input("Enter a number: "))
            except Exception as e:
                logging.info(f"{e} \nInvalid Integer! Please enter a valid Integer.")
                print(f"{e} \nInvalid Integer! Please enter a valid Integer.")

    def add(self):
        return self.__num1 + self.__num2
    
    def sub(self):
        return self.__num1 - self.__num2
    
    def mul(self):
        return self.__num1 * self.__num2
    
    def div(self):
        try: 
            return round(self.__num1 / self.__num2, 4)
        except Exception as e:
            logging.info(f"{e} \nZero division is not allowed")
            print(f"{e} \nZero division is not allowed")
            return None

    def calculation(self, __operator):
        match __operator:
            case '+':
                return self.add()
            case '-':
                return self.sub()
            case '*':
                return self.mul()
            case '/':
                return self.div()
            case _:
                logging.info("Invalid operator! Please choose from available list of operator.")
                print("Invalid operator! Please choose from available list of operator.")
                return None

    def display_result(self):
        print(f"The current output is {self.__result}")

    def execute(self):
        self.__result = self.input_numbers()
        self.display_result()

        op = ['+', '-', '*', '/']
        while True:
            operator = input(f"Choose the operator among this list - {op} or '=': ")

            if operator == '=':
                print(f"The final output is {self.__result}")
                break
            if operator not in op:
                logging.info("Invalid operator! Please choose from available list of operator.")
                print("Invalid operator! Please choose from available list of operator.")
                continue
            
            self.__num2 = self.input_numbers()
            self.__num1 = self.__result

            final_result = self.calculation(operator)
            if final_result is not None:
                self.__result = final_result
                self.display_result()
            else:
                print("Try again")

        
if __name__ == "__main__":    
    cal = Calculator()
    cal.execute()             



    




