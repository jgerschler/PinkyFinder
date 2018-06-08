import wx


class MainFrame(wx.Frame):
    def __init__(self, parent, title, size):
        super(MainFrame, self).__init__(parent, title=title, size=size)

        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW, '&New')
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.Append(wx.ID_SAVE, '&Save')
        fileMenu.AppendSeparator()

        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import new print...')
        imp.Append(wx.ID_ANY, 'Find existing print...')

        fileMenu.Append(wx.ID_ANY, 'I&mport', imp)

        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
##        qmi.SetBitmap(wx.Bitmap('exit.png'))
        fileMenu.Append(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

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
