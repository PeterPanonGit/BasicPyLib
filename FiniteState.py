# -*- coding: utf-8 -*-
"""
Created on Sun Jul 06 13:49:50 2014

@author: Huapu (Peter) Pan
"""
from basic.PrintableObject import PrintableObject

class FiniteStateClass(PrintableObject):
    """
    FiniteStateClass define the finite states of the class instance
    self.states is a class instance whose attributes are the allowed states
    use set_states(states.state) to change state
    """
    class StatesClass(object):
        pass
    
    def __init__(self, stateList = []):
        self.states = self.StatesClass()
        self.__stateList = stateList
        if (len(stateList) > 0):
            for ii, state in enumerate(stateList):
                setattr(self.states, state, state)
        else:
            raise Exception("stateList length must > 0!")
        self.current_state = ""
            
    def set_state(self, state):
        if (hasattr(self.states, state)):
            self.current_state = state
        else:
            raise Exception("no state named %s exists!" % state)
        
    def availableStates(self):
        print self.__stateList
        
if __name__ == "__main__":
    t = FiniteStateClass(stateList = ['test1', 'test'])
    t.set_state(t.states.test)
    print t.current_state
    t.availableStates()