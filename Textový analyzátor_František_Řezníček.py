users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#Přihlášení uživatele
username = input("username: ")
password = input("password: ")

if username not in users or users[username] != password:
    print("unregistered user, terminating the program..")
    exit()

print("----------------------------------------")
print(f"Welcome to the app, {username}")
print("We have 3 texts to be analyzed.")
print("----------------------------------------")

# Výběr textu
try:
    selection = int(input("Enter a number btw. 1 and 3 to select: "))
    if selection < 1 or selection > 3:
        print("Invalid number, terminating the program..")
        exit()
except ValueError:
    print("Invalid input, terminating the program..")
    exit()

# Analýza vybraného textu
text = TEXTS[selection - 1]

# Odstranění nežádoucích znaků a rozdělení textu na slova
words = [word.strip('.,') for word in text.split()]

# Počet slov
word_count = len(words)

# Počet slov začínajících velkým písmenem
titlecase_count = sum(1 for word in words if word.istitle())

# Počet slov psaných velkými písmeny
uppercase_count = sum(1 for word in words if word.isupper() and word.isalpha())

# Počet slov psaných malými písmeny
lowercase_count = sum(1 for word in words if word.islower())

# Počet čísel a součet všech čísel
numbers = [int(word) for word in words if word.isdigit()]
number_count = len(numbers)
number_sum = sum(numbers)

# Výstup statistik
print("----------------------------------------")
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {number_count} numeric strings.")
print(f"The sum of all the numbers {number_sum}")
print("----------------------------------------")

# Výpočet četnosti délek slov
word_lengths = {}
for word in words:
    length = len(word)
    if length in word_lengths:
        word_lengths[length] += 1
    else:
        word_lengths[length] = 1

# Výstup četnosti délek slov
print("LEN|  OCCURENCES  |NR.")
print("----------------------------------------")
for length in sorted(word_lengths):
    print(f"{length:3}|{'*' * word_lengths[length]:<13}|{word_lengths[length]}")
