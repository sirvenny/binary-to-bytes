import struct
path = input('Enter path to binary file')

# file = open(path, "rb")
byte = 0
i=0

with open(path, "rb") as file:
    byte = file.read(1)

    print(int.from_bytes(byte, byteorder='big'))
    while byte != "":
        byte = file.read(1)
        print(int.from_bytes(byte, byteorder='big'))


# try:
#     byte = file.read(1)
#     while byte != "":
#         byte = file.read(1)
#
# finally:
#     file.close()

# while byte != "":
#     byte = file.read(i)
#     print(byte)
#     i = i + 1
#
# file.close()
