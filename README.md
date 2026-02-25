# 🎥 Intelligent Camera Angle & Scene Change Detection System

An automated video analysis system that detects **camera angle changes and scene transitions** using Computer Vision and Machine Learning techniques.

---

## 🧩 Problem
Manual identification of camera angle changes and scene transitions in videos is time-consuming and error-prone.  
This project automates the process to enable fast and reliable video segmentation.

---

## 🧠 Models & Tools
- PySceneDetect – Scene boundary detection  
- K-Means Clustering – Color histogram similarity analysis  
- Python, OpenCV, NumPy  

---

## 🏗️ Architecture
Input Video
→ Frame Extraction
→ Preprocessing
→ PySceneDetect
→ Feature Extraction
→ K-Means Clustering
→ Decision Engine
→ Crop & Save Scenes
→ Output (Scenes + Timestamps)


---

## ⚡ Performance (11-Minute Video)
- Scene detection: 30–35 seconds  
- Crop & save scenes: 2–2.5 minutes  

---

## 🎯 Accuracy
- PySceneDetect: 70–90%  
- K-Means: ~85%  

---

## 🚧 Limitations
- Slower for high-resolution videos  
- Sensitive to extreme lighting changes  

---

## 🚀 Future Enhancements
- Train deep learning models with labeled datasets  
- Automatic genre classification (Action, Drama, Comedy, etc.)  
- GPU acceleration  

---

## 🎬 Demo Video
https://drive.google.com/file/d/17dioWVazRYF0MrNdHTFjgr4SQ_SwJUMP/view
