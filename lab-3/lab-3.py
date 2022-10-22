from tracemalloc import start


file = open("/Users/emrecambolat/Documents/python-projects/veri-bilimi/lab-3/Notlar.txt", "r",encoding="utf-8")
# with open("/Users/emrecambolat/Documents/python-projects/veri-bilimi/lab-3/Notlar.txt", "r") as dosya:
#     dosya.seek(0)
#     liste = dosya.readlines()
#     for x in range(len(liste)):
#         a = liste[x:x+1]
#         # print(a[0][0:3], "\t", a[0][8:20], "\t", a[0][38:45])

liste = []
count = 0      
for satir in file:
    if count == 0:
        count = count +1
        continue
    elif len(satir.split()) == 0:
        continue
    else:
        a = satir.split()
        print(satir.split())
        liste.append(a)
        result = float(a[3])*0.3 +float(a[4])*0.5+float(a[5])*0.2
        if result >= 88:
            print("Başarı Notu:4, Harf: AA")
        elif result >= 80 and result <= 87 :
            print("Başarı Notu:3.50, Harf: BA")
        elif result >= 73 and result <= 79 :
            print("Başarı Notu:3.00, Harf: BB")
        elif result >= 66 and result <= 72 :
            print("Başarı Notu:2.50, Harf: CB")
        elif result >= 60 and result <= 65 :
            print("Başarı Notu:2.00, Harf: CC")
        elif result >= 55 and result <= 59 :
            print("Başarı Notu:1.50, Harf: DC")
        elif result >= 50 and result <= 54 :
            print("Başarı Notu:1.00, Harf: DD")
        elif result >= 0 and result <= 49 :
            print("Başarı Notu:0.00, Harf: FF")
        else:
            print("Başarı Notu:0.00, Harf: F")
        # print(result)
        print("\n")

count = count +1


# print(liste[5][3])

