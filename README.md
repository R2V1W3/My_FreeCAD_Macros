# My FreeCAD Macros

# * <ins>Remap Sketch To LCS Origin Plane Macro</ins>
This Macro detaches selected Sketch and reattaches it to the nearest body origin plane, and applies appropriate offsets to preserve original spatial position. 
#
Please use updated **Remap_Sketch_to_LCS.FCMacro**. 
#
Deprecated **Remap_sketch_to_origin.FCMacro** contains a deprecated function that will no longer work after version 27.2. 
#



(1) Download Macro to your Macro folder, (2) open it in FreeCAD Macro editor, (3) select the sketch and (4) execute the macro. You must select the sketch first. 

# * <ins>Long Right Click Listener Macro</ins>

This Macro listens to Mouse Long-right-click with 400ms delay (_Line: 8 LONGH_CLICK_THRESHOL constant_) and runs any FreeCAD command assigned to it.
#
Edit Line 16: **Gui.runCommand("Std_ViewFitAll")** to run any built in FreeCAD command with Long_Right_Click

# * <ins>Color Swatches Macro</ins>

This Macro applies color to selected objects. Select objects, then select color. 
#
Macro creates **"Quick Colors"** Panel and by default places it at the bottom. It's dockable so can be moved elsewhere. You can run ColorSwatches.FCMacro manually every time you start FreeCAD, or you can run ColorSwatches,py to run automatically at start. 
#
To **run macro** at startup:
Place **ColorSwatches.py** in your **Macro** folder, such as this Linux full path when running AppImage:

.local/share/FreeCAD/v1-2/Macro/ColorSwatches.py

Place **InitGui.py** in **Mod/MacroAtStartup** folder. If it doesn't exist create it. Linux full path: 

.local/share/FreeCAD/v1-2/Mod/MacroAtStartup/InitGui.py

Note that **Macro** folder and **Mod** folders are next to each other. 




