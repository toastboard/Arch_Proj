class Item:
    def __init__(self, name, description, price, quantity_in_cart, stock):
        self.__name = name
        self.__description = description
        self.__price = price
        self.__quantity_in_cart = quantity_in_cart
        self.__stock = stock

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def getPrice(self):
        return self.__price

    def getQuantityInCart(self):
        return self.__quantity_in_cart

    def setQuantityInCart(self, new_quantity):
        if isinstance(new_quantity, int) and 0 < new_quantity <= self.__stock:
            self.__quantity_in_cart = new_quantity
            return True
        else:
            return False

    def getStock(self):
        return self.__stock

    def setStock(self, new_stock):
        if isinstance(new_stock, int) and 0 < new_stock:
            self.__stock = new_stock
            return True
        else:
            return False


class Household(Item):
    def __init__(self, name, description, price, quantity_in_cart, stock, material, area):
        super().__init__(name, description, price, quantity_in_cart, stock)
        self.__material = material
        self.__area = area

    def getMaterial(self):
        return self.__material

    def getArea(self):
        return self.__area


class Book(Item):
    def __init__(self, name, description, price, quantity_in_cart, stock, author, publisher):
        super().__init__(name, description, price, quantity_in_cart, stock)
        self.__author = author
        self.__publisher = publisher

    def getAuthor(self):
        return self.__author
    
    def getPublisher(self):
        return self.__publisher
    

class Toy(Item):
    def __init__(self, name, description, price, quantity_in_cart, stock, brand, age_rating):
        super().__init__(name, description, price, quantity_in_cart, stock)
        self.__brand = brand
        self.__age_rating = age_rating

    def getBrand(self):
        return self.__brand

    def getAgeRating(self):
        return self.__age_rating


class SmallElectronic(Item):
    def __init__(self, name, description, price, quantity_in_cart, stock, type, power):
        super().__init__(name, description, price, quantity_in_cart, stock)
        self.__type = type
        self.__power = power

    def getType(self):
        return self.__type

    def getPower(self):
        return self.__power
