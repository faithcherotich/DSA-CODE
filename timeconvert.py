# def TimeConvert(num):
#     hours=num // 60
#     # // interger division it divides a num by 60 and returns the whole number in hours
#     minutes = num % 60
#     # used to find the remainder when num is divided by 60
#     return f"{hours}:{minutes}"

# inputs = 64
# output= TimeConvert(inputs)

# print(output)


def TimeConvert(num):
    return f"{num // 60}:{num % 60}"


inputs = 64
output = TimeConvert(inputs)

print(output) 

