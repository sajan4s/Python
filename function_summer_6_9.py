# Function to ignore the numbers 6 and 9 and numbers between then and find sum of the rest

def summer_69(arr):

     total = 0
     add = True

     for n in arr:
         while add:
             if n != 6:
                 total += n
                 break
             else:
                 add = False
         while not add:
             if n != 9:
                 break
             else:
                 add = True
                 break
     return total


print(summer_69([2,6,9,11,3]))