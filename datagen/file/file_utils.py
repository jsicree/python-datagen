'''
Created on Oct 30, 2018

@author: joseph.sicree
'''
from datetime import datetime
from datagen.domain.datapoint import DataPoint

class InputFileReader(object):
    '''
    classdocs
    '''
    fileName = None
    
    def __init__(self, fileName):
        '''
        Constructor
        '''
        self.fileName = fileName
        
    def loadData(self):
        print("Loading data from " + self.fileName)
        
        data = []
        
        data.append(DataPoint(datetime(2018,10,30,8,34,25),2.5))
        data.append(DataPoint(datetime(2018,10,30,8,39,27),2.3))
        
        return data
    