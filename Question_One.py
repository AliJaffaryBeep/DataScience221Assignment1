threshold = 100
product = 1
currentNumber = 1

while product <= threshold:

    currentNumber += 1

    product = product * currentNumber


print("Final Product: " , product)
print("Integer that caused the product to exceed the threshold number:" , currentNumber)

