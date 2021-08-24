from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPalette, QColor, QIcon, QPixmap, QValidator

class Validator(QtGui.QValidator):#validator to restict input for flowcells,barcode and sequencinkits
    def validate(self, string, pos):
        return QtGui.QValidator.Acceptable, string.upper(), pos