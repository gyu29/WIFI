import os
import subprocess

def configure_wifi(ssid, password):
    try:
        # Generate WiFi configuration
        config = f"country=US\nssid={ssid}\npsk={password}"
        
        # Write configuration to wpa_supplicant.conf
        with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'w') as f:
            f.write(config)
        
        # Restart networking service
        subprocess.run(['sudo', 'systemctl', 'restart', 'networking'])
        
        print("WiFi configuration successful.")
    except Exception as e:
        print("Error configuring WiFi:", str(e))

def main():
    print("WiFi Connection Setup")
    print("=============================")
    
    # Get WiFi credentials from user
    ssid = input("Enter WiFi SSID: ")
    password = input("Enter WiFi password: ")
    
    configure_wifi(ssid, password)

if __name__ == "__main__":
    main()
