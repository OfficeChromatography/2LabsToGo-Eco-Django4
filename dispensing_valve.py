#Dispensing valve
import os
from pathlib import Path

file = Path("gcodes/dispensing-valve.gcode")
if file.exists():
    os.remove(file) #löscht die alte Datei, damit nichts an diese angehängt wird

print(file)

disp_valve = "G0X1\nM400\nM42P36S255\nM400\nG41\nM400\nG4S30\nM42P36S0\nG28X\n"

def dispensing_valve():
    with open(file, 'a') as r:
        r.write("; dispensing_valve\n")
        r.write(disp_valve)

dispensing_valve()

