pattern = "(\d\d\d)-(\d\d\d)-(\d\d\d\d)"  # Pattern to match phone numbers in the format XXX-XXX-XXXX
new_pattern = r"\1\2\3"  # New pattern to replace dashes with dots
user_input = input("Enter your phone number: ")
new_user_input = re.sub(pattern, new_pattern, user_input) #(pattern, replacement, string)
print("Formatted phone number:", new_user_input)