import pandas

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dictionary)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#  raise exceptions

# #my solution with while loop
# not_all_letters = True
#
# while not_all_letters:
#     word = input("Enter a word: ").upper()
#     try:
#         output_list = [phonetic_dictionary[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#     else:
#         not_all_letters = False
#         print(output_list)


# Angela's solution with creation of a function
def generate_phonetic():
    word = input("Welcome to the NATO alphabet words generator!\nEnter a word: ").upper()
    try:
        output_list = [phonetic_dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
