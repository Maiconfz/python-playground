'''
@author: Maiconfz
'''

## Assigning string to variables ##

firstName = "Maicon"
middleName = "Fonseca"
lastName = "Zanco"

## Printing strings ##
print("First name:")
print(firstName)

print("\nMiddle name:")
print(middleName)

print("\nLast name:")
print(lastName)

## Concat strings ##

fullName = firstName + " " + middleName + " " + lastName

print()
print("Full name: " + fullName)

## Slice strings ##

print()
print("Full name's first 5 characters :" + fullName[:5])
print("Full name's last 5 characters :" + fullName[-5:])
print("Full name's half: " + fullName[:(len(fullName))//2])

## String functions ##

print()
print("Full name's length: ", len(fullName) )
print('Is "Zanco" in Full name? ', "Zanco" in fullName)
print('Is "abc" not in Full name? ', "abc" not in fullName)
print('Full name capitalized: ', str.capitalize(fullName))
print('Full name centered between characters:')
print((' ' + fullName + ' ').center(80, '-'))
print('"a" count in full name: ', fullName.count('a'))

## Multiple lines string ##

print('''
This is a multple line string
printed with \'\'\'
''')
