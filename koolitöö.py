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
