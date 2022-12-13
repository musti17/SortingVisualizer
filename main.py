from concurrent.futures import thread
from glob import glob
import os, time, csv, random, sys, threading
from tkinter import *
from tkinter.ttk import Combobox
from algs.bubble_sort import bubble_sort
from algs.quick_sort import quick_sort
from algs.insertion_sort import insertion
from algs.merge_sort import merge_sort
from algs.selection_sort import selection
from algs import random_sort
from algs.counting_sort import counting
from algs.radix_sort import radixSort
from algs.cocktail_sort import cocktail
from algs.shell_sort import shell
from algs.heapSort import heapSort
from algs.heapify import heapify
from algs.bucket_sort import bucket_sort
from algs.modified_quicksort import modified_quick_sort
from algs.count_range import count_range
import pandas as pd

# start a tkinter window
root = Tk()
widthr = 1700
heightr = 850

# set minsize
root.minsize(1600, 850)
root.config(bg="grey")
root.title("Sorting algorithms visualization")

# vars
selected_alg = StringVar()
dades_file = StringVar()
checkvar = IntVar()
data = []
trys = random_sort.trys
savedArr = []

# draw the rectangles
def drawdata(data, colorarray):
    canvas.delete("all")
    c_height = 700
    c_width = 1600
    x_width = c_width / (len(data) + 1)
    offset = 0
    spacing = 0
    normalizeddata = [i / max(data) for i in data]

    for i, height in enumerate(normalizeddata):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * c_height
        x1 = (i+1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorarray[i])

    root.update_idletasks() # update the triangles

# generate an array
def generate():
    global data, file1, file2, file3, file4, file5

    data = []

    if file_det.get() == 'Default':
        f=open("FileForNumbers/file.txt","r")
        data=[]
        for num in f:
            data.append(int(num))

        print (data)
        drawdata(data, ['red' for x in range (len(data))])

    if file_det.get() == 'File1':
        f=open("FileForNumbers/file1.txt","r")
        data=[]
        for num in f:
            data.append(int(num))
    
        print (data)
        drawdata(data, ['red' for x in range (len(data))])

    if file_det.get() == 'File2':
        f=open("FileForNumbers/file2.txt","r")
        data=[]
        for num in f:
            data.append(int(num))

        print (data)
        drawdata(data, ['red' for x in range (len(data))])    

    if file_det.get() == 'File3':
        f=open("FileForNumbers/file3.txt","r")
        data=[]
        for num in f:
            data.append(int(num))
        
        print (data)
        drawdata(data, ['red' for x in range (len(data))])

    if file_det.get() == 'File4':
        f=open("FileForNumbers/file4.txt","r")
        data=[]
        for num in f:
            data.append(int(num))

        print (data)
        drawdata(data, ['red' for x in range (len(data))])

    if file_det.get() == 'File5':
        f=open("FileForNumbers/file5.txt","r")
        data=[]
        for num in f:
            data.append(int(num))
        
        print (data)
        drawdata(data, ['red' for x in range (len(data))])                        

    print(data)
    drawdata(data, ['black' for x in range(len(data)+1)])    # call the drawdata function and create the squares

def quit_func():
    root.destroy()

def sorting_algs_func(alg_name, end, start, speed):
    timetext = str(f'{alg_name} en {round(end - start, 5)} \n')
    crono.insert(0.0, str(timetext))
    time.sleep(1)

