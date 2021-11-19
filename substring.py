def find_max(t, z):
    last_sub = ""       #En yüksek değere sahip substringi tutmak için boş değişken(şart değil test amaçlı)
    occur_in_z = -1     #En yüksek değeri tutmak için değişken
    current_count = 0   #Okumayı kolaylaştırmak için mevcut durumdaki substringin string içindeki sayısı
    current_occur = -1  #Okumayı kolaylaştırmak için sonucun o an ki değeri
    for idx, val in enumerate(t):                       #Substring içerisindeki harfleri gezmek için(idx index, val ise değeri tutar)
        for i in range(idx + 1, len(t) + 1):            #Bütün substringleri gezmek için 2. for döngüsü, İlk for döngüsünün o an ki değeri +1den dizi sonuna kadar
            current_count = z.count(t[idx:i])           #O an ki substringin string içerisindeki tekrar sayısı
            current_occur = current_count * (i - idx)   #O an ki count ve substring uzunluğu çarpımı değeri
            if (current_occur) > occur_in_z:            #Eğer değerimiz önceki değerlerden büyükse last_sub ve occur_in_z güncellenir
                occur_in_z = current_count * (i - idx)
                last_sub = t[idx:i]
            #print("Count: ", z.count(t[idx:i]), "Len: ", (i - idx), "Word: ", t[idx:i], "Occur:", current_occur)
    print("Substring:", last_sub, " Occur:", occur_in_z)
    return occur_in_z                                   #Sonuç döndürülür

if __name__ == '__main__':
    print(find_max("aclmdmllabcdhsnd", "shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa"))