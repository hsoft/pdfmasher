# Created By: Virgil Dupras
# Created On: 2011-07-22
# Copyright 2011 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

from PyQt4.QtCore import Qt, QRect
from PyQt4.QtGui import QWidget, QPainter

from core.gui.page_repr import PageRepresentation as PageRepresentationModel

class PageRepresentation(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.model = PageRepresentationModel(view=self)
    
    def _paintPage(self, painter):
        pagewidth = self.model.page.width
        pageheight = self.model.page.height
        ratio = pageheight / pagewidth
        # somehow, if we don't put the '-1's, the (bottom/right)most pixel line gets cropped.
        width = self.width() - 1
        height = self.height() - 1
        if width * ratio > height:
            # Our constraint is height, adjust according to it
            adjusted_width = height / ratio
            adjusted_height = height
            x = (width - adjusted_width) / 2
            y = 0
        else:
            # Our constraint is width, adjust according to it
            adjusted_width = width
            adjusted_height = width * ratio
            x = 0
            y = (height - adjusted_height) / 2
        r = QRect(x, y, adjusted_width, adjusted_height)
        painter.fillRect(r, Qt.white)
        painter.drawRect(r)
    
    def paintEvent(self, event):
        QWidget.paintEvent(self, event)
        if self.model.page is None:
            return
        painter = QPainter(self)
        self._paintPage(painter)
    
    #--- model --> view
    def refresh(self):
        self.update()
    