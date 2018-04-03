def main():

    addition = 3 + 4

    subtraction = 4 - 3

    multiplication = 3 * 4

    division = 12 / 3

    exponent = 3 ** 4

    no_float = 12 // 3

    remainder = 7 % 2

    print (addition)
    print (subtraction)
    print (multiplication)
    print (division)
    print (exponent)
    print (no_float)
    print (remainder)

#these are all the math operators (above)


# if statements

    numb = 1
    if numb == 1:
        print("one")
    elif numb == 2:
        print("two")
    else:
        print("biggie smalls")


# while loops

    i = 0
    while i<5:
        print ('hello')
        i += 1


# nested loops

    x = 0
    y = 0
    while x < 5:
        while y < 5:
            print(y, end=" ")
            y += 1
        print('\n############')
        y = 0
        x += 1


# range in loops

    for number in range(12,20):
        print(number)


# boolean operators

    x = 41
    if x == 42:
        print('equals')
    elif x != 42:
        print('not equal')
    elif x > 42:
        print('greater than')
    elif x >= 42:
        print('greater than or equal to')
    elif x < 42:
        print('less than')
    elif x <= 42:
        print('less than or equal to')
    else:
        print('i am slowly gaining consciousness')

#lists

    #this is a list
    fruits = ['apple', 'orange', 'banana', 'grape']

    #the zero is the first position
    first_fruit = fruits[0]

    #negative numbers move backwards
    last_fruit = fruits[-1]

    #for loops through the list
    for fruit in fruits:
        print(fruit)

#arrays

    two_fruits = fruits[1:3]

#dictionaries

    fav_foods = {'cheese': 'american', 'meat': 'chicken', 'vegetable': 'potatoes'}

#returning a keyword within a dictionary
    fav_meat = fav_foods['meat']

#iteration through keys and values
    for food_type, food in fav_foods.items():
        print('My favorite ' + food_type + ' is: ' + food)

#you can indent to improve readability
    fav_foods2 = {'cheese': 'american',
                  'meat': 'chicken',
                  'vegetable': 'potatoes',
                  'dessert': 'ice cream',
                  'pringles': 'buffalo ranch'
                  } 



main()
