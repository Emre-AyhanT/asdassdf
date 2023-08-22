import random

def harf_bulma(hedef_kelime):
    harf_seti = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    deneme_sayisi = 0
    bulunan_harfler = ""

    for harf in hedef_kelime:
        while True:
            denenen_harf = random.choice(harf_seti)
            deneme_sayisi += 1
            print(f"{deneme_sayisi}. deneme: {denenen_harf}")

            if denenen_harf == harf:
                bulunan_harfler += harf
                print(f"Bulunan harfler: {bulunan_harfler}")
                break

    print(f"{hedef_kelime} kelimesini bulmak için {deneme_sayisi} deneme yapıldı.")
    return bulunan_harfler

if __name__ == "__main__":
    kelimeler = input("Kelimeleri boşluk olmadan aralarında yazın: ")
    bulunan_kelimeler = ""
    
    for kelime in kelimeler:
        bulunan_harfler = harf_bulma(kelime)
        bulunan_kelimeler += bulunan_harfler  
        print(f"{kelime} kelimesinin bulunan harfleri: {bulunan_harfler}")

    print(f"Bulunan kelime: {bulunan_kelimeler}")
