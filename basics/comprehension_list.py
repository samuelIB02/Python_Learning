numbers = [3, 8, 12, 5, 20, 7] 

result = [ 
    number * 3 for number in numbers 
    if number % 2 == 0 ] 


print(result)