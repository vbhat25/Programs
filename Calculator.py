class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        if num2!=0:
            return num1/num2
        else:
            return "Error in division"
        
calci = Calculator()

result_add = calci.add(10,5)
result_subtract = calci.subtract(10,5)
result_multiply = calci.multiply(10,5)
result_division = calci.divide(10,5)

print("Addition: {}" .format(result_add))
print("Subtract: {}" .format(result_subtract))
print("Multiplication: {}" .format(result_multiply))
print("Division: {}" .format(result_division))
