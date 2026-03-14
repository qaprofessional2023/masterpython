#in and notin  functions in string

given_string ='sangeet kumar samal';
print(f"does 'k' exist in '{given_string}'?",'k' in given_string);
print(f"does 'sangeet' exist in '{given_string}'?", 'sangeet' in given_string);

#------------------------------------------------------------------------------------------

#String swapcase

string_sentence ='''Hi ,i am in London now . 
Amezing weather here . 
Have fun loving day  with full joy . 
Working in Google. Enjoying life.''';

print(str.swapcase(string_sentence));

#====================================================

# string index

text = """Learning Python"""  

index =text.find("Python");
print(f"Index of 'Python': {index}")  
  
  #-------------------------------------------------

  #IS operator
a =[13,26 ,78,90];
b = a;
c =[13,26,78,90];

print("a is b =>",a is b);
print("a is c =>", a is c);
