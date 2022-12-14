# Importing Language detector form detect module
from langdetect import detect
# Taking user input
text = input("Enter any text in any language: ")
# Outputting predicted output
print(detect(text))
