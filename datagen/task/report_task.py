'''
Created on Nov 1, 2018

@author: joseph.sicree
'''
import sched, time
from datetime import datetime
from datagen.domain.datapoint import DataPoint

class ReportTask():
    '''
    classdocs
    '''
    data = []
    s = None
    
    def __init__(self, data):
        '''
        Constructor
        '''
        self.data = data
        
        
        
    def executeTask(self):
        print("Executing task")
        s = sched.scheduler(time.time, time.sleep)
        def do_something(sc): 
            print("Doing stuff...")
            # do your stuff
            s.enter(5, 1, do_something, (sc,))

        s.enter(5, 1, do_something, (s,))
        s.run()
        