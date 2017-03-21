# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 14:55:22 2015

@author: justin.malinchak
"""
import numpy as np
import pandas as pd


def reveal_and_switch(win_door,first_pick):
    '''Create arrays for the door to be revealed by the host and the switch door'''
    #Take in arrays for the winning door and the contestant's first pick
    doors = [1,2,3]
    switch_door = np.array([0]*len(win_door))
    for i in range(len(switch_door)):
        if first_pick[i] != win_door[i]:
            switch_door[i] = win_door[i]
        else:
            del doors[np.searchsorted(doors,first_pick[i])]
            switch_door[i] = np.random.choice(doors)

    #print switch_door
    return switch_door


def create_doors(iterations):
    '''Create a DataFrame with columns representing the winning doors,
    the picked doors and the doors picked if the player switches and the
    accumulating probabilities'''
    win_door = np.random.random_integers(1,3,iterations)
    first_pick = np.random.random_integers(1,3,iterations)
    switch_door = reveal_and_switch(win_door,first_pick)
    #allocate memory for 
    denom = np.array([0]*len(win_door))
    first_win = np.array([0]*len(win_door))
    switch_win = np.array([0]*len(win_door))
    switch_prob = np.array([0]*len(win_door))
    stay_prob = np.array([0]*len(win_door))
    
    #print range(switch_door)

    for i in switch_door:
        denom[i] = i + 1
        if switch_door[i] == win_door[i]:
            switch_win[i] = 1
            first_win[i] = 0
        elif first_pick[i] == win_door[i]:
            switch_win[i] = 0
            first_win[i] = 1



    switch_prob = np.cumsum(switch_win)/denom
    stay_prob = np.cumsum(first_win)/denom
    df = pd.DataFrame({'iterations': iterations,
                     'Stubborn Win': first_win,
                     'Switch Win': switch_win,
                     'stubborn probability': stay_prob,
                     'switch probability': switch_prob})
    print df
    return df
    
if __name__=='__main__':
    df = create_doors(5)
    print df
    print 'there was no method from library mydata chosen'