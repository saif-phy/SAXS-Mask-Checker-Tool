# SAXS Mask Checking Tool

A Python-based GUI application for visualizing and comparing Small-Angle X-ray Scattering (SAXS) data with its corresponding mask image. Built with tkinter, matplotlib, and PIL, this tool allows users to interactively inspect SAXS .tif images and verify the accuracy of their binary masks by analyzing pixel-level intensity profiles.

🧰 Features
📂 Load SAXS data and mask .tif files.

🎚️ Interactive sliders to examine data row-by-row or column-by-column.

🔁 Toggle between X and Y axis for fixed profile view.

📈 Real-time intensity profile plot with normalized data and mask curves.

🔎 Zoom and pan controls powered by Matplotlib's toolbar.

🧪 Designed for quick inspection and validation of beamstop or gap masks.

📷 GUI Overview
Left Panel: SAXS image loaded from .tif file.

Right Panel: Corresponding intensity profile along selected axis.

Controls:

File loaders for data and mask.

Axis toggle (X or Y).

Sliders to choose specific slice positions.

🚀 Getting Started
🖥️ Prerequisites
Install required Python packages:
pip install numpy matplotlib Pillow
Note: tkinter comes pre-installed with standard Python distributions.

📦 Run the App
Save the script as saxs_gui.py, then launch it using:
python saxs_gui.py
📁 File Requirements
SAXS Data: 2D grayscale .tif file containing raw SAXS image.

Mask File: Binary .tif file (same dimensions) representing masked regions.

📌 Both files must have the same shape and pixel alignment.

🛠️ Usage Tips
Load data first, then the mask.

Use the X/Y toggle to fix a direction for slicing.

Adjust sliders to scan through columns (X) or rows (Y).

Compare the normalized intensity profile with the mask pattern to validate its coverage.

🧪 Example Applications
Checking beamstop masks for alignment and coverage.

Verifying detector gap masks.

Interactive quality control of preprocessing pipelines for SAXS/WAXS.

📸 Screenshots

![screenshot.png](https://github.com/saif-phy/SAXS-Mask-Checker-Tool/blob/1bad3a3b9dbf69d4e9219ac0ac9c90c4e699b3cc/screenshot.png)

📄 License
This project is open source and available under the MIT License.

👤 Author
Developed by saif
If you find this tool useful, feel free to ⭐ the repo and contribute!
