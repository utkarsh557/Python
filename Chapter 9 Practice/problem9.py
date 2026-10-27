with open("8this.txt", "r") as f:
    content1 = f.read()


with open("1poems.txt", "r") as f:
    content2 = f.read()

if content1 == content2:
    print("Yes the files are identical")
else:
    print("No the files are not identical")