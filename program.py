# start
# vakna upp
vaken = "n" # Den tillverkar man en variabel med en sträng

print("Du sover djupt som björnen i iden...")

while vaken == "n":
    vaken = input("Har du vaknat [y/n] ").lower() # Här skapas en .lower-funktion som repeterar processen.

# Duschen
print("Du går direkt in i duschen.")
print("Du har råkat använda brödrosten i duschen.")
# Skapa if, elif och else funktionerna.
duscha = input("Flyttar du på brödrosten? [y/n] ").lower()
if duscha == "n":
    print("Du får en elektriskt shock och det är slutet")
    exit()
elif duscha == "y":
    print("Friskt vatten kan sköljas över dig och kan väcka upp dig.") # Här skapar man en print-funktion som skriver ut koden med parenteser och variabler används alltid med str-funktionen.
else:
    print("DOES NOT COMPUTE")

# Årstiderna
season = False # Så här kodar en boo-funktionen som framställer antingen sant eller falskt variabler.
while season == False:
    season = input("Vilken årstied är det [vår, vinter, sommar, höst]").lower()
    if season == "vår" or season == "vinter" or season == "höst":
        print("Det ska bli väldigt kallt och slaskigt under vintertiden!")
        print("Du ska ta på dig vinterkläder...")
    elif season == "sommar":
        print("Det här ska vara trevligt väder att sola!")
    else:
        season = False
# Ta fram while-funktionen så att dataprocessen ska uppdatereas och upprepas samtidigt och använd boolsk (true och false)datatypen till hjälp också.

