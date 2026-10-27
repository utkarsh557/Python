import random

def game():
    print("You are playing game..")
    score = random.randint(1, 4567)

    #Fetch the hi score
    with open("2hi_score.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score is : {score}")
    if(score > hiscore):
        #write this score to file 
        with open("2hi_score.txt", "w") as f:
            f.write(str(score))

    return score

game()