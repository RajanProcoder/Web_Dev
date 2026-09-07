# Write in File
# W modes if the file is exist then the content will override
# if the file not Exist . the W modes Create a file and write the code
#--------------------------------------------------------
# f = open("sample.txt",'w')
# f.write("Hello rajan I like You. Your the best")
# f.close()



#------------Multiline String-----------------------

# f = open("sample1.txt",'w')
# f.write("Hello How Are You")
# f.write("\nI am Doing Well In my Life")
# f.write("\nFuck You too")



#-----------ReWrite File-------

# f = open("sample.txt",'w')
# f.write("I Love My self")
# f.write("\nI can Do Everything")
# f.write("\nEnjoy Your Life")
# f.close()


#---------------------------------
# APPNED MODE BROTHER ---------------------------------

# f = open("sample.txt",'a')
# f.write("\nHy I am Great")
# f.write("\nTake care")
# f.close()







#---------------------------------
# LIST PASS FILE HANDLING
# WriteLines write more sen ----------------------------------

# s1 = ["Good\n","Fuck You\n","Great\n","File Management\n","I will Forget Her\n"]

# f = open("hello.txt",'w')
# f.writelines(s1)
# f.close()



#-----------------------------------------------------------------
# Reading From Files ------------------------------------------------------------------

# from pathlib import Path

# base_dir = Path(__file__).resolve().parent
# file_path = base_dir / "hello.txt"

# if not file_path.exists():
#     file_path = base_dir.parent / "hello.txt"

# with file_path.open("r", encoding="utf-8") as f:
#     s = f.read()
#     print(s)



#--------------------------------------------

# readlines use for all line read
# ye Pure file ka data read karega readline

# f = open("sample.txt",'r')

# while True:
#     data = f.readline()

#     if data == '':
#         break
#     else:
#         print(data,end=" ")
# f.close()


