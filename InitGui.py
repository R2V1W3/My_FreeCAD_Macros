import os
import FreeCAD as App
import FreeCADGui

def runStartupMacros(workbench_name):
    if workbench_name != "NoneWorkbench":
        # 1. Disconnect immediately so it only executes once
        FreeCADGui.getMainWindow().workbenchActivated.disconnect(runStartupMacros)
        
        macro_dir = App.getUserMacroDir()
        
        # 2. Check for whichever file extension you currently have saved
        macro_path_py = os.path.join(macro_dir, "ColorSwatches.py")
        macro_path_fc = os.path.join(macro_dir, "ColorSwatches.FCMacro")
        macro_path = macro_path_py if os.path.exists(macro_path_py) else macro_path_fc
        
        if os.path.exists(macro_path):
            try:
                # 3. Read the file content raw and execute it globally
                with open(macro_path, "r", encoding="utf-8") as f:
                    macro_code = f.read()
                
                # This executes the macro line-by-line in the main application environment
                exec(macro_code, globals())
                
            except Exception as e:
                App.Console.PrintError(f"Failed to load macro on startup: {str(e)}\n")
        else:
            App.Console.PrintError(f"Startup macro not found at: {macro_path_py}\n")

# Anchor to FreeCAD memory space
import __main__
__main__.runStartupMacros = runStartupMacros
FreeCADGui.getMainWindow().workbenchActivated.connect(runStartupMacros)



