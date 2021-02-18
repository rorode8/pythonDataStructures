# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
from collections import deque

class Orientation:
    left=0
    centerLeft=1
    centerRight=2
    right=3
    root=4


class Node:
    


    
    def deleteValue(self, key):
        if(self.valueLeft==key):
            self.valueLeft=None
        elif(self.valueCenter==key):
            self.valueCenter=None
            if(self.valueLeft!=None):
                self.valueCenter=self.valueLeft
                self.valueLeft=None
            if(self.valueRight!=None):
                self.valueCenter=self.valueRight
                self.valueRight=None
        elif(self.valueRight==key):
            self.valueRight=None
            
    def siblings(self):
        if(self.parent==None):
            return 0
        else:
            return self.parent.sizeChilds() - 1
        
                
    
    def isLeaf(self):
        if(self.sizeChilds()==0):
            return True
        else:
            return False

    def contains(self, key):
        if(key==self.valueLeft or key==self.valueCenter or key==self.valueRight):
            return True
        else:
            return False
    
    def getMax(self):
        if(self.sizeValues()==0):
            raise Exception("empty Node without a maximum value")
        elif(self.sizeValues()==1):
            return self.valueCenter
        else:
            if(self.valueLeft!=None):
                return self.valueCenter
            else:
                return self.valueRight
            
    def getMin(self):
        if(self.sizeValues()==0):
            raise Exception("empty Node without a maximum value")
        elif(self.sizeValues()==1):
            return self.valueCenter
        else:
            if(self.valueLeft!=None):
                return self.valueLeft
            else:
                return self.valueCenter
            

            
    
    def __init__(self, data, parent=None, orientation=Orientation.root):
        self.valueLeft,self.valueCenter, self.valueRight = None, data, None
        self.nodeLeft, self.nodeCenterLeft, self.nodeCenterRight, self.nodeRight = None, None, None, None
        self.parent = parent
        self.orientation = orientation
        
    def sizeValues(self):
        size = 0;
        if(self.valueLeft!=None):
            size=size + 1
        if(self.valueCenter!=None):
            size=size+1
        if(self.valueRight!=None):
            size=size+1
        return size
    
    def sizeChilds(self):
        size=0
        if(self.nodeLeft!=None):
            size=size + 1
        if(self.nodeCenterLeft!=None):
            size=size+1
        if(self.nodeCenterRight!=None):
            size=size+1
        if(self.nodeRight!=None):
            size=size+1
        return size
    
    def push(self, value):
        
        if(self.valueCenter==None):
            self.valueCenter=value
        
        elif(value>=self.valueCenter):
            
            if(self.valueRight==None):
                self.valueRight=value
            else:
                
                self.valueLeft=self.valueCenter
                if(value>=self.valueRight):
                    self.valueCenter=self.valueRight
                    self.valueRight=value
                    
                else:
                    self.valueCenter=value
                #self.split()
        else:
            
            if(self.valueLeft==None):
                self.valueLeft=value
            else:
                
                self.valueRight=self.valueCenter
                if(value>=self.valueLeft):
                    self.valueCenter=value
                else:
                    self.valueCenter=self.valueLeft
                    self.valueLeft = value
                #self.split
        n=self.sizeValues()
        
        if(n==3):
            
            self.split()
        
                
                
    def split(self):
        print("split")
        print("node previous splitting")
        print(self.__str__())
        if(self.parent==None):
            if(self.sizeChilds()==0):
                
                leftValue, self.valueLeft = self.valueLeft, None
                rightValue, self.valueRight=self.valueRight, None
                leftChild = Node(leftValue, self, Orientation.left)
                rightChild = Node(rightValue, self, Orientation.right)
                self.nodeLeft=leftChild
                self.nodeRight=rightChild
            else:
                print(self.sizeChilds())
                print(self)
                if(self.sizeChilds()!=4):
                    #raise Exception("error")
                    print("LOOOOOL")
                leftValue, self.valueLeft = self.valueLeft, None
                rightValue, self.valueRight=self.valueRight, None
                leftChild = Node(leftValue, self, Orientation.left)
                # es importante arreglar los vinculos de los padres y de las orientaciones
                leftChild.nodeLeft=self.nodeLeft
                leftChild.nodeLeft.orientation=Orientation.left
                leftChild.nodeLeft.parent=leftChild
                leftChild.nodeRight=self.nodeCenterLeft
                leftChild.nodeRight.parent=leftChild
                leftChild.nodeRight.orientation=Orientation.right
                rightChild = Node(rightValue, self, Orientation.right)
                rightChild.nodeLeft=self.nodeCenterRight
                rightChild.nodeLeft.orientation=Orientation.left
                rightChild.nodeLeft.parent=rightChild
                rightChild.nodeRight=self.nodeRight
                rightChild.nodeRight.parent=rightChild
                rightChild.nodeRight.orientation=Orientation.right
                self.nodeLeft=leftChild
                self.nodeRight=rightChild
                self.nodeCenterLeft=None
                self.nodeCenterRight=None
        else:
            print("yikes")
            print(self.orientation)
            if(self.sizeChilds()==0):
                print("leeeeeee")
                if(self.orientation==Orientation.left):
                    center=self.valueCenter
                    print("yikes2")
                    if(self.parent.nodeCenterLeft==None):
                        tempNode=Node(self.valueRight, self.parent, Orientation.centerLeft)
                        self.parent.nodeCenterLeft=tempNode
                    else:
                        tempNode=Node(self.valueRight, self.parent, Orientation.centerLeft)
                        self.parent.nodeCenterRight=self.parent.nodeCenterLeft
                        self.parent.nodeCenterLeft=tempNode
                    self.valueCenter=self.valueLeft
                    self.valueLeft=None
                    self.valueRight=None
                    self.parent.push(center)
                    
                elif(self.orientation==Orientation.centerLeft):
                    center=self.valueCenter
                    tempNode=Node(self.valueRight, self.parent, Orientation.centerRight)
                    self.parent.nodeCenterRight=tempNode
                    self.valueCenter=self.valueLeft
                    self.valueLeft=None
                    self.valueRight=None
                    self.parent.push(center)
                    
                elif(self.orientation==Orientation.centerRight):
                    center=self.valueCenter
                    tempNode=Node(self.valueLeft, self.parent, Orientation.centerLeft)
                    self.parent.nodeCenterLeft=tempNode
                    self.valueCenter=self.valueRight
                    self.valueLeft=None
                    self.valueRight=None
                    self.parent.push(center)
                else:
                    center=self.valueCenter
                    print("jkl")
                    print(self.parent.parent)
                    print(self.parent)
                    if(self.parent.nodeCenterRight==None):
                        tempNode=Node(self.valueLeft, self.parent, Orientation.centerRight)
                        self.parent.nodeCenterRight=tempNode
                    else:
                        tempNode=Node(self.valueLeft, self.parent, Orientation.centerRight)
                        self.parent.nodeCenterLeft=self.parent.nodeCenterRight
                        self.parent.nodeCenterRight=tempNode
                    self.valueCenter=self.valueRight
                    self.valueLeft=None
                    self.valueRight=None
                    print(self.parent)
                    self.parent.push(center) 
                    
            else:
                if(self.sizeChilds()!=4):
                    raise Exception("error")
                center = self.valueCenter
                
                # 4 cases
                if(self.orientation==Orientation.left):
                    tempNodeLeft=Node(self.valueLeft, self.parent, Orientation.left)
                    tempNodeLeft.nodeLeft, tempNodeLeft.nodeRight=self.nodeLeft, self.nodeCenterLeft
                    tempNodeLeft.nodeLeft.parent = tempNodeLeft
                    tempNodeLeft.nodeRight.parent = tempNodeLeft
                    self.parent.nodeLeft=tempNodeLeft
                    if(self.parent.nodeCenterLeft==None):
                        tempNodeRight=Node(self.valueRight, self.parent, Orientation.centerLeft)
                                                
                    else:
                        tempNodeRight=Node(self.valueRight, self.parent, Orientation.centerLeft)
                        self.parent.nodeCenterRight=self.parent.nodeCenterLeft
                        
                    tempNodeRight.nodeLeft, tempNodeRight.nodeRight=self.nodeCenterRight, self.nodeRight
                    tempNodeRight.nodeLeft.parent = tempNodeRight
                    tempNodeRight.nodeRight.parent = tempNodeRight
                    self.parent.nodeCenterLeft=tempNodeRight   
                    
                elif(self.orientation==Orientation.centerLeft or self.orientation==Orientation.centerRight):
                    tempNodeLeft=Node(self.valueLeft, self.parent, Orientation.centerLeft)
                    tempNodeLeft.nodeLeft, tempNodeLeft.nodeRight=self.nodeLeft, self.nodeCenterLeft
                    tempNodeLeft.nodeLeft.parent = tempNodeLeft
                    tempNodeLeft.nodeRight.parent = tempNodeLeft
                    tempNodeRight=Node(self.valueRight, self.parent, Orientation.centerRight)
                    tempNodeRight.nodeLeft, tempNodeRight.nodeRight=self.nodeCenterRight, self.nodeRight
                    tempNodeRight.nodeLeft.parent = tempNodeRight
                    tempNodeRight.nodeRight.parent = tempNodeRight
                    self.parent.nodeCenterLeft = tempNodeLeft
                    self.parent.nodeCenterRight = tempNodeRight
                else:
                    if(self.parent.nodeCenterRight!=None):
                        tempNodeRight=Node(self.valueRight, self.parent, Orientation.centerLeft)
                        self.parent.nodeCenterLeft=self.parent.nodeCenterRight                      
                    
                        
                    tempNodeLeft=Node(self.valueLeft, self.parent, Orientation.centerRight)
                    tempNodeLeft.nodeLeft, tempNodeLeft.nodeRight=self.nodeLeft, self.nodeCenterLeft
                    tempNodeLeft.nodeLeft.parent = tempNodeLeft
                    tempNodeLeft.nodeRight.parent = tempNodeLeft
                    
                    tempNodeRight=Node(self.valueRight, self.parent, Orientation.right)
                    tempNodeRight.nodeLeft, tempNodeRight.nodeRight=self.nodeCenterRight, self.nodeRight
                    tempNodeRight.nodeLeft.parent = tempNodeRight
                    tempNodeRight.nodeRight.parent = tempNodeRight
                    print("papa")
                    print(self.parent)
                    print(tempNodeLeft)
                    self.parent.nodeCenterRight = tempNodeLeft
                    self.parent.nodeRight = tempNodeRight
                    print(self.parent.nodeLeft)
                    print(self.parent.nodeCenterLeft)
                    print(self.parent.nodeCenterRight)
                    print(self.parent.nodeRight)
                self.parent.push(center)
                
    def __str__(self):
        value1=""
        value2=""
        value3=""
        if(self.valueLeft!=None):
            t=self.valueLeft.__str__()
            value1="  "+t+"  "
        if(self.valueCenter!=None):
            t=self.valueCenter.__str__()
            value2="  "+t+"  "
        if(self.valueRight!=None):
            t=self.valueRight.__str__()
            value3="  "+t+"  "
        
        return "["+value1+value2+value3+"]"
    
    def pushNode(self, nodo):
        node=Node(nodo)
        if(self.nodeLeft==None):
            self.nodeLeft=node
        if(self.nodeCenterLeft==None):
            self.nodeCenterLeft=node
        if(self.nodeCenterRight==None):
            self.nodeCenterRight=node
        if(self.nodeRight==None):
            self.nodeRight=node
        else:
            raise("the node couldn't be pushed")
        self.sortNodes()
        
    def sortNodes(self):
        nodes = []
        if(self.nodeLeft!=None):
            nodes.append(self.nodeLeft)
        if(self.self.nodeCenterLeft!=None):
            nodes.append(self.nodeCenterLeft)
        if(self.nodeCenterRight!=None):
            nodes.append(self.nodeCenterRight)
        if(self.self.nodeRight!=None):
            nodes.append(self.nodeRight)
        
        self.nodeLeft=None
        self.nodeCenterLeft=None
        self.nodeCenterRight=None
        self.nodeRight=None
        
        if(nodes.count()==2):
            self.nodeLeft=nodes[0]
            self.nodeRight=nodes[1]
        else:
            self.nodeLeft=nodes[0]
            self.nodeCenterLeft=nodes[1]
            self.nodeRight=nodes[2]
        
      
                
                
                
    
    def merge(self):
        #when a node wants to merge, it is given that it has no values, but it may or may not have children or a parent
        if(self.parent==None):
            print(self)
            print(self.nodeLeft)
            print(self.nodeCenterLeft)
            print(self.nodeCenterRight)
            print(self.nodeRight)
            if(self.nodeLeft==None):
                if(self.nodeCenterLeft==None):
                    if(self.nodeCenterRight==None):
                        if(self.nodeRight==None):
                            print("lol")
                        else:
                            self=self.nodeRight
                    else:
                        self=self.nodeCenterRight
                else:
                    self=self.nodeCenterLeft
            else:
                self=self.nodeLeft

                            
        elif(self.isLeaf()):
            
            if(self.parent.sizeValues()==2):
                #si alguno de los hermanos tiene dos valores, podemos "robarlo"
                if(self.orientation==Orientation.left):
                    if(self.parent.nodeCenterLeft!=None and self.parent.nodeCenterLeft.sizeValues()==2):
                        self.push(self.parent.getMin())
                        self.parent.deleteValue(self.parent.getMin())
                        self.parent.push(self.parent.nodeCenterLeft.getMin())
                        self.parent.nodeCenterLeft.deleteValue(self.parent.nodeCenterLeft.getMin())
                    elif(self.parent.nodeCenterRight!=None and self.parent.nodeCenterRight.sizeValues()==2):
                        self.push(self.parent.getMin())
                        self.parent.deleteValue(self.parent.getMin())
                        self.parent.push(self.parent.nodeCenterRight.getMin())
                        self.parent.nodeCenterRight.deleteValue(self.parent.nodeCenterRight.getMin())
                    elif(self.parent.nodeRight.sizeValues()==2):
                        self.push(self.parent.getMin())
                        self.parent.deleteValue(self.parent.getMin())
                        self.parent.push(self.parent.nodeRight.getMin())
                        self.parent.nodeRight.deleteValue(self.parent.nodeRightt.getMin())
                    else:
                        # si no pudimos robar a ninguno de los hermanos, nos juntamos con el hermano inmeadito (el de en medio)
                        # y robamos un valor del padre (en este caso el menor)
                        self.push(self.parent.getMin())
                        self.parent.deleteValue(self.parent.getMin())
                        if(self.parent.nodeCenterLeft!=None):
                            self.push(self.parent.nodeCenterLeft.getMin())
                            self.parent.nodeCenterLeft=None
                        else:
                            self.push(self.parent.nodeCenterRight.getMin())
                            self.parent.nodeCenterRight=None                      
                        
                        
                        
                elif(self.orientation==Orientation.centerLeft or self.orientation==Orientation.centerRight):
                    if(self.parent.nodeLeft.sizeValues()==2):
                        self.push(self.parent.getMin())
                        self.parent.deleteValue(self.parent.getMin())
                        self.parent.push(self.parent.nodeLeft.getMax())
                        self.parent.nodeLeft.deleteValue(self.parent.nodeCenterLeft.getMax())
                    elif(self.parent.nodeRight.sizeValues()==2):
                        self.push(self.parent.getMax())
                        self.parent.deleteValue(self.parent.getMax())
                        self.parent.push(self.parent.nodeRight.getMin())
                        self.parent.nodeRight.deleteValue(self.parent.nodeRightt.getMin())
                    else:
                        # nos unificamos con el vecino derecho
                        self.push(self.parent.getMax())
                        self.parent.deleteValue(self.parent.getMax())
                        self.push(self.parent.nodeRight.getMax())
                        self.parent.nodeRight=self
                        #ahora somos el hijo derecho
                        if(self.orientation==Orientation.centerLeft):
                            self.parent.nodeCenterLeft=None
                        else:
                            self.parent.nodeCenterRight=None
                        self.orientation=Orientation.right
                        
                else:
                    #la orientacion es derecha
                    if(self.parent.nodeCenterLeft!=None and self.parent.nodeCenterLeft.sizeValues()==2):
                        self.push(self.parent.getMax())
                        self.parent.deleteValue(self.parent.getMax())
                        self.parent.push(self.parent.nodeCenterLeft.getMax())
                        self.parent.nodeCenterLeft.deleteValue(self.parent.nodeCenterLeft.getMax())
                    elif(self.parent.nodeCenterRight!=None and self.parent.nodeCenterRight.sizeValues()==2):
                        self.push(self.parent.getMax())
                        self.parent.deleteValue(self.parent.getMax())
                        self.parent.push(self.parent.nodeCenterRight.getMax())
                        self.parent.nodeCenterRight.deleteValue(self.parent.nodeCenterRight.getMax())
                    elif(self.parent.nodeLeft.sizeValues()==2):
                        self.push(self.parent.getMax())
                        self.parent.deleteValue(self.parent.getMax())
                        self.parent.push(self.parent.nodeLeft.getMax())
                        self.parent.nodeLeft.deleteValue(self.parent.Left.getMax())
                    else:
                        # si no pudimos robar a ninguno de los hermanos, nos juntamos con el hermano inmeadito (el de en medio)
                        # y robamos un valor del padre (en este caso el mayor)
                        self.push(self.parent.getMax())
                        self.parent.deleteValue(self.parent.getMax())
                        if(self.parent.nodeCenterLeft!=None):
                            self.push(self.parent.nodeCenterLeft.getMin())
                            self.parent.nodeCenterLeft=None
                        else:
                            self.push(self.parent.nodeCenterRight.getMin())
                            self.parent.nodeCenterRight=None   
            else:
                if(self.orientation==Orientation.left):
                    self.push(self.parent.getMax())
                    self.parent.deleteValue(self.parent.getMax())
                    self.push(self.parent.nodeRight.getMax())
                    self.parent.nodeRight=None
                    self.parent.merge()
                else:
                    print("val: ")
                    print(self.parent.getMax())
                    self.push(self.parent.getMax())
                    self.parent.deleteValue(self.parent.getMax())
                    self.push(self.parent.nodeLeft.getMax())
                    self.parent.nodeLeft=None
                    self.parent.merge()
        # es un nodo interno
        else:
            if(self.parent.sizeChilds()<3):
                if(self.orientation==Orientation.left):
                    if(self.parent.nodeRight.sizeValues()==2):
                        
                        self.push(self.parent.getMin())
                        self.parent.deleteValue(self.parent.getMin())
                        self.parent.push(self.parent.nodeRight.getMin())
                        self.parent.nodeRight.deleteValue(self.parent.nodeRight.getMin())
                        if(self.nodeLeft==None):
                            self.nodeLeft=self.nodeRight
                        self.nodeRight=self.parent.nodeRight.nodeLeft
                        self.parent.nodeRight.nodeLeft=None
                        self.nodeRight.parent=self
                        if(self.parent.nodeRight.nodeCenterLeft==None):
                            self.parent.nodeRight.nodeLeft = self.parent.nodeRight.nodeCenterRight
                            self.parent.nodeRight.nodeLeft.orientation=Orientation.left
                            self.parent.nodeRight.nodeCenterRight=None
                        else:
                            self.parent.nodeRight.nodeLeft = self.parent.nodeRight.nodeCenterLeft
                            self.parent.nodeRight.nodeLeft.orientation=Orientation.left
                            self.parent.nodeRight.nodeCenterLeft=None
                    else:
                        self.push(self.parent.getMax())
                        self.parent.deleteValue(self.parent.getMax())
                        self.push(self.parent.nodeRight.getMin())
                        self.parent.nodeRight.deleteValue(self.parent.nodeRight.getMin())
                        if(self.nodeLeft==None):
                            self.nodeLeft=self.nodeRight
                        self.nodeCenterLeft=self.parent.nodeRight.nodeLeft
                        self.nodeCenterLeft.parent=self
                        self.nodeCenterLeft.orientation=Orientation.centerLeft
                        self.nodeRight=self.parent.nodeRight.nodeRight
                        self.nodeRight.parent=self
                        self.nodeRight.orientation=Orientation.right
                              
                        self.parent.nodeRight=None
                        self.parent.merge();
                        #tiene dos hijos
                        print("")
                else:
                    #somos el hijo derecho
                    if(self.parent.nodeLeft.sizeValues()==2):
                        #robamos un hijo de este
                        self.push(self.parent.getMax())
                        self.parent.deleteValue(self.parent.getMax())
                        self.parent.push(self.parent.nodeLeft.getMax())
                        self.parent.nodeRight.deleteValue(self.parent.nodeLeft.getMax())
                        if(self.nodeRight==None):
                            self.nodeRight=self.nodeLeft
                        self.nodeLeft=self.parent.nodeLeft.nodeRight
                        self.parent.nodeLeft.nodeRight=None
                        self.nodeLeft.parent=self
                        if(self.parent.nodeLeft.nodeCenterLeft==None):
                            self.parent.nodeLeft.nodeRight=self.parent.nodeLeft.nodeCenterRight
                            self.parent.nodeLeft.nodeCenterRight=None
                        else:
                            self.parent.nodeLeft.nodeRight=self.parent.nodeLeft.nodeCenterLeft
                            self.parent.nodeLeft.nodeCenterLeft=None
                        self.parent.nodeLeft.nodeRight.orientation=Orientation.right
                    else:
                        self.push(self.parent.getMax())
                        self.parent.deleteValue(self.parent.getMax())
                        self.push(self.parent.nodeLeft.getMin())
                        self.parent.nodeLeft.deleteValue(self.parent.nodeLeft.getMin())
                        if(self.nodeRight==None):
                            self.nodeRight=self.nodeLeft
                        self.nodeCenterRight=self.parent.nodeLeft.nodeRight
                        self.nodeCenterRight.parent=self
                        self.nodeCenterRight.orientation=Orientation.centerRight
                        
                        self.nodeLeft=self.parent.nodeLeft.nodeLeft
                        self.nodeLeft.parent=self
                        self.nodeLeft.orientation=Orientation.left
                              
                        self.parent.nodeLeft=None
                        self.parent.merge()
                                         
                            
                            
            # tiene tres hijos (el padre)
            else:
                
                if(self.orientation==Orientation.left):
                    if(self.parent.nodeCenterLeft!=None):
                        if(self.parent.nodeCenterLeft.sizeValues()<2):
                            if(self.nodeLeft==None):
                                self.nodeLeft=self.nodeRight
                            self.push(self.parent.getMin())
                            self.parent.deleteValue(self.parent.getMin())
                            self.push(self.parent.nodeCenterLeft.getMin())
                            self.parent.nodeCenterLeft.deleteValue(self.parent.nodeCenterLeft.getMin())
                            self.nodeCenterLeft=self.parent.nodeCenterLeft.nodeLeft
                            self.nodeCenterLeft.orientation=Orientation.centerLeft
                            self.nodeCenterLeft.parent=self
                            self.nodeRight=self.parent.nodeCenterLeft.nodeRight
                            self.nodeRight.orientation=Orientation.right
                            self.nodeRight.parent=self
                            self.parent.nodeCenterLeft=None
                        else:
                            if(self.nodeLeft==None):
                                self.nodeLeft=self.nodeRight
                            self.push(self.parent.getMin())
                            self.parent.deleteValue(self.parent.getMin())
                            self.parent.push(self.parent.nodeCenterLeft.getMin())
                            self.parent.nodeCenterLeft.deleteValue(self.parent.nodeCenterLeft.getMin())
                            self.nodeRight=self.parent.nodeCenterLeft.nodeLeft
                            self.parent.nodeCenterLeft.nodeLeft=None
                            if(self.parent.nodeCenterLeft.nodeCenterLeft!=None):
                                self.parent.nodeCenterLeft.nodeLeft=self.parent.nodeCenterLeft.nodeCenterLeft
                                self.parent.nodeCenterLeft.nodeCenterLeft=None
                            else:
                                self.parent.nodeCenterLeft.nodeLeft=self.parent.nodeCenterLeft.nodeCenterRight
                                self.parent.nodeCenterLeft.nodeCenterRight=None
                            self.parent.nodeCenterLeft.nodeLeft.orientation=Orientation.left
                            self.nodeRight.orientation=Orientation.right
                            self.nodeRight.parent=self
                    else:
                        if(self.parent.nodeCenterRight==None):
                            print(self.siblings())
                            print(self.parent)
                            print("LOOOOL")
                        if(self.parent.nodeCenterRight.sizeValues()<2):
                            if(self.nodeLeft==None):
                                self.nodeLeft=self.nodeRight
                            self.push(self.parent.getMin())
                            self.parent.deleteValue(self.parent.getMin())
                            self.push(self.parent.nodeCenterRight.getMin())
                            self.parent.nodeCenterRight.deleteValue(self.parent.nodeCenterRight.getMin())
                            self.nodeCenterLeft=self.parent.nodeCenterRight.nodeLeft
                            self.nodeCenterLeft.orientation=Orientation.centerLeft
                            self.nodeCenterLeft.parent=self
                            self.nodeRight=self.parent.nodeCenterRight.nodeRight
                            self.nodeRight.orientation=Orientation.right
                            self.nodeRight.parent=self
                            self.parent.nodeCenterRight=None
                        else:
                            if(self.nodeLeft==None):
                                self.nodeLeft=self.nodeRight
                            self.push(self.parent.getMin())
                            self.parent.deleteValue(self.parent.getMin())
                            self.parent.push(self.parent.nodeCenterRight.getMin())
                            self.parent.nodeCenterRight.deleteValue(self.parent.nodeCenterRight.getMin())
                            self.nodeRight=self.parent.nodeCenterRight.nodeLeft
                            self.parent.nodeCenterRight.nodeLeft=None
                            if(self.parent.nodeCenterRight.nodeCenterLeft!=None):
                                self.parent.nodeCenterRight.nodeLeft=self.parent.nodeCenterRight.nodeCenterLeft
                                self.parent.nodeCenterRight.nodeCenterLeft=None
                            else:
                                self.parent.nodeCenterRight.nodeLeft=self.parent.nodeCenterRight.nodeCenterRight
                                self.parent.nodeCenterRight.nodeCenterRight=None
                            self.parent.nodeCenterRight.nodeLeft.orientation=Orientation.left
                            self.nodeRight.orientation=Orientation.right
                            self.nodeRight.parent=self
                elif(self.orientation==Orientation.centerLeft or self.orientation==Orientation.centerRight):
                    #intentar robar de alguno de los vecinos del nodo
                    if(self.parent.nodeLeft.sizeValues()==2):
                        self.push(self.parent.getMin())
                        self.parent.deleteValue(self.parent.getMin())
                        self.parent.push(self.parent.nodeLeft.getMax())
                        self.parent.nodeLeft.deleteValue(self.parent.nodeLeft.getMax())
                        if(self.nodeRight==None):
                            self.nodeRigh=self.nodeCenterRight
                            if(self.nodeRigh==None):
                                self.nodeRigh=self.nodeCenterLeft
                                if(self.nodeRigh==None):
                                    self.nodeRigh=self.nodeLeft
                        self.nodeLeft=self.parent.nodeLeft.nodeRight
                        self.nodeLeft.parent=self
                        self.nodeLeft.orientation=Orientation.left
                        self.parent.nodeLeft.nodeRight=None
                        if(self.parent.nodeLeft.nodeCenterLeft!=None):
                            self.parent.nodeLeft.nodeRight= self.parent.nodeLeft.nodeCenterLeft
                            self.parent.nodeLeft.nodeCenterLeft=None
                        else:
                            self.parent.nodeLeft.nodeRight= self.parent.nodeLeft.nodeCenterRight
                            self.parent.nodeLeft.nodeCenterRight=None
                        self.parent.nodeLeft.nodeRight.orientation=Orientation.right
                    elif(self.parent.nodeRight.sizeValues()==2):
                        self.push(self.parent.getMax())
                        self.parent.deleteValue(self.parent.getMax())
                        self.parent.push(self.parent.nodeRight.getMin())
                        self.parent.nodeRight.deleteValue(self.parent.nodeRight.getMin())
                        if(self.nodeLeft==None):
                            self.nodeLeft=self.nodeCenterLeft
                            if(self.nodeLeft==None):
                                self.nodeLeft=self.nodeCenterRight
                                if(self.nodeLeft==None):
                                    self.nodeLeft=self.nodeRight
                        self.nodeRight=self.parent.nodeRight.nodeLeft
                        self.nodeRight.parent=self
                        self.nodeRight.orientation=Orientation.right
                        self.parent.nodeRight.nodeLeft=None
                        if(self.parent.nodeRight.nodeCenterLeft!=None):
                            self.parent.nodeRight.nodeLeft = self.parent.nodeRight.nodeCenterLeft
                            self.parent.nodeRight.nodeCenterLeft=None
                        else:
                            self.parent.nodeRight.nodeLeft = self.parent.nodeRight.nodeCenterRight
                            self.parent.nodeRight.nodeCenterRight=None
                        self.parent.nodeRight.nodeLeft.orientation=Orientation.left
                    else:
                        #nos fusionamos con la derecha
                        if(self.nodeLeft==None):
                            self.nodeLeft=self.nodeCenterLeft
                            if(self.nodeLeft==None):
                                self.nodeLeft=self.nodeCenterRight
                                if(self.nodeLeft==None):
                                    self.nodeLeft=self.nodeRight
                        self.push(self.parent.getMax())
                        self.parent.deleteValue(self.parent.getMax())
                        self.push(self.parent.nodeRight.getMax())
                        self.parent.nodeRight.deleteValue(self.parent.nodeRight.getMax())
                        self.nodeCenterLeft=self.parent.nodeRight.nodeLeft
                        self.nodeCenterLeft.parent=self
                        self.nodeCenterLeft.orientation=Orientation.centerLeft
                        self.nodeRight=self.parent.nodeRight.nodeRight
                        self.nodeRigh.parent=self
                        self.nodeRigh.orientation=Orientation.right
                        self.parent.nodeRight=None
                        self.parent.nodeRight=self
                        self.orientation=Orientation.right
                        self.parent.nodeCenterLeft=None
                        self.parent.nodeCenterRight=None
                else: #nodeo derecho
                    if(self.parent.nodeCenterLeft!=None):
                        if(self.parent.nodeCenterLeft.sizeValues()<2):
                            if(self.nodeRight==None):
                                self.nodeRight=self.nodeLeft
                            self.push(self.parent.getMax())
                            self.parent.deleteValue(self.parent.getMax())
                            self.push(self.parent.nodeCenterLeft.getMax())
                            self.parent.nodeCenterLeft.deleteValue(self.parent.nodeCenterLeft.getMax())
                            self.nodeCenterLeft=self.parent.nodeCenterLeft.nodeRight
                            self.nodeCenterLeft.orientation=Orientation.centerLeft
                            self.nodeCenterLeft.parent=self
                            self.nodeLeft=self.parent.nodeCenterLeft.nodeLeft
                            self.nodeLeft.orientation=Orientation.left
                            self.nodeLeft.parent=self
                            self.parent.nodeCenterLeft=None
                        else:
                            if(self.nodeRight==None):
                                self.nodeRight=self.nodeLeft
                            self.push(self.parent.getMax())
                            self.parent.deleteValue(self.parent.getMax())
                            self.parent.push(self.parent.nodeCenterLeft.getMax())
                            self.parent.nodeCenterLeft.deleteValue(self.parent.nodeCenterLeft.getMax())
                            self.nodeLeft=self.parent.nodeCenterLeft.nodeRight
                            self.parent.nodeCenterLeft.nodeRight=None
                            if(self.parent.nodeCenterLeft.nodeCenterLeft!=None):
                                self.parent.nodeCenterLeft.nodeRight=self.parent.nodeCenterLeft.nodeCenterLeft
                                self.parent.nodeCenterLeft.nodeCenterLeft=None
                            else:
                                self.parent.nodeCenterLeft.nodeRight=self.parent.nodeCenterLeft.nodeCenterRight
                                self.parent.nodeCenterLeft.nodeCenterRight=None
                            self.parent.nodeCenterLeft.nodeRight.orientation=Orientation.right
                            self.nodeLeft.orientation=Orientation.left
                            self.nodeLeft.parent=self
                    else:
                        if(self.parent.nodeCenterRight==None):
                            print("h")
                            print(self.orientation)
                            print(self.siblings())
                            print(self.parent)
                            print(self.nodeRight)
                        if(self.parent.nodeCenterRight.sizeValues()<2):
                            if(self.nodeRight==None):
                                self.nodeRight=self.nodeLeft
                            self.push(self.parent.getMax())
                            self.parent.deleteValue(self.parent.getMax())
                            self.push(self.parent.nodeCenterRight.getMax())
                            self.parent.nodeCenterRight.deleteValue(self.parent.nodeCenterRight.getMax())
                            self.nodeCenterLeft=self.parent.nodeCenterRight.nodeRight
                            self.nodeCenterLeft.orientation=Orientation.centerLeft
                            self.nodeCenterLeft.parent=self
                            self.nodeLeft=self.parent.nodeCenterRight.nodeLeft
                            self.nodeLeft.orientation=Orientation.left
                            self.nodeLeft.parent=self
                            self.parent.nodeCenterRight=None
                        else:
                            if(self.nodeRight==None):
                                self.nodeRight=self.nodeLeft
                            self.push(self.parent.getMax())
                            self.parent.deleteValue(self.parent.getMax())
                            self.parent.push(self.parent.nodeCenterRight.getMax())
                            self.parent.nodeCenterRight.deleteValue(self.parent.nodeCenterRight.getMax())
                            self.nodeLeft=self.parent.nodeCenterRight.nodeRight
                            self.parent.nodeCenterRight.nodeRight=None
                            if(self.parent.nodeCenterRight.nodeCenterLeft!=None):
                                self.parent.nodeCenterRight.nodeRight=self.parent.nodeCenterRight.nodeCenterLeft
                                self.parent.nodeCenterRight.nodeCenterLeft=None
                            else:
                                self.parent.nodeCenterRight.nodeRight=self.parent.nodeCenterRight.nodeCenterRight
                                self.parent.nodeCenterRight.nodeCenterRight=None
                            self.parent.nodeCenterRight.nodeRight.orientation=Orientation.right
                            self.nodeLeft.orientation=Orientation.left
                            self.nodeLeft.parent=self
                            

    
        
        
    def findMin(self):
        if(self.isLeaf()):
            value=self.getMin()
            return value, self
        else:
            return self.findMin(self.nodeLeft)
        
    def delete(self, key):
        
        #regardless of what we do, we delete the number
        
        #self.deleteValue(key)
        
        if(self.isLeaf()):
            print("reached leaf")
            self.deleteValue(key)
        else:
            if(self.sizeValues()==1):
                # if it's a 1 value node it has 2 childs, we replace the value that we deleted with the smallest from the right subtree
                self.deleteValue(key)
                targetValue, targetNode = self.nodeRight.findMin()
                               
                self.push(targetValue)
                targetNode.delete(targetValue)
            else:
                if(self.valueLeft==None):
                    if(self.valueCenter==key):
                        if(self.nodeCenterLeft==None):
                            
                            self.deleteValue(key)
                            targetValue, targetNode = self.findMin(self.nodeCenterRight)
                            self.push(self.findMin(self.nodeCenterRight))
                            
                        else:
                            self.deleteValue(key)
                            targetValue, targetNode = self.findMin(self.nodeCenterLeft)
                            self.push(self.findMin(self.nodeCenterLeft))
                    else:
                        #hay que sacar el valor del subarbol der. (valor minimo)
                        self.deleteValue(key)
                        targetValue, targetNode =self.findMin(self.nodeRight)
                        self.push(self.findMin(self.nodeRight))
                        
                else:
                    if(self.valueCenter==key):
                        self.deleteValue(key)
                        targetValue, targetNode = self.findMin(self.nodeRight)
                        self.push(self.findMin(self.nodeRight))
                    else:
                        if(self.nodeCenterLeft==None):
                            self.deleteValue(key)
                            targetValue, targetNode =self.findMin(self.nodeCenterRight)
                            self.push(self.findMin(self.nodeCenterRight))
                        else:
                            self.deleteValue(key)
                            targetValue, targetNode =self.findMin(self.nodeCenterLeft)
                            self.push(self.findMin(self.nodeCenterLeft))
                            
                targetNode.delete(targetValue)      
                            
        if(self.sizeValues()==0):
            self.merge()
                
                
    
  
        
    
