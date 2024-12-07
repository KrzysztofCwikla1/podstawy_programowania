def f(password):
    if len(password) < 6:
        return False
    
    seen_chars = []
    for char in password:
        if char in seen_chars:
            return False 
        seen_chars.append(char) #append adds an object to the end of the list
    
    return True 

if __name__ == "__main__":
    print(f("ax15"))        
    print(f("book123"))    
    print(f("A2water3"))  
    print(f("qwerty"))
    print(f(""))