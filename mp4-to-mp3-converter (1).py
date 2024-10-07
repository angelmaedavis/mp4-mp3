from moviepy.editor import VideoFileClip
import os

def convert_mp4_to_mp3(input_file, output_file):
    # Load the video file
    video = VideoFileClip(input_file)
    
    # Extract the audio
    audio = video.audio
    
    # Write the audio to a file
    audio.write_audiofile(output_file)
    
    # Close the video and audio objects
    video.close()
    audio.close()

def main():
    # Get input and output file paths from user
    input_file = input("Enter the path to the MP4 file: ")
    output_file = input("Enter the path for the output MP3 file: ")
    
    # Ensure input file exists
    if not os.path.exists(input_file):
        print("Error: Input file does not exist.")
        return
    
    # Ensure input file is an MP4
    if not input_file.lower().endswith('.mp4'):
        print("Error: Input file must be an MP4.")
        return
    
    # Ensure output file has .mp3 extension
    if not output_file.lower().endswith('.mp3'):
        output_file += '.mp3'
    
    try:
        convert_mp4_to_mp3(input_file, output_file)
        print(f"Conversion complete. MP3 file saved as: {output_file}")
    except Exception as e:
        print(f"An error occurred during conversion: {str(e)}")

if __name__ == "__main__":
    main()
