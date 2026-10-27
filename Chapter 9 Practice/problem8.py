with open("8this.txt", "r") as f:
    lines = f.readlines()

with open("8copy.txt", "w") as f:
    for line in lines:
        f.write(line)