#import gv,pygraph, edge
#from pygraph.classes.graph import graph
#from pygraph.classes.digraph import digraph
#from pygraph.algorithms.searching import breadth_first_search
#from pygraph.readwrite.dot import write
#import pygraphviz as pgv
import math
import copy
from operator import itemgetter
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
from nltk.collocations import*
stop=stopwords.words('english')
class AdjMatrix(object):
    """
        A class defined for the nodes in the word graph. Here nodes include
        node name, node id etc, and any other information needed. The methods
        facilitate the processing specific to text graph
    """

    def __init__(self):
        self.gmatrix ={}
        
    
    def createMatrix(self,wordlist, poslist, directed):
        poslist=sorted(poslist,key=itemgetter(0))
        poslist=sorted(poslist,key=itemgetter(1))
        #print (wordlist)
        from edge import Edge
        for i in wordlist:
            tmatrix = {}
            for j in wordlist:
                temp = Edge()
                #if i == len(wordlist)-1:
                #    temp.updatewt(1.0)                    
                #temp.fromnode = wordlist[i]
                #temp.tonode = wordlist[j]
                tmatrix[j]=temp
            self.gmatrix[i]=tmatrix
            
        
        i=0
        while i < (len(poslist)-1):
            #print(poslist[i][0]," : ",poslist[i][1])
            size=nltk.word_tokenize(poslist[i][0])
            a=i
            z=0
            #print ("size:",len(size))
            c=a+1
            flag=0
            while z<len(size):
                #print ('z:',z)
                a=c
                c=a+1
                #print (a)
                if a<len(poslist):
                    if poslist[a][0] != poslist[i][0]:
                        temp1=[]
                        temp2=[]
                        
                        if poslist[i][1]!=poslist[a][1]:
                            z+=1
                            if z>len(size)-1:
                                temp2.append(a)
                            else:
                                temp1.append(a)
                            print("dwdp", poslist[a][0]," : ",poslist[a][1])
                            count =0
                            if c<len(poslist):
                                if poslist[a][1]==poslist[c][1]:
                                    while poslist[c][1]==poslist[a][1]:
                                        #print("1:",poslist[c][0])
                                        #temp.append(c)
                                        if z>len(size)-1:
                                            temp2.append(c)
                                        else:
                                            temp1.append(c)
                                        count+=1
                                        #print (temp)
                                        if poslist[i][0]==poslist[c][0]:
                                                    flag=1
                                                    for h in range(count+1):
                                                        #temp.pop()
                                                        if z>len(size)-1:
                                                            temp2.pop()
                                                        else:
                                                            temp1.pop()
                                                    break
                                        c+=1
                                        if c==len(poslist):
                                            break

        ##                    for x in temp:
        ##                        dist = poslist[x][1]-poslist[i][1]
        ##                        if dist<0:
        ##                            print ("dist: ",dist,i+1,poslist[i+1][1],i,poslist[i][1])
        ##                        #print "found", poslist[i][0], i
        ##                        row = poslist[i][0]
        ##                        col = poslist[x][0]
        ##                        #print (self.gmatrix[row][col].weight, poslist[i][0], poslist[i+1][0])
        ##                        if self.gmatrix[row][col].numupdate == 0:
        ##                            self.gmatrix[row][col].weight = dist
        ##                        else:
        ##                            self.gmatrix[row][col].updatewt(dist)
        ##                        self.gmatrix[row][col].updatenumber()
        ##        ##                if poslist[i][0]=='executable' or poslist[i+1][0]=='executable':
        ##        ##                   print dist , "......", poslist[i][0], poslist[i+1][0], row, col, self.gmatrix[row][col].weight
        ##                        if directed == False:
        ##                            if self.gmatrix[col][row].numupdate == 0:
        ##                                self.gmatrix[col][row].weight = dist
        ##                            else:
        ##                                self.gmatrix[col][row].updatewt(dist)
        ##                            self.gmatrix[col][row].updatenumber()
                        if poslist[i][1]==poslist[a][1]:
                            if z>len(size)-1:
                                temp2.append(a)
                            else:
                                temp1.append(a)
                            print("dwsp", poslist[a][0]," : ",poslist[a][1])
                            if c<len(poslist):
                                if poslist[a][1]==poslist[a+1][1]:
                                    while poslist[c][1]==poslist[a][1]:
                                        #temp.append(c)
                                        if z>len(size)-1:
                                            temp2.append(c)
                                        else:
                                            temp1.append(c)
                                        #print("1:",poslist[c][0])
                                        c+=1
                                        if c==len(poslist):
                                            break
                                if c<len(poslist):
                                    #temp.append(c)
                                    z+=1
                                    if z>len(size)-1:
                                        temp2.append(c)
                                        #print poslist[c][0]
                                    else:
                                        temp1.append(c)
                                    #print("2:",poslist[c][0])
                                    c+=1
                                    
                                    
                                    count =0
                                    if c <len(poslist):
                                        if poslist[c-1][1]==poslist[c][1]:
                                            while poslist[c-1][1]==poslist[c][1]:
                                                #temp.append(c)
                                                if z>len(size)-1:
                                                    temp2.append(c)
                                                else:
                                                    temp1.append(c)
                                                #print("3:",poslist[c][0])
                                                count+=1
                                                if poslist[i][0]==poslist[c-1][0] or poslist[i][0]==poslist[c][0]:
                                                    flag=1
                                                    for h in range(count+1):
                                                        #temp.pop()
                                                        if z>len(size)-1:
                                                            temp2.pop()
                                                        else:
                                                            temp1.pop()
                                                    break
                                                c+=1
                                                if c==len(poslist):
                                                    break
                        for x in temp1:
                            dist = 0
