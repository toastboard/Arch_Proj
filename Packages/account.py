#import items
import sqlite3
from datetime import date

conn = sqlite3.connect("database/arch_proj.db")
cursor = conn.cursor()

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        result = cursor.execute("SELECT * FROM user WHERE username = ? AND password = ?", (username, password,))
        result = result.fetchall()
        if(result):
            print("\nYou are in!\n")
            return 1
        else:
            print("\nUsername or Password is wrong\n")
            return 0

    def logout(self):
        username = ""
        password = ""
        print("You are logged out")
        return 0

    def getUsername(self, id):
        result = cursor.execute("SELECT username FROM user WHERE id = (?)", (id,) )
        result = result.fetchall()
        return result[0][0]

    def getPurchase(self, purchaseId):
        result = cursor.execute("SELECT * FROM Purchased_Items WHERE purchase_id = ?", (purchaseId,))
        result = result.fetchall()
        return result

    def getPurchases(self, username):
        #result = cursor.execute("SELECT * FROM Purchases WHERE username = ?", (username,))
        result = cursor.execute("SELECT * FROM Purchases")
        result = result.fetchall()
        if(result):
            for item in result:
                print(item)
        else:
            print("not purchases were detected!\n")


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
		elif item not in self.__items_list:
			self.__items_list.append(item)
			return self.updateQuantity(item, 1)

	def deleteItemFromCart(self, item):

		if item in self.__items_list:

			self.__items_list.remove(item)
			return self.updateQuantity(item, 0)
				
		elif item not in self.__items_list:
			print("Item not found in cart")
			return False

	def makePurchase(self, shipping_address, credit_card_number):
		today = date.today()
		d1 = today.strftime("%y-%m-%d")
		purchaseObject = Purchase(self.__username,shipping_address,credit_card_number,d1,self.__items_list,self.__total_price)
		return purchaseObject



class Purchase:
    def __init__(self, username, shipping_address, card_number, purchase_date, items_in_cart, total):
        self.__purchase_id = -1
        self.__username = username
        self.__shipping_address = shipping_address
        self.__card_number = card_number
        self.__date = purchase_date
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
