timur = input()
ruslan = input()
if timur == ruslan:
    print("ничья")
elif timur == "камень" and ruslan == "ножницы":
    print("Тимур")
elif timur == "ножницы" and ruslan == "бумага":
    print("Тимур")
elif timur == "бумага" and ruslan == "камень":
    print("Тимур")
else:
    print("Руслан")
