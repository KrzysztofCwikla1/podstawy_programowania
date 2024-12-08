def f(number):
    number_str = str(number)
    total = 0
    checked = [] 

    for digit in number_str:
        if digit not in checked:            #checks if a digit already occured 
            count = number_str.count(digit)                                            
            if count > 1:                   #if it occured atleast 2 times it adds every instance of the number to the total
                total += int(digit) * count
            checked.append(digit)           # add the digit to the checked list
    
    return total

if __name__ == "__main__":
    print(f(230335))       # Output: 9
    print(f(513553007))   # Output: 21
    print(f(1027))        # Output: 0