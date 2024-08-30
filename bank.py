import os,sys,time,os,json,requests
import colorama
from colorama import Fore,Back,init
from urllib import request
from requests import get,post

import locale

localtime=time.asctime(time.localtime(time.time()))
ip=requests.get('https://api.ipify.org').text

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

hijau="\033[1;92m "
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="\033[1;91m"
biru="\033[1;96m"



def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


def show_balance(balance):
    time.sleep(1.5)
    
    print("******************************************")
    print(f"Saldo kamu saat ini adalah Rp.{balance:.2f}")
    print("******************************************")
    

def deposit():
    
    os.system("clear")
    print("******************************************")
    
    amount = float(input("Silahkan masukkan jumlah deposit : "))
    time.sleep(1.5)
    os.system("clear")
    
    autoketik ("=================please wait=================>>>")
    time.sleep(2)
    os.system("clear")
    #autoketik("sedang memproses...")
    
    if amount < 0:
        print("*********************")
        print("Jumlah yang di masukkan tidak valid!")
        print("*********************")
        return 0
    
    #elif amount > 0:
        print("")
    
    else:
        return amount
    
    
    
        
        

def withdraw(balance):
    
    time.sleep(1.5)
    os.system("clear")
    amount = float(input("Silahkan masukkan jumlah yg ingin di withdraw : "))
    os.system("clear")
    time.sleep(2)
    autoketik ("=================please wait=================>>>")
    time.sleep(2)
    os.system("clear")
    
    
    

    if amount > balance:
        print("**************************************************")
        autoketik("Saldo anda tidak cukup untuk melakukan withdraw...")
        #print("**************************************************")
        time.sleep(1.5)
        os.system("clear")
        
        return 0
    elif amount < 0:
        print("**************************************************")
        print("jumlah tidak boleh kurang dari 0")
        print("**************************************************")
        return 0
        
    else:
        return amount
    
    
        

def main():
    
    balance = 0
    is_running = True
    

    while is_running:
        
        print(f"""

{putih}[{B}•{putih}] {biru}Developer{hijau}: MarshallSetian
{putih}[{B}•{putih}] {ungu}Instagram {putih}: @marshall_setian
{W}[{B}•{W}] Ip Kamu {putih}  :{Y} {ip}
{W}[{B}•{W}] Waktu/Jam {putih}:{merah} {localtime}""")
       
        print("\n")
        print(f"{putih}*********************")
        print("Program Bank Marshall")
        print("*********************")
        print("1.Cek Saldo :")
        print("2.Deposit :")
        print("3.Withdraw :")
        print("4.Exit")
        print("*********************")
        choice = input("silahkan masukkan pilihan dengan angka (1-4): ")
        
      
        if choice == '1':
            time.sleep(1.5)
            os.system("clear")
            autoketik("sedang memproses...")
   
            
            time.sleep(1)
            os.system("clear")
            show_balance(balance)
            time.sleep(3.5)
            os.system("clear")
            
        elif choice == '2':
            #time.sleep(1)
            #os.system("clear")
            
            balance += deposit()
            
            #time.sleep(5)
            #os.system("clear")
            
            #print("deposit sukses!")
            
           # time.sleep(3)
           # os.system("clear")
            
            
            
        elif choice == '3':
            balance -= withdraw(balance)
            #time.sleep(3)
            #os.system("clear")
            
            
            #time.sleep(3)
            #os.system("clear")
        
        
            
            
            
            
        elif choice == '4':
            is_running = False
        else:
            print("*********************")
            print("input yang anda masukkan tidak valid!")
            
    time.sleep(1.5)
    os.system("clear")
    print("*******************************************")
    autoketik("Terima kasih semoga hari anda menyenangkan!")
    
    

if __name__ == '__main__':
    main()
