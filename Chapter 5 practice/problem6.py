d = {}

for i in range(4) :
  name = input("Enter your name : ")
  lang = input("Enter your fav language : ")
  d.update({
    name : lang
  })

print(d)