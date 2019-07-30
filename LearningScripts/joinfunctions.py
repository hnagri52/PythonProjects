"""File to practice join functions"""
ls = ["Hussein", "sabi", "jy", "ahmed"]
print(", ".join(ls))

var = "My name is Hussein"
var2 = "    MY na   mmee kr    er    gff     "

var2 = var2.strip()
print(var2)
var2 = var2.replace(" ", "")
print(var2)


a = var.replace(" ", "")
print(a)
print( "letter: " + " letter: ".join(a))

