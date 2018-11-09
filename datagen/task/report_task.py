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
    interval = 0
        
    def __init__(self, data, interval=0):
        '''
        Constructor
        '''
        self.data = data        
        self.interval = interval
        print("Task interval = ", self.interval)    
        
    def executeTask(self):
        print("Executing task")
        cnt = 0; 
        s = sched.scheduler(time.time, time.sleep)
        def do_something(sc, cnt): 
            
            # do your stuff
            print("[",datetime.now(),"] Temperature:",self.data[cnt].getTemperature())
            if cnt < (len(self.data) - 1):
                cnt = cnt + 1
                s.enter(self.interval, 1, do_something, (sc,cnt))
            else:
                print("Task complete")    

        s.enter(self.interval, 1, do_something, (s,cnt))
#         if not s.empty():
#             print(len(s.queue))
        s.run()
        