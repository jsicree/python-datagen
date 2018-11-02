'''
Created on Oct 30, 2018

@author: joseph.sicree
'''
from datetime import datetime

class DataPoint():
    '''
    classdocs
    '''
    __timeStamp = datetime.now()
    __temperature = 0.0


    def __init__(self, timeStamp, temperature):
        '''
        Constructor
        '''
        self.__timeStamp = timeStamp
        self.__temperature = temperature
        
    def getTimeStamp(self):
        return self.__timeStamp
    
    def getTemperature(self):
        return self.__temperature
    
    def __str__(self):
        return "DataPoint [timeStamp = " + self.__timeStamp.__str__() + "; temperature = " + self.__temperature.__str__() + "]"
        
    def __repr__(self):
        return str(self)