import pandas

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

df = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word : ").upper()

output_letter = [phonetic_dict[letter] for letter in word]

print(output_letter)