import os
from moviepy.editor import VideoFileClip

def convert_video_to_audio(input_file, output_file):
    try:
        # Load the video file
        video = VideoFileClip(input_file)
        
        # Extract the audio from the video
        audio = video.audio
        
        # Write the audio to a file
        audio.write_audiofile(output_file)
        
        # Close the video file
        video.close()
        
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def main():
    print("Video to Audio Converter")
    
    while True:
        # Select video input
        input_file = input("Enter the path to the video file (or 'q' to quit): ")
        
        if input_file.lower() == 'q':
            print("Exiting the program.")
            break
        
        # Check if the file exists and is a valid video file
        if not os.path.exists(input_file):
            print("Alert: Invalid video input. File does not exist.")
            continue
        
        if not input_file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            print("Alert: Invalid video input. Unsupported file format.")
            continue
        
        # Generate output file name
        output_file = os.path.splitext(input_file)[0] + '.mp3'
        
        print("Converting video to audio...")
        success = convert_video_to_audio(input_file, output_file)
        
        if success:
            print(f"Conversion successful. Audio saved as: {output_file}")
        else:
            print("Alert: Error extracting audio. Conversion failed.")

if __name__ == "__main__":
    main()
