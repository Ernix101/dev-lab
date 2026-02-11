import numpy as np

array = np.arange(1, 91)

# print(np.sqrt(array))
# Now let's reshape it into a 3 by 4 & 2D array
array_1d = np.arange(1, 13)
array_2d = array_1d.reshape(3, 4)

# print(f"{array_2d}\n")
# print(f"number at location is {array_2d[0, 1]}")  # Element in the first row, second column
# print(array_2d[-1, :])   # Last row

# print(array_2d[0::2, :])       # Slicing every other 2nd row from 0
# print(array_2d[0:2, 0:3])          # Slicing columns 1 to 3 (inclusive) from rows 0 to 1
# print(array_2d[::-1, :])            # Reversed the order of the rows


# ----------------------------Sclarar and element wise arithmetic
array1_1d = np.array([1, 2, 3, 4])
array2_1d = np.array([10, 20, 30, 40])

# print(array1_1d + array2_1d)
# print(array1_1d - array1_1d)
# print(array1_1d * array2_1d)
# print(array2_1d / array1_1d)
# print(np.power(array1_1d, 2))       # Power of 2 for first 1d array


row_vector = np.array([[1, 2, 3, 4, 5]])         # Broadcasting in action btw both vectors with different shapes
column_vector = np.array([[10], [20], [30]])

# print(row_vector.shape)
# print(column_vector.shape)
# print(row_vector * column_vector)

data = np.array([  [5, 12, 8, 3, 9], 
                   [22, 7, 15, 4, 11],
                   [1, 18, 6, 14, 2], 
                   [20, 10, 19, 13, 16] ])

# print(np.sum(data))
# print(np.sum(data, axis=1))     # Axis of 1 is across the rows and 0 is across the columns
print()

# print(np.mean(data))
# print(np.std(data))
# print(np.var(data))
# print(np.min(data))
# print(np.max(data, axis=1))

# print(np.argmax(data))                   # Index of greatest value.  there's also argmin
# print(np.argmin(data))                   # Index of greatest value.  there's also argmax
# print(data[data > 10])                  # Return all values greater than 10
# print(data[data % 2 == 0])                  # Return even numbers

# data[data < 5] = 0                          # Replace all numbers less than 5 with 0 (but it's manual)

# smalller_data = data[data >= 5]                  # Returns the data but it's flattened to a 1d array
smalller_data = np.where(data >= 5, data, 0)        # 0 replaces all data below 5 AND reurns a full array

# print(smalller_data)



#-------------------random number generator-------RNG-------------
rng = np.random.default_rng()

# print(rng.integers(low=1, high=101, size=20))           # 20 random integers between 1 and 100

# print(rng.integers(low=1, high=101, size=(5, 3)))         # A (5 x 4) array of random numbers


np.random.seed(seed=1)                                      # Seeds set the same values for the array

# print(np.random.uniform(low=0, high=1))                     # A uniformly random floats number btw 0 and 1
# print(np.random.uniform(low=0, high=1, size=3))                     # 3 uniformly random floats numbers btw 0 and 1
# print()
# print(np.random.uniform(low=0, high=1, size=(3, 2)))                     # 3 by 2 array of uniformly random floaating point numbers btw 0 and 1


fruits = np.array(["🍎", "🍊", "🍌", "🥥", "🍍"])

# fruits = rng.shuffle(fruits)                                             # Mix up of all fruits 
# fruit = rng.choice(fruits)                                      # Prints a random fruit
# fruit = rng.choice(fruits, size=3)                                      # Prints 3 random fruits
fruit = rng.choice(fruits, size=(3, 3))                                      # Prints a 3 by 3 array of random fruits

# print(fruit)

# 2-----------Stretch, extra research------------
array25 = np.arange(1, 25)     # 1D array

# Reshape into a 4 by 6 array
new_array1 = array25.reshape(4, 6)
# Reshape into 2 by 3 by 4 array (3D)
new_array_3d = array25.reshape(2, 3, 4)

# print(new_array1)
# print(new_array_3d)

array_one = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
array_two = np.array([[13, 14, 15, 16],[17, 18, 19, 20],[21, 22, 23, 24]])
array_three = np.arange(1, 13)
array_four = np.arange(1, 13)

new_array_one = array_one.reshape(3, 4)
new_array_two = array_one.reshape(3, 4)
new_array_three = array_three.reshape(3, 4)
new_array_four = array_four.reshape(3, 4)


# Vertially stack 2 (3x4) arrays
stacked_array_vstack = np.vstack((array_one, array_two))
stacked_array_concat1 = np.concatenate((new_array_one, new_array_two), axis=1)
stacked_array_concat2 = np.concatenate((new_array_three, new_array_four), axis=0)
# print(stacked_array_concat2)

#---------student scores------------------------

hundred_students = np.random.random_integers(low=40, high=100, size=(100, 5))

# print(hundred_students)
mean_per_student_row = np.mean(hundred_students, axis=0)   # Each row    average per subject
mean_per_student_col = np.mean(hundred_students, axis=1)    # Each column      average per student
# print(mean_per_student_col)

above50 = hundred_students[hundred_students > 50]
ranked_scores = np.sort(hundred_students)
print(above50)

