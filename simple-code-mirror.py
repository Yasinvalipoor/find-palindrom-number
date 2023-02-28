def is_palindrom(string: str):
    if string[::-1]==string:
        return True
    return False

get_input = input("input number to check!!")
if is_palindrom(get_input):
    print("it is palindrom number") 
else:
    print("it is not palindrom number")          
