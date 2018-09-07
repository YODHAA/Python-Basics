name,char=input(" enter the name and character  by comma seperated: ").split(",")
# print(f"the lenght of {name} is {len(name)}")
# print(f" the charcter count is: {name.count(char)}" )
print(name.strip(),char)

#  replace spaces with underscore
s=" how are you?"
print(s.replace(" ","_"))
print(s.find("you"))

print(name.center(len(name)+8,"*"))