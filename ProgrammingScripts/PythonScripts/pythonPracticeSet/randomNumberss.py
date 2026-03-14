
import random
print('random numbers between 5 and 25:',random.randrange(5,25));
print(random.random());

#list 
list_one =[12,14,20,30,67,85];
print(list_one);
# getting random item from list_one  
print("Random Item from the List:", random.choice(list_one));

# shuffling list_one  
random.shuffle(list_one)  
print("Shuffling the List:", list_one);

# printing random element  
print("Printing Random Element:", random.random());