##                            if dist<0:
##                                print ("dist: ",dist,a,poslist[a][1],i,poslist[i][1])
                            #print "found", poslist[i][0], i
                            row = poslist[i][0]
                            col = poslist[x][0]
                            #print row,col,dist
                            #print (self.gmatrix[row][col].weight, poslist[i][0], poslist[i+1][0])
                            #print(row,col,dist)
                            #print (row,col)
                            if self.gmatrix[row][col].numupdate == 0:
                                self.gmatrix[row][col].weight = dist
                            else:
                                self.gmatrix[row][col].updatewt(dist)
                            self.gmatrix[row][col].updatenumber()
            ##                if poslist[i][0]=='executable' or poslist[i+1][0]=='executable':
            ##                   print dist , "......", poslist[i][0], poslist[i+1][0], row, col, self.gmatrix[row][col].weight
                            if directed == False:
                                if self.gmatrix[col][row].numupdate == 0:
                                    self.gmatrix[col][row].weight = dist
                                else:
                                    self.gmatrix[col][row].updatewt(dist)
                                self.gmatrix[col][row].updatenumber()
                                    
                        for x in temp2:
                            dist = poslist[x][1]-poslist[i][1]
##                            if dist<0:
##                                print ("dist: ",dist,a,poslist[a][1],i,poslist[i][1])
                            #print "found", poslist[i][0], i
                            row = poslist[i][0]
                            col = poslist[x][0]
                            #print row,col,dist
                            #print (self.gmatrix[row][col].weight, poslist[i][0], poslist[i+1][0])
                            #print(row,col,dist)
                            #print (row,col)
                            if self.gmatrix[row][col].numupdate == 0:
                                self.gmatrix[row][col].weight = dist
                            else:
                                self.gmatrix[row][col].updatewt(dist)
                            self.gmatrix[row][col].updatenumber()
            ##                if poslist[i][0]=='executable' or poslist[i+1][0]=='executable':
            ##                   print dist , "......", poslist[i][0], poslist[i+1][0], row, col, self.gmatrix[row][col].weight
                            if directed == False:
                                if self.gmatrix[col][row].numupdate == 0:
                                    self.gmatrix[col][row].weight = dist
                                else:
                                    self.gmatrix[col][row].updatewt(dist)
                                self.gmatrix[col][row].updatenumber()
                        
                        if flag==1:
                            break
                                
                    if poslist[a][0] == poslist[i][0]:
                        print("swdp ", poslist[a][0]," : ",poslist[i][0])
                        temp1=[]
                        temp2=[]
                        if c<len(poslist):
                            z+=1
                            while c<len(poslist) and poslist[c][1]==poslist[a][1]:
                                #print("1:",poslist[c][0])
                                #temp.append(c)
                                if z>len(size)-1:
                                    temp2.append(c)
                                else:
                                    temp1.append(c)
                                c+=1
                            for x in temp1:
                                dist = 0
