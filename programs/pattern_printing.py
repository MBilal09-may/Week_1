#Pattern Printing

pattern = "*"
number =int(input("Enter a number: "))
# A function which print stars in a pattern
def pat():
    for star in range(1,number+1):
        print(star * pattern)
pat()