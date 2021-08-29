#  Author: Muhammed Mahdi
#  I hope this can help you ;)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service
import argparse

def main():

    banner = '''\33[1m\033[91m
 ██▓███   ██▀███   ▒█████  ▄▄▄█████▓ ▒█████  
▓██░  ██▒▓██ ▒ ██▒▒██▒  ██▒▓  ██▒ ▓▒▒██▒  ██▒
▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒▒ ▓██░ ▒░▒██░  ██▒
▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░░ ▓██▓ ░ ▒██   ██░
▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░  ▒██▒ ░ ░ ████▓▒░
▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░   ▒ ░░   ░ ▒░▒░▒░ 
░▒ ░       ░▒ ░ ▒░  ░ ▒ ▒░     ░      ░ ▒ ▒░ 
░░         ░░   ░ ░ ░ ░ ▒    ░      ░ ░ ░ ▒  
            ░         ░ ░               ░ ░  
'''
    print(banner)
    print("Coded By Muhammed Mahdi - @muh3ammed\33[0m")

    parser = argparse.ArgumentParser(description="A fast tool to scan prototype pollution vulnerability")
    parser.add_argument("-l" ,"--list" , help = "URL list [ex : domains.txt ]" , required=True)
    args = parser.parse_args()

    chrome_path = "/home/kali/.wdm/drivers/chromedriver/linux64/92.0.4515.107/chromedriver"
    service = Service(chrome_path)

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"

    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument(f"user-agent={user_agent}")

    driver = webdriver.Chrome(service=service, options=options)

    with open(args.list,"r") as url_list:

        urls = url_list.read().splitlines()

    payload = "?__proto__[test]=vuln"
    payload2 = "&__proto__[test]=vuln"

    for url in urls:
        
        if "=" not in url:
        
            try:
          
                driver.get(f"{url}{payload}")
                
            
            except:continue

        else:

            try:
 
                driver.get(f"{url}{payload2}")
                

            except:continue
        try:
            js = driver.execute_script("return window.test;")
        except:pass
    	
        if js == "vuln":
        
            print(f"\n\33[1m{url}{payload} > \033[91mVulnerable\33[0m") if "=" not in url else print(f"\n\33[1m{url}{payload2} > \033[91mVulnerable\33[0m") 
    
        else:
            
            print(f"\n\33[1m{url}{payload} > \33[32mNot Vulnerable\33[0m") if "=" not in url else print(f"\n\33[1m{url}{payload2} > \33[32mNot Vulnerable\33[0m") 

    driver.close()

if __name__ == "__main__":

    main()