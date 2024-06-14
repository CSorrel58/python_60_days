def get_title_length(title):
    return len(title)
    
text = input("Enter a title: ")

print(f"Title {text} is {get_title_length(text)} characters long")