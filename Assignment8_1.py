'''
Created on May 28, 2015

    A program in which you define a class called Project, which has the following attributes: name, budget, start date and end date. 
    Define the constructor and the following methods for the class:
    - getInfo(), which returns the object information as text,  
    - search(), which receives a name as argument and then compares the given name with the name of the project and returns either the 
       project information or informs that the project with given name was not found.  
    - update(), which receives the name and budget as arguments and updates the project budget if the given name and the name of the 
       project are the same.  
    Define some objects of the class Project and call the methods to test that the methods are working correctly.
    
@author: Likai
'''

class Project():
    def __init__(self, name, budget, startDate, endDate):
        self.name = name
        self.budget = budget
        self.startDate = startDate
        self.endDate = endDate
        
    def getInfo(self):
        return 'name: {}, budget: {}, start date: {}, end date: {}'.format(self.name, self.budget, self.startDate, self.endDate)
        
    def search(self, name):
        if name == self.name:
            return self.getInfo()
        else:
            return 'Given name was not found!'
    
    def update(self, name, budget):
        if name == self.name:
            self.budget = budget

if __name__ == '__main__':    
    project = Project('Management System', '10000', '2015-5-29', '2015-9-1')
    print(project.getInfo())
    print(project.search('Management System'))
    print(project.search('Bank System'))
    project.update('Management System', '12000')
    print(project.getInfo())
            
