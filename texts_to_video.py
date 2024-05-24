from moviepy.editor import ImageClip, concatenate_videoclips
import os

# Get a list of all image files in the current directory
image_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(('.jpg', '.jpeg', '.png'))]

# Sort the image files by filename (you may want to change this to your preferred order)
image_files.sort()

# Set the duration for each image (2 seconds)
image_duration = 30  

# Create a list of ImageClips for each image, with the specified duration
clips = [ImageClip(image_file).set_duration(image_duration) for image_file in image_files]

# Concatenate the ImageClips into a single video clip
video_clip = concatenate_videoclips(clips)

# Set the duration of the entire video to 45 seconds
video_clip = video_clip.set_duration(60)

# Export the video
video_clip.write_videofile("output2.mp4", fps=24)





 













