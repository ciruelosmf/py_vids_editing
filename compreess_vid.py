import moviepy.editor as mp

def reduce_video_size(input_file, output_file, target_size_mb):
    # Load the video
    video = mp.VideoFileClip(input_file)
    
    # Calculate the target bitrate in kbps
    target_size_kb = target_size_mb * 1024  # Convert MB to KB
    duration = video.duration  # Duration in seconds
    target_bitrate = (target_size_kb * 8) / duration  # kbps

    # Set the new video parameters
    video.write_videofile(
        output_file,
        codec='libx264',
        bitrate=f'{int(target_bitrate)}k',
        audio_codec='aac',
        audio_bitrate='128k'
    )

# Usage
input_file = "C:\\Users\\p\\Documents\\estudios\\01\\python\\projects\\compiled_dude_coding_frontend_v0_vercel_project_ai.mp4"
output_file = "compiled_dude_coding_frontend_v0_vercel_project_ai_compress_output_video.mp4"
target_size_mb = 900  # Target size in MB

reduce_video_size(input_file, output_file, target_size_mb)
