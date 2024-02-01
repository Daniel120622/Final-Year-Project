import get_unlimit_idea_from_txt
import HumanParameterChange
import os
import get_N_idea_from_txt_csv


cont = True
def continous(x):
    if x == "-1":
        cont = False


while cont:
#Ask user which function you want to use.
    user_input = input("Which function you want to use? OneIdea, Parameter Change, ChatGPT Bot, N idea \n")
    if user_input == "OneIdea":
        get_unlimit_idea_from_txt.random_idea()
        continous(input("Continous?"))
    elif user_input == "Parameter Changes":
        x = HumanParameterChange.giveFeedback(input("Which function you want to choose \n"))

        continous(input("Continous?"))
    elif user_input == "ChatGPT Bot":
        print("Not yet done")
        continous(input("Continous?"))

    elif user_input == "N Idea":
        get_N_idea_from_txt_csv.get_Idea()

        print("\n")
        continous(input("Continous?"))
    else:
        print("Wrong Input. Please try again")



