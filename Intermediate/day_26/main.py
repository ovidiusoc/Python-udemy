
import pandas


alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter:row.code for (index, row) in alphabet_data_frame.iterrows()}
print(nato_alphabet_dict)

message = input("Send a message: \n")

list = [nato_alphabet_dict[letter.upper()] for letter in message]
print(list)