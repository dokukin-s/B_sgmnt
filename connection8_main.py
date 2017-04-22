#!/usr/bin/python
#_*_ coding: utf-8 _*_ 



import Image, ImageDraw
from PIL.ImageQt import ImageQt
import locale
import sys
import math, random
from itertools import product
from test_array_find import *
#from interface import *
import PIL.ImageOps 

from PyQt4.QtGui import *
from PyQt4.QtCore import *


loc=locale.getlocale()
locale.setlocale(locale.LC_ALL, ('RU','UTF8'))

def run(img):
    data = img.load()
    width, height = img.size

    # реализация системы непересекающихся множеств для нахождения связных областей 
    DSU = Disjoint_set_union()
 

    # первый проход
 

    # словарь который содержит пары меток
    labels = {}
 
    for y, x in product(range(height), range(width)):
 
        #
        # 
        #  представление нашей маски, с помощью которой будет производиться сканирование изображения
        #   -----------------------------------
        #   | x-1 , y-1 | x , y-1 | x+1 , y-1 |          | A | B | C |
        #   -----------------------------------          ------------- 
        #   |   x-1 ,y  |  x , y  | x+1 , y   |    =>    | D | E | F |
        #   -----------------------------------          -------------
        #   | x-1 , y+1 | x , y+1 | x+1 , y+1 |          | G | H | I |
        #   -----------------------------------           
        #

	# Сканирование изображениея начинаем с пикселя E который имеет координаты (x , y) 
	# пиксели A, B, C, D являются соседями пикселя E
	# Пиксели белого цвета являются пикселями фона,нас они не интересуют
	# если при сканировании маска выходит за границы изображения, то пиксели которые оказываются вне границ 
	# интерпретируются как белые
	#
 

	# если пиксель белый то он не является эллементом области,пропускаем и идём дальше
        if data[x, y] == 255:
            pass
	#
	# если пиксель b часть области и он черный, a,b,c являются его соседями,а значит они 
	# они пренадлежат одной и той же связной области, следовательно не нужно проверять их метки
	# достаточно просто присвоить метку b метке e
	#
	#
        elif y > 0 and data[x, y-1] == 0:
            labels[x, y] = labels[(x, y-1)]
	#
	# если пиксель c часть области изображения не являющийся фоном и он черный,
	# b - его сосед, но a и b нет, значит мф должны проветить метки у a и b
	#
	#
        elif x+1 < width and y > 0 and data[x+1, y-1] == 0:
 
            c = labels[(x+1, y-1)]
            labels[x, y] = c
	    #
	    # если пиксель a часть области изображения не являющийся фоном и он черный,  
	    # тогда a и c соеденены через e, следовательно мы должны объеденить их метки
            #
            if x > 0 and data[x-1, y-1] == 0:
                a = labels[(x-1, y-1)]
                DSU.union(c, a)
	    #
	    # если пиксель b часть области изображения не являющийся фоном и он черный,
	    # тогда d и c соедененны через e, значит мы должны объеденить их
            #
            elif x > 0 and data[x-1, y] == 0:
                d = labels[(x-1, y)]
                DSU.union(c, d)
        #
	# если пиксель a часть области изображения не являющийся фоном и он черный,
	# и т.к. мы знаем что что b и c белые, d будет соседом a, и у них уже одинаковые метки
	# то просто присваиваем метку  A к C
	#
        elif x > 0 and y > 0 and data[x-1, y-1] == 0:
            labels[x, y] = labels[(x-1, y-1)]
	#
	# если пиксель D часть области изображения не являющийся фоном и он черный,
	# и т.к. мы знаем что что a , b и c белые, то просто добавляем метку D к метке E
	#
	#
        elif x > 0 and data[x-1, y] == 0:
            labels[x, y] = labels[(x-1, y)]
	#
	# Все соседи пикселя белые, следовательно текущий пиксель получает новую метку
	#
        else: 
            labels[x, y] = DSU.makeLabel()

    # втрой проход
 
 
    # присваиваем конечные метки элементам связной области 
    DSU.flatten()
 
    colors = {}


    # Создаем изображение для отображения найденных областей в наглядной форме,присваяивая индивидуальный цвет определенной области 
    output_img = Image.new("RGB", (width, height))
    outdata = output_img.load()

    for (x, y) in labels:
 

	# Имя компонента связной области которому принадлежит текущая точка
        component = DSU.find(labels[(x, y)])


	# обновляем метку новыми данными
        labels[(x, y)] = component
 

	# присваиваем случайный цвет компонетнтам связной области
        if component not in colors: 
            colors[component] = (random.randrange(1,255,3),random.randrange(1,255,3),random.randrange(1,255,3))


	# раскрашиваем изображение присваивая цвет согласно принадлежности к связной области
        outdata[x, y] = colors[component]

    return (labels, output_img)
 
def main_seg():

    # открываем изображение
    img = Image.open("o2.jpg")
    #img = filedialogdemo.getfile()


    #производим пороговую обработку изображения,превращаем его в черно бело
	
    img = img.point(lambda p: p > 190 and 255)
    img = img.convert('1')
    #img = PIL.ImageOps.invert(img)
    #img= Image.open("out.jpg")
    
    #img.save(ing___)

    #
    # наша метка представленна в виде словаря,который содержит координаты и id 
    #    (x_coordinate, y_coordinate) : component_id
    #
    #  output_image конечный результат обработки в наглядном виде
    
    (labels, output_img) = run(img)
    output_img.save("o2_.jpg")
     
	#test----- 
def PILimageToQImage(pilimage):
    """converts a PIL image to QImage"""
    imageq = ImageQt(pilimage) #convert PIL image to a PIL.ImageQt object
    qimage = QImage(imageq) #cast PIL.ImageQt object to QImage object -that´s the trick!!!
    return qimage    
    #----------
    
def img_show():
    app = QApplication(sys.argv)
    #im = Image.open("out.jpg")
    #im.show()
    pim = Image.open("out.jpg")
    pim.show() #show pil image

    qim = PILimageToQImage(pim)
    pm = QPixmap(qim)
    #return qim
    lbl = QLabel()
    lbl.setPixmap(pm)
    lbl.show() #show label with qim image
    sys.exit(app.exec_())



    
    

if __name__ == "__main__": main()
