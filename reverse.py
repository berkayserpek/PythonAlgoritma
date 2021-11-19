def fix_text(mystr):
    splited_str = mystr.split(" ")          #Girdi olarak verilen String'i boşluklarını silerek dizi haline getiriyoruz
    last_str = ""                           #Yeni oluşturacağımız string için boş bir değişken oluşturuyoruz
    for s in splited_str:                   #En başta oluşturduğumuz dizinin içerisinde geziniyoruz
        if "(" not in s:                    #Eğer kelimenin içerisinde ( ve ) varsa parantez içi kelime olduğunu anlarız. Kontrolü burada yapılıyor
            last_str += s[::-1] + " "       #Parantez içi değilse kelimeyi ters çevirip boş stringimize ekliyoruz
        else:
            last_str += s[s.find("(")+1:s.find(")")] + " "  #Parantez içi ise parantez içindeki kelimeyi ekliyoruz
    mystr = last_str.rstrip()                               #Kelimeleri eklerken sonuna boşluk eklediğimizden son çıktımızın sonunda boşluk olacaktır
    print(mystr)                                            #Bu yüzden rstrip ile sondaki boşluğu siliyoruz ve girdi değişkenine eşitliyoruz(şart değil)
    return mystr                                            #Eşitleme şart değil sadece return değerini değiştirmek istemedim.

if __name__ == "__main__":
    INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
             ",tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc "
             "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
             "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
             "(and) nrae a egral enutrof (from) ).gnitirw")
    CORRECT_ANSWER = "John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"
    print("Correct!" if fix_text(INPUT) == CORRECT_ANSWER else "Sorry, it does not match with the correct answer.")