##                                if dist<0:
##                                    print ("dist: ",dist,a,poslist[a][1],i,poslist[i][1])
                                #print "found", poslist[i][0], i
                                
                                row = poslist[i][0]
                                col = poslist[x][0]
                                #print row,col,dist
                                #print (self.gmatrix[row][col].weight, poslist[i][0], poslist[i+1][0])
                                #print(row,col,dist)
                                if self.gmatrix[row][col].numupdate == 0:
                                    self.gmatrix[row][col].weight = dist
                                else:
                                    self.gmatrix[row][col].updatewt(dist)
                                self.gmatrix[row][col].updatenumber()
                ##                if poslist[i][0]=='executable' or poslist[i+1][0]=='executable':
                ##                   print dist , "......", poslist[i][0], poslist[i+1][0], row, col, self.gmatrix[row][col].weight
                                if directed == False:
                                    if self.gmatrix[col][row].numupdate == 0:
                                        self.gmatrix[col][row].weight = dist
                                    else:
                                        self.gmatrix[col][row].updatewt(dist)
                                    self.gmatrix[col][row].updatenumber()
                            for x in temp2:
                                dist = poslist[x][1]-poslist[i][1]
##                                if dist<0:
##                                    print ("dist: ",dist,a,poslist[a][1],i,poslist[i][1])
                                #print "found", poslist[i][0], i
                                
                                row = poslist[i][0]
                                col = poslist[x][0]
                                #print row,col,dist
                                #print (self.gmatrix[row][col].weight, poslist[i][0], poslist[i+1][0])
                                #print(row,col,dist)
                                if self.gmatrix[row][col].numupdate == 0:
                                    self.gmatrix[row][col].weight = dist
                                else:
                                    self.gmatrix[row][col].updatewt(dist)
                                self.gmatrix[row][col].updatenumber()
                ##                if poslist[i][0]=='executable' or poslist[i+1][0]=='executable':
                ##                   print dist , "......", poslist[i][0], poslist[i+1][0], row, col, self.gmatrix[row][col].weight
                                if directed == False:
                                    if self.gmatrix[col][row].numupdate == 0:
                                        self.gmatrix[col][row].weight = dist
                                    else:
                                        self.gmatrix[col][row].updatewt(dist)
                                    self.gmatrix[col][row].updatenumber()
                            
                else:
                    break
            i += 1
        return self.gmatrix

    def addFilename(self,filename, wordlist):
        from edge import Edge
        initsize = len(self.gmatrix)
        tmatrix = list()
        for i in range(len(wordlist)):
            #print wordlist(i)
            #print wordlist[i]
            temp = Edge()
            #temp.updatewt(1.0)
            tmatrix.insert(initsize,temp)
            #self.gmatrix[initsize][i].updatewt(1.0)
            #self.gmatrix[initsize][i].updatenumber()
        self.gmatrix.insert(initsize,tmatrix)
        print (wordlist[len(wordlist)-1])
        for i in range(len(wordlist)):
            self.gmatrix[len(wordlist)][i].weight = 1.0
            #self.gmatrix[len(wordlist)][i].updatenumber()
            #if self.gmatrix[len(wordlist)][i].weight != float('inf'):
            
        return self.gmatrix
		
    def updateIndMatrix(self, matrix, tok, itxt,txt):
        mat=copy.deepcopy(matrix)
        itxt=list(set(itxt))
        #print(len(itxt))
        #print(len(txt))
        for i in range(len(itxt)):
            for j in range(len(itxt)):
                mat.gmatrix[i][j].weight=matrix.gmatrix[i][j].weight-self.gmatrix[i][j].weight
                mat.gmatrix[i][j].numupdate=matrix.gmatrix[i][j].numupdate-self.gmatrix[i][j].numupdate
                if(mat.gmatrix[i][j].numupdate==0):
                    mat.gmatrix[i][j].weight=float('inf')
        return mat
		
    """
        Given the current matrix and a new matrix with new values, the matrix must be updated
    """
    def updateMatrix(self, wordlist, poslist, directed):
        poslist=sorted(poslist,key=itemgetter(0))
        poslist=sorted(poslist,key=itemgetter(1))
        #print (poslist)
        #print ("updateMatrix")
        from edge import Edge
        #print ("matrix initial size", len(wordlist), len(self.gmatrix), len(self.gmatrix[0]))
        initsize = len(self.gmatrix)
        x=0
        #print wordlist
        for i in wordlist:
            tmatrix = {}
            if x>=initsize:
                for j in wordlist:
                    temp = Edge()
                    tmatrix[j]=temp
                self.gmatrix[i]=tmatrix
            else:
                j = initsize
                while j < len(wordlist):
                    temp = Edge()
                    self.gmatrix[i][wordlist[j]]=temp
                    j+=1
                
            x+=1
