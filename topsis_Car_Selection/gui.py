__author__ = 'Nerya Yekutiel'

import numpy as np
from topsis_Car_Selection.topsis_algorithm import topsis
from tkinter import *
from tkinter.ttk import Combobox
import time


class MyWindow:

    userWeightVector = None
    topsisObj = None
    labelDict = None
    criteriaPosNegVector = None
    criteriaVector = None
    familyWeightVector = None
    teenagerWeightVector = None
    goldenWeightVector = None
    carsVector = None
    valueMatrix = None

    def __init__(self, win, criteriaPosNegVector, criteriaVector, familyWeightVector,
                 teenagerWeightVector, goldenAgeWeightVector,
                 carsVector, valueMatrix):
        self.win = win
        self.criteriaPosNegVector = criteriaPosNegVector
        self.criteriaVector = criteriaVector
        self.familyWeightVector = familyWeightVector
        self.teenagerWeightVector = teenagerWeightVector
        self.goldenWeightVector = goldenAgeWeightVector
        self.carsVector = carsVector
        self.valueMatrix = valueMatrix

        Label(self.win, text="Run Time", font="Ariel") \
            .place(x=450, y=535)
        self.runTime = Entry()
        self.runTime.place(x=550, y=540)

        self.calcBt = Button(self.win, text="Calculate", command=self.calculateCar)
        self.calcBt.place(x=500, y=580)

        self.resetBt = Button(self.win, text="Reset", command=self.resetGUI)
        self.resetBt.place(x=580, y=580)

        self.familyBt = Button(self.win, text="Family", command=self.setFamWeight)
        self.familyBt.place(x=800, y=520)

        self.teenagerBt = Button(self.win, text="Teenagers", command=self.setTeenWeight)
        self.teenagerBt.place(x=800, y=560)

        self.goldenBt = Button(self.win, text="Golden Age", command=self.setGoldenWeight)
        self.goldenBt.place(x=800, y=600)

        Label(self.win, text="*Best Choice", font="Ariel") \
            .place(x=200, y=570)
        self.bestAns = Entry()
        self.bestAns.place(x=350, y=575)
        Label(self.win, text="*Worst Choice", font="Ariel") \
            .place(x=200, y=600)
        self.worstAns = Entry()
        self.worstAns.place(x=350, y=605)

        Label(self.win, text="*Rank Wisely :)", font="Dubai") \
            .place(x=20, y=470)
        Label(self.win, text="Car Selection - TOPSIS Implementation - Rank Criteria from 1 to 10*",
              font="Corbel").place(x=200, y=10)
        Label(self.win, text="1 = Least Important").place(x=870, y=10)
        Label(self.win, text="10 = Most Important").place(x=870, y=30)

    def getUserPreferences(self):
        criteriaDict = dict()
        for label in self.labelDict:
            criteriaDict[label] = self.labelDict[label].get()
        self.userPreferencesToWeightVector(criteriaDict, self.criteriaVector)

    def userPreferencesToWeightVector(self, criteriaDict, criteriaVector):
        size = len(criteriaVector)
        userWeightVector = np.ndarray((1, size))
        for i in range(size):
            userWeightVector[0][i] = criteriaDict[criteriaVector[i]]
        sumOfWeights = sum(userWeightVector[0])
        self.userWeightVector = userWeightVector / sumOfWeights

    def setFamWeight(self):
        for i in range(len(self.criteriaVector)):
            self.labelDict[self.criteriaVector[i]].\
                current(int(self.familyWeightVector[i] - 1))

    def setTeenWeight(self):
        for i in range(len(self.criteriaVector)):
            self.labelDict[self.criteriaVector[i]]. \
                current(int(self.teenagerWeightVector[i] - 1))

    def setGoldenWeight(self):
        for i in range(len(self.criteriaVector)):
            self.labelDict[self.criteriaVector[i]]. \
                current(int(self.goldenWeightVector[i] - 1))

    def resetGUI(self):
        for key in self.labelDict:
            self.labelDict[key].current(0)
        self.bestAns.delete(0, END)
        self.worstAns.delete(0, END)
        self.runTime.delete(0, END)

    def calculateCar(self):
        self.getUserPreferences()
        startTime = time.clock()
        self.topsisObj = topsis(self.valueMatrix.copy(),
                                self.userWeightVector.copy(), self.criteriaPosNegVector)
        endTime = time.clock()
        self.bestAns.delete(0, END)
        self.worstAns.delete(0, END)
        self.runTime.delete(0, END)
        bestCar, worstCar = self.topsisObj.calc()

        self.bestAns.insert(0, self.carsVector[bestCar])
        self.worstAns.insert(0, self.carsVector[worstCar])
        self.runTime.insert(0, endTime - startTime)


    def prepareWindow(self):
        attributesNameCoordsX, attributeNameCoordsY = 25, 110
        data = [i for i in range(1, 11)]
        self.labelDict = dict()
        Label(self.win, text="Comfort", font="Aharoni").place(x=20, y=80)
        Label(self.win, text="Economics", font="Aharoni").place(x=20, y=360)
        Label(self.win, text="Performance", font="Aharoni").place(x=500, y=80)
        Label(self.win, text="Miscellaneous ", font="Aharoni").place(x=500, y=360)

        # for criterion in self.criteriaVector:
        for i in range(len(self.criteriaVector)):
            if i == 6:
                attributeNameCoordsY += 70
            if i == 8:
                attributesNameCoordsX = 510
                attributeNameCoordsY = 110
            if i == 15:
                attributeNameCoordsY += 40
            lb = Label(self.win, text=self.criteriaVector[i], font="Ariel")
            lb.place(x=attributesNameCoordsX, y=attributeNameCoordsY)
            cb = Combobox(self.win, values=data, state="readonly")
            cb.place(x=attributesNameCoordsX+260, y=attributeNameCoordsY)
            cb.current(0)
            self.labelDict[self.criteriaVector[i]] = cb
            attributeNameCoordsY += 35
