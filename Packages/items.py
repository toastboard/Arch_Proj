import sqlite3

conn = sqlite3.connect("database/arch_Proj.db")
cursor = conn.cursor()

# Item class. Parent to all subcategories of items.
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
        pass


# Child class of Item class containing material and area in addition.
# To elaborate on area, area is the area of the house where the item would typically be located.
class Household(Item):
    def __init__(self, name, description, price, quantity_in_cart, stock, material, area):
        Item.__init__(self, name, description, price, quantity_in_cart, stock)
        self.__material = material
        self.__area = area

    # setStock is more complicated because it requires a database change. The function tries to edit the database and
    #  returns true if it succeeds.
    def setStock(self, new_stock):
        if isinstance(new_stock, int) and 0 < new_stock:
            try:
                cursor.execute('''UPDATE HouseholdItems
                                  SET stock = ?
                                  WHERE
                                    name = ?''', (str(new_stock), self.getName()))
                conn.commit()

                self.__stock = new_stock
                return True
            except sqlite3.ProgrammingError:
                return False
        else:
            return False

    def getMaterial(self):
        return self.__material

    def getArea(self):
        return self.__area


# Child class of Item class containing author and publisher in addition.
class Book(Item):
    def __init__(self, name, description, price, quantity_in_cart, stock, author, publisher):
        Item.__init__(self, name, description, price, quantity_in_cart, stock)
        self.__author = author
        self.__publisher = publisher

    def setStock(self, new_stock):
        if isinstance(new_stock, int) and 0 < new_stock:
            try:
                cursor.execute('''UPDATE Books
                                  SET stock = ?
                                  WHERE
                                    name = ?''', (new_stock, self.getName()))
                conn.commit()

                self.__stock = new_stock
                return True
            except sqlite3.ProgrammingError:
                return False
        else:
            return False

    def getAuthor(self):
        return self.__author

    def getPublisher(self):
        return self.__publisher


# Child class of Item class containing brand and age_rating in addition.
class Toy(Item):
    def __init__(self, name, description, price, quantity_in_cart, stock, brand, age_rating):
        Item.__init__(self, name, description, price, quantity_in_cart, stock)
        self.__brand = brand
        self.__age_rating = age_rating

    def setStock(self, new_stock):
        if isinstance(new_stock, int) and 0 < new_stock:
            try:
                cursor.execute('''UPDATE Toys
                                  SET stock = ?
                                  WHERE
                                    name = ?''', (new_stock, self.getName()))
                conn.commit()

                self.__stock = new_stock
                return True
            except sqlite3.ProgrammingError:
                return False
        else:
            return False

    def getBrand(self):
        return self.__brand

    def getAgeRating(self):
        return self.__age_rating


# Child class of Item class containing electronic_type and power in addition.
class SmallElectronic(Item):
    def __init__(self, name, description, price, quantity_in_cart, stock, electronic_type, power):
        Item.__init__(self, name, description, price, quantity_in_cart, stock)
        self.__electronic_type = electronic_type
        self.__power = power

    def setStock(self, new_stock):
        if isinstance(new_stock, int) and 0 < new_stock:
            try:
                cursor.execute('''UPDATE SmallElectronics
                                  SET stock = ?
                                  WHERE
                                    name = ?''', (new_stock, self.getName()))
                conn.commit()

                self.__stock = new_stock
                return True
            except sqlite3.ProgrammingError:
                return False
        else:
            return False

    def getType(self):
        return self.__electronic_type

    def getPower(self):
        return self.__power
