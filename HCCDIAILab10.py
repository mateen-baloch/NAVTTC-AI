# Print vs Return
# def user(Email, Password):
#     return(Email, Password)
# user("admin@gmail.com", "12345") #admin
# print(user("user@gmail.com", "123456")) #user

# def add_numbers(a, b):
#     return a + b  # Calculates the sum and sends it back

# # The value 7 is sent back and stored in 'result'
# result = add_numbers(3, 4) 
# print(result)  # Output: 7

a = 20 #Global
def  data():
     a = 10 #local
     print (a)
data()

print (a) #Global
