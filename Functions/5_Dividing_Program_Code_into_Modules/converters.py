def m_to_cm(n):
    return n * 100

def cm_to_m(n):
    return n / 100

def cm_to_inch(n):
    return n / 2.54

def ft_inch_to_cm(feet, inches):
    total_inches = (feet * 12) + inches
    return total_inches * 2.54

if __name__ == "__main__":
    # Test the functions directly when this module is run
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'100cm = {cm_to_inch(100):.2f} inches')
    print(f'5 feet 8 inches = {ft_inch_to_cm(5, 8)}cm')
