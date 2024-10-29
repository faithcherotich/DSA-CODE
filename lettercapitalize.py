# def LetterCapitalize(str):
#     #split the string into words& capitalize each then join
#     return ' '.join(word.capitalize() for word in str.split())

# inputs = "hello word"  
# output = LetterCapitalize(inputs)
# print(output) 


# def LetterCapitalized(str):
#     capitalized = [word.capitalize() for word in str.split(" ")]
#      return ' '.join(capitalized)

# Example usage
# input_str = "hello world"
# output = LetterCapitalized(input_str)
# print(output)  # Output: "Hello World"


def LetterCapitalize(s):
    return s.title()

# Example usage
input_str = "hello world"
output = LetterCapitalize(input_str)
print(output)  

