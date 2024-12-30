person = {
    "name": "Mirian Quispe",
    "age": 25,
    "address": "Ruas das Oliveiras, 450"
}
# Dictionary should have unique keys

person["name"] = "Marina Quispe"

# Display an error
# print(person["birth_date"])

# Not display errror, if the property not exists return None
print(person.get("birth_date", "15 may 1997"))

