text= "[ Pealkiri E-kiri kirikakar ]"
print " ", text.count("kiri")

text = "rein" 
print " ", text.capitalize()

text = "[ Pealkiri ]"
print " ", text.ljust(50, "=")

text = "[ Pealkiri ]"
print " ", text.rjust(50, "=")

text = "[ Pealkiri ]"
print " ", text.center(50, "=")

filename = raw_input("Sisesta failinimi: ")
print filename.endswith(".py")

text = "Lorem ipsum dolor sit amet, consectetur adipisci"
print "", text.find("sit")

klass = "anton algis madis anna"
if "algis" in klass:
    print "", "Algis t2na ei puudu :)"

text = "abc1"
print "", text.isalnum()
print "", text.isalpha()
print "", text.islower()
print "", text.isspace()
print "", text.istitle()
print "", text.isupper()

print "", "-".join(["ta","ga","va","ra"])

text = "Rein Prii"
print "", text.lower()
print "", text.lstrip("Re")
print "", text.replace("Rein", "Eins")
print "", text.rfind("sub")
print "", text.rindex("R")
print "", text.rstrip("i")
print "", text.split("R")
print "", text.startswith("Ein")
print "", text.strip("Rei")
print "", text.swapcase()
print "", text.title()
