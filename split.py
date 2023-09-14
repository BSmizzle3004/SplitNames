

Record = "Surname:Smith,Mark:17,Forename:Bob"

seperate = Record.split(',')

last_name = ""
first_name = ""

for i in seperate:
    key, value = i.split(':')
    if key == "Surname":
        last_name = value
    elif key == "Forename":
        first_name = value

full_name = f"{first_name} {last_name}"
print(full_name)
