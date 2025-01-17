# Program to check if the user has the required permissions
required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

# Check if user_permissions is a subset of required_permissions
has_permissions = required_permissions.issubset(user_permissions)
print(has_permissions)  # Will return False because "execute" is missing.
