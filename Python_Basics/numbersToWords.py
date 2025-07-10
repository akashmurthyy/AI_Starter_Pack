number = input("Enter the number ")
numbermap = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
output = ""
for item in number:
    output+=numbermap.get(item) + " "
print(output)