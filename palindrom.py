s = "A man, a plan, a canal: Panama"
modified = ""
lst = []
for i in s:
    if i.isalnum():
        a = i.lower()
        modified = modified+a
word = modified.strip()

if word == word[::-1]:
    print(word, "True")

else:
    print(word, "False")

