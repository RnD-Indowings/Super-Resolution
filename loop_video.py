from moviepy.editor import VideoFileClip, concatenate_videoclips

# Load your video
clip = VideoFileClip("/home/udit/Downloads/5mins.qt")

# Repeat it 6 times
final_clip = concatenate_videoclips([clip] * 6)

# Save the output
final_clip.write_videofile("/home/udit/Real-ESRGAN/30mins.mp4", codec="libx264", audio_codec="aac")
