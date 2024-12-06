import re

with open('input/input.txt', 'r') as file:
    pattern = r"mul\([0-9]{1,3}[,][0-9]{1,3}\)"
    total_sum = 0
    for line in file:
        match = re.findall(pattern, line)
        
        # print(f"Mul expression extracted: {match} from {line}")
        for match_subtr in match:
            print(f"Mul expression extracted: {match_subtr} from {line}")
            
            split = match_subtr.split(",")
            num1 = int(split[0].split("mul(")[1])
            num2 = int(split[1].split(")")[0])
            
            product = num1 * num2
            total_sum += product
            print(f"Parsed num1 {num1} * parsed num2 {num2} = sub product {product}")
        
    print(f"Total sum: {total_sum}")