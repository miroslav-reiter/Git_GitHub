import subprocess
import pymsgbox
import pyinputplus as pyin

cesto = pyin.inputMenu(['tenke', 'strerdne', 'hrube'], numbered=True)
maso = pyin.inputMenu(['sunka', 'salama', 'bez masa'], numbered=True)
syr = pyin.inputYesNo("chcete syr?", yesVal="ano", noVal="nie")
syr_typ = None
if syr == "ano":
    syr_typ = pyin.inputMenu(['Mozzarella', 'Parmesan', 'Eidam'], numbered=True)
adresa = 'nie'
donaska = pyin.inputYesNo("chcete pizzu doniest?", yesVal="ano", noVal="nie")
if donaska == "ano":
    adresa = pyin.inputStr("Na aku adresu?")

# Creating the pizza details as text
pizza_details = f"""
Pizza objednávka:
- Cesto: {cesto}
- Mäso: {maso}
- Syr: {'Áno, ' + syr_typ if syr == 'ano' else 'Nie'}
- Doručenie: {adresa}
"""

# Writing to a text file
with open("pizza_objednavka.txt", "w", encoding="utf-8") as file:
    file.write(pizza_details)

print("Objednávka bola uložená do súboru 'pizza_objednavka.txt'! 😊")
subprocess.Popen(["notepad.exe", "pizza_objednavka.txt"])
