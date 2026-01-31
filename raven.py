import socket
from datetime import datetime

def scan():
    print("-" * 50)
    target = input("Hedef IP veya Domain: ")
    print(f"Tarama başlatıldı: {target}")
    print("Zaman: " + str(datetime.now()))
    print("-" * 50)

    try:
        # En yaygın 10 portu kontrol edelim
        for port in [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port}: AÇIK")
            s.close()
    except:
        print("\n Durduruldu.")

if __name__ == "__main__":
    scan()
