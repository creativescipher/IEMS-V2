from services.auth_service import AuthService

username = input("Username: ")
password = input("Password: ")

if AuthService.login(username, password):
    print("\n✅ Login successful!")

else:
    print("\n❌ Login failed.")