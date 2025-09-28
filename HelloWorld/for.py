# for num in range(1, 4):
#     print("Att", num, num * ".")

# o/p:
# Att 1 .
# Att 2 ..
# Att 3 ...

successful = False
for num in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
# o/p: if successful = True
# Attempt
# Successful

#o/p: if successful = False
# Attempt
# Attempt
# Attempt
# Attempted 3 times and failed


#Iterating over a collection(Iterable)
shopping_cart = ["apple", "banana", "mango"]
for item in shopping_cart:
    print(item) 