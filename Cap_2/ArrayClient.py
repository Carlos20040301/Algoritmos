import Array
maxSize = 10 
arr = Array.Array(maxSize) 
arr.insert(77) 
arr.insert(44)
arr.insert(5)
arr.insert(9)
arr.insert(44)
arr.insert(555)
arr.insert(12.34)
arr.insert(0)
arr.insert(2)
arr.insert(-17)

m=arr.getMaxNum()
arr.traverse()
print("El máximo es:", m)

arr.deleteMaxNum()
print("Search for 555, returns", arr.search(555))


arr.traverse()
