import os
address = input("Enter your address:")
file = open("staff.csv","r")
found=False
for line in file:
    staff = line.split(",")
    writefile = open("staffupdated.csv","a")
    if staff[2] == address:
        found=True
        print("Enter the new information for this member of staff")
        firstname = input("Enter their first name: ")
        surname = input("Enter their surname: ")
        address = input("Enter their address: ")
        phoneNumber =input("Enter their number of years teaching: " )
        writefile.write(firstname + "," + surname + "," + address + "," + phoneNumber+"\n") #new line 3
    else:
        writefile.write(staff[0] + "," + staff[1] + "," + staff[2] + "," + staff[3]) #new line 5
    writefile.close()
file.close() 
os.remove("staff.csv")
os.rename("staffupdated.csv","staff.csv")
if found==True:
    print("Details updated")
else:
    print("That staff member's email cannot be found in the file, no changes made")