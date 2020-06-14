__author__ = 'Nerya Yekutiel'

from topsis_Car_Selection.read_data_from_xlsx import getValuesFromXlsx
import topsis_Car_Selection.gui as gui
from tkinter import *


criteriaPosNegVector, \
    criteriaVector, \
    familyWeightVector,\
    teenagerWeightVector,\
    goldenAgeWeightVector, \
    carsVector, \
    valueMatrix = getValuesFromXlsx()

print(

)

window = Tk()
var = StringVar()
var.set("one")
myWindow = gui.MyWindow(window, criteriaPosNegVector,
                        criteriaVector, familyWeightVector,
                        teenagerWeightVector, goldenAgeWeightVector,
                        carsVector, valueMatrix)
myWindow.prepareWindow()

window.title('Car Selection - TOPSIS Implementation')
window.geometry("1000x650+10+10")
window.mainloop()