class TwoThreeTree:
    
    def deleteMin(self, nodo):
        node=Node(nodo)
        if(node.isLeaf()):
            value=node.getMin()
            node.deleteValue(node.getMin())
            return value
        else:
            return self.deleteMin(node.nodeLeft)
        
    def findMin(self, node):
        if(node.isLeaf()):
            value=node.getMin()
            return value, node
        else:
            return self.findMin(node.nodeLeft), node
    
    def findHeight(self):
        if(self.root==None):
            raise Exception("empty collection")
        else:
            return self.heightRecursive(self.root)
            
    def heightRecursive(self, node):
        if(node==None):
            return 0
        elif(not node.isLeaf()):
            return 1 + self.heightRecursive(node.nodeLeft)
        else:
            return 0
    
    def delete(self, dato):
        if(self.root==None):
            raise Exception("empty collection")
        else:
            node=self.find(dato)
            self.deleteT(dato, node)
            
        if(self.root.sizeValues()==0):
            if(self.root.nodeLeft==None):
                if(self.root.nodeCenterLeft==None):
                    if(self.root.nodeCenterRight==None):
                        if(self.root.nodeRight==None):
                            print("lol")
                        else:
                            self.root=self.root.nodeRight
                    else:
                        self.root=self.root.nodeCenterRight
                else:
                    self.root=self.root.nodeCenterLeft
            else:
                self.root=self.root.nodeLeft
                
            
                
    def deleteT(self, key, node):
        if(node.isLeaf()):
            node.deleteValue(key)
        else:
            if(node.sizeValues()==1):
                node.deleteValue(key)
                node.push(self.deleteMin(node))
            else:
                if(node.valueLeft==None):
                    if(node.valueCenter==key):
                        if(node.nodeCenterLeft==None):
                            
                            node.deleteValue(key)
                            mini, nodoHoja=self.findMin(node.nodeCenterRight)
                            node.push(self.findMin(node.nodeCenterRight))
                            
                        else:
                            node.deleteValue(key)
                            mini, nodoHoja=self.findMin(node.nodeCenterLeft)
                            node.push(self.findMin(node.nodeCenterLeft))
                    else:
                        #hay que sacar el valor del subarbol der. (valor minimo)
                        node.deleteValue(key)
                        mini, nodoHoja=self.findMin(node.nodeRight)
                        node.push(self.findMin(node.nodeRight))
                        
                else:
                    if(node.valueCenter==key):
                        node.deleteValue(key)
                        mini, nodoHoja=self.findMin(node.nodeRight)
                        node.push(self.findMin(node.nodeRight))
                    else:
                        if(node.nodeCenterLeft==None):
                            node.deleteValue(key)
                            mini, nodoHoja=self.findMin(node.nodeCenterRight)
                            node.push(self.findMin(node.nodeCenterRight))
                        else:
                            node.deleteValue(key)
                            mini, nodoHoja=self.findMin(node.nodeCenterLeft)
                            node.push(self.findMin(node.nodeCenterLeft))
                            
                self.deleteT(mini, nodoHoja)           
                            
        if(node.sizeValues()==0):
            node.merge()
            
        
    
    def find(self, key):
        if(self.root==None):
            raise Exception("empty collection")
        else:
            return self.findT(self.root, key)
        
    def findT(self, node, key):
                
        print("I'm in ")
        print(node.__str__())
        if(node==None):
            raise Exception("key wasn't found")
        # 2 cases, it's a node with 1 value or 2 values (and respectively 2 childs or 3 childs)
        # case 1, regular node
        if(node.sizeValues()==1):
            if(key>node.valueCenter):
                return self.findT(node.nodeRight, key)
            elif(key<node.valueCenter):
                return self.findT(node.nodeLeft, key)
            else:
                return node
        else:
            # tiene 3 hijos, pero uno de ellos es None por seguro(centerLeft o centerRight)
            #if both are None, then it's a leaf
            if(key<node.getMin()):
                return self.findT(node.nodeLeft, key)
            elif(key>node.getMax()):
                return self.findT(node.nodeRight)
            elif(node.contains(key)):
                return node
            else:
                #if they are both None, we send whicever one
                if(node.nodeCenterLeft==None and node.nodeCenterRight==None):
                    raise Exception("key wasn't found")
                elif(node.nodeCenterLeft!=None):
                    return self.findT(node.nodeCenterLeft, key)
                else:
                    return self.findT(node.nodeCenterRight, key)
                
    
    def __init__(self, root=None):
        self.root=root
        
    def insert(self, value):
        if(self.root==None):
            self.root=Node(value)
        else:
            self.insertT(value, self.root)
        
    def insertT(self, value, nodo):
        print("x")
        # 3 cases, it's empty, it's a simple node or it's a node with 2 values and 3 childs
        if(nodo.sizeChilds()==0):
            nodo.push(value)
        elif(nodo.sizeChilds()<3):
            if(value>=nodo.valueCenter):
                self.insertT(value, nodo.nodeRight)
            else:
                self.insertT(value, nodo.nodeLeft)
        else:
            if(value>=nodo.valueCenter):
                if(nodo.valueRight!=None):
                    if(value>=nodo.valueRight):
                        self.insertT(value, nodo.nodeRight)
                    else:
                        if(nodo.nodeCenterLeft!=None):
                            self.insertT(value, nodo.nodeCenterLeft)
                        else:
                            self.insertT(value, nodo.nodeCenterRight)
                else:
                    self.insertT(value, nodo.nodeRight)
            else:
                if(nodo.valueLeft!=None):
                    if(value>=nodo.valueLeft):
                        if(nodo.nodeCenterLeft!=None):
                            self.insertT(value, nodo.nodeCenterLeft)
                        else:
                            self.insertT(value, nodo.nodeCenterRight)
                    else:
                        self.insertT(value, nodo.nodeLeft)
                else:
                    self.insertT(value, nodo.nodeLeft)

    def __str__(self):
        return self.printLevelOrder()
        
    def printLevelOrder(self): 
        # Base Case 
        #space="   -   "
        result = ""
        queue = deque([])
        if(self.root==None): 
            return
      
        
        # Enqueue Root and initialize height 
        queue.append(self.root) 
  
        while(len(queue) > 0): 
            # Print front of queue and remove it from queue 
            
            node = queue.popleft()
            result = result + node.__str__() + "-"

            if(node.nodeLeft!=None):
                #print("b")
                queue.append(node.nodeLeft) 
            if(node.nodeCenterLeft!=None):
                #print("c")
                queue.append(node.nodeCenterLeft)
            if(node.nodeCenterRight!=None):
                #print("d")
                queue.append(node.nodeCenterRight)
            if(node.nodeRight!=None):
                #print("e")
                queue.append(node.nodeRight)
                
        return result
    
    def printPretty(self): 
        # Base Case 
        #space="   -   "
        result = ""
        space = ""
        level = ""
        queue = deque([])
        if(self.root==None): 
            return
      
        
        # Enqueue Root and initialize height 
        queue.append(self.root) 
        n=1
        nextGen=0
        m=self.findHeight()
        while(len(queue) > 0): 
            # Print front of queue and remove it from queue 
            i=m
            while(i>0):
                space=space+"      "
                i=i-1
            while(n>0):
                
                node = queue.popleft()
                nextGen=nextGen + node.sizeChilds()
            
                level =  level + space + node.__str__() 

                if(node.nodeLeft!=None):
                #print("b")
                    queue.append(node.nodeLeft) 
                if(node.nodeCenterLeft!=None):
                #print("c")
                    queue.append(node.nodeCenterLeft)
                if(node.nodeCenterRight!=None):
                #print("d")
                    queue.append(node.nodeCenterRight)
                if(node.nodeRight!=None):
                #print("e")
                    queue.append(node.nodeRight)
                n=n-1
                
            result = result + level + "\n"
            result = result + "\n"
            
            level=""
            space=" "
            n=nextGen
            nextGen=0
            m=m-1
        return result
            
  
                # Enqueue right child 
                
                        
            
            
        
        
        
    
"""    
root=Node(4)
print(root)
root.push(1)
print(root)
root.push(6)
print(root)
root.nodeLeft.push(0)
root.nodeLeft.push(2)
print(root)
print(root.nodeCenterLeft)
root.nodeRight.push(7)
root.nodeRight.push(9)
print(root)
print(root.nodeRight)
"""

arbol=TwoThreeTree()
arbol.insert(6)

arbol.insert(7)
arbol.insert(8)
arbol.insert(20)

arbol.insert(21)
arbol.insert(1)

arbol.insert(2)
arbol.insert(40)
arbol.insert(9)
print(arbol)

arbol.insert(10)
arbol.insert(30)
print(arbol)

arbol.insert(51)
print(arbol)

print(arbol)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
arbol.insert(90)
print(arbol)
arbol.insert(100)
arbol.insert(110)
arbol.insert(200)
p=arbol.find(200)
print(arbol.printPretty())


arbol.delete(200)
print(arbol.printPretty())

print(p)


print("w")
print(arbol.printPretty())
arbol.delete(110)
print(arbol.printPretty())







                        
                
                    
                
            
            
            
            
            
                
                        
            
