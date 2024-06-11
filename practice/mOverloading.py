class math:
        
    def area(self, length, b=0):
        if b == 0:
            return 3.14*length*length
        else:
            return length*b       

obj1 = math()
print(obj1.area(14))