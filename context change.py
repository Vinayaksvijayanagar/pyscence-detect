import os
import cv2
import numpy as np
from scenedetect import VideoManager, SceneManager, split_video_ffmpeg
from scenedetect.detectors import ContentDetector
from sklearn.cluster import KMeans

def detect_scenes(video_path, threshold=30.0):
    """Detects scenes in a video using PySceneDetect."""
    video_manager = VideoManager([video_path])
    scene_manager = SceneManager()
    scene_manager.add_detector(ContentDetector(threshold=threshold))
    
    video_manager.set_downscale_factor()
    video_manager.start()
    scene_manager.detect_scenes(video_manager)
    scene_list = scene_manager.get_scene_list()
    video_manager.release()
    
    return scene_list

def analyze_scene_context(video_path, start_time, end_time):
    """Analyzes visual context of a detected scene."""
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    start_frame = int(start_time.get_seconds() * fps)
    end_frame = int(end_time.get_seconds() * fps)
    middle_frame = start_frame + (end_frame - start_frame) // 2
    
    cap.set(cv2.CAP_PROP_POS_FRAMES, middle_frame)
    ret, frame = cap.read()
    cap.release()
    
    if not ret:
        return None
    
    # Visual analysis
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    pixels = hsv.reshape((-1, 3))
    kmeans = KMeans(n_clusters=2).fit(pixels)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    
    return {
        'dominant_colors': kmeans.cluster_centers_,
        'edge_density': np.sum(edges) / (edges.size * 255),
        'brightness': np.mean(hsv[:,:,2]) / 255,
        'frame': frame
    }

def process_video(input_path, output_dir='output', threshold=30.0):
    """Main processing pipeline."""
    os.makedirs(output_dir, exist_ok=True)
    
    scene_list = detect_scenes(input_path, threshold)
    print(f"Detected {len(scene_list)} scenes")
    
    scene_contexts = []
    for i, (start_time, end_time) in enumerate(scene_list):
        context = analyze_scene_context(input_path, start_time, end_time)
        scene_contexts.append({
            'scene_num': i+1,
            'start_time': start_time.get_seconds(),
            'end_time': end_time.get_seconds(),
            'duration': (end_time - start_time).get_seconds(),
            'context': context
        })
    
    split_video_ffmpeg(input_path, scene_list, output_dir=output_dir, hide_progress=False)
    return scene_contexts

if __name__ == "__main__":
    # ===== Hardcoded Configuration - MODIFY THESE VALUES =====
    VIDEO_FILE_PATH = r""#  Replace with your video path
    OUTPUT_DIRECTORY = "output"     # Folder for scene clips
    DETECTION_THRESHOLD = 30.0      # Lower = more sensitive
    
    # ===== Processing =====
    results = process_video(
        input_path=VIDEO_FILE_PATH,
        output_dir=OUTPUT_DIRECTORY,
        threshold=DETECTION_THRESHOLD
    )
    
    # ===== Results Output =====
    print("\nScene Context Analysis:")
    for scene in results:
        if scene['context']:
            colors = scene['context']['dominant_colors']
            print(f"\nScene {scene['scene_num']} ({scene['duration']:.2f}s):")
            print(f"  - Brightness: {scene['context']['brightness']:.2f}")
            print(f"  - Edge Density: {scene['context']['edge_density']:.2f}")
            print(f"  - Dominant Colors (HSV): {colors[0].astype(int)}, {colors[1].astype(int)}")
