from PySide import QtCore, QtGui
from block import Block

class Dot(QtGui.QDialog):

    def __init__(self, parent=None):

        super(Dot, self).__init__(parent, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setStyleSheet("background:#D06261")
        self.move(25, 820)
       
        #layout = QtGui.QVBoxLayout(self)
        button = HoverButton(self)
        button.setStyleSheet("background:rgba(0,0,0,0); margin-left: -10px; margin-top: -10px")
        button.setIconSize(QtCore.QSize(90,90))

        #layout.addWidget(button) 
        #button.setStyleSheet("outline:none;")

    def paintEvent(self, event):
        side = min(self.width(), self.height())
        
        painter = QtGui.QPainter(self)
        #painter.setFont(QtGui.QFont('kates', 5))
        painter.setFont(QtGui.QFont('artwiz cure', 15))
        painter.setPen('#222222')
              
        painter.drawText(event.rect(), QtCore.Qt.AlignCenter, " >< ")
        #painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 200.0, side / 200.0)
        
        #painter.setFont(QtGui.QFont('Arial', 50))
        #painter.drawText(event.rect(), QtCore.Qt.AlignTop, "+")

        painter.setPen(QtCore.Qt.NoPen)
        
        painter.save()
        painter.restore()

    def paintStatusEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen('#FFFFFF')

        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 200.0, side / 200.0)
        
        painter.setPen(QtCore.Qt.NoPen)
        
        painter.save()
        painter.restore()

    def resizeEvent(self, event):
        side = min(self.width(), self.height())

        maskedRegion = QtGui.QRegion(self.width()/2 - side/2, self.height()/2 - side/2, side, side, QtGui.QRegion.Ellipse)

        self.setMask(maskedRegion)

    def sizeHint(self):
        return QtCore.QSize(50, 50)

    
class HoverButton(QtGui.QToolButton):

    def __init__(self, parent=None):
        super(HoverButton, self).__init__(parent)
        self.setMouseTracking(True)

    def enterEvent(self,event):
        print("Enter")
        block.show()
        self.setStyleSheet("background:rgba(0,0,0,0); margin-left: -10px; margin-top: -10px")

    def leaveEvent(self,event):
        self.setStyleSheet("background:rgba(0,0,0,0); margin-left: -10px; margin-top: -10px")
        block.hide()
        print("Leave")


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    block = Block()
    dot = Dot()
    button = HoverButton()
    
    dot.show()
    sys.exit(app.exec_())