##        while (i<len(wordlist)):
##            #print("i:",i)
##            tmatrix = {}
##            if i>= initsize:
##                j=0
##                while j < len(wordlist):
##                    temp = Edge()
##                    if i == len(wordlist)-1:
##                        temp.updatewt(1.0)
##                    tmatrix.insert(j,temp)
##                    j+=1
##                self.gmatrix.insert(i,tmatrix)
##            else:
##                j = initsize
##                while j < len(wordlist):
##                    temp = Edge()
##                    self.gmatrix[i].insert(j,temp)
##                    j+=1
##            i+=1
       
        i=0
        while i < (len(poslist)-1):
            #print(poslist[i][0]," : ",poslist[i][1])
            size=nltk.word_tokenize(poslist[i][0])
            a=i
            z=0
            #print ("size:",len(size))
            c=a+1
            flag=0
            while z<len(size):
                #print ('z:',z)
                a=c
                c=a+1
                #print (a)
                if a<len(poslist):
                    if poslist[a][0] != poslist[i][0]:
                        temp1=[]
                        temp2=[]
                        
                        if poslist[i][1]!=poslist[a][1]:
                            z+=1
                            if z>len(size)-1:
                                temp2.append(a)
                            else:
                                temp1.append(a)
                            #print("dwdp", poslist[a][0]," : ",poslist[a][1])
                            count =0
                            if c<len(poslist):
                                if poslist[a][1]==poslist[c][1]:
                                    while poslist[c][1]==poslist[a][1]:
                                        #print("1:",poslist[c][0])
                                        #temp.append(c)
                                        if z>len(size)-1:
                                            temp2.append(c)
                                        else:
                                            temp1.append(c)
                                        count+=1
                                        #print (temp)
                                        if poslist[i][0]==poslist[c][0]:
                                                    flag=1
                                                    for h in range(count+1):
                                                        #temp.pop()
                                                        if z>len(size)-1:
                                                            temp2.pop()
                                                        else:
                                                            temp1.pop()
                                                    break
                                        c+=1
                                        if c==len(poslist):
                                            break

        ##                    for x in temp:
        ##                        dist = poslist[x][1]-poslist[i][1]
        ##                        if dist<0:
        ##                            print ("dist: ",dist,i+1,poslist[i+1][1],i,poslist[i][1])
        ##                        #print "found", poslist[i][0], i
        ##                        row = poslist[i][0]
        ##                        col = poslist[x][0]
        ##                        #print (self.gmatrix[row][col].weight, poslist[i][0], poslist[i+1][0])
        ##                        if self.gmatrix[row][col].numupdate == 0:
        ##                            self.gmatrix[row][col].weight = dist
        ##                        else:
        ##                            self.gmatrix[row][col].updatewt(dist)
        ##                        self.gmatrix[row][col].updatenumber()
        ##        ##                if poslist[i][0]=='executable' or poslist[i+1][0]=='executable':
        ##        ##                   print dist , "......", poslist[i][0], poslist[i+1][0], row, col, self.gmatrix[row][col].weight
        ##                        if directed == False:
        ##                            if self.gmatrix[col][row].numupdate == 0:
        ##                                self.gmatrix[col][row].weight = dist
        ##                            else:
        ##                                self.gmatrix[col][row].updatewt(dist)
        ##                            self.gmatrix[col][row].updatenumber()
                        if poslist[i][1]==poslist[a][1]:
                            if z>len(size)-1:
                                temp2.append(a)
                            else:
                                temp1.append(a)
                            #print("dwsp", poslist[a][0]," : ",poslist[a][1])
                            if c<len(poslist):
                                if poslist[a][1]==poslist[a+1][1]:
                                    while poslist[c][1]==poslist[a][1]:
                                        #temp.append(c)
                                        if z>len(size)-1:
                                            temp2.append(c)
                                        else:
                                            temp1.append(c)
                                        #print("1:",poslist[c][0])
                                        c+=1
                                        if c==len(poslist):
                                            break
                                if c<len(poslist):
                                    #temp.append(c)
                                    z+=1
                                    if z>len(size)-1:
                                        temp2.append(c)
                                        #print poslist[c][0]
                                    else:
                                        temp1.append(c)
                                    #print("2:",poslist[c][0])
                                    c+=1
                                    
                                    
                                    count =0
                                    if c <len(poslist):
                                        if poslist[c-1][1]==poslist[c][1]:
                                            while poslist[c-1][1]==poslist[c][1]:
                                                #temp.append(c)
                                                if z>len(size)-1:
                                                    temp2.append(c)
                                                else:
                                                    temp1.append(c)
                                                #print("3:",poslist[c][0])
                                                count+=1
                                                if poslist[i][0]==poslist[c-1][0] or poslist[i][0]==poslist[c][0]:
                                                    flag=1
                                                    for h in range(count+1):
                                                        #temp.pop()
                                                        if z>len(size)-1:
                                                            temp2.pop()
                                                        else:
                                                            temp1.pop()
                                                    break
                                                c+=1
                                                if c==len(poslist):
                                                    break
                        for x in temp1:
                            dist = 0
