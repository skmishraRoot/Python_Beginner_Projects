# Need to setup detect before using this for help link:https://pypi.org/project/detect/
# Importing Language detector form detect module
from langdetect import detect
# Taking user input
text = input("Enter any text in any language: ")
# Outputting predicted output
print(detect(text))
