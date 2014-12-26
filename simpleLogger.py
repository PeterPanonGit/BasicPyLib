# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 19:01:54 2014

@author: Huapu (Peter) Pan
"""
import os

class SimpleLoggerClass(object):
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists('Log'):
            os.makedirs('Log')
        self._log_file = open('Log/' + filename, 'w')
        
    def info(self, msg):
        print msg
        self._log_file.write(msg + '\n')
        
    def debug(self, msg):
        print msg
        self._log_file.write(msg + '\n')

    def error(self, msg):
        print msg
        self._log_file.write(msg + '\n')
        
    def close_log(self):
        self._log_file.close()