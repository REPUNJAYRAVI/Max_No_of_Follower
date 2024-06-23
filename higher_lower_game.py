#import the game logo from art page
from art import higher_lower , vs
#import data for game
from higher_game_data import data
#import random module
import random
#function for fetching data
def format_data(account):
    name = account["name"]
    profession = account["description"]
    origin = account["country"]
    return f"{name}, a {profession}, from {origin}"

#function to calculate the user score
def check_ans(count_a,count_b,user_input):
    if count_a > count_b:
        return user_input == "a"
    else:
        return user_input == "b"

def game():
    #assigned variable for tracking Player score
    final_score = 0
    
    #random account selection for game data
    account_a =random.choice(data)
    account_b =random.choice(data)

    while True:
        if account_a == account_b:
            account_b = random.choice(data)
        #assigns the followers count
        count_a = account_a["follower_count"]
        count_b = account_b["follower_count"]
        #pints the game logo
        print(higher_lower)
        #print("""Hey Welcome to the Higher Lower game, in this game you need to guess the person
        #who is having the highest number of Instagram Followers. So are you ready? Lets Go !!
        #""")
        #prints the format for comparision
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")
        #guessing the input by user
        user_input = input("Who has more Followers? Type 'A' or 'B':").lower()
        #for checking the answer
        ans_correct = check_ans(count_a,count_b,user_input)

        if ans_correct:
           final_score +=1
           print(f"You are right !! Your current score is {final_score}")
           account_a = account_b
           account_b = random.choice(data)
        else:
            print(f"Sorry that's wrong, Your score {final_score}")
            break
#start the game
game()             

