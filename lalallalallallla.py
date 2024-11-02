def __init__(self):
        self.result = 0

    def add(self, num):
        """Add a number to the result."""
        self.result += num
        return self.result

    def subtract(self, num):
        """Subtract a number from the result."""
        self.result -= num
        return self.result

    def multiply(self, num):
        """Multiply the result by a number."""
        self.result *= num
        return self.result

    def divide(self, num):
        """Divide the result by a number."""
        if num == 0:
            raise ValueError("Cannot divide by zero.")
        self.result /= num
        return self.result

    def clear(self):
        """Reset the calculator's result to zero."""
        self.result = 0
        return self.result

    def get_result(self):
        """Get the current result."""
        return self.result

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(5))         # Output: 5
    print(calc.subtract(2))    # Output: 3
    print(calc.multiply(10))   # Output: 30
    print(calc.divide(3))      # Output: 10.0
    print(calc.clear())        # Output: 0
    print(calc.get_result())   # Output: 0
