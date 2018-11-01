'''
Created on Oct 30, 2018

@author: joseph.sicree
'''
from datagen.file.file_utils import InputFileReader
from datagen.task.report_task import ReportTask

def main():
    fileReader = InputFileReader("foo")    
    data = fileReader.loadData()
    print(data)    

    task = ReportTask(data)
    #task.executeTask()

if __name__ == '__main__':
    main()


