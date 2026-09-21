# -*- coding: utf-8 -*-
import FreeCAD as App
import FreeCADGui as Gui
from PySide import QtGui, QtCore

class ColorPanelWidget(QtGui.QWidget):

  def __init__(self):
    super().__init__()

    # Define color choices (RGB tuples scaled 0.0 to 1.0 by dividing by RGB color by 255)
    self.colors = {
        'Red': (0.8, 0.1, 0.1),
        'Green': (0.1, 0.8, 0.1),
        'Blue': (0.1, 0.3, 0.8),
        'Yellow': (0.9, 0.8, 0.1),
        'Gray': (0.5, 0.5, 0.5),
        'Brass': (0.7, 0.65, 0.26),
        'Aluminum': (0.66,0.62,0.71),
        'copper': (0.7,0.427,0.18),
        'Magenta': (0.99,0.01,0.99),
        'Cyan': (0.01,0.99,0.99),
    }

    # Ultra-tight horizontal layout
    layout = QtGui.QHBoxLayout(self)
    layout.setContentsMargins(1, 0, 1, 0)  # Zero top/bottom margin
    layout.setSpacing(2)  # Tiny gaps between swatches

    # Create micro-buttons for each color
    for name, rgb in self.colors.items():
      btn = QtGui.QPushButton()
      btn.setFixedSize(16, 16)  # 10x10 micro swatches

      # Unpack the tuple into individual R, G, B components
      r, g, b = rgb
      hex_col = '#{:02x}{:02x}{:02x}'.format(
          int(r * 255), int(g * 255), int(b * 255)
      )

      btn.setStyleSheet(
          f'background-color: {hex_col}; border: 1px solid #777; border-radius:'
          ' 1px;'
      )
      btn.setToolTip(f'Set color to {name}')

      btn.clicked.connect(lambda checked=False, c=rgb: self.apply_color(c))
      layout.addWidget(btn)

  def apply_color(self, rgb_color):
    sel = Gui.Selection.getSelection()
    if not sel:
      return

    for obj in sel:
      if hasattr(obj, 'ViewObject') and obj.ViewObject:
        obj.ViewObject.ShapeColor = rgb_color


def run():
    # Create a Dock Widget wrapper
    mw = Gui.getMainWindow()

    # Remove existing panel if it is already open to avoid duplicates
    existing = mw.findChild(QtGui.QDockWidget, 'QuickColorPanel')
    if existing:
      mw.removeDockWidget(existing)
      existing.deleteLater()

    dock = QtGui.QDockWidget('Quick Colors', mw)
    dock.setObjectName('QuickColorPanel')

    # Hide the title bar / handle completely
    empty_title_bar = QtGui.QWidget()
    dock.setTitleBarWidget(empty_title_bar)

    # Allow it to be docked anywhere
    dock.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)

    # Extreme compact constraints so it doesn't stretch long
    dock.setMaximumHeight(14)
    dock.setMinimumHeight(12)
    dock.setMaximumWidth(300)  # Restricts horizontal stretching

    # Set our swatch widget inside the dock panel
    panel = ColorPanelWidget()
    dock.setWidget(panel)

    # Snap it to the bottom dock area by default
    mw.addDockWidget(QtCore.Qt.BottomDockWidgetArea, dock)
    dock.show()


# This line ensures the macro can still be run manually inside FreeCAD
if __name__ == "__main__":
    run()
