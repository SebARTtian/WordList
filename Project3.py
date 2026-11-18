def num_letters(num_rows, num_cols):
    return num_rows * num_cols

    
assert num_letters(3, 4) == 12  #3 is the num_rows and 4 is the num_columns
assert num_letters(6, 6) == 36  
assert num_letters(10, 5) == 50
assert num_letters(3, 9) == 27

print("Checking assertions.")
