def numero_primo():
    for number in range(1,101):

        if number >= 2:
            divisible = False    
            for i in range(2,number):
                if number % i == 0:
                    divisible = True
                    break
            if not divisible:    
                print(number)

numero_primo()
  