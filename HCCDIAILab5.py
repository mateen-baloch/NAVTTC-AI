# a = {
 
#     "Name" : "Shakoor",
#     "ID" : 1
# }

# a["City"] = "Gwadar" #Modify
# a["Name"] = "Ali" # add
# a.update ({"country": "Pakistan", "role" : "developer"})
# a.update ({"Name": "Ilyas", "ID" : "12"}) #For Update multiple Values via dictionary {}
# a.pop ("ID") #remove the key with value
# print (a)

# If Else Conditional Program
# a = "Admin"
# if a == "Admin":
#     Print("True")
# else :
#     Print ("false")

# a = 80
# if a > 50 :
#     print("pass")
# else :
#     print ("fail")

# # Exam Result

# Passing  = 80
# Student_Name = input ("Enter your Name:")
# if Passing > 50 :
#     print("pass")
# else :
#     print ("fail")


a = int (input ("Input your marks:"))

if a > 90 :
    print ("A",a)

elif a > 70 :
     print ("Your Grade is B",a)

elif a > 60 :
     print ("Your Grade is C",a)

else :
     print (" You are Fail",a)