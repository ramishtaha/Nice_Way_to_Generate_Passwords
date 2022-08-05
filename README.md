# Nice_Way_to_Generate_Passwords

What most peoples do is they make a list of all the characters manually 
and then use it to generate the password.

This is definitely not they way you should do things when you are Programming in Python.
In this project I would use the power of Python to Generate the above list Automatically.

I used a module named string which gives all the Alphabets and Special Characters,
and a simple List Comprehension to get the numbers.

```
# Getting all the alphabets
characters = list(string.ascii_letters)

# Adding numbers from 0 to 9 to the list
characters.extend(x for x in range(0, 10))

# Adding all the Special Characters
characters.extend(list(string.punctuation))
```
The characters list will look like this:
```
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
```
Now I got the list of the characters I can use a simple for loop to generate the password
```angular2html
size = int(input("Enter the Size of the Password: "))
password = ''
for i in range(size):
    password += str(random.choice(characters))
print(password)
```
Or better use the list comprehension to do all this in one line.
```angular2html
size = int(input("Enter the Size of the Password: "))
password = "".join((random.choice(characters)) for x in range(size))
print(password)
```