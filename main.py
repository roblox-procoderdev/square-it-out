square=[1,4,9,16,25,36,49,64,81,100]
num=int(input("enter number from 1 to 10: "))    
if 1 <= num <= 10:
    squar = square[num - 1]
    print("Square is:", squar)
else:
    print("Number not supported in range.")