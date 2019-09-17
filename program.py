# start

vaken = "n"

print("Du sover djupt som björnen i iden...")

while vaken == "n":
    vaken = input("Har du vaknat [y/n] ").lower()

print("Du går direkt in i duschen.")
print("Du har råkat använda brödrosten i duschen.")

duscha = input("Flyttar du på brödrosten? [y/n] ").lower()
if duscha == "n":
    print("Du får en elektriskt shock och det är slutet")
    exit()
elif duscha == "y":
    print("Friskt vatten kan sköljas över dig och kan väcka upp dig.")
else:
    print("DOES NOT COMPUTE")

season = False
while season == False:
    season = input("Vilken årstied är det [vår, vinter, sommar, höst]").lower()
    if season == "vår" or season == "vinter" or season == "höst":
        print("Det ska bli väldigt kallt och slaskigt under vintertiden!")
        print("Du ska ta på dig vinterkläder...")
    elif season == "sommar":
        print("Det här ska vara trevligt väder att sola!")
    else:
        season = False

