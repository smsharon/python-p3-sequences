#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print("[]")
        return
    elif length == 1:
        print("[0]") 
        return    
    a, b = 0, 1  
    fib_sequence = [0]

    for i in range(1, length):
        fib_sequence.append(b)
        a, b = b, a + b  

    print(f"[{', '.join(map(str, fib_sequence))}]") 