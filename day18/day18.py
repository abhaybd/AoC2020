with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

op_map = {"*": lambda a, b: a * b, "+": lambda a, b: a + b}


def eval_expr(expression: str):
    expression = expression.replace(" ", "")
    val = 0
    op = "+"
    i = 0
    while i < len(expression):
        print("\t" + str(op), val)
        if expression[i] == "(":
            balance = 1
            end = None
            for j in range(i+1, len(expression)):
                if expression[j] == ")":
                    balance -= 1
                elif expression[j] == "(":
                    balance += 1
                if balance == 0:
                    end = j
                    break
            val = op_map[op](val, eval_expr(expression[i+1:end]))
            i = end+1
        elif expression[i].isdigit():
            for j in range(i+1, len(expression)+1):
                if j == len(expression) or not expression[j].isdigit():
                    num = int(expression[i:j])
                    val = op_map[op](val, num)
                    i = j
                    break
        else:
            op = expression[i]
            i += 1
    print("\t=" + str(val))
    return val


print(sum(eval_expr(line) for line in lines))
