import sqlite3
from datetime import datetime

conn = sqlite3.connect('gym.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS members(
               name TEXT NOT NULL,
               member_id INTEGER PRIMARY KEY,
               phone_no INTEGER NOT NULL,
               membership_type TEXT NOT NULL,
               start_date TEXT NOT NULL,
               end_date TEXT NOT NULL
               )

''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance(
               attendance_id INTEGER PRIMARY KEY,
               date TEXT NOT NULL
               )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS equipment(
               equipment_id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               quantity INTEGER NOT NULL
               )
''')


def register_members():
    name = input("Enter name:")
    member_id = input("Enter member ID:")
    phone_no = input("Enter phone no:")
    membership_type = input("Enter membership type:")
    start_date = input("Enter starting date:")
    end_date = input("Enter ending date:")

    cursor.execute("""INSERT INTO members(name,member_id,phone_no,membership_type,start_date,end_date) VALUES(?,?,?,?,?,?)""",(name,member_id,phone_no,membership_type,start_date,end_date))

    conn.commit()

    print("Member registered sucessfully!")

def view_members():
    print("Members are: ")
    cursor.execute("SELECT * FROM members")
    for i in cursor.fetchall():
        print(f"Name: {i[0]},ID : {i[1]},phone no : {i[2]},Membership type:{i[3]},Start date : {i[4]}, End date : {i[5]}")

def mark_attendance():
    attendace_id = input("Enter attendace_id:")
    date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""INSERT INTO attendance(attendance_id,date) VALUES (?,?)""",(attendace_id,date))

    conn.commit()
    print("Attendance marked successfully!")

def view_attendance():
    print("Viewing Attedance...")
    cursor.execute("SELECT * FROM attendance")
    for i in cursor.fetchall():
        print(f"Attendace ID: {i[0]},Date: {i[1]}")

def add_equipment():
    equipment_id = input("Enter equipment ID:")
    name = input("Enter equipment name:")
    quantity = input("Enter quantity:")

    cursor.execute("""INSERT INTO equipment(equipment_id,name,quantity) VALUES (?,?,?)""",(equipment_id,name,quantity))

    conn.commit()
    print("Equipment added Successfully! ")

def view_equipment():
    print("Viewing Equipments: ")
    cursor.execute("SELECT * FROM equipment")
    for i in cursor.fetchall():
        print(f"Equipemt ID : {i[0]},Equipment Name: {i[1]},Quantity: {i[2]}")



def main():
    while True:
        print("--------------GYM SYSTEM-------------")
        print("1.Register members")
        print("2.view members")
        print("3.Mark attendance")
        print("4.View attendance")
        print("5.Add equipment")
        print("6.view equipments")
        print("7.Exit")

        choice = input("Enter choice:")

        match choice:
            case '1':
                register_members()
            case '2':
                view_members()
            case '3':
                mark_attendance()
            case '4':
                view_attendance()
            case '5':
                add_equipment()
            case '6':
                view_equipment()
            case '7':
                break
            case _:
                print("Invalid Choice!")
    
    conn.close()



if __name__ == "__main__":
    main()