import string

def main():
    file = open("A:\\Coding\\adventofcode\\challangethree.txt", 'r')
    lines = file.readlines()
    count = 1
    values = {}
    value = 0
    ndvalue = 0
    for i in string.ascii_lowercase:
        values[i] = count
        count += 1
    for j in string.ascii_uppercase:
        values[j] = count
        count += 1

    for line in lines:
        line = line.replace("\n", "")
        half = int(len(line) / 2)
        half_one = line[:half]
        half_two = line[half:]

        matches = ''
        for char in half_one:
            if char in half_two:
                matches = char
        value += values[matches]

    for i in range(int(len(lines)/3)):
        match = ''
        fin = ""
        backpack_one = lines[(i * 3) - 3].replace('\n', '')
        backpack_two = lines[(i * 3) - 2].replace('\n', '')
        backpack_three = lines[(i * 3) - 1].replace('\n', '')

        for char in backpack_one:
            if char in backpack_two and char in backpack_three:
                match = char
        ndvalue += values[match]
        
                
    print(value)
    print(ndvalue)

if __name__ == "__main__":
    main()