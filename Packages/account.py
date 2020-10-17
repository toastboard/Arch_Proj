import sqlite3

conn = sqlite3.connect("database/arch_Proj.db")
cursor = conn.cursor()

class User:
    # TODO: User class goes here
    pass


class Cart:
    # TODO: Cart class goes here
    pass


class Purchase:
    def __init__(self, username, shipping_address, card_number, date, items_in_cart, total):
        self.__purchase_id = -1
        self.__username = username
        self.__shipping_address = shipping_address
        self.__card_number = card_number
        self.__date = date
        self.__confirmed = False
        self.__items_in_cart = items_in_cart
        self.__total = total

    def confirmPurchase(self):
        self.getPurchaseID()
        cursor.execute("INSERT INTO Purchases VALUES (?, ?, ?, ?, ?, ?)", (self.__purchase_id, self.__username, self.__shipping_address, self.__card_number, self.__date, self.__total))
        conn.commit()

        items_tuples = []
        for item in self.__items_in_cart:
            items_tuples.append((self.__purchase_id, item.name, item.quantity_in_cart))

        cursor.executemany("INSERT INTO Purchased_Items VALUES (?, ?, ?)", items_tuples)
        conn.commit()
        self.__confirmed = True
        return self.__confirmed

    def getPurchaseID(self):
        if self.__purchase_id == -1:
            cursor.execute("SELECT MAX(purchase_id) FROM Purchases")
            self.__purchase_id = cursor.fetchone()[0]
        return self.__purchase_id

    def getUsername(self):
        return self.__username
