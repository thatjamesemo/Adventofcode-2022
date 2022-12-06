
def main():
    file = open('A:\\Coding\\adventofcode\\challangetwo.txt', 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
    x_var = "R"
    y_var = "P"
    z_var = "S"

    a_var = "R"
    b_var = "P"
    c_var = "S"

    score = 0
    for challange in lines:
        move = challange.split(" ")
        if move [0] == 'A':
            if move [1] == 'Y':
                score += 6
                score += 2
            elif move[1] == 'X':
                score += 3
                score += 1
            elif move[1] == 'Z':
                score += 3
        elif move [0] == 'B':
            if move[1] == 'Z':
                score += 6
                score += 3
            elif move[1] == 'Y':
                score += 3
                score += 2
            elif move[1] == 'X':
                score += 1
        elif move[0] == 'C':
            if move[1] == 'X':
                score += 6
                score += 1
            elif move[1] == 'Z':
                score += 3
                score += 3
            elif move[1] == 'Y':
                score += 2
    
    print(f"Your score is: {score}")

    win_dict = {'A':'P', 'B':'S', 'C':'R'}
    draw_dict = {'A':'R', 'B':'P', 'C':'S'}
    lose_dict = {'A':'S', 'B':'R', 'C':'P'}
    scores = {'R':1, 'P':2, 'S':3}
    score = 0
    for challange in lines:
        move = challange.split(" ")
        if move[1] == 'X':
            print("Loosing")
            score += scores[lose_dict[move[0]]]
        elif move[1] == 'Y':
            print("Drawing")
            score += 3
            score += scores[draw_dict[move[0]]]
        elif move[1] == 'Z':
            print("Winning")
            score += 6
            score += scores[win_dict[move[0]]]
    print(f"Your new score is now {score}")

if __name__ == "__main__":
    main()