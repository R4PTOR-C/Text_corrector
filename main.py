from autocorrect import Speller


print("Welcome to text corrector. ")
print("Your text: ")
text_with_errors = input()
def proofread(text):
    spell = Speller(lang='en')
    corrected_text = spell(text)

    print("Correction: {}".format(corrected_text))




proofread(text_with_errors)

print("Thanks for using text corrector")