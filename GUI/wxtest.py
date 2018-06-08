import wx


class Example(wx.Frame):
    def __init__(self, parent, title, size):
        super(Example, self).__init__(parent, title=title, size=size)
        self.Center()
        self.Maximize()
        
def main():
    app = wx.App()
    size = wx.Display().GetGeometry()[2:4]
    width, height = size[0] * 0.9, size[1] * 0.9
    ex = Example(None, title='Sizing', size=(width, height))
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
