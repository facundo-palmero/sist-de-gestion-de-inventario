ing = int(input("cuantos productos ingresara?: "))
list = []
cant = []
counter = 0
k = 0
ñ = 0
for n in range(ing):
    products = input("que producto? ")
    list.insert(k,products)
    k += 1
for i in range(len(list)):
    cant_user = int(input(f"cuantos productos tienes de: {list[i]}"))
    cant.insert(ñ,cant_user)
    ñ += 1
for a in range(len(list)):
    if cant[a] < 5:
        print("tienes menos de 5 productos en",list[a])
        counter += 1
if counter > 0:
    print("hacer restock")
else:
    print("el stock esta bien")
