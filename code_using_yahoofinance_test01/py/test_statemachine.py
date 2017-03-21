# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 16:15:24 2015

@author: justin.malinchak
"""
import statemachine
import re
class MyState(statemachine.State):
    patterns = {'atransition': r'pattern'}
    initial_transitions = ['atransition']
    def atransition(self, match, context, next_state):
        # do something
        result = ['a','b']  # a list
        return context, next_state, result

sm = statemachine.StateMachine(state_classes=[MyState],
             initial_state='MyState')

input_string = open('cov1.csv').read()
input_lines = statemachine.string2lines(input_string)
print input_lines
results = sm.run(input_lines)
sm.unlink()
# context, next_state may be altered
