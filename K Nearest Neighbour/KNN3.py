#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fd
import numpy as np
import matplotlib.pyplot as plt
import random as rd


##======================================
##  KNN Code

def euclid(a, b):
    dist = (sum((a-b)**2))
    return dist

    #==================================
    ## reading the image file

def knn(file, nCentroid, nIter):
    print("in KNN", file, nCentroid, nIter)
    pixel = plt.imread(file)
    

    dime = np.shape(pixel)

    Maxrow = dime[0]
    Maxcol = dime[1]

    print(dime)


    #==================================
    # initializing cluster centroids

    # number of centroids
    #nCentroid = input("How many centroids?\n")
    nCentroid = int(nCentroid)
    print("You want",nCentroid, "centroids")



    #init centroids
    Centroid = []
    for i in range(nCentroid):
        Centroid = Centroid +[ [rd.randint(0,256)] + [rd.randint(0,256)] + [rd.randint(0,256)] ]

    Centroid = np.array(Centroid)    
        
    print("Centroids are=\n",Centroid)

    #number of members assoc with centroid
    memberSum = np.array([[0,0,0]]*nCentroid)
    memberCount = np.array([1]*nCentroid)









    #init a blank array to put cluster members in at the end
    Blank = [[[0,0,0]]*Maxcol]*Maxrow
    #Blank = np.zeros((Maxcol,Maxrow,3))

    #init several blankarrays to put cluster members in
    Cluster = [Blank]*nCentroid
    #Cluster = np.zeros((nCentroid, Maxcol, Maxrow, 3))

    Blank = np.array(Blank)
    Cluster = np.array(Cluster)

    print("blank image", np.shape(Blank))
    print("Clusters", np.shape(Cluster))






    #==================================
    # public static void main

    #nIter = input("How Many Iterations?\n")
    nIter = int(nIter)


    dist = [0]*nCentroid

    for iter in range(nIter):
        
        for i in range(Maxrow):
            for j in range(Maxcol):
                

                #calc euclidean dist of pixel to each centroid
                for k in range(nCentroid):
                    #print(i,j,k,euclid(Centroid[k], pixel[i,j]))
                    dist[k] = euclid(Centroid[k], pixel[i][j])

                

                indeks = np.argmin(dist)
                #print(indeks, min(dist))

                memberSum[indeks] = memberSum[indeks] + pixel[i][j]
                memberCount[indeks] = memberCount[indeks]+1

            progress["value"]=progress["value"]+90/(nIter*Maxrow)
            window.update_idletasks()
            




                #print(memberSum, memberCount)

        for b in range(nCentroid):
            Centroid[b]=memberSum[b]/memberCount[b]
        print("In this", iter, "iteration,")    
        print("Centroids=\n", Centroid)


        
    ## assign the pixels to the clusters
    for i in range(Maxrow):
        for j in range(Maxcol):
            for k in range(nCentroid):
                dist[k] = euclid(Centroid[k], pixel[i][j])


            indeks = np.argmin(dist)

            Blank[i][j] = Centroid[indeks]

            Cluster[indeks][i][j] = Centroid[indeks]

        progress["value"]=progress["value"]+90/(nIter*Maxrow)
        window.update_idletasks()
            

                                 


            
    progress["value"]=0
    plt.imshow(pixel)

    for i in range(nCentroid):
        plt.figure(i)
        plt.imshow(Cluster[i])

    plt.figure(nCentroid+1)
    plt.imshow(Blank)

    plt.show()


















##============================================================
##  Tkinter GUI Code

window = tk.Tk()



def openFile():
    filename =""
    filename = fd.askopenfilename(filetypes=(("jpeg", "*.jpg"), ("PNG", "*.png"),("GIF","*.gif")))
    #filename = fd.LoadFileDialog(window)
    entry.insert(0,filename)
    print("openfile",filename)
    imag=plt.imread(filename)
    progress["value"]=0
    
    
    
def RunProg():
    filename=""
    filename = entry.get()
    entry.delete(0, tk.END)
    print("RunProg",filename)
    
#    imag=plt.imread(filename)
#    bentuk = imag.shape()
    

    centroids = int(spinbox1.get())
    
    
    iterations = int(spinbox2.get())

#    maxx = bentuk(0)*iterations
    
    knn(filename, centroids, iterations)
    entry.delete(0, tk.END)






btn = tk.Button(text = "Click to Load File", width=20, height=1, command= openFile)
#btn.pack()
btn.grid(row=0, column =0, columnspan=2)

entry = tk.Entry()
#entry.pack()
entry.grid(row=1, column =0, columnspan=2)


lable1 = tk.Label(text="Number of Clusters")
#lable1.pack()
lable1.grid(row=2, column =0)

spinbox1 = tk.Spinbox(window, from_=2, to = 32)
#spinbox1.pack()
spinbox1.grid(row=2, column =1)

lable2 = tk.Label(text="Number of Iterations")
#lable2.pack()
lable2.grid(row=3, column =0)

spinbox2 = tk.Spinbox(window, from_=5, to = 15)
#spinbox2.pack()
spinbox2.grid(row=3, column =1)


btn2 = tk.Button(text = "Click to begin Clustering", command=RunProg)
btn2.grid(row = 4, column=0, columnspan=2 )


progress = ttk.Progressbar(length=300, )
progress.grid(row =6, column = 0, columnspan=2)
lable3 = tk.Label(text="Let's Progress Bar")
lable3.grid(row = 5, column =0, columnspan=2)


window.mainloop()
