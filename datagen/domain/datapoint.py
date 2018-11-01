'''
Created on Oct 30, 2018

@author: joseph.sicree
'''
from datetime import datetime

class DataPoint():
    '''
    classdocs
    '''
    timeStamp = datetime.now()
    temperature = 0.0


    def __init__(self, timeStamp, temperature):
        '''
        Constructor
        '''
        self.timeStamp = timeStamp
        self.temperature = temperature
        
    def getTimeStamp(self):
        return self.timeStamp
    
    def getTemperature(self):
        return self.temperature
    
    def __str__(self):
        return "DataPoint [timeStamp = " + self.timeStamp.__str__() + "; temperature = " + self.temperature.__str__() + "]"
        
    def __repr__(self):
        return str(self)