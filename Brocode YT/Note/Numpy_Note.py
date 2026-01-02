import numpy as np

# array = np.array([1, 2, 3, 4, 5])

# array = array * 2 #? Multiply each element by 2, python cant do this with normal lists

# print(array)


# #?---------------------------------
# #?---------array dimensions--------
# #?---------------------------------

# array = np.array([['A','B','C','D'],   #? 2D array
#                   ['A','B','C','D'],   #? need same number of elements in each sub-array
#                   ['A','B','C','D']])

# print(array.ndim) #? dimension of array


# array = np.array([[['A','B','C','D'], ['A','B','C','D'], ['A','B','C','D']]     #? 3D array
#                   , [['E','F','G','H'], ['A','B','C','D'], ['A','B','C','D']]   #? need same number of elements in each sub-array
#                   , [['A','B','C','D'], ['A','B','C','D'], ['A','B','C','D']]])

# print(array.ndim) #? dimension of array
# print(array.shape) #? shape of array (layers, rows, columns)(3, 3, 4)

# #?-----------chain indexing to get specific element-----------
# print(array[1,0,2]) #? G because its in 2nd layer, 1st row, 3rd column

# #?-----------get multiple elements to form a word-----------
# word = array[0,1,3] + array[2,2,0] + array[1,0,1] #? D + A + F +
# print(word)  #? DAF 


# #?---------------------------------
# #?-------------SLICING-------------
# #?---------------------------------

# array = np.array([[1, 2, 3, 4], 
#                   [5, 6, 7, 8], 
#                   [9, 10, 11, 12],
#                   [13, 14, 15, 16]])

# #?array[start:end:step] 

# #?accessing rows
#print(array[0:3]) #? ends at index 3 but doesnt include index 3(exclusive)
#output:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
#print(array[0:4:2]) #? step of 2
#output:
# [[ 1  2  3  4]
#  [ 9 10 11 12]]

# #?accessing columns
# print(array[:, ::2]) #? all rows, every 2nd column (Rows,Columns)
#output:
# [[ 1  3]
#  [ 5  7]
#  [ 9 11]
#  [13 15]]

# #?combine row and column access
# print(array[0:2, 0:2]) #? rows 0 and 1, columns 0 and 1
# print(array[0:2, 2:4]) #? rows 0 and 1, columns 2 and 3
# print(array[2:4, 2:4]) #? rows 2 and 3, columns 2 and 3

# #?---------------------------------
# #?------arithmetic operations------
# #?---------------------------------

# array = np.array([1, 2, 3, 4])

# #?element-wise arithmetic operations 
# print(array + array)  #? addition
# print(array - array)  #? subtraction
# print(array * array)  #? multiplication
# print(array / array)  #? division
# print(array ** 2)     #? exponentiation

# #? mathematical functions 
# array2 = np.array([5, 6, 7, 8])
# print(np.sqrt(array2))     #?square root
# print(np.floor(array2))    #?floor
# print(np.ceil(array2))     #?ceil is rounding up
# print(np.round(array2))    #?round
# print(np.pi)               #?prints value of pi  

# #?comparison operations
# scores = np.array([70, 85, 90, 55, 60])
# pass_mark = 60
# print(scores >= pass_mark) #?check which scores are passing

# scores[scores < pass_mark] = 0 #?set all failing scores to 0
# print(scores)


##?---------------------------------
##?-----------broadcasting-----------
##?----------------------------------
#* broadcasting allows numpy to perform operations on arrays of different shapes
#* similar to matric multiplication but not exactly the same
#* key rule: the dimensions of the smaller array are "stretched" to match the dimensions of the larger array
#* for each dimension, the sizes must either be the same or one of them must be 1

# array1 = np.array([[1, 2, 3]])          #?shape (1, 3) , (column, row)
# array2 = np.array([[1],[4],[5],[6]])    #?shape (4, 1)
                   
# print(array1 * array2)
# #output:
# # [[ 1  2  3]
# #  [ 4  8 12]
# #  [ 5 10 15]
# #  [ 6 12 18]]
# #?shape of result is (4, 3) - numpy automatically expanded the dimensions of the smaller array to match the larger array

# array1 = np.array([[1, 2, 3, 4,5,6,7,8,9,10]])                   #? shape (1, 10) 
# array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])    #? shape (10, 1)
# print(array1 * array2)                                           #? shape of result is (10, 10)


# #?--------------------------------------
# #?---------aggregation functions--------
# #?--------------------------------------

# array = np.array([[1, 2, 3, 4],
#                   [5, 6, 7, 8]])

# print(np.sum(array))          #?sum of all elements output: 36
# print(np.mean(array))         #?mean of all elements output: 4.5
# print(np.median(array))       #?median of all elements output: 4.5
# print(np.std(array))          #?standard deviation of all elements output: 2.29128784747792
# print(np.var(array))          #?variance of all elements output: 5.25
# print(np.min(array))          #?minimum element output: 1
# print(np.max(array))          #?maximum element output: 8
# print(np.argmin(array))       #?index of minimum element output: 0
# print(np.argmax(array))       #?index of maximum element output: 7

#? axis meaning:
#? axis=0 operation the rows for each column
#? axis=1 operation across the columns for each row
# print(np.sum(array, axis=0))  #?sum of each column output: [ 6  8 10 12]
# print(np.sum(array, axis=1))  #?sum of each row output: [10 26]


##? --------------------------------------
##? --------------filtering---------------  
##? --------------------------------------

# ages = np.array([[22, 25, 18, 60, 27, 19, 24],
#                  [20, 23, 26, 28, 21, 69, 17]])

# # #? filtering arrays
# # teenagers = ages[ages < 20]                 #?get all ages less than 20
# # adults = ages[(ages >= 20) & (ages < 60)]   #?get all ages between 20 and 59
# # seniors = ages[ages >= 60]                  #?get all ages 60 and above
# # evens = ages[ages % 2 == 0]                 #?get all even ages
# # odds = ages[ages % 2 != 0]                  #?get all odd ages

# # print("Teenagers:", teenagers) 
# # print("Adults:", adults)    
# # print("Seniors:", seniors)    
# # print("Even ages:", evens)
# # print("Odd ages:", odds)

# # #!filtering and preserving original shape
# adult = np.where(ages >= 20, ages,np.nan) #?set all non-adult ages to 0
# print(adult)


##? --------------------------------------
##? -------random number generation-------
##? --------------------------------------

# rng = np.random.default_rng(seed=1)  #?create a random number generator instance, seed ensures reproducibility
# print(rng.integers(low=1, high=101, size=(10,2)))  #?random integer between 1 and 100
# #? size specifies the shape of the output array (10 rows, 2 columns)

# np.random.seed(1)  #?set seed for reproducibility    
# print(np.random.uniform(low=-1, high=1, size=(3,2)))  #?random float between -1.0 and 1.0
# #? uniform means all numbers in the range are equally likely

# rng = np.random.default_rng(seed=1)  #?create a random number generator instance
# fruits = np.array(['apple', 'banana', 'cherry', 'date', 'blueberry'])
# fruit = rng.choice(fruits, size=(3,2))  #?randomly select 6 fruits and arrange them in a 3x2 array
# print(fruit)


































