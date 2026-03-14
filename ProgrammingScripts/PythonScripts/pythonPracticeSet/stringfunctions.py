#strip  and replace

#strip
str_1 ="I am a young man leaves in Bengaluru from 25 years  ";
print(str_1.strip());

#replace
str_2 = 'I am a young man leaves in Bengaluru from 25 years';
print(str_2.replace('Bengaluru','Cuttack'));

#String Concatenation and repetition

str_3 ='men is here'
str_4 ='big men  : '

new_str =str_3 + str_4
print(new_str);

#repetition
mul_str =new_str*3;
print(mul_str);


#formatting string
first_name ='john';
last_name ='samson';
city_lives ='chennai';
print(f'{first_name}');
print(f'{last_name}');
print(f'{city_lives}');

print(f'{first_name} { last_name} lives in {city_lives}')

#string membership test
str_full_Sentence ='i works in COFORGE as Test Architet';
#in  and #notin
print('coforge' in str_full_Sentence);
print('coforge' not in str_full_Sentence);

#split 
#split the  words  where there is a space 

string_name ='whereare u going';
print(string_name.split());
