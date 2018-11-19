'''
Created on Oct 30, 2018

@author: joseph.sicree
'''
from datagen.file.file_utils import InputFileReader
from datagen.task.report_task import ReportTask

def main():
    fileReader = InputFileReader("foo")    
    data = fileReader.loadData()

    task = ReportTask(data, 3)
    task.executeTask()

if __name__ == '__main__':
    main()