##                            if dist<0:
##                                print ("dist: ",dist,a,poslist[a][1],i,poslist[i][1])
                            #print "found", poslist[i][0], i
                            row = poslist[i][0]
                            col = poslist[x][0]
                            #print row,col,dist
                            #print (self.gmatrix[row][col].weight, poslist[i][0], poslist[i+1][0])
                            #print(row,col,dist)
                            #print (row,col)
                            if self.gmatrix[row][col].numupdate == 0:
                                self.gmatrix[row][col].weight = dist
                            else:
                                self.gmatrix[row][col].updatewt(dist)
                            self.gmatrix[row][col].updatenumber()
            ##                if poslist[i][0]=='executable' or poslist[i+1][0]=='executable':
            ##                   print dist , "......", poslist[i][0], poslist[i+1][0], row, col, self.gmatrix[row][col].weight
                            if directed == False:
                                if self.gmatrix[col][row].numupdate == 0:
                                    self.gmatrix[col][row].weight = dist
                                else:
                                    self.gmatrix[col][row].updatewt(dist)
                                self.gmatrix[col][row].updatenumber()
                                    
                        for x in temp2:
                            dist = poslist[x][1]-poslist[i][1]
##                            if dist<0:
##                                print ("dist: ",dist,a,poslist[a][1],i,poslist[i][1])
                            #print "found", poslist[i][0], i
                            row = poslist[i][0]
                            col = poslist[x][0]
                            #print row,col,dist
                            #print (self.gmatrix[row][col].weight, poslist[i][0], poslist[i+1][0])
                            #print(row,col,dist)
                            #print (row,col)
                            if self.gmatrix[row][col].numupdate == 0:
                                self.gmatrix[row][col].weight = dist
                            else:
                                self.gmatrix[row][col].updatewt(dist)
                            self.gmatrix[row][col].updatenumber()
            ##                if poslist[i][0]=='executable' or poslist[i+1][0]=='executable':
            ##                   print dist , "......", poslist[i][0], poslist[i+1][0], row, col, self.gmatrix[row][col].weight
                            if directed == False:
                                if self.gmatrix[col][row].numupdate == 0:
                                    self.gmatrix[col][row].weight = dist
                                else:
                                    self.gmatrix[col][row].updatewt(dist)
                                self.gmatrix[col][row].updatenumber()
                        
                        if flag==1:
                            break
                                
                    if poslist[a][0] == poslist[i][0]:
                        #print("swdp ", poslist[a][0]," : ",poslist[i][0])
                        temp1=[]
                        temp2=[]
                        if c<len(poslist):
                            z+=1
                            while c<len(poslist) and poslist[c][1]==poslist[a][1]:
                                #print("1:",poslist[c][0])
                                #temp.append(c)
                                if z>len(size)-1:
                                    temp2.append(c)
                                else:
                                    temp1.append(c)
                                c+=1
                            for x in temp1:
                                dist = 0
