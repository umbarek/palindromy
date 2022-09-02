print("Moduł 4.2, zadanie: palindromy")
print("")
n = input("Podaj słowo do sprawdzenia: ")
print(f"Podane przez Ciebie słowo to:" + "\033[1m",n)
print ("\033[0m")

def palindromy(word):
    word = word.lower()
    reverse_word = "".join(reversed(word))

    print (f"Sprawdzam, czy podane słowo jest palindromem...")
    print ("Wynik sprawdzenia: " + "\033[1m", (word == reverse_word))
    print ("\033[0m")
palindromy(n)