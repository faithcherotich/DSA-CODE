# Question1: 👇👇                                                                       #Count characters
from collections import Counter

def count_characters(s: str) -> dict:
   
    return dict(Counter(s))

input_string = "hello world"
character_counts = count_characters(input_string)
print(f"Character counts: {character_counts}")
