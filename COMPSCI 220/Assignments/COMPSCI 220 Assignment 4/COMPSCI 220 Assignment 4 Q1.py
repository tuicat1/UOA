import sys

input_lines = []
for line in sys.stdin:
    element_list = line.rstrip().split(sep = ",")
    input_lines.append(element_list)
count = 0

def eval(position_of_a_root):
    allowed = ["+", "*"]
    evaluated_result = "sum"
    if operators[position_of_a_root] in allowed:
        for i in children[str(position_of_a_root)]:
            if operators[i] != "+" and operators[i] != "*":
                if operators[position_of_a_root] == "+":  
                    if evaluated_result == "sum":
                        evaluated_result = int(operators[i])
                    else:
                        evaluated_result += int(operators[i])
                elif operators[position_of_a_root] == "*":
                    if evaluated_result == "sum":
                        evaluated_result = int(operators[i])
                    else:
                        evaluated_result *= int(operators[i])
            else:
                if operators[position_of_a_root] == "+":  
                    if evaluated_result == "sum":
                        evaluated_result = eval(i)
                    else:
                        evaluated_result += eval(i) 
                elif operators[position_of_a_root] == "*":
                    if evaluated_result == "sum":
                        evaluated_result = eval(i)
                    else:
                        evaluated_result *= eval(i) 
    if evaluated_result == "sum":
        evaluated_result = operators[position_of_a_root]
    return evaluated_result   



while count < len(input_lines):
    pred = input_lines[count]
    global operators
    operators = input_lines[count + 1]
    length = len(pred)
    position_of_root = pred.index("-1")
    global children
    children = {}
    for i in range(length):
        try:
            children[pred[i]].append(i)
        except:
            children[pred[i]] = [i]
    print(eval(position_of_root))
    count += 2