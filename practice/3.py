'''
Comprehensions in Python provide us with a short and 
concise way to construct new sequences (such as lists, sets, dictionaries, etc.) 
using previously defined sequences. 

Python supports the following 4 types of comprehension:

1.List Comprehensions
2.Dictionary Comprehensions
3.Set Comprehensions
4.Generator Comprehensions

1. List Comprehension:
    - List comprehension provides an elegant way to create new list.
    
    Syntax:
        output_list = [output_exp for var in input_list if (var satisfies this condition)]


    Example:
    
'''
list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

listcomprehension = [var for var in list if var % 2 == 0]

print("Output List using list comprehensions:",listcomprehension)

'''
2. Dictionary Comprehension:
    - Extending the idea of list comprehensions, we can also create a 
    dictionary using dictionary comprehensions.
    
    Syntax:
        output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}
        
    Example:
'''
list = [1,2,3,4,5,6,7]

dictcomprehension = {var:var ** 3 for var in list if var % 2 != 0}

print("Output Dictionary using dictionary comprehensions:",dictcomprehension)

'''
3. Set Comprehension:
    - Set comprehensions are pretty similar to list comprehensions. 
    The only difference between them is that set comprehensions use curly brackets { }

    Syntax:
        output_list = {output_exp for var in input_list if (var satisfies this condition)}
    Example:
'''
list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

setcomprehension = {var for var in list if var % 2 == 0}

print("Output Set using set comprehensions:",setcomprehension)

'''
4. Generator Comprehension:
    - Generator Comprehensions are very similar to list comprehensions. 
    One difference between them is that generator comprehensions use circular brackets 
    whereas list comprehensions use square brackets. The major difference between them 
    is that generators don’t allocate memory for the whole list. Instead, they generate 
    each value one by one which is why they are memory efficient.
'''
list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

gencomprehension = (var for var in list if var % 2 == 0)

print("Output values using generator comprehensions:", end = ' ')

for var in gencomprehension:
	print(var, end = ' ')


