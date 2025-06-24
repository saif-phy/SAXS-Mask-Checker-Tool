import tkinter as tk
from tkinter import filedialog
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class SAXSGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SAXS Mask Checking Tool")
        self.geometry("1000x600")
        
        # Initialize data variables
        self.data = None
        self.mask = None

        # Top frame for file selection and toggle controls
        frame_controls = tk.Frame(self)
        frame_controls.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        
        # Button to load SAXS data file
        self.btn_load_data = tk.Button(frame_controls, text="Load SAXS Data (.tif)", command=self.load_data)
        self.btn_load_data.pack(side=tk.LEFT, padx=5)
        
        # Button to load mask file
        self.btn_load_mask = tk.Button(frame_controls, text="Load Mask (.tif)", command=self.load_mask)
        self.btn_load_mask.pack(side=tk.LEFT, padx=5)
        
        # Toggle to choose fixed axis (x or y)
        self.fixed_axis = tk.StringVar(value="x")  # default is to fix x axis
        frame_toggle = tk.Frame(frame_controls)
        frame_toggle.pack(side=tk.LEFT, padx=10)
        tk.Label(frame_toggle, text="Fixed Axis:").pack(side=tk.LEFT)
        tk.Radiobutton(frame_toggle, text="X", variable=self.fixed_axis, value="x", command=self.update_profile).pack(side=tk.LEFT)
        tk.Radiobutton(frame_toggle, text="Y", variable=self.fixed_axis, value="y", command=self.update_profile).pack(side=tk.LEFT)
        
        # Frame for slider controls
        frame_sliders = tk.Frame(self)
        frame_sliders.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        
        # Slider for x axis (will be updated after data load)
        self.slider_x = tk.Scale(frame_sliders, label="X Position", from_=0, to=100, orient=tk.HORIZONTAL, command=self.slider_changed)
        self.slider_x.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        # Slider for y axis (will be updated after data load)
        self.slider_y = tk.Scale(frame_sliders, label="Y Position", from_=0, to=100, orient=tk.HORIZONTAL, command=self.slider_changed)
        self.slider_y.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        # Create matplotlib figure with two subplots:
        # Left: SAXS data image; Right: intensity profile plot
        self.fig, (self.ax_image, self.ax_profile) = plt.subplots(1, 2, figsize=(10, 5))
        plt.tight_layout()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Add the matplotlib navigation toolbar to enable zoom/pan features
        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    def load_data(self):
        """Load the original SAXS data (.tif) file."""
        filename = filedialog.askopenfilename(filetypes=[("TIFF files", "*.tif *.tiff")])
        if filename:
            self.data = np.array(Image.open(filename))
            self.update_image_plot()
    
    def load_mask(self):
        """Load the corresponding mask (.tif) file."""
        filename = filedialog.askopenfilename(filetypes=[("TIFF files", "*.tif *.tiff")])
        if filename:
            self.mask = np.array(Image.open(filename))
            self.update_image_plot()
    
    def update_image_plot(self):
        """Plot the SAXS data image and update slider ranges based on image dimensions."""
        if self.data is not None:
            self.ax_image.clear()
            self.ax_image.imshow(self.data, cmap='viridis')
            self.ax_image.set_title("SAXS Data")
            
            # Update slider ranges based on image dimensions
            ny, nx = self.data.shape
            self.slider_x.config(to=nx - 1)
            self.slider_y.config(to=ny - 1)
            # Set initial slider positions at center
            self.slider_x.set(nx // 2)
            self.slider_y.set(ny // 2)
            
            self.canvas.draw()
            self.update_profile()
    
    def slider_changed(self, event=None):
        """Callback when slider values change."""
        self.update_profile()
    
    def update_profile(self):
        """Plot the intensity profile for the fixed axis selection.
        
        If the fixed axis is 'x', the program extracts the column at the given x position 
        and plots the intensity vs. y for both the normalized data and the mask.
        If 'y' is fixed, the row at the given y position is used and intensity is plotted vs. x.
        """
        if self.data is None or self.mask is None:
            return  # Wait until both files are loaded
        
        x_pos = int(self.slider_x.get())
        y_pos = int(self.slider_y.get())
        self.ax_profile.clear()
        
        if self.fixed_axis.get() == "x":
            # Fixed x axis: extract column data (all y values) at x position
            data_profile = self.data[:, x_pos]
            mask_profile = self.mask[:, x_pos]
            # Normalize the original data intensity so its maximum is 1
            data_profile_norm = data_profile / np.max(data_profile)
            mask_profile_norm = mask_profile / np.max(mask_profile)
            # Plot data intensity (normalized) and mask along y
            self.ax_profile.plot( np.arange(len(data_profile)),data_profile_norm, label="Data (norm)")
            self.ax_profile.plot( np.arange(len(mask_profile)),mask_profile_norm, label="Mask")
            # Invert the y-axis
            self.ax_profile.invert_yaxis()
            self.ax_profile.set_xlabel("Y Axis")
            self.ax_profile.set_ylabel("Intensity")
            self.ax_profile.invert_yaxis()  # Optional: invert y-axis to match image orientation
        else:
            # Fixed y axis: extract row data (all x values) at y position
            data_profile = self.data[y_pos, :]
            mask_profile = self.mask[y_pos, :]
            mask_profile_norm = mask_profile / np.max(mask_profile)
            data_profile_norm = data_profile / np.max(data_profile)

            # Plot data intensity (normalized) and mask along x
            self.ax_profile.plot( np.arange(len(data_profile)),data_profile_norm, label="Data (norm)")
            self.ax_profile.plot(  np.arange(len(mask_profile)),mask_profile_norm, label="Mask")
            self.ax_profile.set_xlabel("X Axis")
            self.ax_profile.set_ylabel("Intensity")
        
        self.ax_profile.legend()
        self.ax_profile.set_title("Intensity Profile")
        self.canvas.draw()

if __name__ == "__main__":
    app = SAXSGUI()
    app.mainloop()
