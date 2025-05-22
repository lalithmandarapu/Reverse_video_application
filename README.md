# Reverse Video Web Application

A Flask-based web application that lets users upload a video, reverses its video and audio, and allows downloading the reversed output.

---

##  Project Structure

```
Reverse-Video-Application/
├── app.py
├── reverse_video.py
├── requirements.txt
├── uploads/
├── outputs/
├── static/
│   └── index.html
├── ffmpeg/
│   └── ffmpeg.exe (optional, if using custom path)
```

---

##  Features

- Upload `.mp4` videos from your browser
- Reverses both video frames and audio
- Downloads the processed video with reversed content
- Temporary files are auto-deleted
- Cross-platform support (Windows tested)

---

##  Requirements

Make sure you have Python 3.7+ installed.  
Install all required packages:

```bash
pip install -r requirements.txt
```

**requirements.txt**
```
moviepy
opencv-python
numpy
scipy
```

---

##  FFMPEG Setup (Important)

If `moviepy` complains about missing ffmpeg, do one of the following:

### Option 1: Let moviepy handle it automatically

It should work out of the box.

### Option 2: Use your own ffmpeg binary

If you have a local ffmpeg installed (like in this path):

```
D:\Projects\Reverse-Video-Application-main\ffmpeg-7.1.1\ffmpeg-7.1.1\ffbuild\bin
```

Update your Python script (`reverse_video.py`) to set the path:

```python
import os
os.environ["IMAGEIO_FFMPEG_EXE"] = r"D:\Projects\Reverse-Video-Application-main\ffmpeg-7.1.1\ffmpeg-7.1.1\ffbuild\bin\ffmpeg.exe"
```

---

##  Running the App

1. Activate your virtual environment (optional but recommended):

```bash
venv\Scripts\activate  # For Windows
```

2. Run the Flask app:

```bash
python app.py
```

3. Open your browser and go to:  
   `http://127.0.0.1:5000/`

---

##  Usage

1. Choose a `.mp4` file.
2. Click "Upload and Process".
3. The reversed video will be downloaded automatically.

---

##  Clean-Up

Temporary audio and video files are deleted after processing, so your disk stays clean.

---

##  Output

The processed reversed file is saved temporarily in the `outputs/` folder and served to the user as a download.

---

##  Troubleshooting

- **moviepy not found?** → Run: `pip install moviepy`
- **ffmpeg not working?** → Set the `IMAGEIO_FFMPEG_EXE` environment variable
- **Permission denied?** → Try running the terminal as admin

---

##  Credits

- Flask – web framework
- OpenCV – video frame processing
- MoviePy – audio extraction and video output
- NumPy & SciPy – audio manipulation
