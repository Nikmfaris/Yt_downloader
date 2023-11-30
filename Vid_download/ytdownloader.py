from pytube import YouTube
condition =True

while condition  :

    link = input("enter your link : ") 

    # file location 
    directory = "D:/yt"
    try:
        yt = YouTube(link)
    except:
        print("Download failed")


    vid_type = input("Choose mp3 or mp4: ")  

    stream = yt.streams

    if vid_type.lower() == 'mp3':
        video_stream = stream.filter(only_audio=True).first()
        video_stream.download(output_path=directory)

        print("video downloaded check " + directory)

    elif vid_type.lower() == 'mp4':

        # use this to get highiest resolution,
        #  video_stream = stream.filter(file_extension="mp4").get_highest_resolution()
        # video_stream= stream.download(output_path=directory)

        video_stream = stream.filter(file_extension="mp4")
        video_stream= stream.filter(res="1080p").first().download(output_path=directory)
        
        print("video downloaded check " + directory)

    else:
        print("Invalid video type. Please choose 'mp3' or 'mp4'.")

    UserLoop = input("do you want to continue (yes/no) : " )

    if UserLoop.lower() == 'yes':
       condition = True 
    elif UserLoop.lower() == 'no':
       condition = False 
    else:
        print("Invalid choice. Assuming 'no' to exit.")
        condition = False


