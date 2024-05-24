import random
from moviepy.editor import VideoFileClip, concatenate_videoclips

# List of video files
video_files = ['1.mp4', '2.mp4', '3.mp4', '4.mp4', '5.mp4', '6.mp4', '7.mp4']

# Duration of each random segment in seconds
segment_duration = 7

# List to store selected segments
selected_segments = []

# Select random segments from each video
for file in video_files:
    clip = VideoFileClip(file)
    duration = clip.duration
    
    # Select a random starting point for the segment
    start_time = random.uniform(0, duration - segment_duration)
    
    # Extract the segment using the start time and duration
    segment = clip.subclip(start_time, start_time + segment_duration)
    
    # Add the segment to the list
    selected_segments.append(segment)

# Concatenate the selected segments
final_clip = concatenate_videoclips(selected_segments)

# Write the final clip to a new file
final_clip.write_videofile('merged_video.mp4')
