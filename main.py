import getpass

# Login credentials
USERNAME = "admin"
PASSWORD = "root"
MASTER_PASSWORD = "1"

def login():
    """User login function"""
    attempts = 3
    while attempts > 0:
        user = input("Enter username: ")
        pwd = getpass.getpass("Enter password: ")
        
        if user == USERNAME and pwd == PASSWORD:
            print("Login successful!\n")
            return True
        else:
            attempts -= 1
            print(f"Invalid credentials. Attempts remaining: {attempts}\n")
    
    print("Login failed. Exiting...")
    return False

def verify_gh_password():
    """Verify GH master password"""
    pwd = getpass.getpass("Enter GH password: ")
    return pwd == MASTER_PASSWORD

def change_network_name():
    """Change network name"""
    if not verify_gh_password():
        print("Wrong GH password!\n")
        return
    
    networks = {
        1: {"name": "Network1", "password": "pass123", "security": "WPA2"},
        2: {"name": "Network2", "password": "pass456", "security": "WPA3"},
        3: {"name": "Network3", "password": "pass789", "security": "WEP"}
    }
    
    print("\n--- Available Networks ---")
    for key, net in networks.items():
        print(f"{key}. Name: {net['name']} | Password: {net['password']} | Security: {net['security']}")
    
    choice = input("\nSelect network to modify (1-3): ")
    
    if choice in networks:
        new_name = input("Enter new network name: ")
        new_pwd = input("Enter new password: ")
        new_security = input("Enter new security type: ")
        
        networks[int(choice)] = {"name": new_name, "password": new_pwd, "security": new_security}
        print(f"Network updated successfully!\n")
    else:
        print("Invalid choice!\n")

def main_menu():
    """Display main menu"""
    print("\n--- Network Management ---")
    print("1. Change Network Name")
    print("2. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    """Main program"""
    if not login():
        return
    
    while True:
        choice = main_menu()
        
        if choice == "1":
            change_network_name()
        elif choice == "2":
            print("Goodbye!")
            networks = {
                1: {"name": "oredoo_4sGH0sy", "password": "pass123", "security": "WPA2", "frequency": "2.4GHz", "channel": 6, "bandwidth": "20MHz"},
                2: {"name": "BEE_WIFI4", "password": "pass456", "security": "WPA3", "frequency": "5GHz", "channel": 36, "bandwidth": "80MHz"},
                3: {"name": "ZAIN_7kL9mP2", "password": "pass789", "security": "WPA2", "frequency": "2.4GHz", "channel": 11, "bandwidth": "20MHz"},
                4: {"name": "VIVA_NetX5Q", "password": "pass321", "security": "WPA3", "frequency": "5GHz", "channel": 149, "bandwidth": "160MHz"},
                5: {"name": "HOME_WiFi_8Qm3", "password": "pass654", "security": "WPA2", "frequency": "2.4GHz", "channel": 1, "bandwidth": "20MHz"}
            }
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()