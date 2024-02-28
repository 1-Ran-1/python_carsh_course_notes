## Variables
print("---- Variable basic ----")
message = "Hello World!"
print(message)
# Try it yourself
message_2 = "2-1"
print(message_2)
message_2 = '2-N'
print(message_2)

                        ####### Strings #########
# ---------------------------------------------------------------------------- #
    # You can use single'' or double quotes"" 
    # This flexibility allows you to use quotes and apostrophes within strings
# ---------------------------------------------------------------------------- #
## Changing Case in a String with Methods
print("---- Change Case in Stirng ----")
name = "Ada lovelace"
print(name.title())
    # title() method changes each word to title case
print(name.upper())
print(name.lower())
    # lower() method is useful for sorting data
# ---------------------------------------------------------------------------- #
# Using Variables in Strings
print("---- Variables in Strings ----")
first_name = "yuna"
last_name = "tamago"
full_name = f"{first_name} {last_name}"
print(full_name)
    # the letter f is used to insert variables into strings.
print(f"Hello, {full_name.title()}!")
    # use f-string compose a message and assign to a variable
message_3 = f"Hello, {full_name.title()}!"
print(message_3)
# ---------------------------------------------------------------------------- #
# Adding Whitespaces to Strings with Tabs or Newlines
    # whitespaces refers to any # nonprinting characters #
    # spaces, tabs, end-of-line symbols
    # use whitespace to organize output
print("---- Add Whitespaces to String with Tabs or Newlines ----")
print("Python")
print("\tPython")
    # \t add a tab to text
print("Languages:\nPython\nC\nJavaScript")
    # \n add a newline in a string
print("Languages:\n\tPython\n\tC\n\tJavaScript")
    # combine \n\t move to a new line and start with a tab
# ---------------------------------------------------------------------------- #
# Stripping Whitespace
print("---- Stripping Whitespace ----")
favourite_language = '   python   '
print(favourite_language)
print(favourite_language.rstrip() + "(rstrip)")
print(favourite_language.lstrip() + "(lstrip)")
print(favourite_language.strip() + "(strip)")
    # rstrip\lstrip remove whitespaces from the right\left side
    # strip remove whitespaces from both sides
favourite_language = favourite_language.strip()
print(favourite_language)
    # stirp() methods works temporily 
    # assign the value to variable again to renew
# ---------------------------------------------------------------------------- #
# Removing Prefixes
print("---- Removing Prefixes ----")
nostarch_url = "https://nostarch.com"
print(nostarch_url.removeprefix('https://'))
    # variable_name.removeprefix('prefixes')
# ---------------------------------------------------------------------------- #
# Avoiding Syntax Errors with Strings
print("---- Avoiding Syntax Error with Strings ----")
    # Use single and double quotes correctly
message_4 = "One of Python's strengths is its divese community."
print(message_4)
    # double quotes here cannot be replaced by single quotes
    









