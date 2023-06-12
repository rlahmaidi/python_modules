from NumPyCreator import NumPyCreator
npc = NumPyCreator()
print(npc.from_list([[1, 2, 3], [6, 3, 4]]))

print(npc.from_list([[1, 2, 3], [6, 4]]))

print(npc.from_list([[1, 2, 3], ['a', 'b', 'c'], [6, 4, 7]]))

print(npc.from_list(((1, 2), (3, 4))))

print(npc.from_tuple(("a", "b", "c")))

print(npc.from_tuple(["a", "b", "c"]))

print(npc.from_iterable(range(5)))

shape = (3, 5)
print(npc.from_shape(shape))

print(npc.random(shape))

print(npc.identity(4))
