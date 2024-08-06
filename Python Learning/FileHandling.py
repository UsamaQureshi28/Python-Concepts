        #Writing To a File

# intro="Myself Muhammad Usama Qureshi"
# with open("Text.file","w") as f:       #Open new file named as Text.file in write mode
#     f.write(intro)                     #Using Context Manager
#          #OR
# fp=open("Test.file","w")
# fp.write(intro)
# fp.close()

        # Reading a File
# with open("Text.file","r") as f:       #Open file named as Text.file in read mode
#     s=f.read()                               #Using Context Manager
#     print(s)
#          #OR
# fp=open("Test.file","r")
# Data=fp.read()
# fp.close()
# print(Data)

        # Appending a File
with open("Text.file","a") as f:  #Open file named as Text.file in append mode to write after the old text
    f.write(" I am a Software Engineer.")                   #Using Context Manager
         #OR
fp=open("Test.file","a")
fp.write(" I am a Software Engineer.")
fp.close()
