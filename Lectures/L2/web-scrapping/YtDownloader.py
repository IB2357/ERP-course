from pytube import YouTube

video_url = input("Welcome to YtDownloader\n\n\t Enter URL: ")

yt = YouTube(video_url)

streams = yt.streams.filter(progressive=True, file_extension='mp4')

print("Available streams:")
for stream in streams:
    print(f"Resolution: {stream.resolution}, File Type: {stream.type}")

chosen_resolution = input("Enter the desired resolution (e.g., '720p'): ")
chosen_type = input("Do you want to download 'video' or 'audio'?: ")

selected_stream = streams.filter(res=chosen_resolution, type=chosen_type).first()

if selected_stream:
    if chosen_type == 'video':
        selected_stream.download(output_path='downloads', filename_prefix='video_')
        print(f"Video downloaded in {chosen_resolution} successfully.")
    elif chosen_type == 'audio':
        selected_stream.download(output_path='downloads', filename_prefix='audio_')
        print("Audio downloaded successfully.")
else:
    print("No matching stream found. Please check your chosen resolution and type.")
