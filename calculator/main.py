
import sys

def calculate(expression):
    try:
        # Using eval to correctly handle operator precedence
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        expression = sys.argv[1]
        print(calculate(expression))
    else:
        print("Usage: python main.py "<expression>"")