##                                if dist<0:
##                                    print ("dist: ",dist,a,poslist[a][1],i,poslist[i][1])
                                #print "found", poslist[i][0], i
                                
                                row = poslist[i][0]
                                col = poslist[x][0]
                                #print row,col,dist
                                #print (self.gmatrix[row][col].weight, poslist[i][0], poslist[i+1][0])
                                #print(row,col,dist)
                                if self.gmatrix[row][col].numupdate == 0:
                                    self.gmatrix[row][col].weight = dist
                                else:
                                    self.gmatrix[row][col].updatewt(dist)
                                self.gmatrix[row][col].updatenumber()
                ##                if poslist[i][0]=='executable' or poslist[i+1][0]=='executable':
                ##                   print dist , "......", poslist[i][0], poslist[i+1][0], row, col, self.gmatrix[row][col].weight
                                if directed == False:
                                    if self.gmatrix[col][row].numupdate == 0:
                                        self.gmatrix[col][row].weight = dist
                                    else:
                                        self.gmatrix[col][row].updatewt(dist)
                                    self.gmatrix[col][row].updatenumber()
                            for x in temp2:
                                dist = poslist[x][1]-poslist[i][1]
##                                if dist<0:
##                                    print ("dist: ",dist,a,poslist[a][1],i,poslist[i][1])
                                #print "found", poslist[i][0], i
                                
                                row = poslist[i][0]
                                col = poslist[x][0]
                                #print row,col,dist
                                #print (self.gmatrix[row][col].weight, poslist[i][0], poslist[i+1][0])
                                #print(row,col,dist)
                                if self.gmatrix[row][col].numupdate == 0:
                                    self.gmatrix[row][col].weight = dist
                                else:
                                    self.gmatrix[row][col].updatewt(dist)
                                self.gmatrix[row][col].updatenumber()
                ##                if poslist[i][0]=='executable' or poslist[i+1][0]=='executable':
                ##                   print dist , "......", poslist[i][0], poslist[i+1][0], row, col, self.gmatrix[row][col].weight
                                if directed == False:
                                    if self.gmatrix[col][row].numupdate == 0:
                                        self.gmatrix[col][row].weight = dist
                                    else:
                                        self.gmatrix[col][row].updatewt(dist)
                                    self.gmatrix[col][row].updatenumber()
                            
                else:
                    break
            i += 1
        
    def Floyd_Warshall(self):
        paths = AdjMatrix()
        for i in range(len(self.gmatrix[0])):
            tmatrix = list()
            for j in range(len(self.gmatrix[0])):
                dist = self.gmatrix[i][j].weight
                tmatrix.insert(j,dist)
            paths.gmatrix.insert(i,tmatrix)

        n = len(self.gmatrix[0])
        print (n)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    #print paths.gmatrix[i][j]
                    #paths.gmatrix[i][j] = min(paths.gmatrix[i][j], paths.gmatrix[i][k]+paths.gmatrix[k][j])
                    if paths.gmatrix[i][j] > paths.gmatrix[i][k]+paths.gmatrix[k][j]:
                       paths.gmatrix[i][j] = paths.gmatrix[i][k]+paths.gmatrix[k][j]

        return paths           
    def display(self,text):
        x=0
        for i in text:
            y=0
            for j in text:
