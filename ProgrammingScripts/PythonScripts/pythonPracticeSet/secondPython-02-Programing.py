#use keyword  for - while

#defining a list
shoppingList =['apple', 'mango','bread','meat','fish','sweet'];
print(shoppingList);

#print items using loop
for item in shoppingList:
    print("print items using for loop: ");
    print(item);

#print item using while loop
print("print while loop");
index = 0
while index<len(shoppingList):
    print(shoppingList[index]);
    index =index+1;
