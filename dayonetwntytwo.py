
def main():
    file = open('A:\\Coding\\adventofcode\\challangeone.txt', 'r')
    lines = file.readlines()
    end_list_numbers = []
    count = 0
    for item in lines:
        lines[count] = item.replace('\n', '')
        count += 1
    number_addition = 0
    for item in lines:
        if item == '':
            end_list_numbers.append(number_addition)
            number_addition = 0
        else:
            number_addition += int(item)
    maxim = 0
    index = 0
    for item in end_list_numbers:
        if item >= maxim:
            index = end_list_numbers.index(item)
            maxim = item
    print(f"Your maximim number is {maxim} at range {index}.")

    end_list_numbers.sort()
    first = end_list_numbers[-1]
    second = end_list_numbers[-2]
    third = end_list_numbers[-3]

    result = first + second + third

    print(f"The top three elves are carrying {result}")


if __name__ == "__main__":
    main()