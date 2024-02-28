# Defining a Function

# def function_name(param1, param2...)
# if no param required leave empty.
def greet_user(username):
    # """ docstring """
    # describe what the function does.
    # useful for documentation generation.
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

# function call
greet_user('cory')

