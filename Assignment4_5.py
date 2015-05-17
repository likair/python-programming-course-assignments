'''
Created on May 17, 2015

   A program which displays the following list so that name values have 15 places and are left aligned, 
   unit prices have 10 places and are center aligned and amount values have 5 places and are right aligned.  

        Name             Unit Price        Amount
        
        Apple             1.98                150
        
        Orange            0.99                250
        
        Peach             1.99                180
        
        Passion           3.45                235

@author: Likai
'''
lineFormat = "{:<15}{:^10}{:>5}"

print(lineFormat.format('Name', 'Unit Price', 'Amount'))
print(lineFormat.format('Apple', 1.98, 150))
print(lineFormat.format('Orange', 0.99, 250))
print(lineFormat.format('Apple', 1.99, 180))
print(lineFormat.format('Passion', 3.45, 235))
