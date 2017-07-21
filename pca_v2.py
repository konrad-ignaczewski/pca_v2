#! /usr/bin/python3
#libraries
import re
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
#validation VARIABLES
MS_pattern = re.compile("^MS\d\d\d$")
cell_id_pattern = re.compile('^[NS]\d$')
protocole_pattern = re.compile('^[DU]L$')
signal_pattern = re.compile('^-[456789]\d$')
quality_pattern = re.compile('^$|[012345]')


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
    if (protocole_pattern.match(current_list[0]) and
        cell_id_pattern.match(current_list[1]) and
        MS_pattern.match(current_list[2]) and
        signal_pattern.match(current_list[3]) and
        quality_pattern.match(current_list[4])):
       x = True
    else:
        x = False
    return x

def append_to_dictionary(input_list):
    if input_list[0] == "DL":
        if input_list[2] not in DL.keys():
            DL[input_list[2]] = [input_list[3]]
        else:
            DL[input_list[2]].append(input_list[3])
    elif input_list[0] == "UL":
        if input_list[2] not in UL.keys():
            UL[input_list[2]] = [input_list[3]]
        else:
            UL[input_list[2]].append(input_list[3])



while True:
    input_list = load_input()
    append_to_dictionary(input_list)
    input_validation(input_list)
