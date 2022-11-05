import random
import tkinter as TK
import turtle
import time



def main():
    tr = turtle.Turtle()
    tr.ht()
    tr.speed(0)
    dictionary = {}
    while True:
        option = menu()
        if option == "4":
            tr.clear()
        elif option == "3":
            break
        elif option =="2":
            time.sleep(1)
            drawPicture(dictionary, tr)
        elif option == "1":
            color = (random.randint(0,255)/255,random.randint(0,255)/255,random.randint(0,255)/255)
            text = input("what is the csv: ")
            text = text.split(", ")
            if "" in text:
                text.remove("")
            for square in text:
                if '-' in square:
                    ind = int(square.index('-'))
                    for i in range(int(square[1:ind]), int(square[ind+1:])+1):
                        dictionary[square[0] + str(i)] = color
                else:
                    dictionary[square] = color
    turtle.done()
    print(f"There was {len(dictionary)} objects in the dictionary")

def drawPicture(dict, tr):
    keys = list(dict.keys())
    random.shuffle((keys))
    homeX = -250
    homeY = -250
    tr.speed(0)
    tr.penup()
    for key in keys:
        tr.color(dict[key])
        letter = key
        xOffset = (ord(letter[0]) - 65) * 25
        yOffset = int(letter[1:]) * 25
        tr.penup()
        tr.goto(homeX + xOffset, homeY + yOffset)
        tr.pendown()
        tr.begin_fill()
        drawRectangle(tr)
        tr.end_fill()


def drawRectangle(tr):
    for i in range(4):
        tr.forward(25)
        tr.left(90)
    tr.seth(0)

def menu():
    return input("""Would you like to 
    (1) add another color
    (2) draw the data
    (3) be done
    (4) CLEAR
    """)


if __name__ == "__main__":
    main()