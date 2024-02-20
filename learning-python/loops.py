"""count = 0
while ( count <= 5):
    print("Kelly")
    count = count + 1
"""
name_list = [["Kelly", "Kelvin", "Sope"], ["Veena", "Tony"], ["Albin", "Johanna", "Simi"]]
age_list = [[1,2,3], [4,5,6], [7,8,9]]

sum = 0
num_of_items = len(age_list)
for i in age_list:
    sum += int(i[1])
mean = sum / num_of_items
print(mean)

print(name_list[0].index("Kelvin"))
