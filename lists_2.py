# tuple_ = 1, 2, 3, 4
# tuple_0 = 1, 2, 3, True, "String"
# tuple_2 = (1, 2, 3, 4)
# tuple_3 = tuple([1, 2, 3, 4])
# print(type(tuple_))
# print(tuple_0)
# print(tuple_2)
# print(tuple_3)
# print(tuple_[0])
# tuple_ = 1, 2, 3, True, "String"
# list_ = [1, 2, 3, True, "String"]
# print(tuple_.__sizeof__())
# print(list_.__sizeof__())
tuple_ =([1, 2], 0) + (1, 2)
print(tuple_)
tuple_[0][0] = 2
print(tuple_)
tuple_ = (1, 2) * 3
print(tuple_)