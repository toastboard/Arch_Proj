import items

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
			self.__total_prices+=x.getPrice()

	def updateQuantity(self, item, new_quantity):
		for x in self.__items_list:
			if x == item:
				return x.setQuantityInCart(new_quantity)
			else:
				return False

	def getTotalPrice(self):
		return self.__total_price

	def getAllItems(self):
		return self.__items

	def makePurchase(self, shipping_address, credit_card_number):
		pass
    # TODO: makePurchase class here


class Purchase:
    # TODO: Purchase class goes here
    pass