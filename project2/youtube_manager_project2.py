
import json




def load_data():
    try:
        with open('youtube.txt','r') as file:
            test = json.load(file)  
            print(type(test))    #it is a json list 
            # print(test)
            return test    
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)      #json.dump() takes 2 parameters 1.kaha lena hai, 2.kaha pe lena hai


def list_all_videos(videos):
    #as it is a list we can directly access the elements by using for loop so why we need to convert it into enumerate() bcoz we dont know the order so to know perfect order after deletion and updation we are using enumerate().
    print("\n")
    print("*" * 50)
    for index,video in enumerate(videos,start=1):
        
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 50)

def add_video(videos):
    name=input("Enter video name:")
    time=input("Enter video time:")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number you want to update"))
    if 1<=index <= len(videos):
        name=input("Enter new video name:")
        time=input("Enter new video time:")
        videos[index-1] = {'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number you want to delete"))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index selected")  


def main():
    videos = load_data()
    while True:
        print("\n youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video")
        print("3. Update a youtube video ")
        print("4. Delete a youtube video ")
        print("5. Close the app ")
        choice=input("Enter a choice:") 
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice")

if __name__=="__main__":
    main()



