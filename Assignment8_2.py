'''
Created on May 28, 2015

    Add to class Project a new method compare(), which receives an object of class Project as an argument and 
    checks whether the attributes of the calling object and the given object are equal and returns the result 
    of comparison as text. Define a list of objects of class Project and use a loop to go through the list and 
    compare them with each other. 
    
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
    
    def compare(self, project):
        text = ''
        if self.name == project.name:
            text += 'name '
        if self.budget == project.budget:
            text += 'budget '
        if self.startDate == project.startDate:
            text += 'startDate '
        if self.endDate == project.endDate:
            text += 'endDate '
        if text == '':
            return 'Nothing is equal!'
        return text + 'are(is) equal.'
    
if __name__ == '__main__':
    projects = []
    projects.append(Project('Management System', '12000', '2015-3-29', '2015-9-1'))
    projects.append(Project('Student System', '12000', '2015-5-19', '2015-9-1'))
    projects.append(Project('Office System', '17000', '2015-3-29', '2015-7-1'))
    
    for i in range(len(projects)):
        for j in range(i + 1, len(projects)):
            print(projects[i].name + ' and ' + projects[j].name + ': ' + projects[i].compare(projects[j]))

            
            
            
            
            
            
            
            
            