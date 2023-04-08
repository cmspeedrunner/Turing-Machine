import random
tape = []
# Initalise the tape
for i in range(99999):
    tape.append((random.randint(0,1)))
pos = 0
while True:
    try:
        reader = input("\u001b[35mREADER>\u001b[0m")
    except KeyboardInterrupt:
        print("\n[^C]utting Tape...")
        exit()
    reader = list(reader)
    for i, item in enumerate(reader):
        if item == "<":
            oldpos = pos
            pos = pos-1
            if pos < 0:
                print("\u001b[31mUFE: UNDERFLOW ERROR IN \"<\" FUNC\u001b[0m")
                exit()
            else:
                print("JUMPED FROM: \u001b[31m"+str(oldpos)+"\u001b[0m\nTO: \u001b[36m"+str(pos)+"\u001b[0m")
        if item == ">":
            oldpos = pos
            pos = pos+1
            print("JUMPED FROM: \u001b[31m"+str(oldpos)+"\u001b[0m\nTO: \u001b[36m"+str(pos)+"\u001b[0m")
        if item == "r":
            print("VALUE: \u001b[32m"+str(tape[pos])+"\u001b[0m\nM-ADDRESS:\u001b[36m"+str(pos)+"\u001b[0m")
        if item == "w":
            tape[pos] = reader[i+1]        
        if item == "t":
            print(tape)    