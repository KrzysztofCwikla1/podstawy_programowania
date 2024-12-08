def f(n):
    return ''.join(map(str, range(1, n + 1)))   #range creates the list of integers 
                                                #map applies the str fucntion to all list elemenents,
                                                #then join combines the elements of the list to a string

if __name__ == "__main__":                     
    print(f(11))