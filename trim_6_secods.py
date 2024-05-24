from moviepy.video.io.VideoFileClip import VideoFileClip

# Load the video file
clip = VideoFileClip("a6.mp4")

# Extract the first 6 seconds of the video
start_time = 1
end_time = 6
clip = clip.subclip(start_time, end_time)

# Save the trimmed video to a new file
clip.write_videofile("output_video6.mp4")
