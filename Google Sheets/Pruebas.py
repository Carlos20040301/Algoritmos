import gspread
import random
import pygsheet
import array

arr = []

for i in range(10):
     z = random.randrange(1,10)
     arr.append(z)

print(arr)

for i in range (10):
    print(arr[i])
