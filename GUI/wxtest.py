import wx


class MainFrame(wx.Frame):
    def __init__(self, parent, title, size):
        super(MainFrame, self).__init__(parent, title=title, size=size)

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

        self.Center()
        self.Maximize()

    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    size = wx.Display().GetGeometry()[2:4]
    width, height = size[0] * 0.9, size[1] * 0.9
    ex = MainFrame(None, title='Pinky Finder', size=(width, height))
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
