from Packages.items import Household, Toy, SmallElectronic, Book
from Packages.account import User
import sqlite3

conn = sqlite3.connect("database/arch_proj.db")
cursor = conn.cursor()
# Function that fetches all items in the database and returns them in an array as sqlite3.Row items.
# SQLite3 row items can be treated as dictionaries. You can simply call them with row['column_name'].
# All quantity_in_cart attributes for each item are set to 0 when added to the array.
def fetchAllItems(database_connection):
    item_array = []
    cursor = database_connection.cursor()
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM HouseholdItems")
    household_items = cursor.fetchall()
    for item_row in household_items:
        household_item = Household(item_row['name'], item_row['description'], item_row['price'], 0, item_row['stock'],
                                   item_row['material'], item_row['area'])
        item_array.append(household_item)

    cursor.execute("SELECT * FROM Toys")
    toys = cursor.fetchall()
    for item_row in toys:
        toy = Toy(item_row['name'], item_row['description'], item_row['price'], 0, item_row['stock'],
                             item_row['brand'], item_row['age_rating'])
        item_array.append(toy)

    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    for item_row in books:
        book = Book(item_row['name'], item_row['description'], item_row['price'], 0, item_row['stock'],
                    item_row['author'], item_row['publisher'])
        item_array.append(book)

    cursor.execute("SELECT * FROM SmallElectronics")
    small_electronics = cursor.fetchall()
    for item_row in small_electronics:
        small_electronic = SmallElectronic(item_row['name'], item_row['description'], item_row['price'], 0,
                                           item_row['stock'], item_row['type'], item_row['power'])
        item_array.append(small_electronic)
    return item_array

def main():
    print("Hello to Demo program!")
    print("Please enter username and Password (username = Mike, Password = Mike)")
    username = input("username: ")
    password = input("password: ")
    user = User(username, password)
    login = user.login(username, password)
    while login:
        menu()
        menuOption = input("option: ")
        if(menuOption == '1'):
            user.getPurchases(username)
        elif(menuOption == '2'):
            result = cursor.execute("SELECT * FROM Items")
            result = result.fetchall()
            print("\n")
            for item in result:
                strint = ""
                space = "  "
                for entery in item:
                    strint += str(entery)
                    strint += str(space)
                print(strint)
                strint = ""
        elif(menuOption == '3'):
            user.logout()
            break
        else:
            print("Input is not in menu ...\n")
            break


        else:
            break


def menu():
    print("\nSelect one of the following options: ")
    print("1- view cart")
    print("2- Display all items")
    print("3- logout\n")


if __name__ == "__main__":
    main()
