import sys
import string

# Registrovaní uživatelé
users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Texty k analýze
TEXTS = [
    '''
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley.
    ''',
    '''
    At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.
    ''',
    '''
    The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.
    '''
]

# Funkce pro analýzu textu, kde se zkontroluje, zda první znak je abecední a zda je velké písmeno, samotná metoda issupper nedělala přesně co jsme chtěli
def is_title_case(word):
        return word[0].isalpha() and word[0].isupper()

def analyze_text(text):
    words = text.split()
    no_punctuation = string.punctuation # tahle proměnná je udělaná z metody z importované knihovny string, abych pokryl všechna interpunkční znaménka
    words = [word.strip(no_punctuation) for word in words]
    word_count = len(words)
    titlecase_words = [word for word in words if is_title_case(word)]
    titlecase_count = len(titlecase_words)
    uppercase_count = sum(1 for word in words if word.isupper() and word.isalpha())
    lowercase_count = sum(1 for word in words if word.islower())
    numbers = [int(word) for word in words if word.isdigit()]
    number_count = len(numbers)
    number_sum = sum(numbers)
    
    print(f"There are {word_count} words in the selected text.")
    print(f"There are {titlecase_count} titlecase words: {', '.join(titlecase_words)}.")
    print(f"There are {uppercase_count} uppercase words.")
    print(f"There are {lowercase_count} lowercase words.")
    print(f"There are {number_count} numeric strings.")
    print(f"The sum of all the numbers {number_sum}")

    # Vytvoření grafu
    word_lengths = [len(word) for word in words]
    max_len = max(word_lengths)
    length_counts = {length: word_lengths.count(length) for length in range(1, max_len + 1)}

    print("----------------------------------------")
    print("LEN|  OCCURENCES  |NR.")
    print("----------------------------------------")
    for length in range(1, max_len + 1):
        print(f"{length:>3}|{'*' * length_counts.get(length, 0):<13}|{length_counts.get(length, 0)}")

# Hlavní program by měl být nyní schopný pokrýt situaci, kdy bychom chtěli dát do výběru vyšší počet různých textů
if __name__ == "__main__":
    username = input("username: ")
    password = input("password: ")
    
    if users.get(username) == password:
        print("----------------------------------------")
        print(f"Welcome to the app, {username}")
        print(f"We have {len(TEXTS)} texts to be analyzed.")
        print("----------------------------------------")
        
        try:
            index_selection = int(input(f"Enter a number between 1 and {len(TEXTS)} to select: ")) - 1
            if 0 <= index_selection < len(TEXTS):
                analyze_text(TEXTS[index_selection])
            else:
                print("Invalid number, terminating the program.") # tady by šlo napsat string a vyžádat si správný input, něco jako špatné číslo, vložte číslo mezi 1 a {len(TEXTS), ale v zadání je tento string
                sys.exit()
        except ValueError:
            print("Invalid input, terminating the program.")
            sys.exit()
    else:
        print("Unregistered user, terminating the program.")
        sys.exit()
