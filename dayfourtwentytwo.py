
def main():
    file = open('A:\\Coding\\adventofcode\\challangefour.txt', 'r')
    lines = file.readlines()
    count = 0
    for line in lines:
        line = line.replace('\n', '').split(',')
        section_one, section_two = line[0].split('-'), line[1].split('-')
        
        

if __name__ == "__main__":
    main()