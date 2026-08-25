# My FreeCAD Macros

# * <ins>Remap Sketch To LCS Origin Plane Macro</ins>
This Macro detaches selected Sketch and reattaches it to the nearest body origin plane, and applies appropriate offsets to preserve original spatial position. 
#
Please use updated **Remap_Sketch_to_LCS.FCMacro**. 
#
Deprecated **Remap_sketch_to_origin.FCMacro** contains a deprecated function that will no longer work after version 27.2. 
#



(1) Download Macro to your Macro folder, (2) open it in FreeCAD Macro editor, (3) select the sketch and (4) execute the macro. You must select the sketch first. 

# * <ins>Right Long Click Listener Macro</ins>

This Macro listens to Mouse-right-click with 400ms delay (_Line: 8 LONGH_CLICK_THRESHOL constant_) and runs any FreeCAD command assignet to it.
#
Edit Line 16: **Gui.runCommand("Std_ViewFitAll")** to run any built in FreeCAD command with Long_Right_Click

