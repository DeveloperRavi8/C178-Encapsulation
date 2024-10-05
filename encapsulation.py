from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

root = Tk()
root.geometry("800x600")
root.title("Encapsulation")

class Fruit:
    def __init__(self, fruit, quantity):
        self.fruit = fruit
        self.quantity = quantity
        self.__cost = 250

    def __calculateCost(self):
        totalCost = self.quantity * self.__cost
        print("You have to pay " + str(totalCost) + "USD")

        if self.fruit == "Apple":
            calories = 52 * self.quantity
        elif self.fruit == "Mango":
            calories = 60 * self.quantity
        elif self.fruit == "Orange":
            calories = 65 * self.quantity

        print(self.fruit + " x" + str(self.quantity)+ " = " + str(calories))

    def getCost(self):
        self.__calculateCost()


def orderFruit():
    fruit = "Apple"
    quantity = 38
    obj1 = Fruit(fruit, quantity)
    obj1.getCost()


button = Button(root, text="Total Cost", command=orderFruit)
button.place(relx=0.95, rely=0.5, anchor=E)

root.mainloop()