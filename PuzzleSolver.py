# -*- coding: utf-8 -*-
"""
Introduction to Cog Sci Final Project

@author: Sohan Biswal
"""

import sys

def printer(ipuzzle):
    #print the puzzle
    
    if ipuzzle == None:
        print("Not Possible")
        sys.exit()
    
    for i in range(0,3):
        print(ipuzzle[i], end = "\t", flush=True)
    
    print(flush=True)
    
    for i in range(3,6):
        print(ipuzzle[i], end = "\t", flush=True)

def get_nbers_list(ipuzzle, index):
    #get a list of neighbours from smallest to largest
    nber_list=[]
    if index==0:
        nber_list.append(ipuzzle[1])
        nber_list.append(ipuzzle[3])
    elif index==1:
        nber_list.append(ipuzzle[0])
        nber_list.append(ipuzzle[2])
        nber_list.append(ipuzzle[4])
    elif index==2:
        nber_list.append(ipuzzle[1])
        nber_list.append(ipuzzle[5])
    elif index==3:
        nber_list.append(ipuzzle[0])
        nber_list.append(ipuzzle[4])
    elif index==4:
        nber_list.append(ipuzzle[3])
        nber_list.append(ipuzzle[1])
        nber_list.append(ipuzzle[5])
    elif index==5:
        nber_list.append(ipuzzle[2])
        nber_list.append(ipuzzle[4])
        
    return nber_list

def swap(ipuzzle, i1, i2):
    #swap two values in the list which represents the puzzle
    outpuzzle = ipuzzle.copy()
    store = ipuzzle[i1]
    outpuzzle[i1] = ipuzzle[i2]
    outpuzzle[i2] = store
    return outpuzzle

def list_equal(l1, l2):
    if len(l1)!=len(l2):
        return False
    else:
        for i in range(len(l1)):
            if l1[i]!=l2[i]:
                return False
            
    return True

def check_for_puzzle(ipuzzle, all_states_):
    #checks if this board state has already occured
    if ipuzzle in all_states_:
        return True
    else:
        return False

def solver(puzzle):
    #final state
    correct_state=[1,2,3,4,5,'_']
    #using a set to prevent dealing with duplicates
    checked = set()
    all_possible_states = [puzzle]
    level = 1
    print(flush=True)
    print(flush=True)
    print(flush=True)
    
    #loop through all possible board states and add other possible ones in the loop
    while len(all_possible_states)!=0:
        #check if current board state is the right one
        state = all_possible_states.pop(0)
        if list_equal(list(state), correct_state):
            return state
        
        checked.add(tuple(state))
        
        #get neighbours to the blank spot
        neighbours = get_nbers_list(state, state.index('_'))
        print_lev = True
        for i in range(len(neighbours)):
            #create a board from the neighboring spots of the blank square
            val_index = state.index(neighbours[i])
            blank_index = state.index('_')
            possible_state = swap(list(state), val_index, blank_index)
            
            #add it to the states to check
            if tuple(possible_state) not in checked:
                if print_lev:
                    print("Level: ",level, flush = True)
                    print_lev = False
                all_possible_states.append(possible_state)
                printer(possible_state)
                print(flush=True)
                print(flush=True)
                
        level+=1
    
    #if nothing is found
    return None
    
if __name__ == "__main__":

    #get user input
    file_name=input("Enter the file name:").strip()
    
    puzzle_file = open(file_name, 'r')
    
    contents = puzzle_file.read()
    
    puzzle = contents.split(',')
    
    for i in range(len(puzzle)):
        if puzzle[i] == "_":
            continue
        
        puzzle[i] = int(puzzle[i])
    
    #print Current state of the board
    print("Initial Board State:", flush=True)
    printer(puzzle)
    print(flush=True)
    
    puzzle=tuple(puzzle)
    
    #print the final solved board and how many levels deep it took to solve it
    final=solver(puzzle)
    print("Final: ", flush=True)
    printer(final)