# Import library
import json

# Loading the json data as python dictionary, we have two json files:
# One for English to German and the other from German to English

data_Eng2Germ = json.load(open("english_german.json"))
data_Germ2Eng = json.load(open("german_english.json"))


def retrive_Eng2Germ_definition(word):
    # Converting all letters to lower because out data is in that format
    word = word.lower()

    if word in data_Eng2Germ:
        return data_Eng2Germ[word]
    else:
        return "The word doesn't exist, please double check it."


def retrive_Germ2Eng_definition(word):
    # Converting all letters to lowercase
    word = word.lower()

    if word in data_Germ2Eng:
        return data_Germ2Eng[word]
    else:
        return "The word doesn't exist, please double check it."


# Input from user for dictionary choice


choice = input("If you want English to German dictionary press 1 then hit enter, "
               "If you want German to English dictionary press 2 then hit enter! ")

#While loop to choose the dictionary file

i = 1
while i == 1:
    if choice == 1:
        print 'You are at 1'
        Eng_word_user = raw_input("Enter the English word that you want to translate: ")
        print(retrive_Eng2Germ_definition(Eng_word_user))
        break
    elif choice == 2:
        print 'You are at 2'
        Germ_word_user = raw_input("Enter a the German word that you want to translate: ")
        print(retrive_Germ2Eng_definition(Germ_word_user))
        break
    else:
        choice = input("You can choose 1 or 2, please try again!")
        i = 1
