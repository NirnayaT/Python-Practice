# # 1.Write a program to find the sum of all even numbers in a given list using a for loop.

# from functools import reduce

# def sum(a,b):
#     return a+b

# n=int(input("Enter the no of elements to be in the list: "))
# l=[]
# even_list=[]
# for i in range(n):
#     a=int(input(f"Enter the {i+1} number: "))
#     l.append(a)
    
# for x in l:
#     t=0
#     if x % 2 == 0:
#        even_list.append(x)
#     else:
#         pass

# print(reduce(sum,even_list))


# Write a program to print the multiplication table of a given number using a while loop.

# n=int(input("Enter the number for the multiplication table:"))
# m=int(input("Upto how much? : "))
# z = 1
# do:
#     print(f"{n} X {z} =",n*z)
#     z+=1
# while z < m


# Write a program to sort a list of numbers in ascending and descending order.

# list=[]
# n=(int(input("Enter the number the list to be: ")))
# for i in range(n):
#     list.append(int(input(f"Enter the number index {i}: ")))
# print(sorted(list))
# print(sorted(list,reverse=True))


# Write a program to find the maximum and minimum elements in a tuple.

# list=[]
# n=(int(input("Enter the number the tuples to be: ")))
# for i in range(n):
#     list.append(int(input(f"Enter the number index {i}: ")))
# tpl=tuple(list)
# print(tpl)
# print("The minimum is",min(tpl))
# print("The maximum is",max(tpl))

# Write a program that calculates the factorial of a number using a while loop.

# def factorial(n):
#     if n<0:
#         return 0
#     elif n==1 or n==0:
#         return 1
#     else:
#         fact=1
#         while n>1:
#             fact=fact*n
#             n-=1
#         return fact

# n=(int(input("Enter the number: ")))
# print(f"The factorial for {n} is", factorial(n))

# # Write a program that checks if a given string is a palindrome using an if-else statement.

# n=str(input("Enter the string: "))
# reverse_n=n[::-1]
# if n == reverse_n:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# Write a program to count the number of vowels in a given string.

# st=str(input("Enter the string: "))
# t=len(st)
# count=0
# for i in range(t):
#     if st[i]=='a' or st[i]=='e'or st[i]=='i' or st[i]=='o' or st[i]=='u':
#         count+=1
#     else:
#         pass
#         print("Nirnaya")

# print("The number of vowels in the string is: ", count)

# Write a program to merge two dictionaries and sort the resulting dictionary by keys.

# dict1={}
# dict2={}
# result_dict={}
# entry1=int(input("Enter the number of entries of first dictionary: "))
# for i in range(entry1):
#     key=input("Enter Key: ")
#     value=input("Enter Value: ")
#     dict1[key]=value
# ans=str(input("Do you want to make another dictionary? Y/N: "))
# lower_ans=ans.lower()

# if lower_ans == 'y':
#     entry2=int(input("Enter the number of entries of second dictionary: "))
#     for i in range(entry2):
#         key=input("Enter Key: ")
#         value=input("Enter Value: ")
#         dict2[key]=value
# else:
#     print(dict1)
# print(dict1)
# print(dict2)
# ans1=str(input("Do you want to merge this two dictionary? Y/N: "))
# lower_ans1=ans1.lower()
# if lower_ans1 == 'y':
#     dict1.update(dict2)
#     result_dict_asc=dict(sorted(dict1.items()))
#     result_dict_dsc=dict(sorted(dict1.items(),reverse=True))
#     print("Merged and Sorted Dictionary asc: ",result_dict_asc)
#     print("Merged and Sorted Dictionary dsc: ",result_dict_dsc)
# else:
#     print("No merging performed.")
    
    
#Write a program to find the second largest number in a given list.
# def secondmax(list):
#     sublist = [x for x in list if x < max(list)]
#     return max(sublist)

# list=[]
# n=int(input("Enter the number of elements to be in the list: "))
# for i in range(n):
#     a=int(input(f"Enter the {i+1} number: "))
#     list.append(a)
# print(list)
# print("The second greatest number is",secondmax(list))


