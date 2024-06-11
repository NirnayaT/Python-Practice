# i=0
# while True:
#     i+=1
    
#     if(i==11):
#         break
#     print(i)


# words="Hello World"
# for word in words:
#     print(word)
#     for letter in word:
#         if letter=='l':
#             break
#         print(letter)

# string="Hello World"
# for s in string:
#     if(s=='a'or s=='e'or s=='i'or s=='o' or s=='u'):
#         continue 
#     print (s)

# list=[1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1]
# sets=set(list)
# frozen=frozenset(sets)
# print(frozen)
# f=list.append(10)
# print(set(list))
# list.insert(0,0)
# print(list)
# order=set(list)
# o=order[True]
# print(o)


# def sum(a,b):
#     print(a+b)

# sum(1,6)


# for i in range(1,6,2):
#     print(i)




# def is_leap(year):
#     leap = False
#     if year % 4 ==0:
#         print("True")
#     else:
#         print(leap)

# is_leap(2100)

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     a=set(arr)
    
#     for x in a:
#         x=sorted(a)
#         print(x)

# from functools import reduce
# l=[1,2,3,4,5,6]


# new=map(lambda x: x*x*x,l)
# print(list(new))






# for i in range(5): #this is used to set the range for the loop
# 	print(i)

# def function(**meat):
# 	print("i like  "+meat["pork"])

# function (pork="pork",chicken="chicken",buff="buff")



# def function(food):
# 	for f in food:
# 		print(f)

# fruits=["banana","apple","orange"]
# #lists
# function(fruits)


# a="1"
# b=1
# c=int(a) #convertable string to int
# print(b+c) #OUTPUT will be 2


# def leapyear_check(year):
#     Leap = True
#     if year%4==0 or year%400==0 and year%100!=0:
# 	    print(Leap)
#     else:
# 	    print(False)

# leapyear_check(1990)

# a=3.14#float
# b=5#int
# print(a+b)#OUTPUT will be 8.14

# l = [1, 2, 4, 6, 4, 3]
# newl = []
# for item in l:
#   newl.append(cube(item))

# newl = map(lambda x: x*x*x, l)
# print(newl)

# def filter_function(a):
#   return a>2
  
# newnewl = list(filter(filter_function, l))
# print(newnewl)


# from functools import reduce
# l = [1, 2, 4, 6, 4, 3]
# def sum(x,y):
#     return x+y
# r=reduce(sum,l)
# print(r)