import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    clear_screen()
    print("""
██████╗ ██╗   ██╗     ███████╗████████╗██████╗ 
██╔══██╗╚██╗ ██╔╝     ██╔════╝╚══██╔══╝██╔══██╗
██████╔╝ ╚████╔╝█████╗█████╗     ██║   ██████╔╝
██╔═══╝   ╚██╔╝ ╚════╝██╔══╝     ██║   ██╔═══╝ 
██║        ██║        ██║        ██║   ██║     
╚═╝        ╚═╝        ╚═╝        ╚═╝   ╚═╝ 
    netx421@proton.me   
                                               
    """)
    print("FILE TRANSFER")
    print("----------------------")
    remote_ip = input("Enter remote IP address: ")
    username = input("Enter remote username: ")
    filename = input("Enter filename to transfer: ")
    
    print("\nTransferring file...")
    
    # Use the scp command to transfer the file
    os.system(f"scp {filename} {username}@{remote_ip}:~")
    
    print("\nFile transfer completed!")

if __name__ == "__main__":
    main_menu()