##                if (text[i] == 'Corpus/intro/ds1.txt'):
##                    print (text[i], ",", i, ":", self.gmatrix[i][j].weight)
                #print (text[i],i, text[j],j, self.gmatrix[i][j].weight, len(self.gmatrix), len(self.gmatrix[0]))
                if self.gmatrix[i][j].weight != float('inf'):
                    #if self.gmatrix[i][j].weight < 10.0:
                    wt1= self.gmatrix[i][j].getwt()
                    if wt1 ==0:
                        wt1 = 0.5
                        #if self.gmatrix[i][j].weight ==0:
                                #print (text[i],i, text[j],j, wt1)
                         #gr.add_edge((text[i],text[j]),wt = wt1, label = str(wt1))
                    print(i,j,str(wt1),str(self.gmatrix[i][j].numupdate))
                y+=1
            x+=1

    def getMaxNumUpdate(self,text):
        maxi=0
        for x in range(len(text)):
            for y in range(len(text)):
                if self.gmatrix[text[x]][text[y]].numupdate>maxi:
                    maxi=self.gmatrix[text[x]][text[y]].numupdate
                    print text[x],text[y]
        return maxi
            
    def draw_png(self, text):
        #gr = digraph()
        #f = open("db/ds2a.gdf","w")
        #f = open("db/full.gdf","w")
        f = open("db/introhier.gdf","w")
        #fw = open("db/removed_edges.txt","w")
        #fw.write("node1    node2    wt    occurance \n")
        f.write("nodedef> name,label"+"\n")
        #G=pgv.AGraph(strict=False,directed=True)
        
            
        for x in range(len(text)):
##            if gr.has_node((text[x])) == False:
##                gr.add_node(text[x])
            f.write("v"+str(x)+","+text[x]+"\n")
        maxi=self.getMaxNumUpdate(text)
        print 'maxi: ',maxi
        f.write("edgedef> node1,node2,directed,weight,labelvisible"+"\n")        
        #print text
        for x in range(len(text)):
            y=x+1
            for y in range(len(text)):
##                if (text[i] == 'Corpus/intro/ds1.txt'):
##                    print (text[i], ",", i, ":", self.gmatrix[i][j].weight)
                #print (text[i],i, text[j],j, self.gmatrix[i][j].weight, len(self.gmatrix), len(self.gmatrix[0]))
                if self.gmatrix[text[x]][text[y]].weight != float('inf'):
                    #if self.gmatrix[i][j].weight < 10.0:
                    wt1= self.gmatrix[text[x]][text[y]].getwt(maxi)
##                    if wt1 ==0:
##                        wt1 = 0.5
                        #if self.gmatrix[i][j].weight ==0:
                                #print (text[i],i, text[j],j, wt1)
                         #gr.add_edge((text[i],text[j]),wt = wt1, label = str(wt1))
                    f.write("v"+str(x)+","+"v"+str(y)+","+"false"+","+str(wt1)+","+"true"+"\n")
##                    if self.gmatrix[text[x]][text[y]].numupdate>1:
##                        f.write("v"+str(x)+","+"v"+str(y)+","+"false"+","+str(wt1)+","+"true"+"\n")
##                    else:
##                        fw.write(text[x]+"    "+text[y]+"    "+str(wt1)+"    "+str(self.gmatrix[text[x]][text[y]].numupdate)+"\n")
                #if (i == 1081 or j==1081):
                #        	print self.gmatrix[i][j].weight
        f.close()
        #fw.close()
