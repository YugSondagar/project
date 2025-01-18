import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
            )

''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for i in cursor.fetchall():
        print(i)


def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    conn.commit()


def update_video(name,time,video_id):
    cursor.execute("UPDATE videos SET name=? ,time=? WHERE id=?",(name,time,video_id))
    conn.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?",(video_id,))   #idar comma is liye bcoz vo ek tuple leta hai tho agar ek hi hai then hamlog hamesha , lagayenge.
    conn.commit()



def main():
    while True:
        print("\n Youtube Manager with DB")
        print("1.List videos")
        print("2.Add videos")
        print("3.Update videos")
        print("4.Delete videos")
        print("5. Exit app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter name:")
            time = input("Enter time:")
            add_video(name,time)
        elif choice == '3':
            video_id = input("Enter video ID:")
            name = input("Enter name:")
            time = input("Enter time:")
            update_video(name,time,video_id)
        elif choice == '4':
            video_id = input("Enter video id:")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice!")

    conn.close()



if __name__ == "__main__":
    main()

















