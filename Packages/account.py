import items
import sqlite3
from datetime import date

conn = sqlite3.connect("database/arch_Proj.db")
cursor = conn.cursor()

class User:

    # TODO: User class goes here
    pass


class Cart:
	def __init__(self, username):
		self.__items_list = []
		self.__username = username
		self.__total_price = 0

	def calculate_total(self):
		for x in self.__items_list:
			self.__total_price+=x.getPrice()

	def updateQuantity(self, item, new_quantity):
		for x in self.__items_list:
			if x == item:
				return x.setQuantityInCart(new_quantity)
			else:
				return False

	def getTotalPrice(self):
		return self.__total_price

	def getAllItems(self):
		return self.__items_list

	def addItemToCart(self, item):
		
		if item in self.__items_list:
			print("Item already in cart")
			return False

		else if item not in self.__items_list:
			self.__items_list.append(item);
			return updateQuantity(item, 1)
				

	def deleteItemFromCart(self, item):
		
		if item in self.__items_list:
			self.__items_list.remove(item);
			return updateQuantity(item, 0)
				
		else if item not in self.__items_list:
			print("Item not found in cart")
			return False
			


	def makePurchase(self, shipping_address, credit_card_number):
		today = date.today();
		d1 = strftime("%y-%m-%d")
		purchaseObject = Purchase(self.username,shipping_address,credit_card_number,d1,self.__items_list,self.__total_price)
		return purchaseObject.confirmPurchase()
	
    # TODO: makePurchase class here


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
