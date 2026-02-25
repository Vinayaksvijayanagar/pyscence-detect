<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Intelligent Camera Angle & Scene Change Detection System</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            background: #f5f7fb;
            color: #333;
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }
        header {
            background: linear-gradient(135deg, #1f2933, #111827);
            color: #fff;
            padding: 40px 20px;
            text-align: center;
        }
        section {
            max-width: 1000px;
            margin: auto;
            padding: 25px 20px;
            background: #fff;
            margin-top: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        }
        h1, h2 {
            color: #1f2933;
        }
        ul {
            padding-left: 20px;
        }
        .diagram {
            background: #f1f5f9;
            padding: 20px;
            font-family: monospace;
            border-left: 5px solid #3b82f6;
            white-space: pre-wrap;
            border-radius: 6px;
        }
        .badge {
            display: inline-block;
            background: #3b82f6;
            color: white;
            padding: 6px 12px;
            border-radius: 20px;
            margin-right: 10px;
            font-size: 14px;
        }
        footer {
            text-align: center;
            padding: 25px;
            background: #111827;
            color: white;
            margin-top: 40px;
        }
        a {
            color: #2563eb;
            text-decoration: none;
            font-weight: bold;
        }
    </style>
</head>

<body>

<header>
    <h1>🎥 Intelligent Camera Angle & Scene Change Detection System</h1>
    <p>Automated video segmentation using Computer Vision & Machine Learning</p>
</header>

<section>
    <h2>🧩 Problem Definition</h2>
    <p>
        Manual identification of camera angle changes and scene transitions in videos is time-consuming and error-prone.
        This project proposes an automated system that detects scene changes and camera angle variations to enable
        efficient video segmentation and analysis.
    </p>
</section>

<section>
    <h2>🧠 Models & Techniques Used</h2>
    <span class="badge">PySceneDetect</span>
    <span class="badge">K-Means Clustering</span>
    <span class="badge">OpenCV</span>
    <span class="badge">Python</span>
    <span class="badge">NumPy</span>
</section>

<section>
    <h2>🏗️ System Architecture</h2>

    <div class="diagram">
Input Video
   │
   ▼
Frame Extraction (OpenCV)
   │
   ▼
Preprocessing (Resize, Normalize, Noise Reduction)
   │
   ▼
Scene Detection (PySceneDetect)
   │
   ├──► Candidate Scene Boundaries
   │
   ▼
Feature Extraction (Color Histograms)
   │
   ▼
K-Means Clustering
   │
   ▼
Decision Engine (Scene / Camera Angle Change)
   │
   ▼
Crop & Save Video Segments
   │
   ▼
Final Output (Scenes + Timestamps)
    </div>
</section>

<section>
    <h2>🔍 Architecture Explanation</h2>
    <ol>
        <li><b>Input Video:</b> The system takes a raw video file as input.</li>
        <li><b>Frame Extraction:</b> Video is split into frames using OpenCV.</li>
        <li><b>Preprocessing:</b> Frames are resized, normalized, and denoised.</li>
        <li><b>Scene Detection:</b> PySceneDetect detects abrupt and gradual transitions.</li>
        <li><b>Feature Extraction:</b> Color histograms are computed.</li>
        <li><b>K-Means Clustering:</b> Frames are grouped by visual similarity.</li>
        <li><b>Decision Engine:</b> Confirms true scene/camera angle change.</li>
        <li><b>Crop & Save:</b> Each validated scene is saved separately.</li>
        <li><b>Final Output:</b> Scene clips, timestamps, and scene count.</li>
    </ol>
</section>

<section>
    <h2>⚡ Performance (11-Minute Video)</h2>
    <ul>
        <li>Scene detection: <b>30–35 seconds</b></li>
        <li>Crop & save scenes: <b>2–2.5 minutes</b></li>
    </ul>
</section>

<section>
    <h2>🎯 Accuracy</h2>
    <ul>
        <li>PySceneDetect: <b>70–90%</b></li>
        <li>K-Means: <b>~85%</b></li>
    </ul>
</section>

<section>
    <h2>🚧 Limitations</h2>
    <ul>
        <li>Slower processing for high-resolution videos</li>
        <li>Sensitive to extreme lighting changes</li>
    </ul>
</section>

<section>
    <h2>🚀 Future Work</h2>
    <ul>
        <li>Train deep learning models with labeled datasets</li>
        <li>Automatic genre classification (Action, Drama, Comedy, etc.)</li>
        <li>GPU acceleration</li>
    </ul>
</section>

<section>
    <h2>🎬 Demo Video</h2>
    <a href="https://drive.google.com/file/d/17dioWVazRYF0MrNdHTFjgr4SQ_SwJUMP/view" target="_blank">
        Click here to watch demo
    </a>
</section>

<footer>
    <p>© 2026 Intelligent Scene Detection Project</p>
</footer>

</body>
</html>
