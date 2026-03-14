#use List
myList = [12, 22, 28, 35, 42, 49, 54, 65, 92, 103, 245, 874] 

#initalize  x  and y  and some values
x= 100;
y =203;

print('Given List :',myList);

if(x not in myList):
    print(x , ': is not present in myList');
if(y in myList):
    print(y,":is in the list");
else:
    print(x, ': is present in the myList');
    print(y,': is not in the list');