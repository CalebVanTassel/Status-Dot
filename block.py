from PySide import QtCore, QtGui
import datetime
import calendar
import psutil

#Obtain status information
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(int(battery.percent))
yourPercent =str("{}% battery".format(percent))

now = datetime.datetime.now()

yy= now.year
mm = now.month

class Block(QtGui.QDialog):

    def __init__(self, parent=None):
        #Set Block style borderless and position
        
        super(Block, self).__init__(parent, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.setStyleSheet("background:#FFFFFF")
               
        self.move(50, 634) 
        self.resize(QtCore.QSize(180,210))
        
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)
    
    def paintEvent(self, event):
        '''Paints block'''
        
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = str(int(battery.percent))
        yourPercent =str("{}% battery".format(percent))

        now = datetime.datetime.now()

        yy= now.year
        mm = now.month
        
        side = min(self.width(), self.height())
        
        painter = QtGui.QPainter(self)
        painter.setFont(QtGui.QFont('Dina', 8))
        painter.setPen('#222222')
        painter.translate(0, -70)
        painter.drawText(event.rect(), QtCore.Qt.AlignCenter, now.strftime("%b %dth, %I:%M %p"))
        painter.translate(0, 15)
        painter.drawText(event.rect(), QtCore.Qt.AlignCenter, now.strftime("Today is a %A"))
        painter.translate(0, 15)
        painter.drawText(event.rect(), QtCore.Qt.AlignCenter, yourPercent)
        painter.translate(0, 70)
        painter.drawText(event.rect(), QtCore.Qt.AlignCenter, calendar.month(yy,mm))


        painter.scale(side / 200.0, side / 200.0)
        painter.setPen(QtCore.Qt.NoPen)
        
        painter.save()
        painter.restore()

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    block = Block()
    block.show()
    sys.exit(app.exec_())
