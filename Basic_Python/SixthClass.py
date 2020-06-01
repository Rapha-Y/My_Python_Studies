set_a = {1, 2, 3, 4, 5}
set_b = {5, 6, 7, 8}

union_set = set_a.union(set_b)
print("União: {}".format(union_set))

intersection_set = set_a.intersection(set_b)
print("Intersecção: {}".format(intersection_set))

difference_set_a = set_a.difference(set_b)
print("Diferença A-B: {}".format(difference_set_a))

difference_set_b = set_b.difference(set_a)
print("Diferença B-A: {}".format(difference_set_b))

symmetric_diff_set = set_a.symmetric_difference(set_b)
print("Diferença simétrica: {}".format((symmetric_diff_set)))

set_c = {1, 2, 3}
set_d = {1, 2, 3, 4, 5}

subset_set = set_c.issubset(set_d)
print("C is a subset of D: {}".format(subset_set))

superset_set = set_d.issuperset(set_c)
print("D is superset of C: {}".format(superset_set))

animals = ["Gato", "Chinchila", "Coelho", "Chinchila", "Aranha"]
animal_set = set(animals)
print(animal_set)