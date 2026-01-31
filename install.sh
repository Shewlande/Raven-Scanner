echo "[*] Raven-Scanner Kurulumu Başlatılıyor..."
sleep 1

sudo apt update
sudo apt install python3 python3-pip -y

pip3 install pyfiglet

echo "[+] Kurulum Tamamlandı! 'python3 raven.py' yazarak çalıştırabilirsin."
