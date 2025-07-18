student = {
    "Name" : "Joha",
    "Id"   : "2202124",
    "Dept" : "EEE",
    "Age"  : 22,
    "Section" : 'C'
}

print(student["Id"])

student["Group"] = "C1"      # Add a new key "Group"

del student["Section"]       # Removes the key "Section"

for key in student:                         # Loop through each key
    print(key, ":", student[key])           # Print key and its value

print(student.keys())         # Get all keys -> dict_keys(['Name', 'Id', 'Dept', 'Age', 'Group'])
print(student.values())       # Get all values -> dict_values(['Joha', '2202124', 'EEE', 22, 'C1'])
print(student.items())        # Get key-value pairs -> dict_items([('Name', 'Joha'), ('Id', '2202124'), ('Dept', 'EEE'), ('Age', 22), ('Group', 'C1')])



