# Codewars Bar recommends you drink 1 glass of water per standard drink so you're not hungover tomorrow morning.

#Your fellow coders have bought you several drinks tonight in the form of a string. Return a string suggesting how many glasses of water you should drink to not be hungover.

# import re

# def hydrate(drinks: str) -> str:
#     # Find all digits in the input string and sum them up
#     total_drinks = sum(int(num) for num in re.findall(r'\d+', drinks))
    
#     # Return the appropriate string based on the total count
#     if total_drinks == 1:
#         return "1 glass of water"
#     else:
#         return f"{total_drinks} glasses of water"

# # Example usage:
# print(hydrate("1 beer"))           # Output: "1 glass of water"
# print(hydrate("2 glasses of wine and 1 shot"))  # Output: "3 glasses of water"
# print(hydrate("5 shots and 2 beers"))  # Output: "7 glasses of water"



def hydrate(drinks: str) -> str:
    # Sum up all digit characters in the input string as integers
    total_drinks = sum(int(char) for char in drinks if char.isdigit())
    
    # Return the appropriate string based on the total count
    if total_drinks == 1:
        return "1 glass of water"
    else:
        return f"{total_drinks} glasses of water"

# Example usage:
print(hydrate("1 beer"))           # Output: "1 glass of water"
print(hydrate("2 glasses of wine and 1 shot"))  # Output: "3 glasses of water"
print(hydrate("5 shots and 2 beers"))  # Output: "7 glasses of water"