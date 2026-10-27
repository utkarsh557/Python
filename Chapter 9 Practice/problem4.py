word = "Donkey"

with open("4-5file.txt", "r") as f:
    content = f.read()

content_new = content.replace(word, "######")

with open("3file.txt", "w") as f:
    f.write(content_new)