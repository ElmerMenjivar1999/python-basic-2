#FizzBuzz

num = int(input("Digite el rango de fizzbuzz: "))

output = []

for i in range(1,num+1):
    divisible_by_5 = (i % 5 == 0)
    divisible_by_3 = (i % 3 == 0)

    if divisible_by_5 and divisible_by_3:
        output.append("FizzBuzz")
    if divisible_by_3:
        output.append("Fizz")
    if divisible_by_5:
        output.append("buzz")
    else:
        output.append(i)
print(output)                    