rehber=[["ayşe","1234"],["hüsna","7894"]]
def kayit_ekle(rehber):
    while True:
        isim=input("LÜTFEN BİR İSİM GİRİNİZ:")
        numara=input("LÜTFEN BİR NUMARA GİRİNİZ:")
        rehber.append([isim,numara])
        if islem_onay():
            rehber=[[isim,numara]]
        

        if devam_mi():
            continue
        else:
            break
    
def islem_onay():
    onay=input("Onaylamak istiyorsanız (e) ye onaylamak istemiyorsanız (h) ye basınız:")
    if onay=="e":
        return True
    else:
        False


def devam_mi():
    cikis=input("Seçmiş olduğunuz işleme devam etmek istiyorsanız (e) çıkmak istiyorsanız (h) ye basınız:")
    if cikis=="e":
        return True
    else:
        False





def kayit_ara(rehber):
    while True:
        isim=input("Rehberden aramak istediğiniz kişinin adını veya numarasını giriniz:")
        for i in rehber:
            if isim in i:
                print("isim:{} Kişisi aranıyor.... numara:{}".format(i[0],i[1]))

        if devam_mi():
            continue
        else:
            break


def kayit_sil(rehber):

    while True:
        for i in rehber:
            print(i)

        isim=input("Rehberden silmek istediğiniz kişinin adını giriniz:")

        if islem_onay():
            for i in rehber:
                if isim in i:
                    rehber.remove(i)
        print("Kayıt silinmiştir")

        if devam_mi():
            continue
        else:
            break




while True:
    menu=input("""
    -Kayıt eklemek için (1)
    -Kayıt aramak için (2)
    -Kayıt silmek için (3)
    -çıkmak için(4)
    tuşlarından birine basınız""")

    if menu=="1":
        kayit_ekle(rehber)
    elif menu=="2":
        kayit_ara(rehber)
    elif menu=="3":
        kayit_sil(rehber)
    elif menu=="4":
        print("iyi günler ")

        break