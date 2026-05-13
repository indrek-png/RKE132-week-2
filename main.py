
# Esimene programm - Mis päev ?
""" day = input ("Mis päev on homme ? (tööpäev/ puhkepäev):")
if day == "tööpäev":
    print ("Ma lähen magama, hed ööd !")
elif day=="puhkepäev":
    print ("Veel üks osa Netflix-ist ! " )
else:
    print ("Vale väärtus") """

#Esimes programmi lõpp

#Teine programm - Fiantsnõustaja ?

""" print ("Tere tulemst programmi 'Finantsnõustaja' !")
print ("Sinu isiklik nõustaja ei tee emotsionaalseid oste.")
money = int(input("Kui palju sinul on raha praegu ?"))
if money < 2500:
    print( "Sinul ei ole piisavalt raha . Ole kannatlik ja kogu edasi !")
elif money == 2500:
    print("<Palju õnne,  saad osta iPhone 17 Pro sularahas !")
else:
    print ("Saad osta iPhone 17 Pro sularahas. ja veel jääb raha üle.") """

# Teise programmi lõpp

# Kolams programm - Sammulugeja 

goal = 10000
steps = int(input("Mitu sammu oled juba teinud ?: "))
percent = (steps/goal)* 100

print(f"{percent}%")

if percent < 50:
    print("Alles poolel teel, liigu edasi !")
elif percent < 75:
    print("Tubli, oled peaaegu kohal !")
elif percent < 100:
    print("Suurepärane, oled peaaegu kohal !")
else:
    print("Palju õnne, oled oma eesmärgi täitnud !")



