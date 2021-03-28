import os, sys
import random

#Path to mouse movements
path = "C:/Users/Omistaja/Desktop/duplicator/movements/"
#All the files that are located in the direcotry
dirs = os.listdir(path)


def get_Length_File(file_path):
    with open(file_path, 'r') as f:
        counter = 0
        length_of_file = len(f.readlines())
        
    return length_of_file

#Loop through the files
for file in dirs:
    #print(file)
    file_path = path + file
    file_to_split = file.strip('.txt')
    splitted = file_to_split.split(',')

    #Getting the x values and y values
    x_first = int(splitted[0])
    y_first = int(splitted[1])
    x_last = int(splitted[2])
    y_last = int(splitted[3])

                
    random_coordinates = random.randint(-5,5)

    new_file_start_x = x_first + random_coordinates
    new_file_start_y = y_first + random_coordinates
    new_file_end_x = x_last + random_coordinates
    new_file_end_y = y_last + random_coordinates

    new_file_name = str(new_file_start_x) + "," + str(new_file_start_y) + "," + str(new_file_end_x) + "," + str(new_file_end_y) + ".txt"
    print(new_file_name)

    if new_file_name in dirs:
        print("new file name already exists -> don't make new movement file")
        pass
    else:
        file_length = get_Length_File(file_path)
        #print(file_length)
        counter = 0
        with open(file_path, 'r') as f:
            for line in f:
                line = line.rstrip()
                #print(line)
                line_split = line.split(',')
                x_value = int(line_split[0])
                y_value = int(line_split[1])

                new_x_value = x_value + random_coordinates
                new_y_value = y_value + random_coordinates
     
                #LETS MAKE A TEXT FILE WITH X AND Y VALUE 1 HIGHER#
                with open(path + new_file_name, 'a') as newfile:
                    ##RANDOMIZING THE MOUSE MOVEMENTS WITH FEW DIFFERENT X AND Y VALUES
                    chance_calculator = random.randint(0,100)
                    ##18 percent chance to have different x and y values
                    #print(chance_calculator)
                    if chance_calculator < 19 and counter > 0 and counter < file_length-1:
                        #Inititate list of values to choose difference of x and y
                        list_of_values = [-2,-1,1,2]
                        #Choose random value between 0,3
                        randomizer_values = random.randint(0,3)
                        #Choose value difference from the list of values using the random value
                        value_randomizer = list_of_values[randomizer_values]
                        #Write the new changed coordinates
                        newfile.write(str(int(new_x_value+value_randomizer)) + "," + str(int(new_y_value+value_randomizer)) + "\n")
                        counter += 1
                    else:      
                        newfile.write(str(new_x_value) + "," + str(new_y_value) + "\n")
                        counter += 1

        #print(counter)
