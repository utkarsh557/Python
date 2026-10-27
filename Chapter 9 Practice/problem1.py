# with open("poems.txt") as p:
#     st = p.read()
    
#     if (st.find("Twinkle") == -1):
#         print("File does not have the word Twinkle")
#     else:
#         print("File contains the word Twinkle")

with open("poems.txt") as p:
    st = p.read()
    
    if ("Twinkle" in st):
        print("File contains the word Twinkle")
    else:
        print("File does not have the word Twinkle")

