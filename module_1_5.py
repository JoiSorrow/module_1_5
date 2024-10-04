# immutable_var = 1, 5.236, False, "Кортеж"
# print(immutable_var)
# immutable_var[0] = 256
# print(immutable_var)
# immutable_var.uppend = ("Good morning")
# print(immutable_var)
# поменять элемент не удастся, т.к. кортеж - последовательность, созданная специально для того, чтобы элементы внутри нельзя было поменять
mutable_list = ["House", "Big Bang", "Friends", 5, 2.236, True]
print(mutable_list)
mutable_list [2] = "Breaking Bad"
mutable_list.append ("Game of Thrones")
mutable_list.extend (["The Lord of the Rings", "№ 1"])
print (mutable_list)
