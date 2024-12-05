import math


class CalculatorLogic:
    def calculate(self, expression: str) -> str:
        """
        Evaluates a mathematical expression and returns the result.
        """
        try:
            result = eval(expression, {"__builtins__": None}, math.__dict__)
            return str(result)
        except Exception as e:
            return f"Error: {e}"
