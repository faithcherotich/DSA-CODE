def custom_fizzbuzz(fizz: str = "Fizz", buzz: str = "Buzz", fizz_num: int = 3, buzz_num: int = 5) -> list:
    result = []
    
    for i in range(1, 101):
        if i % fizz_num == 0 and i % buzz_num == 0:
            result.append(fizz + buzz)
        elif i % fizz_num == 0:
            result.append(fizz)
        elif i % buzz_num == 0:
            result.append(buzz)
        else:
            result.append(str(i))
    
    return result

# Example usage:
print(custom_fizzbuzz())  # Classic FizzBuzz from 1 to 100
print(custom_fizzbuzz("Foo", "Bar", 2, 7))  # Custom FizzBuzz with "Foo" for multiples of 2 and "Bar" for multiples of 7