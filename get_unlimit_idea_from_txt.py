import random
import os

def readtxtdata(txt_input):
    txt_directory = r"C:\Users\lhy854a\PycharmProjects\FYP_callingChatGPT\txt directory"
    file_path = os.path.join(txt_directory, txt_input)

    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding="utf-8") as f:
            lines = f.readlines()

        lines = [line.strip() for line in lines if line.strip()]  # Remove empty lines and leading/trailing whitespaces

        key_array = []
        value_array = []

        for line in lines:
            line = line.replace('"', " ")
            line = line.replace(' ', "")
            line = line.replace('\n', "")

            line = line.split(":")
            try:
                key_array.append(line[0])
                value_array.append(line[1])
            except IndexError:
                print("Invalid line format")

        return key_array, value_array

    else:
        print("File not found")
        return [], []

def random_idea():
    txt_input = input("Select which idea aspects you want to choose (e.g., action.txt, basic.txt, clothing.txt, facial expression.txt, color.txt): ")
    num_input = int(input("How many ideas do you want to get? "))

    key_array, value_array = readtxtdata(txt_input)

    for _ in range(num_input):
        if value_array:
            seed = random.randint(0, len(value_array) - 1)
            print(value_array[seed])
        else:
            print("No ideas available for this input")

