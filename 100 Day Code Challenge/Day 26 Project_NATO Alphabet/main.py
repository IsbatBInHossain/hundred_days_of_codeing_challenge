import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

while True:
    name = input("Enter your nane: ")
    try:
        nato_code = [nato_dict[letter.upper()] for letter in name]
    except KeyError:
        print("Enter alphabets only please")
    else:
        print(nato_code)
        break
