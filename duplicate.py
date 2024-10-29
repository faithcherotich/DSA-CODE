def duplicate(arr):
   
    elements = set()
    for num in arr: 
        if num in elements:
            return True  
        elements.add(num)  
    return False  

arr2 = [1, 2, 3, 4, 5, 1, 2]
print(duplicate(arr2))  
        
    
    
    