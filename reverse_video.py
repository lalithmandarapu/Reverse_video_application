import cv2
import numpy as np
from scipy.io import wavfile
import moviepy.editor as mp
import os
import time
from moviepy.config import change_settings

# ✅ Set the path to your FFmpeg binary (adjust if needed)
change_settings({
    "FFMPEG_BINARY": r"D:/Projects/Reverse-Video-Application-main/ffmpeg-7.1.1/ffmpeg-7.1.1/bin/ffmpeg.exe"
})

def reverse_video(input_path, output_path):
    timestamp = str(int(time.time()))
    temp_audio = f"temp_audio_{timestamp}.wav"
    temp_reversed_audio = f"temp_reversed_audio_{timestamp}.wav"
    temp_video = f"temp_video_{timestamp}.mp4"

    try:
        video = mp.VideoFileClip(input_path)
        if video.audio:
            video.audio.write_audiofile(temp_audio)
        video.close()

        cap = cv2.VideoCapture(input_path)
        if not cap.isOpened():
            raise Exception("Cannot open video file.")

        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(temp_video, fourcc, fps, (width, height))

        frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)

        for frame in reversed(frames):
            out.write(frame)

        cap.release()
        out.release()

        if os.path.exists(temp_audio):
            sr, audio_data = wavfile.read(temp_audio)
            reversed_audio = audio_data[::-1]
            wavfile.write(temp_reversed_audio, sr, reversed_audio)

            video_clip = mp.VideoFileClip(temp_video)
            audio_clip = mp.AudioFileClip(temp_reversed_audio)
            final_clip = video_clip.set_audio(audio_clip)

            final_clip.write_videofile(
                output_path,
                codec="libx264",
                audio_codec="aac",
                temp_audiofile=f"temp_final_audio_{timestamp}.m4a",
                remove_temp=True
            )

            video_clip.close()
            audio_clip.close()
            final_clip.close()
        else:
            os.rename(temp_video, output_path)

    finally:
        for f in [temp_audio, temp_reversed_audio, temp_video]:
            if os.path.exists(f):
                try:
                    os.remove(f)
                except Exception as e:
                    print(f"Could not delete temp file {f}: {e}")
