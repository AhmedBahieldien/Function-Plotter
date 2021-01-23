from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import numpy as np


#main window
class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        #Read UI file
        designer_file = QFile("UI.ui")
        designer_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        loader.registerCustomWidget(MplWidget)
        self.ui = loader.load(designer_file, self)
        designer_file.close()
        #end of reading from UI file

        #plot btn listener
        self.ui.plotbtn.clicked.connect(self.update_graph)
        #exit btn listener
        self.ui.exitbtn.clicked.connect(self.exitapp)
        #set title
        self.setWindowTitle("Plotter")
        #set window icon "plotter.png"
        self.setIcon()
        #intializing grilayout and setting it
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.ui)
        self.setLayout(grid_layout)
        self.valid = True


    def setIcon(self):
        appIcon = QIcon('plotter.png')
        self.setWindowIcon(appIcon)



    def exitapp(self):
        ret = QMessageBox.question(self,"Exit","Are you sure you want to exit the program!",QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.Yes:
            app.quit()
        else:
            pass

    def error(self,etext):
        ret = QMessageBox.question(self,"Error!",etext,QMessageBox.Ok)
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.draw()
        self.ui.maxV.clear()
        self.ui.minV.clear()
        self.ui.input.clear()
        self.valid = False


    def errorhandler(self, fun, min_value, max_value):

        if not fun:
            self.error("No function entered!")
            return True

        for c in fun:
            if c.isalpha() and c.lower() != "x":
                self.error(f"Incorrect function input:({fun})!")
                return True

        if not min_value:
            self.error("No Minimum value entered!")
            return True

        if not max_value:
            self.error("No Maximum value entered!")
            return True


    #plot btn actions
    def update_graph(self):
        self.valid = True
        #function input text
        fun = self.ui.input.text()
        #convert ^ to **
        if '^' in fun:
            fun = fun.replace("^","**")
        #min value input text
        min_value = self.ui.minV.text()

        #max value input text
        max_value = self.ui.maxV.text()

        #handle input errors
        if self.errorhandler(fun,min_value,max_value):
            return None
        #set x min and max value with 100 points
        x = np.linspace(int(min_value),int(max_value))
        #clear canvas
        self.ui.MplWidget.canvas.axes.clear()
        #plot on canvas
        try:
            self.ui.MplWidget.canvas.axes.plot(x,eval(fun))
        except :
            self.error(f"Incorrect function input:({fun})!")
        #apply plot on canvas
        self.ui.MplWidget.canvas.draw()

#canvas
class MplWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.canvas = FigureCanvas(Figure())
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        vertical_layout.addWidget(NavigationToolbar(self.canvas, self))
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)


#create the app instance
app = QApplication([])
#create a window
window = Window()
#show the created window
window.show()
#start the app
app.exec_()