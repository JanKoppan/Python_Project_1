"""
projekt_1.py: První projekt do Engeto Online Python Akademie

author: Jan Koppan
email: jan.koppan@seznam.cz
"""
# Seznam uživatelů a jejich hesel
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Texty pro analýzu
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    
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

# Funkce pro analýzu textu
def analyze_text(text):
    words = text.split()
    
    # Počet slov
    word_count = len(words)
    
    # Počet slov začínajících velkým písmenem
    titlecase_words = len([word for word in words if word.istitle()])
    
    # Počet slov psaných velkými písmeny
    uppercase_words = len([word for word in words if word.isupper()])
    
    # Počet slov psaných malými písmeny
    lowercase_words = len([word for word in words if word.islower()])
    
    # Počet čísel
    numeric_strings = len([word for word in words if word.isdigit()])
    
    # Součet čísel
    sum_of_numbers = sum([int(word) for word in words if word.isdigit()])
    
    # Vytvoření sloupcového grafu četnosti délek slov
    word_lengths = [len(word) for word in words]
    length_counts = {}
    
    for length in word_lengths:
        length_counts[length] = length_counts.get(length, 0) + 1
    
    print(f"LEN|  OCCURENCES  |NR.")
    for length in sorted(length_counts.keys()):
        print(f" {length}|{'*' * length_counts[length]} |{length_counts[length]}")
    
    return (
    word_count, 
    titlecase_words, 
    uppercase_words, 
    lowercase_words, 
    numeric_strings, 
    sum_of_numbers
)

# Hlavní program
def main():
    print("Enter your username:")
    username = input()
    
    print("Enter your password:")
    password = input()
    
    # Ověření uživatele
    if username in users and users[username] == password:
        print(f"----------------------------------------")
        print(f"Welcome to the app, {username}")
        print(f"We have {len(TEXTS)} texts to be analyzed.")
        print(f"----------------------------------------")
        
        try:
            # Výběr textu
            print("Enter a number btw. 1 and 3 to select:")
            choice = int(input())
            
            if choice < 1 or choice > 3:
                print("Invalid selection, terminating the program.")
                return
            
            selected_text = TEXTS[choice - 1]

            # Analýza vybraného textu
            word_count, titlecase_words, uppercase_words, lowercase_words, numeric_strings, sum_of_numbers = analyze_text(selected_text)
            
            print(f"\nThere are {word_count} words in the selected text.")
            print(f"There are {titlecase_words} titlecase words.")
            print(f"There are {uppercase_words} uppercase words.")
            print(f"There are {lowercase_words} lowercase words.")
            print(f"There are {numeric_strings} numeric strings.")
            print(f"The sum of all the numbers {sum_of_numbers}")
            
        except ValueError:
            print("Invalid input, terminating the program.")
    else:
        print(f"Unregistered user, terminating the program.")

if __name__ == "__main__":
    main()
