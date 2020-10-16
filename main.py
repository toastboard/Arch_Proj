from Packages.items import Household, Toy, SmallElectronic, Book
import sqlite3

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
    # TODO: Put GUI code up in this fat boy function
    pass


if __name__ == "__main__":
    main()