# def fibonacci(num):
#     if num == 0 or num == 1:
#         return num
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)
# result = fibonacci(15)
# print(result)  

def fibonacci():
    prev = 0
    next = 1
    for i in range(0,50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib
        
fibonacci()        