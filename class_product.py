class Product:
    pass

def newProduct(name, price, quantity):
    product = Product()
    product.name = name
    product.price = price
    product.quantity = quantity
    return product

my_product = newProduct("Pizza", 40, 2) 
your_product = newProduct("Salami", 50, 1) 


def printProduct(product):
    print("*" * 50)
    print(product.name, product.price, product.quantity)
    print("*" * 50)
    

def compareProducts(product1, product2):
    if product1.price > product2.price:
        print(printProduct(product2))
    else:
        print(printProduct(product1))

compareProducts(my_product, your_product)
