def main():
    operation = input("Expression: ")
    x, op, z = operation.split()
    x=float(x)
    z=float(z)
    math(x,op,z)

    #print(f"x: {x}, z {z}, op: {op}")



def math(number1, operator, number2):
    match operator:
        case "+":
            resp = number1 + number2
        case "-":
            resp = number1 - number2
        case "*":
            resp = number1 * number2
        case "/":
            if number2 == 0:
                print("Error div 0")
                return
            else:
                resp = number1 / number2
        case _:
                print("please input an valid operator")
    resp_float = float(resp)
    print(format(resp_float, '.1f'))

main()