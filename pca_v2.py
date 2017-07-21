#! /usr/bin/python3

#initialization
input_file = open("./input/sampleInput.txt", "r")
config_file = open("config.ini", "r")
config = config_file.readlines()
config_file.close()
target = (config[4].split(" "))[2]
hysteresis = (config[5].split(" "))[2]
debug = (config[6].split(" "))[2]
measurements_window = (config[7].split(" "))[2]
measurements_missing = (config[8].split(" "))[2]

print(target, hysteresis, debug, measurements_missing, measurements_window)
DL = {}
UL = {}

def load_input():
    current_line = input_file.readline()
    current_list = current_line.split('  ')
    x =current_list[4].replace("\n", "")
    del current_list[4]
    current_list.append(x)
    input("press any key > ")
    print(current_list)
    return current_list

def input_validation(current_list):
    #take from basic code
    print(placeholder)

def append_to_dictionary(input_list):
    if input_list[0] == "DL":
        if input_list[2] not in DL.keys():
            DL[input_list[2]] = [input_list[3]]
            print(DL)
        else:
            DL[input_list[2]].append(input_list[3])
            print(DL)
    elif input_list[0] == "UL":
        if input_list[2] not in UL.keys():
            UL[input_list[2]] = [input_list[3]]
            print(UL)
        else:
            UL[input_list[2]].append(input_list[3])
            print(UL)


while True:
    input_list = load_input()
    append_to_dictionary(input_list)