##        dot = write(gr)
##        gvv = gv.readstring(dot)
##        gv.layout(gvv,'dot')
##        gv.render(gvv,'png','textgraph.png')
##        gr.clear()

    def draw_ind_png(self, text, itext, textfile):
        #gr = digraph()
        #f = open("db/ds2a.gdf","w")
        #f = open("db/full.gdf","w")
        f = open("db/"+textfile[0:-4]+".gdf","w")
        f.write("nodedef> name,label"+"\n")
        #G=pgv.AGraph(strict=False,directed=True)
        #print(len(text))
            
        for x in range(len(text)):
##            if gr.has_node((text[x])) == False:
##                gr.add_node(text[x])
            if text[x] in itext:
                f.write("v"+str(x)+","+text[x]+"\n")
                
        f.write("edgedef> node1,node2,directed,weight,labelvisible"+"\n")        
        #print text
        i = j = 0
        for i in range(len(text)):
            for j in range(len(text)):
                if (text[i] == 'Corpus/intro/ds1.txt'):
                    print (text[i], ",", i, ":", self.gmatrix[i][j].weight)
                #print (text[i],i, text[j],j, self.gmatrix[i][j].weight, len(self.gmatrix), len(self.gmatrix[0]))
                if self.gmatrix[i][j].weight != float('inf'):
                    #print("true")
                    #if self.gmatrix[i][j].weight < 10.0:
                    wt1= self.gmatrix[i][j].getwt()
                    if wt1 ==0:
                        wt1 = 0.5
			#if self.gmatrix[i][j].weight ==0:
				#print (text[i],i, text[j],j, wt1)
	                 #gr.add_edge((text[i],text[j]),wt = wt1, label = str(wt1))
                    f.write("v"+str(i)+","+"v"+str(j)+","+"false"+","+str(wt1)+","+"true"+"\n")
                #if (i == 1081 or j==1081):
                #        	print self.gmatrix[i][j].weight
        
##        dot = write(gr)
##        gvv = gv.readstring(dot)
##        gv.layout(gvv,'dot')
##        gv.render(gvv,'png','textgraph.png')
##        gr.clear()

    def draw_paths(self, text):
        #gr = digraph()
        f = open("test.gdf","w")
        f.write("nodedef> name,label"+"\n")
        #G=pgv.AGraph(strict=False,directed=True)

        for x in range(len(text)):
            #if gr.has_node((text[x])) == False:
                #gr.add_node(text[x])
            f.write("v"+str(x)+","+text[x]+"\n")
                
        f.write("edgedef> node1,node2,directed,weight,labelvisible"+"\n")
        i = j = 0
        for i in range(len(text)):
            for j in range(len(text)):
                #if self.gmatrix[i][j]!= float('inf'):
                if self.gmatrix[i][j] < 10.0:
                    wt1= self.gmatrix[i][j]
                    #print (text[i],i, text[j],j, wt1)
                    #gr.add_edge((text[i],text[j]),label = str(wt1))
                    f.write("v"+str(i)+","+"v"+str(j)+","+"true"+","+str(wt1)+","+"true"+"\n")
                    
                
        print ("done")
        #dot = write(gr)
        print ("done1")
##        gvv = gv.readstring(dot)
##        print "done2"
##        gv.layout(gvv,'nop1')
##        print "done3"
##        gv.render(gvv,'png','pathgraph.png')

        #G=pgv.AGraph(dot)
        #G.write("test.xml")
        # G.layout(prog='dot')
       #G.layout(prog = 'dot')
        #G.draw('pathgraph.png')
if __name__ == '__main__':
##    from nltk.corpus import gutenberg
##    words = ['biochem2.txt']
##    create_graph(gutenberg.words('austen-sense.txt'), words)
    txt=['c','c b','c b t','b','b t','t','d']
    mlist=[['c',0],['c b',0],['b',1],['b',2],['b t',2],['t',3],['d',4]]
    amatrix = AdjMatrix()
    amatrix.createMatrix(txt, mlist, False)
