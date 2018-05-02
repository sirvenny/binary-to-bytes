
from tkinter import Tk
from tkinter import filedialog

Tk().withdraw()

path = filedialog.askopenfilename(title = "Select binary file to convert to p and q decimal arrays")

recp=[]
recq=[]
i=2
bytee=0
with open(path, "rb") as file:
    for x in range (0, 200):
        byte = file.read(1)
        print(byte)
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

print("recorded p = " + str(recp))
print("recorded q = " + str(recq))

print("adjusted p = " + str(p))
print("adjusted q = " + str(q))
