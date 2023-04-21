import random
import readline

tape = [random.choices([0, 1])[0] for _ in range(99999)]
pos = 0
history = []
hist_pos = 0

while True:
    try:
        reader = input("\033[35mREADER>\033[0m")
        if reader.strip():
            history.append(reader)
            hist_pos = len(history)
    except KeyboardInterrupt:
        exit("\n[^C]utting Tape...")

    if reader == "":
        if len(history) > 0:
            reader = history[hist_pos-1]
        else:
            continue

    if reader == "\x1b[A":  # up arrow key
        if hist_pos > 0:
            hist_pos -= 1
        reader = history[hist_pos] if hist_pos < len(history) else ""
    elif reader == "\x1b[B":  # down arrow key
        if hist_pos < len(history):
            hist_pos += 1
        reader = history[hist_pos] if hist_pos < len(history) else ""

    for i, item in enumerate(reader):
        if item == "<":
            oldpos = pos
            pos -= 1
            if pos < 0:
                exit("\033[31mUFE: UNDERFLOW ERROR IN \"<\" FUNC\033[0m")
            else:
                print("JUMPED FROM: \033[31m"+str(oldpos)+"\033[0m\nTO: \033[36m"+str(pos)+"\033[0m")
        if item == ">":
            oldpos = pos
            pos += 1
            print("JUMPED FROM: \033[31m"+str(oldpos)+"\033[0m\nTO: \033[36m"+str(pos)+"\033[0m")
        if item == "r":
            print("VALUE: \033[32m"+str(tape[pos])+"\033[0m\nM-ADDRESS:\033[36m"+str(pos)+"\033[0m")
        if item == "w":
            if not (i+1 >= len(reader)) and reader[i+1].isdigit() and int(reader[i+1]) in [0, 1]:
                tape[pos] = int(reader[i+1])
        if item == "t":
            print(tape)
