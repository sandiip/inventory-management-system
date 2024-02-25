import sqlite3

conn = sqlite3.connect('products.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               price TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM products")
    for row in cursor.fetchall():
        print(row)

def add_video(name, price):
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    conn.commit()

def update_video(product_id, new_name, new_price):
    cursor.execute("UPDATE products SET name = ?, price = ? WHERE id = ?", (new_name, new_price, product_id))
    conn.commit()

def delete_video(product_id):
    cursor.execute("DELETE FROM videos where id = ?", (product_id,))
    conn.commit()

def main():
    while True:
        print("\n inventory-management-system app with DB")
        print("1. List of Products")
        print("2. Add Products")
        print("3. Update product")
        print("4. Delete product")
        print("5. exit app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the product name: ")
            price = input("Enter the product price: ")
            add_video(name, price)
        elif choice == '3':
            product_id = input("Enter product ID to update: ")
            name = input("Enter the product name: ")
            price = input("Enter the product price: ")
            update_video(product_id, name, price)
        elif choice == '4':
            product_id = input("Enter video ID to delete: ")
            delete_video(product_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice ")

    conn.close()

if __name__ == "__main__":
    main()