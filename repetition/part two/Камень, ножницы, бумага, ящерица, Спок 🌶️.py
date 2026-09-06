items = ['камень', 'ящерица', 'Спок', 'ножницы', 'бумага']
t = input()
r = input()
t_ind = items.index(t)
r_ind = items.index(r)
if t_ind == r_ind:
    print("ничья")
elif abs(t_ind - r_ind) % 2:
    if t_ind < r_ind:
        print("Тимур")
    else:
        print("Руслан")
else:
    if t_ind > r_ind:
        print("Тимур")
    else:
        print("Руслан")