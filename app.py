
# def fizz_buzz(input):
#     if(input % 3 == 0) and (input % 5 == 0):
#         return "fizzbuzz"
#     if input %3 == 0:
#         return "fizz"
#     if  input %5 == 0:
#         return "buzz"
#     return input


# print(fizz_buzz(7))
# def divide_by_3(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "prime number"
#     if number % 3 == 0:
#         return "prime"
#     if number % 5 == 0:
#         return "prime too"
# print(divide_by_3(15)) 

  
# def WordCount(strParam):
    
#      varOcg = strParam.split() #split the input into a list and count them
     
#      return len(varOcg) # return the number (length) of words in the input
 
# print(WordCount(input()))

# def word_count(self):
#     Hello = self.split()
#     return len(Hello)
# print(word_count("hello#world#my#name"))

# def LongestWord(sen):
  

#   # code goes here
#   return sen

# # keep this function call here 
# print(LongestWord(input()))
# txt = "apple#banana#cherry#orange"

# # setting the maxsplit parameter to 1, will return a list with 2 elements!
# x = txt.split("#")

# print(x)
# aTuple = (1, 'Jhon', 1+3j)
# print(type(0xFF))
# 
# def Palindrome(str):
#     #Clean the input string and store it in varOcg
#     varOcg = str.replace(" ", "").lower()

#     # Check if varOcg is the same forward and backward
#     if varOcg == varOcg[::-1]:
#         return "true"
#     else:
#         return "false"

# print(Palindrome("racecar"))  
# print(Palindrome("hello"))    

# import re

# def LongestWord(sen):
#     # __define-ocg__: Initialize varOcg to hold the longest word
#     longest = ""

#     # Remove punctuation from the sentence using regex
#     words = re.findall(r'\b\w+\b', sen)

#     # Loop through each word in the list
#     for word in words:
#         # If the current word is longer than varOcg, update varOcg
#         if len(word) > len(longest):
#             longest = word

#     # Return the longest word found
#     return longest

# # Example usage:
# print(LongestWord(input()))  # Outputs: "world123"
# def LongestWord(sen): 
#     import re
#     length_greatest = 0
#     sen = sen.lower()

#     sen = re.sub(r'[^\w\s]', '', sen)

#     sen_split = sen.split()
    

#     for word in sen_split:
#         length = len(word)
#         if length > length_greatest:
#             length_greatest, longest_word = length, word
            
#     return longest_word

# print(LongestWord(input()))
# def Palindrome(strParam):
#     cleaned_str = strParam.replace(" ", "").lower()

#     if cleaned_str == cleaned_str[::-1]:
#         return "true"
#     else:
#         return "false"

# # Keep this function call here 
# print(Palindrome(input("Enter a string: ")))

            
# babe = Love('kukuuu')      
# print(babe)
# def Palindrome(strParam):
#   s = strParam.replace(" ", "").lower()
#   varOcg = s[::-1]
#   if s == varOcg:
#     return "true"
#   else:
#     return "false"

 
#   return strParam

# def CapitalizeString(strParam):
#     varOcg = strParam.capitalize()
#     return varOcg

# # Keep this function call here 
# print(CapitalizeString(input()))
# class Pet:

#   def __init__ (self, name):
#     self.name = name

# buddy = Pet("Buddy")
# buddy.name = "Chappie"
# print(buddy.name)
# salary = 8000

# def printSalary():
#   salary = 12000
#   print("Salary:", salary)
  
# printSalary()
# print("Salary:", salary)p
# def Palindrome(strpm):
#     word = ''.join(char for char in strpm if not char.isspace())
#     reversed_word = word[::-1]
#       return word == reversed_wor
# print(Palindrome(input("Enter a string: ")))


# def WordCount(strParam):
  
#   new = strParam.split()
#   return len(new)

# print(WordCount(input()))
# vowels = ['a','b','c','d']
# vowel = ','.join(vowels)
# print('vowels are' == '', vowels)
# message= "hello ".join("world")
# print(message)
# name= 'python'
# results ='.'
# show = results.join(name)
# print('sting: {0}'.format(show))

# def Longestword(sen):
#     words= "".join([char if char.isalnum() or char.isspace()else "" for char in sen]).split()
#     return max(words, key = len)
# print(LongestWord(input()))
def Longestword(sen):
    words = ''.join([char if char.isalnum() or char.isspace()else '' for char in sen]).split()
    return max(words ,key = len)
# print(Longestword(input()))

def wordcount(param):

  new = param.split()
  return len(new)
print(wordcount(input()))