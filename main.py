student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)


import pandas
student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(index)
#     print(row)
#     if row.student == "Angela":
#         print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#  raise exceptions

# my solution with while loop
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
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
