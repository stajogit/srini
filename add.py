def birthday_wish(srini):
    message = "Happy birthday, " + srini + "!"
    return message

# Example usage
birthday_person = input("Enter the birthday person's name: ")
wish = birthday_wish(birthday_person)
print(wish)