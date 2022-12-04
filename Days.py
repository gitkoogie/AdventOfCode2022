

#day 1 
def day_one(file):
    # grab data for the day
    with open(file) as f:
        lines = f.readlines()
    
    most = 0
    second = 0
    third = 0
    each = 0
    for k,val in enumerate(lines):
        if val == "\n":
            if each > most:
                most = each
            each = 0
        else:
            each = each + int(val.strip("\n"))
    print(f"part one: {most}") # part one answer

    order = [0,0,0,0]
    each = 0
    counter = 0
    for k,val in enumerate(lines):
        # fill up first four
        if val == "\n" and counter < 4:
            order[counter] = each
            each = 0
            counter = counter + 1
        # add to last position
        elif val == "\n":
            order.sort(reverse=True)    # sort descending
            order[3] = each
            each = 0
        else:
            each = each + int(val.strip("\n"))
    total = sum(order[0:3])
    print(f"part two: {total}") # part two answer    

def day_two(file):
    # grab data for the day
    with open(file) as f:
        lines = f.readlines()
    #A = ROCK = X => PTS: 1
    #B = PAPER = Y => PTS: 2
    #C = SCISSORS = Z => PTS: 3
    # + win = 6, draw = 3, lose = 0

    # fix data (remove newline)
    mod_lines = []
    for k,val in enumerate(lines):
        mod_lines.append(val.strip("\n"))

    pts = 0
    for val in mod_lines:
        if val[0] == "A":       # he play rock
            if val[2] == "Y":   # I play paper
                pts = pts + 6 + 2
            elif val[2] == "X": # I play rock
                pts = pts + 3 + 1
            else:
                pts = pts + 3
        elif val[0] == "B":     # he play paper
            if val[2] == "Z":   # I play scissor
                pts = pts + 6 + 3
            elif val[2] == "Y": # I play paper
                pts = pts + 3 + 2
            else:
                pts = pts + 1
        elif val[0] == "C":         #he play scissors
            if val[2] == "X":       #I play rock
                pts = pts + 6 + 1
            elif val[2] == "Z":
                pts = pts + 3 + 3   #I play scissor
            else:
                pts = pts + 2

    print(f"part one pts:{pts}")      
    #A = ROCK => LOSE X : 1 pts
    #B = PAPER => DRAW Y : 2 pts 
    #C = SCISSORS => WIN Z : 3 pts
    # + win = 6, draw = 3, lose = 0
    pts = 0
    for k,val in enumerate(mod_lines):
        if val[0] == "A":           # he play rock
            if val[2] == "X":       # lose
                pts = pts + 3
            elif val[2] == "Y":     # draw
                pts = pts + 3 + 1
            else:                   # win
                pts = pts + 6 + 2
        elif val[0] == "B":         # he play paper
            if val[2] == "X":       # lose
                pts = pts + 1
            elif val[2] == "Y":     # draw
                pts = pts + 3 + 2
            else:                   # win
                pts = pts + 6 + 3
        elif val[0] == "C":         # he play scissors
            if val[2] == "X":       # lose
                pts = pts + 2
            elif val[2] == "Y":     # draw
                pts = pts + 3 + 3
            else:                   # win
                pts = pts + 6 + 1
        #print(f"Line {k}: {val[0]}:{val[2]}->{pts}")
    print(f"part two pts:{pts}")

def day_three(file):
    import string
    # grab data for the day
    with open(file) as f:
        lines = f.readlines()
    # fix data (remove newline)
    mod_lines = []
    for k,val in enumerate(lines):
        mod_lines.append(val.strip("\n"))
    pts = 0
    for line in mod_lines:
        comp1 = line[0:int(len(line)/2)]
        comp2 = line[int(len(line)/2):]
        for val in set(comp1):
            if val in set(comp2):
                pts += string.ascii_letters.index(val)+1
    print(f"Part one: {pts}")

    pts = 0
    for k, line in enumerate(mod_lines):
        if k>0 and (k+1) % 3 == 0:
            for val in set(line):
                if val in set(mod_lines[k-1]):
                    for vel in set(mod_lines[k-2]):
                        if val == vel:
                            pts += string.ascii_letters.index(val)+1
    print(f"Part two: {pts}")      

def day_four(file):
    with open(file) as f:
        data = f.read().strip()
    
    sections = data.split("\n")
    
    cnt = 0
    for s in sections:
        s1,s2 = s.split(",")
        s11, s12 = map(int, s1.split("-"))
        s21, s22 = map(int, s2.split("-"))
        if (s11 <= s21 and s22 <= s12 or \
            s21 <= s11 and s12 <= s22):
            cnt += 1
    print(f"Part one: {cnt}")
    
    cnt = 0
    print(len(sections))
    for s in sections:
        s1,s2 = s.split(",")
        s11, s12 = map(int, s1.split("-"))
        s21, s22 = map(int, s2.split("-"))
        if (s12 >= s21 and s11 <= s21 or\
            s22 >= s11 and s21 <= s11):
            cnt += 1
    print(f"Part two: {cnt}")


#day_one("day1.txt")
#day_two("day2.txt")
#day_three("day3.txt")
day_four("day4.txt")