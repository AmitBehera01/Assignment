# Loop through numbers between 200 and 2500
for num in range(2000, 2501):
    # Check if the number is a multiple of 17 but not a multiple of 5
    if num % 17 == 0 and num % 5 != 0:
        print(num)
