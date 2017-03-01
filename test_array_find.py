#_*_ coding: utf-8 _*_ 
#Реализация системы неперескающихся множеств

# Parent - массив который содержит набор всех пренадлежаших множеству элементов

class Disjoint_set_union:
    def __init__(self):

	# Массив который содержит набор эквивалентностей между пикселями
        self.Parent = []


	# номер метки после того как она будет создана
        self.label = 0

    def makeLabel(self):
        r = self.label
        self.label += 1
        self.Parent.append(r)
        return r

    # Делает все узлы на пути из i указывающими на корень 
    def setRoot(self, i, root):
        while self.Parent[i] < i:
            j = self.Parent[i]
            self.Parent[i] = root
            i = j
        self.Parent[i] = root
      
      
    #test#
    def find(self, i):
      while self.Parent[i] < i:
            i = self.Parent[i]
      root = 	i
      self.setRoot(i, root)
      return root


    #
    # Объединяем два дерева содержащие ветви i и j
    # 

    def union(self, i, j):
        if i != j:
            #root = self.findRoot(i)
            #rootj = self.findRoot(j)
            while self.Parent[i] < i:
	      i = self.Parent[i]
	    root = i
	    while self.Parent[j] < j:
	      j = self.Parent[j]
	    rootj = j
	    
            if root > rootj: root = rootj
            self.setRoot(j, root)
            self.setRoot(i, root)
    

    #
    #flatten осуществляет выполнение аналитической фазы алгоритма 
    #присваивая окончательные метки связным областям
    #
    def flatten(self):
        for i in range(1, len(self.Parent)):
            self.Parent[i] = self.Parent[self.Parent[i]]
    