
# EZEL IG HESAP AÇMA TOOL - YASAL & RENKLİ
import webbrowser
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(Fore.RED + Style.BRIGHT + "=" * 60)
    print(Fore.YELLOW + Style.BRIGHT + "           EZEL IG HESAP AÇMA TOOL ✨ (YASAL)")
    print(Fore.RED + Style.BRIGHT + "=" * 60)

def menu():
    print(Fore.CYAN + "1. Hesabım neden kapandı?")
    print(Fore.CYAN + "2. Geri açma formu (resmî)")
    print(Fore.CYAN + "3. Yardım Merkezi")
    print(Fore.CYAN + "4. Çıkış\n")

def neden_kapandi():
    print(Fore.GREEN + "\nInstagram hesapları şu nedenlerle kapatılabilir:")
    print("- Topluluk kurallarının ihlali")
    print("- Telif hakkı ihlali")
    print("- Kimlik doğrulama başarısızlığı")
    print("- Hatalı şikayet sonucu\n")

def form_ac():
    print(Fore.YELLOW + "\nResmî geri açma formu tarayıcıda açılıyor...")
    url = "https://help.instagram.com/contact/606967319425038"
    webbrowser.open(url)

def yardim():
    print(Fore.YELLOW + "\nInstagram Yardım Merkezi açılıyor...")
    webbrowser.open("https://help.instagram.com/")

while True:
    banner()
    menu()
    secim = input(Fore.BLUE + "Bir seçenek seçin (1-4): ")

    if secim == "1":
        neden_kapandi()
    elif secim == "2":
        form_ac()
    elif secim == "3":
        yardim()
    elif secim == "4":
        print(Fore.RED + "Çıkılıyor...")
        break
    else:
        print(Fore.RED + "Geçersiz giriş, tekrar deneyin.\n")
