#alfabe=a,b,c,d,e
sayac=0
kelime=[]

def list_to_string(x):
    last_word=""
    for i in x:
        if i!="]" and i!="[" and i!="'" and i!="," and i!=" ":
            last_word=last_word+i
    return last_word
print("Kontrol etmek istediğiniz kelime isterseniz tek seferde isterseniz harf harf giriniz.\n")
while True:
    try:
        a=input("Bir harf ve ya kelime girin:")
        say=0
        for i in a:
            say=say+1

        if say>1:
            print("String üzerinde işlem yapılıyor("+a+")")
            tanimli=True
            for i in a:
                if i!="a" and i!="b" and i!="c" and i!="d" and i!="e":
                    print("Alfabede olmayan harf içeriyor")
                    tanimli =False
                    break 
            for j in range(0,len(a)):
                if a[j]=="b" or a[j]=="c" or a[j]=="d":
                    if j<len(a)-1:
                        if a[j+1]=="b" or a[j+1]=="c" or a[j+1]=="d":
                            print("Tanınmayan kelime")
                            tanimli=False
                            break
                    elif j==len(a):
                        print("s")
            if tanimli:
                print("Tanımlı kelime")
            
        else:
            print("Girdiğiniz karakterler teker teker analiz ediliyor")
            if a!="a" and a!="b"and a!="c"and a!="d"and a!="e":
                print("Alfabede olmayan harf")
                son_kelime=str(kelime)
                print(list_to_string(son_kelime))
                a=input("Bir harf giriniz :")
            if a=="a" or a=="e":
                kelime.append(a)
                sayac=sayac+1
                son_kelime=str(kelime)
                print(list_to_string(son_kelime))
            elif a=="b" or a=="c" or a=="d":
                kelime.append(a)
                if sayac!=0:
                    if kelime[sayac-1]=="b" or kelime[sayac-1]=="c" or kelime[sayac-1]=="d":
                        kelime.pop(sayac)
                        son_kelime=str(kelime)
                        print(list_to_string(son_kelime))
                        print("[*]Tanınmayan kelime")
                        sayac=sayac-1
                sayac=sayac+1
                son_kelime=str(kelime)
                print(list_to_string(son_kelime))
    except KeyboardInterrupt:
        print("\nÇıkış yapılıyor")
        break

        


