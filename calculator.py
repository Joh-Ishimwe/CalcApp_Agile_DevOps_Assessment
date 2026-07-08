import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Calculation history stored here
history = []


def add(a, b):
    result = a + b
    logging.info(f"Addition: {a} + {b} = {result}")
    return result


def subtract(a, b):
    result = a - b
    logging.info(f"Subtraction: {a} - {b} = {result}")
    return result


def multiply(a, b):
    result = a * b
    logging.info(f"Multiplication: {a} * {b} = {result}")
    return result



def run_calculator():
    print("Welcome to CalcApp!")
    print("Operations: +, -, *, /")
    print("Type 'history' to see past calculations")
    print("Type 'exit' to quit")
    print("-----------------------------------")

    while True:
        user_input = input("\nEnter calculation (e.g. 5 + 3): ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        

        try:
            # Split input into parts
            parts = user_input.split()

            if len(parts) != 3:
                print("Invalid format. Please use: number operator number")
                print("Example: 5 + 3")
                continue

            a = float(parts[0])
            operator = parts[1]
            b = float(parts[2])

            if operator == '+':
                result = add(a, b)
                calculation = f"{a} + {b} = {result}"

            elif operator == '-':
                result = subtract(a, b)
                calculation = f"{a} - {b} = {result}"

            elif operator == '*':
                result = multiply(a, b)
                calculation = f"{a} * {b} = {result}"

            
            else:
                print(f"Unknown operator '{operator}'. Use +, -, *")
                continue

            
        except ValueError as e:
            print(e)

        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            print("Something went wrong. Please try again.")


if __name__ == "__main__":
    run_calculator()