#!/usr/bin/env python3

def print_fibonacci(length):
   
    fibonacci_sequence = []
    
   
    if length <= 0:
        print(fibonacci_sequence)
        return
    
   
    for i in range(length):
        if i == 0:
            
            fibonacci_sequence.append(0)
        elif i == 1:
            
            fibonacci_sequence.append(1)
        else:
            
            fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    
   
    print(fibonacci_sequence)


print_fibonacci(10)  
            