
# Underdstand brother read , w right

# f = open("file.txt",'w')
# f.write("Hello Rajan Kushwaha")

# f = open("file.txt",'r')
# print(f.readlines())

# f.close()




#------------------------------------------------------------------

# # Read mode mein file kholi

# L1 = {"name\n","rajan\n","Siwan\n","Bihar\n","Powerful\n"}
# file = open("students.txt", "w")

# file.writelines(L1)

# file.close()  # File hamesha close karni chahiye!




# readlines ek bar mein ek line

# file = open("students.txt", "r")

# # print(file.read())
# line1 = file.readline()
# line2 = file.readline()

# print("Pehli Line:", line1)
# print("Dusri Line:", line1)


# file.close()






# Read All Lines

# f = open("students.txt",'r')

# print(f.readlines()) # List mein bhejta hai

# f.close()



# Use With in filehandling



# with open("students.txt",'w') as f:

#     f.write("I am Rajan\n")
#     f.write("I am Fine \n")
#     f.write("I am Great\n")
#     f.write("I am Fit\n")
#     f.write("I am Nice")