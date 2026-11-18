import numpy as np

def num_letters(num_rows, num_cols):
    return num_rows * num_cols
    
assert num_letters(3, 4) == 12  #3 is the num_rows and 4 is the num_columns
assert num_letters(5, 6) == 30  
assert num_letters(10, 5) == 50
assert num_letters(3, 9) == 27

print("Checking assertions.")


data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')


words = [] #this will store the letters we extract from the data file
rows, columns = data.shape  #this gives you the number of rows and number of columns in the data file

for r in range(rows):
    for c in range(columns):
        words.append(str(data[r, c]))

print(words) #check that you collected all the letters in your data file

assert len(words) == num_letters(rows, columns) 

  #this should not throw an error. If it does, most likely your main code is not getting the correct number of letters
