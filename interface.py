#!/usr/bin/python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from connection8_main import *
from PIL import Image
from PIL.ImageQt import ImageQt


class filedialogdemo(QWidget):
    
   def __init__(self, parent = None):
      super(filedialogdemo, self).__init__(parent)
        
      self.setWindowTitle("SGMNT") 
      self.resize(500, 500) 
      
      
        
      layout = QVBoxLayout()
      
     
      
      self.btn = QPushButton("Upload your image")
      self.btn.clicked.connect(self.getfile)
      layout.addWidget(self.btn)
      
      self.btn2 = QPushButton("Segmentate")
      self.btn2.clicked.connect(self.segmentFile)
      layout.addWidget(self.btn2)
      
      
      self.btn1 = QPushButton("Save result")
      self.btn1.clicked.connect(self.saveFile)
      layout.addWidget(self.btn1)
      
      #self.btn3 = QPushButton("Show result")
      #self.btn3.clicked.connect(self.segment_result)
      #layout.addWidget(self.btn3)
      
      
      self.le = QLabel("image here")
      self.le1 = QLabel("result here")
      
      
      
        
      layout.addWidget(self.le)
      layout.addWidget(self.le1)

  
      self.setLayout(layout)
      
        
   def getfile(self):
      fname = QFileDialog.getOpenFileName(self, 'Open file', "Image files (*.*)")
      self.le.setPixmap(QPixmap(fname))
      
      
   def saveFile(self):
       #fname = QFileDialog.getOpenFileName(self, 'Open file', "Image files (*.*)")
       #self.le1.setPixmap(QPixmap(fname))
       filename = QFileDialog.getSaveFileName(self, "Save file", "", ".png")   
       self.le1.setPixmap(QPixmap(filename))
       
    #test-------   
   def segmentFile(self):
       main_seg()
       
   def segment_result(self):
       fname = QFileDialog.getOpenFileName(self, 'Open file', "Image files (*.*)")
       self.le1.setPixmap(QPixmap(fname))
       #filename = ImageQt(img_show)
       #self.le.setPixmap(QPixmap(img_show))
       #img_show()
    #---------------       

         
def main():
   app = QApplication(sys.argv)
   ex = filedialogdemo()
   ex.show()
   sys.exit(app.exec_())
    
if __name__ == '__main__':
   main()