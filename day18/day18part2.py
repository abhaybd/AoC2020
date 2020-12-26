with open("input.txt") as f:
    lines = [line.strip().replace(" ", "") for line in f.readlines()]


def tokenize(expression: str) -> list:
    tokens = []
    i = 0
    while i < len(expression):
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
            tokens.append(expression[i+1:end])
            i = end+1
        elif expression[i].isdigit():
            for j in range(i+1, len(expression)+1):
                if j == len(expression) or not expression[j].isdigit():
                    tokens.append(expression[i:j])
                    i = j
                    break
        else:
            tokens.append(expression[i])
            i += 1
    return tokens


def join_tokens(tokens: list):
    return "".join([token if len(token) == 1 or token.isdigit() else "(" + token + ")" for token in tokens])


def eval_expr(expression: str):
    tokens = tokenize(expression)
    if "*" in tokens:
        index = tokens.index("*")
        val = eval_expr(join_tokens(tokens[:index])) * eval_expr(join_tokens(tokens[index+1:]))
    else:
        val = sum(int(token) if token.isdigit() else eval_expr(token) for token in tokens if token != "+")
    return val


print(sum(eval_expr(line) for line in lines))
