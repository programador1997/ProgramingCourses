def calculate_expression(x, operator, z):
    if operator == '+':
        return x + z
    elif operator == '-':
        return x - z
    elif operator == '*':
        return x * z
    elif operator == '/':
        return x / z

def main():
    user_input = input("Enter an arithmetic expression (e.g., 1 + 1): ")
    try:
        x, op, z = user_input.split()
        x = float(x)
        z = float(z)
        if op in ['+', '-', '*', '/']:
            if op == '/' and z == 0:
                print("Error: Division by zero!")
            else:
                result = calculate_expression(x, op, z)
                print(f"The result is: {result:.1f}")
        else:
            print("Invalid operator! Please use one of: +, -, *, /")
    except ValueError:
        print("Invalid input format! Please follow the format: x operator z")

if __name__ == "__main__":
    main()
