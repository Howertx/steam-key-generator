import random

wordlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't' , 'u' 'w', 'x', 'v', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'V', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

dosya = open("Steam Key.txt", "w")

g = int(input("Kaç tane üreteyim ? >> "))


print("Steam keyler üretilip bilgisayarınızda oluşturulan Steam Key.txt dosyasına kaydedilmektedir, eğer bitirmek istiyorsanız programı kapatın...")
def uret():
  for x in range(g):
    print(random.choice(wordlist) +  random.choice(wordlist) +  random.choice(wordlist) +  random.choice(wordlist) +  random.choice(wordlist) + "-" + random.choice(wordlist) +  random.choice(wordlist) +  random.choice(wordlist) +  random.choice(wordlist) +  random.choice(wordlist) + "-" + random.choice(wordlist) +  random.choice(wordlist) +  random.choice(wordlist) +  random.choice(wordlist) +  random.choice(wordlist),file = dosya, flush = True)

uret()
