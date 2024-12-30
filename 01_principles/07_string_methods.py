# Length
name = "Mirian Quispe Montevilla"
print("String length: " + str(len(name)))

# Upper and Lower
# Does not modify the original string 
print("Upper name: " + name.upper())
print("Lower name: " + name.lower())

# Find
# Print index 7
print(name.find("Quispe"))
# Print index 14 for M position
print(name.find("Montevilla"))

# In: returns Boolean value
print("qusipe" in name) # False
print("Quispe" in name) # True

