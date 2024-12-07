import converters

print('### Test converters')

# Test m_to_cm
print(f'Two meters is {converters.m_to_cm(2)} cm')

# Test cm_to_m
print(f'532 cm is {converters.cm_to_m(532):.2f} m')

# Test cm_to_inch
print(f'100 cm is {converters.cm_to_inch(100):.2f} inches')

# Test ft_inch_to_cm
print(f'5 feet 8 inches is {converters.ft_inch_to_cm(5, 8):.2f} cm')
