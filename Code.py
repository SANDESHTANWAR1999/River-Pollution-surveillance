import csv   
import matplotlib.pyplot as plt
from Tkinter import *

def getgraph(y):
    x = []
    for a in range(len(y)):
        x.append(a+1)
    print x,y
    plt.plot(x, y)
    plt.xlabel('Station Number')
    plt.ylabel('Average')
    plt.title('Stats')
    plt.show()

root = Tk()

root.title("answer window")
root.geometry("500x500")

app = Frame(root)
app.grid() 
label = Label(app,text= "todays observation")


#import csv , matplotlibk
t = ""
y = []
with open('rajasthan.csv','r') as csv_file: 
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
          
    for line in csv_reader:
          if line[0]=="":
              break
            
          avgint = float(line[3])+float(line[4])+float(line[5])+float(line[6])+float(line[7])+float(line[8])+float(line[9])+float(line[10])+float(line[11])+float(line[2])
          avgint = avgint/10.0
          y.append(avgint)
          if avgint<float(line[12]):
              t = t+"the garbage creation before station "+str(line[1])+"\n" 

          else:
              t = t+"no problem at station "+str(line[1])+"\n"


    label = Label(app,text= t,width=100)
    label.grid()
    Button(root, text="get graph", command=getgraph(y)).grid(row=1,column=1)
    root.mainloop()
 
