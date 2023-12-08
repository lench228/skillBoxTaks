from typing import List

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

powered_floats = list(map(lambda x: round(x ** 3, 3), floats))

filtered_names = list(filter(lambda name: len(name) >= 5, names))

product_of_numbers = eval('*'.join(map(str, numbers)))

print(powered_floats)
print(filtered_names)
print(product_of_numbers)
