import random
import os
import csv
import UserProfiles



def read_data_from_txt(txt_input):
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
                print('')

        return key_array, value_array

    else:
        print("File not found")
        return [], []


def get_Idea():
    txt_directory = r"C:\Users\lhy854a\PycharmProjects\FYP_callingChatGPT\txt directory"
    txt_files = ["action.txt", "basic.txt", "clothing.txt", "facial expression.txt", "color.txt"]

    for txt_file in txt_files:
        key_array, value_array = read_data_from_txt(txt_file)

        if value_array:
            for _ in range(5):
                seed = random.randint(0, len(value_array) - 1)
                print(value_array[seed] + ',')
        else:
            print(f"No ideas available from {txt_file}")



