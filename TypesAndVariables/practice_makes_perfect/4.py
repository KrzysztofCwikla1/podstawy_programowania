###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170
feet = int(cm // 30.48)

remainder = cm % 30.48

inches = remainder/2.54
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches:.0f} inches')