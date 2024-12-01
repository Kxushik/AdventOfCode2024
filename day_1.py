
input_file = open("day_1_input.txt", "r")
from collections import defaultdict
def solve_1(input_file):
    data = input_file.readlines()
    list_1 = []
    list_2 = []
    for item in data:
        item = item.strip().split()
        list_1.append(int(item[0]))
        list_2.append(int(item[1]))
    

    list_1 = sorted(list_1)
    list_2 = sorted(list_2)

    sum = 0
    for i in range(len(list_1)):
        sum += abs(list_1[i] - list_2[i])
    return sum

def solve_2(input_file):
    data = input_file.readlines()
    dict_1 = defaultdict(int)
    dict_2 = defaultdict(int)
    score = 0

    for item in data:
        item = item.strip().split()
        dict_1[int(item[0])] += 1
        dict_2[int(item[1])] += 1

    for key1, value1 in dict_1.items():
        value2 = dict_2[key1]
        score += abs((key1 * value1) * (value2))

    return score
        
if __name__ == "__main__":
    print(f'Part 1: {solve_1(input_file)}')
    input_file.seek(0)
    print(f'Part 2: {solve_2(input_file)}')