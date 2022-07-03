# ---------------- FONCTIONS / CONDITIONS ----------------

def demanderNom() :
    nom = ""
    while nom == "" :
        nom = input("Votre nom : ")
    return nom
    
def demanderAge(nom) :
    age = 0
    while age == 0 :
        age = input(nom + ", votre âge : ")
        try:
            age = int(age)    
        except:
            print("Erreur : vous devez renseigner un âge numérique !")
    return age

def verifierAge(age) :
    condition = age >= 18
    res = "Majeur" if(condition) else "Mineur"
    return "Vous êtes " + res

def afficherInfos(nom, age) :
    print("Vous vous appelez " + nom + " et vous avez " + str(age) + " ans")
    print(verifierAge(age))

# for i in range(1, 4) :
#     nom = "Personne" + str(i)
#     age = demanderAge(nom)
#     afficherInfos(nom, age)
    
# --------------- TUPLES ---------------
marques = ("BMW", "Mercedes", "Tesla", "Toyota")
print(marques)
print("Il y a " + str(len(marques)) + " marques")

for marque in marques: 
    print(marque)

# --------------- LISTES ---------------
marques = ["BMW", "Mercedes", "Tesla", "Toyota"]
new = "Renault"
# ajouter un élément
marques.append(new)
# supprimer un élément
del marques[0]

print(marques)

# ---------------- SLICES -------------

# Afficher tout --> in marques[:] 
# Afficher tout sauf les n dernier --> in marques[:-n]
# Afficher tout dans l'ordre inverse --> in marques[::-1] 
# Afficher un sur 2 --> in marques[::2] 
# Afficher les 2 premiers --> in marques[:2] 

for i in marques[::2]:
    print("Marque : " + i)

clients = []

while True: 
    client = input("Client : ")
    if client == "":
        break
    clients.append(client)

# trier un tableau (A-Z a-z)
clients.sort()
sorted(clients)
# trier un tableau (Z-A z-a)
clients.sort(reverse=True)
sorted(clients, reverse=True)

print(clients)

print("Liste des clients")
for c in clients:
    print(c) 
    
# ---------------- DICTIONNAIRES (associatifs) -------------

knights = {'Gallahad': 'The Pure', 'Robin': 'The Brave'}
for k, v in knights.items():
     print(k, v)

tel = {'jack': 4098, 'sape': 4139}
# ajouter un élément dans un tableau associatif
tel['guido'] = 4127
print(tel)
print(tel['jack'])
