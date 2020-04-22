classe1 = str(input())
classe2 = str(input())
classe3 = str(input())

if(classe1 == "vertebrado" and classe2 == "ave" and classe3 == "carnivoro"):
    classe4 = ("aguia")
if(classe1 == "vertebrado" and classe2 == "ave" and classe3 == "onivoro"):
    classe4 = ("pomba")
if(classe1 == "vertebrado" and classe2 == "mamifero" and classe3 == "onivoro"):
    classe4 = ("homem")
if(classe1 == "vertebrado" and classe2 == "mamifero" and classe3 == "herbivoro"):
    classe4 = ("vaca")  
if(classe1 == "invertebrado" and classe2 == "inseto" and classe3 == "hematofogo"):
    classe4 = ("pulga")
if(classe1 == "invertebrado" and classe2 == "inseto" and classe3 == "herbivoro"):
    classe4 = ("lagarta")
if(classe1 == "invertebrado" and classe2 == "anelideo" and classe3 == "hematofogo"):
    classe4 = ("sanguessuga")
if(classe1 == "invertebrado" and classe2 == "anelideo" and classe3 == "onivoro"):
    classe4 = ("minhoca")
    
print(classe4)
