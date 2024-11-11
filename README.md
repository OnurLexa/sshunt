# SSH Brute Force Aracı | SSH Brute Force Tool

## Bu Python betiği, belirli bir SSH sunucusuna karşı brute-force saldırısı gerçekleştiren basit bir araçtır. Bir şifre listesi (wordlist) kullanarak, belirttiğiniz SSH kullanıcı adı ve IP adresine bağlanmaya çalışır. Başarılı bir bağlantı durumunda, doğru şifreyi bildirir.

Özellikler:

- SSH bağlantıları için şifre denemeleri yapar.
- Paramiko kütüphanesi kullanılarak geliştirilmiştir.
- Kullanıcı adı ve şifre listesi ile hedef sunucuya bağlanmaya çalışır.
- Başarı durumunda doğru şifreyi bildirir.

## Kullanım:
- !Python 3.x ve paramiko kütüphanesinin yüklü olduğundan emin olun.

- !Şifre listesi dosyanızı (passwords.txt) oluşturun ve bu dosyayı script ile aynı klasöre yerleştirin.

- !Host, port ve username bilgilerini script içerisinde düzenleyin.

Aşağıdaki komutla script’i çalıştırın:

![code](https://github.com/user-attachments/assets/50294027-7172-4986-95e5-6da023f76c16)

----------------------------------------------------------------------------------------
# SSH Brute Force Aracı | SSH Brute Force Tool

## This Python script is a simple tool for performing brute-force attacks against a specific SSH server. It attempts to connect to the target SSH server using a username and a password list (wordlist). When a successful connection is made, it reports the correct password.

Features:

- Attempts brute-force SSH login using a password list.
- Developed using the paramiko library.
- Tries to connect to the specified SSH server with a given username and password list.
- Reports the correct password when a connection is successful.

## Usage:
- Ensure Python 3.x and the paramiko library are installed.

- Create a password list (passwords.txt) and place it in the same directory as the script.

- Edit the host, port, and username values in the script.

Run the script with the following command:
![code](https://github.com/user-attachments/assets/50294027-7172-4986-95e5-6da023f76c16)
