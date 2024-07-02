import os
import time

menu=1
descuento= "soyotaku"

PR=4500
OR=5000
PVR=5200
AER=4800


while True:
    print("menu")
    print("Pikachu Roll")
    print("Otaku Roll")
    print("Pulpo Venenoso Roll")
    print("Anguila Electrica Roll")
    orden=int(input("seleccione los rolls que desee"))
    if orden ==1:
    PR +=1
    print('Pikachu Roll se a  agregado a su lista')
    