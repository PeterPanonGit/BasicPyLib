# -*- coding: utf-8 -*-
"""
Created on Sun Jul 06 13:49:50 2014

@author: Huapu (Peter) Pan
"""
from basic.PrintableObject import PrintableObject

class EnumClass(PrintableObject):
    """
    EnumClass is a class that mimic the behavior of enum in C++
    There can be only one True state at a time
    default state is the first state
    """
    def __init__(self, stateList = []):
        if (len(stateList) > 0):
            for ii, state in enumerate(stateList):
                if (ii == 0):
                    setattr(self, state, True)
                elif (ii > 0):
                    setattr(self, state, False)
        else:
            raise Exception("Enum stateList length must > 0!")
            
    def set_state(self, state):
        if (hasattr(self, state)):
            for var in vars(self):
                # set everything to false at first
                setattr(self, var, False)
            setattr(self, state, True)
        else:
            raise Exception("no state named %s exists!" % state)
            
    def current_state(self):
        for ii, state in enumerate(self.__dict__):
            if (getattr(self, state)):
                return state
                
    def print_obj(self):
        print 'Enum state: ', self.current_state()
        
if __name__ == "__main__":
    t = EnumClass(stateList = ['test1', 'test'])
    t.set_state('test')
    print t.__dict__
    t.print_obj()