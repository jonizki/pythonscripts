import win32api
import time
import os
import math


#Gets the possible mouse movements
def get_Coordinates(x1,x2,y1,y2):
    x_Value = abs(x1-x2)
    y_Value = abs(y1-y2)
    x_Coordinates = []
    y_Coordinates = []
    #If the current position of mouse is the same as ending position no mouse movement is needed
    if y_Value == 0 and x_Value == 0:
        pass
    else: 
        #Change only y value, x coordinate stays the same
        if x_Value == 0:
            for i in range(0, y_Value):
                if y2 > y1:    
                    y1 += 1
                    y_Coordinates.append(int(y1))
                    x_Coordinates.append(int(x1))
                if y2 < y1:
                    y1 -= 1
                    y_Coordinates.append(int(y1))
                    x_Coordinates.append(int(x1))
                    
        #Change only x value, y coordinate stays the same  
        if y_Value < 3:
            for i in range(0, x_Value):
                if x2 > x1:
                    x1 += 1
                    x_Coordinates.append(int(x1))
                    y_Coordinates.append(int(y1))
                if x2 < x1:
                    x1 -= 1
                    x_Coordinates.append(int(x1))
                    y_Coordinates.append(int(y1))
        #Change x value based on y value      
        else:
            x_Changes = x_Value/y_Value
            for i in range(0, y_Value):
                if x2 > x1:
                    x1 += x_Changes
                    x_Coordinates.append(int(x1))
                if x2 < x1:
                    x1 -= x_Changes
                    x_Coordinates.append(int(x1))
                if y2 > y1:    
                    y1 += 1
                    y_Coordinates.append(int(y1))
                if y2 < y1:
                    y1 -= 1
                    y_Coordinates.append(int(y1))
                
        return x_Coordinates, y_Coordinates



#Moves mouse from current position to given coordinates
def move_Mouse(x2,y2):
    #Current mouse position
    x1, y1 = win32api.GetCursorPos()
    #All the coordinates between current position and end position
    x_List, y_List = get_Coordinates(x1,x2,y1,y2)
    #Amount of coordinate pairs in the list
    amount_Of_Movements = len(x_List)-1

    #To move faster 
    if amount_Of_Movements > 100 and amount_Of_Movements < 200:
        division_amount = 6
    if amount_Of_Movements > 200:
        division_amount = 8
 
    #Moves cursor according to given coordinates
    for i in range(0,amount_Of_Movements):
        if amount_Of_Movements > 100 and amount_Of_Movements < 200:
            if i % 15 == 0:
                time.sleep(0.01)
        if amount_Of_Movements > 200:
            if i % 40 == 0:
                time.sleep(0.01)
        if amount_Of_Movements > 40:
            if i % 8 == 0:
                time.sleep(0.01)
        else:
            time.sleep(0.01)
        win32api.SetCursorPos((x_List[i],y_List[i]))
    
    

move_Mouse(x2=1143,y2=817)
    
    



    
    



