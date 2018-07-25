import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
import os
import csv

"""
    Converts binary file to two decimal arrays, p and q, where p = every even value and q every odd value (e.g. dec=12345678, p=[1,3,5,7] q=[2,4,6,8]).
    Also ouputs adjusted p -> padj = p / 25.6 -1  q -> qadj = q / 25.6
"""



#creates frame

class FRM(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
root = Tk()
app = FRM(master=root)
app.master.title("Binary to Dec")

frame = Frame(root)

frame.pack(side = LEFT)



def generate():
    Tk().withdraw()

    path = filedialog.askopenfilename(title = "Select binary file to convert to p and q decimal arrays")

    recp=[]
    recq=[]
    i=2
    bytee=0
    with open(path, "rb") as file:
        csvfile = os.path.basename(file.name) + ".csv"
        for x in range (0, 10000):
            byte = file.read(1)
            # print(byte)
            bytee = int.from_bytes(byte, byteorder='big')

            if bytee == 0:
                pass
            else:
                if i % 2 == 0:
                    recp.append(bytee)
                else:
                    recq.append(bytee)

            i += 1

    p = [ x / 25.6 -1 for x in recp ]
    q = [ x / 25.6 for x in recq ]
    print("Length of p" + str(len(p)))
    print("Length of q" + str(len(q)))
    # print("recorded p = " + str(recp))
    # print("recorded q = " + str(recq))
    #
    # print("adjusted p = " + str(p))
    # print("adjusted q = " + str(q))

    # csvfile = "DecData.csv"
    # csvfile = "../Data/" + csvfile
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')

        for i in range(len(p)):
            writer.writerows(zip(p, q))


        # writer.writerow("p")
        # for val in p:
        #     writer.writerow([val])
        # writer.writerow("q")
        # for val in q:
        #     writer.writerow([val])

generate_btn = tkinter.Button(frame, text="Generate!", command=generate)
generate_btn.pack(side = BOTTOM, padx = 5, pady = 5)






frame.mainloop()
