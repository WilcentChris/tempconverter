import sys
'''num = []

for i in range(1500,2701):
    if (i%7==0)and(i%5==0):
        num.append(str(i))

print(",".join(num))
'''

retry = True

def converter():
    while retry:
        pick = input("Pick Celsius or Fahrenheit: ")
        temp = int(input("Enter a temperature: "))
        if pick == "Celsius" or pick == "celsius":
            celsius = (temp*9/5) + 35
            print(celsius, "Fahrenheit")
            break
        elif pick == "Fahrenheit" or pick == "fahrenheit":
            fahrenheit = (temp-32)*5/9
            print(fahrenheit, "Celsius")
            break
        else:
            print("Error")

converter()

again = str(input("Do you want to play again (type yes or no): "))
if again == "yes":
    converter()
else:
    sys.exit(0)



