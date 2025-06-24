#SAXS Mask Checking Tool
This repository contains a graphical user interface (GUI) built with Python and Tkinter for interactively inspecting and verifying masks for 2D SAXS/WAXS data.

The tool allows a user to load both a raw data file and its corresponding mask file. It provides a visual interface to slide through the data and see a 1D profile of both the data intensity and the mask values, making it easy to confirm if artifacts (like beamstops or detector gaps) are correctly covered by the mask.

Key Features
Interactive GUI: A user-friendly interface for visual inspection.

File Loading: Buttons to easily load SAXS data and mask files (.tif format).

Linked Image and Profile Views: Displays the 2D SAXS image alongside a 1D intensity profile plot.

Interactive Sliders: Sliders for both X and Y axes allow the user to select a specific row or column to inspect.

Switchable Profile Axis: Radio buttons let you instantly switch between viewing a vertical (fixed X) or horizontal (fixed Y) intensity profile.

Normalized Overlay: The profile plot shows the normalized data intensity and the mask values overlaid, making it easy to see where the mask is active relative to data features.

How to Use the Tool
Launch the application.

Click "Load SAXS Data (.tif)" and select your 2D scattering data file. The image will appear in the left panel.

Click "Load Mask (.tif)" and select the corresponding mask file.

Once both are loaded, the intensity profile will appear in the right panel.

Use the "X Position" and "Y Position" sliders to move the selection line through the data.

Use the "Fixed Axis" radio buttons to choose whether you are viewing a vertical slice (fixing the X position) or a horizontal slice (fixing the Y position).

Analyze the "Intensity Profile" plot on the right. This plot shows how the mask aligns with the features in your data along the selected slice.

Requirements
The script requires the following Python libraries:

tkinter (usually included with standard Python installations)

numpy

Pillow (PIL)

matplotlib

You can install the necessary libraries using pip:

pip install numpy Pillow matplotlib

Running the Application
Clone the repository or save the script to a .py file.

Open your terminal or command prompt.

Navigate to the directory where you saved the script.

Run the script:

python your_script_name.py

License
This project is licensed under the MIT License. See the LICENSE file for details.
