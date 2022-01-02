import wx
from pcbnew import *
import os

class SwapComponents(ActionPlugin):
    def defaults(self):
        self.name = "SwapComponents"
        self.category = "Modify PCB"
        self.description = "Swap two selected components on the PCB"
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png')
        self.dark_icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png')
        self.show_toolbar_button = True

    def Run(self):
        board = GetBoard()
        selected_modules = []

        for module in board.GetModules():
            if module.IsSelected():
                selected_modules.append(module)

        if len(selected_modules) != 2:
            self.popup("Please select two components that you want to swap in place")
        else:
            tmp_position = selected_modules[0].GetPosition()
            tmp_orientation = selected_modules[0].GetOrientation()
            selected_modules[0].SetPosition(selected_modules[1].GetPosition())
            selected_modules[0].SetOrientation(selected_modules[1].GetOrientation())
            selected_modules[1].SetPosition(tmp_position)
            selected_modules[1].SetOrientation(tmp_orientation)
            Refresh()

    def popup(self, message, caption="SwapComponents plugin"):
        dlg = wx.MessageDialog(None, message, caption, wx.OK | wx.ICON_INFORMATION | wx.CENTRE)
        dlg.ShowModal()
        
