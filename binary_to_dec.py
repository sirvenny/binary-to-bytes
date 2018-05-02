
from tkinter import Tk
from tkinter import filedialog

Tk().withdraw()

path = filedialog.askopenfilename(title = "Select binary file to convert to p and q decimal arrays")

p=[]
q=[]
i=2
bytee=0
with open(path, "rb") as file:
    for x in range (0, 200):
        byte = file.read(1)
        print(byte)
        bytee = int.from_bytes(byte, byteorder='big')

        if i % 2 == 0:
            p.append(bytee)
        else:
            q.append(bytee)

        i += 1

print("p = " + str(p))
print("q = " + str(q))