def Start_alg():
    global data, crono, speed_entry

    if checkvar.get() == 1:
        time.sleep(1)

    try:
        speed = float(speed_entry.get())
    except:
        speed = 0

    if alg_menu.get() == "Bubble Sort":     # if buble sort selected:
        start = time.perf_counter()         # start a timer
        bubble_sort(data, drawdata, speed)  # call the sort function
        end = time.perf_counter()           # stop the timer when the function ends
        sorting_algs_func('bubble', end, start, speed)
        crono.insert(0.0,"Bubble Sort\n")
        crono.insert(0.0,"Space Complexity: O(n)\n")
        crono.insert(0.0,"Time Complexity: O(n)\n")

    elif alg_menu.get() == "Quick Sort":
        start = time.perf_counter()
        quick_sort(data, 0, len(data)-1, drawdata, speed)
        end = time.perf_counter()
        drawdata(data, ['green' for x in range(len(data))])
        sorting_algs_func('quick', end, start, speed)
        crono.insert(0.0,"Time Complexity: O(n log n)\n")#for best and avg case 
        crono.insert(0.0,"Space Complexity: O(n+n)\n")
        crono.insert(0.0,"Quick Sort\n")


    elif alg_menu.get() == "Insertion Sort":
        start = time.perf_counter()
        insertion(data, drawdata, speed)
        end = time.perf_counter()
        sorting_algs_func('insertion', end, start, speed)
        crono.insert(0.0,"Space Complexity: O(n)\n")
        crono.insert(0.0,"Time Complexity: O(n) Best Case\n")
        crono.insert(0.0,"Time Complexity: O(n^2) Worst Case\n")
        crono.insert(0.0,"Insertion Sort\n")

    elif alg_menu.get() == "Merge Sort":
        start = time.perf_counter()
        merge_sort(data, drawdata, speed)
        end = time.perf_counter()
        sorting_algs_func('merge', end, start, speed)
        crono.insert(0.0,"Time Complexity: O(n log n)\n")#for best and avg case 
        crono.insert(0.0,"Space Complexity: O(n+n)\n")
        crono.insert(0.0,"Merge Sort\n")


    elif alg_menu.get() == "Heap Sort":
        start = time.perf_counter()
        heapSort(data, drawdata, speed)
        end = time.perf_counter()
        sorting_algs_func('heapSort', end, start, speed)
        crono.insert(0.0,"Time Complexity: O(n log n)\n")#for best,avg,worst case 
        crono.insert(0.0,"Space Complexity: O(n)\n")
        crono.insert(0.0,"Heap Sort\n")

    elif alg_menu.get() == "Modified Quick Sort":
        start = time.perf_counter()
        modified_quick_sort(data,0, len(data)-1, drawdata, speed)
        end = time.perf_counter()
        sorting_algs_func('modified_quick_sort', end, start, speed)
        crono.insert(0.0,"Time Complexity: O(n log (n/k))\n")#for best and avg case 
        crono.insert(0.0,"Space Complexity: O(n+n)\n")
        crono.insert(0.0,"Modified Quick Sort\n")

    elif alg_menu.get() == "Bucket Sort":
        start = time.perf_counter()
        bucket_sort(data, drawdata, speed)
        end = time.perf_counter()
        sorting_algs_func('bucket_sort', end, start, speed)
        crono.insert(0.0,"Time Complexity: O(k)\n")#O(k) for oounts array
        crono.insert(0.0,"Space Complexity: O(n+k)\n")#O(n) for animations array and O(k) for allBuckets array
        crono.insert(0.0,"Bucket Sort\n")

    elif alg_menu.get() == "Counting Sort":
        start = time.perf_counter()
        counting(data, drawdata, speed)
        end = time.perf_counter()
        sorting_algs_func('counting', end, start, speed)
        crono.insert(0.0,"Time Complexity: O(n+k) for counts array\n")
        crono.insert(0.0,"Time Complexity: O(n) for copy array\n")# 
        crono.insert(0.0,"Space Complexity: O(n+k)\n") 
        crono.insert(0.0,"Count Sort\n")

    elif alg_menu.get() == "Count Range":
        start = time.perf_counter()
        count_range(data, drawdata, speed)
        end = time.perf_counter()
        sorting_algs_func('count_range', end, start, speed)
        crono.insert(0.0,"Time Complexity: O(n+k)\n")#for best and avg case 
        crono.insert(0.0,"Space Complexity: O(n+k+1)\n")# O(k) since we are creating an array B of size k where k is the maximum value in the array and n is the size of the animations array
        crono.insert(0.0,"CountRange Sort\n")

    elif alg_menu.get() == "Radix Sort":
        start = time.perf_counter()
        radixSort(data, drawdata, speed)
        end = time.perf_counter()
        drawdata(data, ['green' for x in range(len(data))])
        sorting_algs_func('radix', end, start, speed)
        crono.insert(0.0,"Time Complexity: O(nk)\n")#for best,avg,worst case 
        crono.insert(0.0,"Space Complexity: O(n+k)\n")
        crono.insert(0.0,"Radix Sort\n")



def save_func():        # a function to save the array in a button and use it on the use_func
    global savedArr

    if len(data) == 0:
        textt = str('Gen data first\n')
        crono.insert(0.0, str(textt))
    else:
        savedArr = data
        textt = str('Successfuly saved\n')
        crono.insert(0.0, str(textt))

def use_func():         # save the data that the save_func has saved
    global savedArr

    drawdata(savedArr, ['black' for x in range(len(savedArr)+1)])


#1700
#850
# frames
canvas = Canvas(root, width=1600, height=700, bg="white")
canvas.place(x=0, y=150)

# ui
alg_menu = Combobox(root, width=15, textvariable=selected_alg, values=['Algs' , 'Bubble Sort', 'Insertion Sort','Heap Sort', 'Quick Sort','Modified Quick Sort','Merge Sort', 'Counting Sort', 'Radix Sort','Bucket Sort','Count Range'])
alg_menu.place(x=290, y=20)
alg_menu.current([0])
#ser_menu.current(2) # delete this after testing

#nEntry.insert(END, 30) #delete this after testing

order = Button(root, text='Order', font=("arial", 12), command=Start_alg, bg='red')
order.place(x=440, y=15)

Button(root, text='Create', font=("arial", 12), command=generate, bg='red').place(x=160, y=80)

file_det = Combobox(root, width=10, textvariable=dades_file, values=['Default', 'File1', 'File2', 'File3', 'File4','File5'])
file_det.place(x=50, y=90)
file_det.current([0])

#Text widget
crono = Text(root, width=50, height=6, state='normal')
crono.place(x=600, y=20)

Label(root, text="Speed:", bg='white').place(x=50, y=50)
speed_entry = Entry(root, width=25)
speed_entry.place(x=100, y=50)

quit_but = Button(root, text='Quit', font=("arial", 12), command=quit_func, bg='red')
quit_but.place(x=1100, y=15)

root.mainloop()