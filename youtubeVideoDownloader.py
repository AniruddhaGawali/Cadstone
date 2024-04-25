
from pytube import YouTube

def download_video_with_audio(url, output_path):
    try:
        yt = YouTube(url)

        # Filter streams for a stream that contains both audio and video
        stream = yt.streams.filter(progressive=True).first()

        # Download the stream
        stream.download(output_path)

        print("Download completed successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
video_url = input("Enter the video URL: ")
output_path = "./videos/"
download_video_with_audio(video_url, output_path)


