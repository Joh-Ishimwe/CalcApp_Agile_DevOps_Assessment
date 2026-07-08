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


def divide(a, b):
    if b == 0:
        logging.error("Division by zero attempted")
        raise ValueError("Error: Cannot divide by zero")
    result = a / b
    logging.info(f"Division: {a} / {b} = {result}")
    return result


def save_to_history(calculation):
    history.append(calculation)


def get_history():
    return history


def display_history():
    if not history:
        print("No calculations yet.")
    else:
        print("\n--- Calculation History ---")
        for i, entry in enumerate(history, 1):
            print(f"{i}. {entry}")
        print("---------------------------\n")


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

        if user_input.lower() == 'history':
            display_history()
            continue

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

            elif operator == '/':
                result = divide(a, b)
                calculation = f"{a} / {b} = {result}"

            else:
                print(f"Unknown operator '{operator}'. Use +, -, *, /")
                continue

            print(f"Result: {calculation}")
            save_to_history(calculation)

        except ValueError as e:
            print(e)

        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            print("Something went wrong. Please try again.")


if __name__ == "__main__":
    run_calculator()