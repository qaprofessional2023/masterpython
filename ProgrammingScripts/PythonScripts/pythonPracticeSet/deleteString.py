# DELETING STRING in python and confirm its not present

message ="I am a man of 40 years";
del(message);
try:
    message
    print("message still exists");
except NameError:
    print("message is deleted");
 

 