#multiple assignment

var_1=var_2=var_3 ='sangeet';
print(var_1)
print(var_2)
print(var_3)

#------------------------------------------------------------------

#initalize some variables  and datatypes

var_11 =1.72;
var_12 =0.05;
var_13 =3;
var_14 ="sangeet"

print("data type of",var_11,"=",type(var_11));
print("data type of",var_12,"=",type(var_12));
print("dat type of",var_13,"=",type(var_13));
print("data type of",var_14,"=",type(var_14));

#-------------------------------------------------------

list_1 = [1, 0.5, 'hello', 1+5j, 1.7e2, -12, 'welcome'] # different types of elements  
  
# printing details  
print("Initialized List:", list_1) # printing elements of the list  
print("Data Type:", type(list_1)) # printing data type  

#-------------------------------------------------------------------------------

#arithmetic 
p=7
q=5

print("sum of two numbers : ",p+q);
print("subtract of two numbers :",p,"-",q,"=",p-q);

#------------------------------------------------------------------

#exponent
print("power of 7 square is :",p,"=",p**2);

#---------------------------------------------------------------

p =4+7j;
q =6-2j;
r =3j;

print(p , type(p));
print(q, type(q));
print(r, type(r));

#==============================================================

#Arithmatic Operations on Complex

p =12+8j;
q =4-3j;

print("Real part of p","=",p.real);
print("Imaginary part of p","=",p.imag);

#-------------------------------------------------

p =4+6j
#conjugate of the number
print("conjugate of p is :","=",p.conjugate());

#--------------------------------------------------------------
var_1 =int(7.2);
print(type(var_1));

var_2 =float(8.8);
print(type(var_2));

var_3 =complex(8);
print(type(var_3));


