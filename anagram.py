kelime1 = input("Lütfen bir kelime girin: ")
kelime2 = input("Lütfen başka bir kelime girin: ")

kelime1 = kelime1.lower()
kelime2 = kelime2.lower()

if len(kelime1) == len(kelime2):
    sıralı_kelime1 = sorted(kelime1)
    sıralı_kelime2 = sorted(kelime2)

    if sıralı_kelime1 == sıralı_kelime2:
        print(kelime1 + " ve " + kelime2 + " bir anagramdır.")
    else:
        print(kelime1 + " ve " + kelime2 + " bir anagram değildir.")
else:
    print(kelime1 + " ve " + kelime2 + " bir anagram değildir.")
