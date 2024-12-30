course = 'Python course for "Beginners"'
name = 'Jennifer'
names = ["Iago", "Evair", "Hamed", "Mirian"]
message = '''
Hi John,

It's my first email to you.

Thanks,
Support team
'''

print(course)
print(message)
print("Print a string between the 0 until 3 word, excluding the letter in 3º position ", course[0:3])
print("Print all sentence ", course[0:])
print("Print all sentence ", course[:])
print("Pytho for this: "+ course[:5])
print("ennifer for this: " + name[1:-1])
names[2] = "Panjeh"
print("Listas permitem a substituição de itens: ", names)