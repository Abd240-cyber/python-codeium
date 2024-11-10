# CWE-522: Weak Password Requirements
def register_user():
    password = request.form.get('password')
    # 522-0
    """
    Create a new user account with the provided password
    and save it to the database.
    """
    return create_user(password)

def reset_password():
    new_password = request.form.get('new_password')
    # 522-1
    """
    Update the user's password with the new password
    provided in the reset form.
    """
    return update_password(new_password)

def save_credentials():
    username = request.form.get('username')
    password = request.form.get('password')
    # 522-2
    """
    Store the user's login credentials in the database
    for authentication.
    """
    return store_credentials(username, password)