
list = [5, 2, 12, 9, 8, 6, 5]

sum = lambda sum, value : sum + value 

def reduce(list, sum):
    new_sum = 0
    for number in list :
        new_sum = sum(new_sum, number)
    print(new_sum)

reduce(list, sum)

products = {
    "Bib Shorts": ["Clothing", 92.50],
    "Roubaix" : ["Bicycle", 3,599.99],
    "Cycling Computer" : ["Accessories", 394.99],
    "Helmet" : ["Accessories", 299.99],
    "Road Shoes" : ["Shoes", 144.99],
    "700c presta tube" : ["Accessories", 5.25],
    "Jersey" : ["Clothing", 25.99],
    "Multi-Functional Tool" : ["Accessories", 22.99],
    "Gloves" : ["Accessories", 8.99],
    "Cleats" : ["Shoes", 15.99],
    "Power Pedals" : ["Accessories", 999.99],
    "Socks" : ["Clothing", 8.50]
}

desired_item = lambda dictionary, key, desired : dictionary[key][0] == desired

def filter(products: dict):
    new_dict = {}
    for item in products.keys() :
        if desired_item(products, item, "Accessories") :
            new_dict[item] = products[item]
            print(new_dict)

filter(products)
            
