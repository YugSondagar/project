import sqlite3

conn = sqlite3.connect('customer.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               phone_no INTEGER NOT NULL,
               email TEXT 
            )
''')

def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    for i in cursor.fetchall():
        print(i)


def add_contacts(name,phone_no,email):
    cursor.execute("INSERT INTO contacts(name,phone_no,email) VALUES(?,?,?)",(name,phone_no,email))
    conn.commit()

def update_contacts(name,phone_no,email,id):
    cursor.execute("UPDATE contacts SET name =?,phone_no=?,email=? WHERE id=?",(name,phone_no,email,id))
    conn.commit()

def delete_contacts(id):
    cursor.execute("DELETE FROM contacts WHERE id =?",(id,))
    conn.commit()


def main():
    while True:
        print("-----------Contact Management System-----------")
        print("1.View contact")
        print("2.Add contact")
        print("3.Update contact")
        print("4.Delete contact")
        print("5.Exit")

        choice = input("Enter your choice:")

        match choice:
            case '1':
                view_contacts()
            case '2':
                name = input("Enter name:")
                phone_no = int(input("Enter phone no:"))
                email = input("Enter email:")
                add_contacts(name,phone_no,email)
            case '3':
                id = int(input("Enter contact id you want to update:"))
                name = input("Enter name:")
                phone_no = int(input("Enter phone no:"))
                email = input("Enter email:")
                update_contacts(name,phone_no,email,id)
            case '4':
                id = int(input("Enter contact id you want to delete:"))
                delete_contacts(id)
            case '5':
                break
            case _:
                print("Invalid choice!")
            
    


if __name__ == "__main__":
    main()