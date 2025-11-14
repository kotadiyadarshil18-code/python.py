    #Q1
first_name=input("Enter your first name:")
last_name=input("Enter your last name:")

print(f"Hello,{first_name}  {last_name}")

#Q2
item="Apple"
price=5.50
print(f"The price of {item} is {price} dollars")

# Q3

text=input("Enter your name:")
reversed_text=text[::-1]
print("Reversed name",reversed_text)

if(text == reversed_text):
    print("Name is Palindrome ")
else:
    print("Name is not palindromeee")

# Q4

text1=input("Enter your text:")
print("Upper case",text1.upper())
print("Lower case",text1.lower())
print("Title case",text1.title())

# Q5

sentence = "Machine Learning and AI are trending"
pos = sentence.find("AI")
print("Position of 'AI':", pos)

new_sentence = sentence.replace("AI", "Artificial Intelligence")
print("After replacement:", new_sentence)

data_text = "data data mining and big data"
count = data_text.count("data")
print("Count of 'data':", count)

#Q6

fruits = "apple,banana,grapes"
fruit_list = fruits.split(",")
print("List:", fruit_list)


words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print("Joined sentence:", sentence)


multiline = """Python
is
fun"""
lines = multiline.splitlines()
print("Lines:")
for line in lines:
    print(line)

    #Q7

text = "Hello everyone, Welcome to the World"
print("Starts with Hello?", text.startswith("Hello"))
print("Ends with World?", text.endswith("World"))


data = "Data123#Science!"
cleaned = "".join(ch for ch in data if ch.isalpha())
print("Cleaned string:", cleaned)

word = "Python"
print("Reversed:", word[::-1])
