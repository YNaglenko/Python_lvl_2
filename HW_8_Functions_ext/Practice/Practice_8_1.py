class Cat:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return "Cat [name={}, age={}]".format(self.name, self.age)


def get_max_cat(cats_list, cat_comparator):
    max_cat = cats_list[0]
    for cat in cats_list:
        if cat_comparator(max_cat, cat) < 0:
            max_cat = cat
    return max_cat


def cat_comparator_age(cat_a, cat_b):
    if cat_a.age > cat_b.age:
        return 1
    elif cat_a.age < cat_b.age:
        return -1
    elif cat_a.age == cat_b.age:
        return 0


cat_1 = Cat("Smoky", 1)
cat_2 = Cat("Snowflake", 1.5)
cat_3 = Cat("Mr_Cat", 1.7)
cat_4 = Cat("Sonya", 2)
cat_5 = Cat("Koko", 6)

cat_list = [cat_1, cat_2, cat_3, cat_4, cat_5]

super_cat = get_max_cat(cat_list, cat_comparator_age)

print(super_cat)
