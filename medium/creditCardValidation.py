#credit card validation
import argparse
import re 

def luhn_algorithm(card_number): 
    def digits_of(n): 
        return [int(d) for d in str(n)] 
    digits = digits_of(card_number) 
    odd_digits = digits[-1::-2] 
    even_digits = digits[-2::-2] 
    checksum = sum(odd_digits) 
    for d in even_digits: 
        checksum += sum(digits_of(d*2)) 
    if checksum % 10 == 0 and len(str(card_number)) == 16:
        return("valid")
    else:
        return("not valid")

print(luhn_algorithm(int(input())))

