# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 19:01:54 2014

@author: Huapu (Peter) Pan
"""
import os
import datetime

class SimpleLoggerClass(object):
    def __init__(self, filename):
        """ determine US Eastern time zone depending on EST or EDT """
        if datetime.datetime.now(pytz.timezone('US/Eastern')).tzname() == 'EDT':
            self.USeasternTimeZone = pytz.timezone('Etc/GMT+4')
        elif datetime.datetime.now(pytz.timezone('US/Eastern')).tzname() == 'EST':
            self.USeasternTimeZone = pytz.timezone('Etc/GMT+5')   
        else:
            self.USeasternTimeZone = None
            
        self.filename = filename
        if not os.path.exists('Log'):
            os.makedirs('Log')
        self._log_file = open('Log/' + filename, 'w')
        
    def info(self, msg):
        currentTime = datetime.datetime.now(tz = self.USeasternTimeZone)
        print msg
        self._log_file.write(currentTime + ": " + msg + '\n')
        
    def debug(self, msg):
        currentTime = datetime.datetime.now(tz = self.USeasternTimeZone)
        print msg
        self._log_file.write(currentTime + ": " + msg + '\n')

    def error(self, msg):
        currentTime = datetime.datetime.now(tz = self.USeasternTimeZone)
        print msg
        self._log_file.write(currentTime + ": " + msg + '\n')
        
    def close_log(self):
        self._log_file.close()