import PySide2
import pytest
import Main
from PySide2.QtCore import QFile

@pytest.fixture
def app(qtbot):
    test_app = Main.Window()
    qtbot.addWidget(test_app)
    return test_app

#testing Qlineedits functionality (Enter function)
def test_input(app,qtbot):
    qtbot.keyClicks(app.ui.input, "x^2")
    assert app.ui.input.text() == "x^2"

#testing Qlineedits functionality (Min)
def test_minV(app,qtbot):
    qtbot.keyClicks(app.ui.minV, "-5")
    assert app.ui.minV.text() == "-5"

#testing Qlineedits functionality (Max)
def test_maxV(app,qtbot):
    qtbot.keyClicks(app.ui.maxV, "5")
    assert app.ui.maxV.text() == "5"

#plot x^2 (Valid)
def test_input_fun_plotting_1(app,qtbot):
    qtbot.keyClicks(app.ui.input, "x^2")
    qtbot.keyClicks(app.ui.minV, "-5")
    qtbot.keyClicks(app.ui.maxV, "5")
    qtbot.mouseClick(app.ui.plotbtn, PySide2.QtCore.Qt.LeftButton)
    assert app.valid == True

#plot x**2 (Valid)
def test_input_fun_plotting_2(app,qtbot):
    qtbot.keyClicks(app.ui.input, "x**2")
    qtbot.keyClicks(app.ui.minV, "-5")
    qtbot.keyClicks(app.ui.maxV, "5")
    qtbot.mouseClick(app.ui.plotbtn, PySide2.QtCore.Qt.LeftButton)
    assert app.valid == True

#plot x^2 + x + x^3 (Valid)
def test_input_fun_plotting_3(app,qtbot):
    qtbot.keyClicks(app.ui.input, "x^2 + x + x^3")
    qtbot.keyClicks(app.ui.minV, "-5")
    qtbot.keyClicks(app.ui.maxV, "5")
    qtbot.mouseClick(app.ui.plotbtn, PySide2.QtCore.Qt.LeftButton)
    assert app.valid == True
#plot x***2 (Invalid)
def test_input_fun_plotting_4(app,qtbot):
    qtbot.keyClicks(app.ui.input, "x***2")
    qtbot.keyClicks(app.ui.minV, "-5")
    qtbot.keyClicks(app.ui.maxV, "5")
    qtbot.mouseClick(app.ui.plotbtn, PySide2.QtCore.Qt.LeftButton)
    assert app.valid == False


#plot xx + 1   (Invalid)
def test_input_fun_plotting_5(app,qtbot):
    qtbot.keyClicks(app.ui.input, "xx + 1")
    qtbot.keyClicks(app.ui.minV, "-5")
    qtbot.keyClicks(app.ui.maxV, "5")
    qtbot.mouseClick(app.ui.plotbtn, PySide2.QtCore.Qt.LeftButton)
    assert app.valid == False

#plot 5*x^3 + 2*x   (valid)
def test_input_fun_plotting_6(app,qtbot):
    qtbot.keyClicks(app.ui.input, "5*x^3 + 2*x")
    qtbot.keyClicks(app.ui.minV, "-5")
    qtbot.keyClicks(app.ui.maxV, "5")
    qtbot.mouseClick(app.ui.plotbtn, PySide2.QtCore.Qt.LeftButton)
    assert app.valid == True


#max = y "string"   (Invalid)
def test_input_fun_plotting_7(app,qtbot):
    qtbot.keyClicks(app.ui.input, "5*x^3 + 2*x")
    qtbot.keyClicks(app.ui.minV, "-5")
    qtbot.keyClicks(app.ui.maxV, "y")
    qtbot.mouseClick(app.ui.plotbtn, PySide2.QtCore.Qt.LeftButton)
    assert app.valid == False


'''
pytest ./test.py
'''