from cmath import exp
import csv
from ntpath import join
import time
from tkinter import E
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
chrome_options2 = webdriver.ChromeOptions()
chrome_options2.add_argument("window-size=1280,800")
chrome_options2.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options2.add_experimental_option('useAutomationExtension', False)
chrome_options2.headless = True
chrome_options2.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options2.add_argument('--disable-dev-shm-usage')

chrome_options2.add_argument('--disable-blink-features=AutomationControlled')
chrome_options2.add_argument('log-level=3')
chrome_options2.add_argument("--lang=en-GB")
driver=webdriver.Chrome(chrome_options=chrome_options2)
driver.maximize_window()

class cryptoBot():
    

    
    def goToWeb(self):
        
        print("Scraping For Launch Pads, It takes some time...")
        
        with open("launchPads.csv","a+", encoding="utf8", newline='') as file:
            wr=csv.writer(file)
            wr.writerow(("#","Name", "Blockchain","Current ROI","ATH ROI","TGEs","Raise","Entry","Volume (24 hr)","Market Cap"))
            
        driver.get("https://cryptorank.io/fundraising-platforms")
        
        time.sleep(3)
        
        try:
            driver.find_element_by_xpath('//*[@id="root-container"]/div[2]/div/div[3]/button').click()
        except:
            pass
        time.sleep(3)
        
        #self.scrollDown()
        
        numbers=WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'//td[@class="styled__StyledTableCell-sc-1oam7fn-7 esCYLk rank"]')))

        for i in range(0,len(numbers)):
            

            item_list=[]
            for d in range(0,11):
                item_list.append("")
                
            
            #Numbers
            item_list[0]=numbers[i].text
            
            
            #Names
            names=driver.find_elements_by_xpath('//div[@class="styled__BlockchainIconWrapper-sc-1uzf5p4-2 doRYPh"]/following-sibling::span')
            item_list[1]=names[i].text
            
            
            #Blockchain
            bchains=driver.find_elements_by_xpath(f'//tr[@class="styled__StyledTableRow-sc-1oam7fn-5 ftyTMR"][{i+1}]//div[@class="rows__BlockchainIconWrapper-sc-37k85a-2 IkmDN"]/div')
            raw_bchain=''
            for a in bchains:
                if raw_bchain=='':
                    raw_bchain=a.get_attribute("title")
                else:
                    raw_bchain=f"{raw_bchain}, {a.get_attribute('title')}"    
                    
            item_list[2]=raw_bchain
            
            
            #Current ROI
            
            curroi=driver.find_elements_by_xpath('//td[@class="styled__StyledTableCell-sc-1oam7fn-7 rows__TableCellBlockChains-sc-37k85a-0 esCYLk iFAhIq"]/following-sibling::td[1]')
            item_list[3]=curroi[i].text
            
                
            #Ath ROI
            athroi=driver.find_elements_by_xpath('//td[@class="styled__StyledTableCell-sc-1oam7fn-7 esCYLk"][2]')
            item_list[4]=athroi[i].text

            
            #TGEs
            tges=driver.find_elements_by_xpath('//td[@class="styled__StyledTableCell-sc-1oam7fn-7 esCYLk"][3]')
            item_list[5]=tges[i].text
            
            #raise ROI
            raiseraw=driver.find_elements_by_xpath('//td[@class="styled__StyledTableCell-sc-1oam7fn-7 esCYLk"][4]')
            item_list[6]=raiseraw[i].text
            
            #Entry
            entry=driver.find_elements_by_xpath('//td[@class="styled__StyledTableCell-sc-1oam7fn-7 esCYLk"][5]')
            item_list[7]=entry[i].text
            
            #volume
            volume=driver.find_elements_by_xpath('//td[@class="styled__StyledTableCell-sc-1oam7fn-7 esCYLk"][6]')
            item_list[8]=volume[i].text
            
            #market cap
            market=driver.find_elements_by_xpath('//td[@class="styled__StyledTableCell-sc-1oam7fn-7 esCYLk"][7]')
            item_list[9]=market[i].text
            
            item_list[10]=driver.find_elements_by_xpath('//a[@class="table-ido-platform-link__StyledLink-sc-nb8h32-1 efcoKs"]')[i].get_attribute("href")

            with open("launchPads.csv","a+", encoding="utf8", newline='') as file:
                wr=csv.writer(file)

                wr.writerow((item_list[0],item_list[1],item_list[2],item_list[3],item_list[4],item_list[5],item_list[6],item_list[7],item_list[8],item_list[9],item_list[10]))


        
        crypto_links_raw=driver.find_elements_by_xpath('//a[@class="table-ido-platform-link__StyledLink-sc-nb8h32-1 efcoKs"]')
        crypto_links=[]
        for i in crypto_links_raw:
            crypto_links.append(i.get_attribute("href"))
            
        return crypto_links
        


    def goToLinks(self,crypto_links):
        
        print("\n\n\nScraping For DaoMaker...\n\n\n\n")
        
        with open("DaoMaker.csv","a+", encoding="utf8", newline='') as file:
            wr=csv.writer(file)
            wr.writerow(("Name", "Price","Chg 24H","Market Cap","Volume (24hr)","TGE ROI","ATH TGE ROI","Raise by","Total Raise","When","Link","Scraped Place"))
            
        other_links=[]
        for link in crypto_links:
            item_list=[]
            for d in range(0,12):
                item_list.append("")
                
            driver.get(link)
            button_num=1
            try:
                button_num=len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="styled__StyledPagination-sc-1picoj-0 kTegoG"]/button'))))
            except:
                pass
            
            if button_num==1:
                button_num=3
            for i in range(0,button_num-2):
                
                try:
                    driver.find_elements_by_xpath('//div[@class="styled__StyledPagination-sc-1picoj-0 kTegoG"]/button')[i+1].click()
                    time.sleep(12)
                except:
                    pass
                
                
                
                #names=WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'//span[@class="table-coin-link__Name-sc-pprt06-0 euDQYh"]')))
                
                raw=WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'//td[@class="styled__StyledTableCell-sc-1oam7fn-7 esCXeP"]')))
                item_counter=0
                link_counter=0
                for item in raw:

                    if item_counter==0:
                        url=driver.find_elements_by_xpath('//td[@class="styled__StyledTableCell-sc-1oam7fn-7 esCXeP sticky"]/div/a')[link_counter].get_attribute("href")
                        print(url)
                        item_list[item_counter]=driver.find_elements_by_xpath('//span[@class="table-coin-link__Name-sc-pprt06-0 euDQYh"]')[link_counter].text
                        
                        link_counter=link_counter+1
                        item_list[10]=url
                        other_links.append(url)
                        item_counter=item_counter+1
                    print(item.text)
                    item_list[item_counter]=item.text
                    
                    item_counter=item_counter+1
                    
                    item_list[11]=driver.find_element_by_xpath('//h1[@class="name"]').text
                    if item_counter==10:
                        item_counter=0
                        
                        with open("DaoMaker.csv","a+", encoding="utf8", newline='') as file:
                            wr=csv.writer(file)

                            wr.writerow((item_list[0],item_list[1],item_list[2],item_list[3],item_list[4],item_list[5],item_list[6],item_list[7],item_list[8],item_list[9],item_list[10],item_list[11]))
  
        return other_links
                


    def tokens_info(self,other_links):
        
        other_links=list(dict.fromkeys(other_links))
        with open("Tokens.csv","a+", encoding="utf8", newline='') as file:
            wr=csv.writer(file)
            wr.writerow(("Token Name", "Blockchains","Address","Category","Sub Categories","Price","ROI","ATH ROI","Raise","Platform","Website","Funds and Backers","Fund and Backers Websites","Raw Tags"))
            
        for url in other_links:
            item_list=[]
            for d in range(0,14):
                item_list.append("")
                
            driver.get(url)
            time.sleep(2)
            #name
            try:
                item_list[0]=WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH,'//div[@class="app-header__AppHeader-sc-13ssse4-0 hMhNCk coin-info__name"]'))).text
            except:
                continue
            x=0
            try:
                WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'View All')]/.."))).click()
                x=1
                
                
            except:
                raw_tags=driver.find_elements_by_xpath('//a[@class="label__Label-sc-1p5pknx-0 iDFySq"]')
                tags=''
                for tag in raw_tags:
                    if tags=='':
                        tags=tag.text
                    else:
                        tags=f"{tags}, {tag.text}"
                    
                item_list[13]="Token, "+tags
                
            if x==1:
                try:
                    #blockchain
                    blockchain=WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH,"//p[contains(text(),'Blockchains')]/following-sibling::div/a")))
                    bchain=''
                    for chain in blockchain:
                        if bchain=='':
                            bchain=chain.text
                        else:
                            bchain=f"{bchain}, {chain.text}"
                    item_list[1]=bchain
                except:
                    pass
                
                try:    
                    #category
                    category=WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//p[contains(text(),'Category')]/following-sibling::div/a")))
                    cat=''
                    for cate in category:
                        if cat=='':
                            cat=cate.text
                        else:
                            cat=f"{cat}, {cate.text}"
                    item_list[3]=cat
                except:
                    pass
                
                try:
                    #Sub categories
                    sub_category=WebDriverWait(driver, 7).until(EC.presence_of_all_elements_located((By.XPATH,"//span[contains(text(),'Sub-Categories')]/../following-sibling::div/A")))
                    sub_cat=''
                    for sub_cate in sub_category:
                        if sub_cat=='':
                            sub_cat=sub_cate.text
                        else:
                            sub_cat=f"{sub_cat}, {sub_cate.text}"
                    item_list[4]=sub_cat
                except:
                    pass
                try:
                    view_close_button=driver.find_element_by_xpath('//button[@class="styled__CloseButton-sc-i2am3s-4 iAXjIU"]').click()
                except:
                    pass
                ####END OF THE VİEW DETAILS
            
           
            
            #address
            try:
                item_list[2]=driver.find_element_by_xpath('//div[@class="styled__ContainerTokenAddress-sc-hvzfqu-0 ZZSLy"]/a').get_attribute("href").split("/token/")[1]
            except:
                pass
            
            #Go to token sale
            url=driver.find_element_by_xpath("//a[contains(text(),'Token Sale')]").get_attribute("href")
            
            driver.get(url)
            time.sleep(3)
            
            #prices
            try:
                raw_prices=WebDriverWait(driver, 7).until(EC.presence_of_all_elements_located((By.XPATH,"//h4[contains(text(),'Price')]/following-sibling::div/p")))
                price=''
                for i in raw_prices:
                    if price=='':
                        price=i.text
                    else:
                        price=f"{price}, {i.text}"
                item_list[5]=price
            except:
                pass
                
            #self.scrolDown()
            
            #ROI and ath roi
            try:
                raw_roi=WebDriverWait(driver, 7).until(EC.presence_of_all_elements_located((By.XPATH,"//h4[contains(text(),'ROI')]/following-sibling::div/p")))
                roi=''
                ath_roi=''
                a=1
                for i in raw_roi:
                    if a%2==0:
                        if ath_roi=='':
                            ath_roi=i.text
                        else:
                            ath_roi=f"{ath_roi}, {i.text}"
                        a=a+1
                        continue
                    
                    if roi=='':
                        roi=i.text
                    else:
                        roi=f"{roi}, {i.text}"
                        
                    a=a+1
                        
                item_list[6]=roi
                item_list[7]=ath_roi
            except:
                pass
                    
            #raise
            try:
                raw_raise=WebDriverWait(driver, 7).until(EC.presence_of_all_elements_located((By.XPATH,"//h4[contains(text(),'Raise')]/following-sibling::div/p")))
                raise_price=''
                for i in raw_raise:
                    if raise_price=='':
                        raise_price=i.text
                    else:
                        raise_price=f"{raise_price}, {i.text}"
                item_list[8]=raise_price
            except:
                pass
            
            #Platform
            try:
                platform_raw=WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH,'//a[@class="platform-link"]')))
                item_list[9]=platform_raw.text
            except:
                pass
                
                
            #Website
            try:
                item_list[10]=WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH,'//a[@class="platform-link"]'))).get_attribute("href")
            except:
                pass
            
            #show more button
            try:
                driver.find_element_by_xpath('//button[@class="styled__ShowMoreButton-sc-1i7kb4h-2 fIubcM"]').click()
            except:
                pass
            
            
            
            #Fund and backers
            try:
                fun_raw=driver.find_elements_by_xpath('//div[@class="styled__CoinInfoWrapper-sc-c8y8yi-0 dDtDHF"]/span')
                fun=''
                for i in fun_raw:
                    if fun=='':
                        fun=i.text
                    else:
                        fun=f"{fun}, {i.text}"
                item_list[11]=fun
            except:
                pass
                
            #websites
            try:
                website_raw=driver.find_elements_by_xpath('//div[@class="styled__CoinInfoWrapper-sc-c8y8yi-0 dDtDHF"]/span/../..')
                websites=''
                for i in website_raw:
                    if websites=='':
                        websites=i.get_attribute("href")
                    else:
                        websites=f"{websites}, {i.get_attribute('href')}"
                        
                item_list[12]=websites
            except:
                pass
              
            print(" ".join(item_list))      
            with open("Tokens.csv","a+", encoding="utf8", newline='') as file:
                
                wr=csv.writer(file)

                wr.writerow((item_list[0],item_list[1],item_list[2],item_list[3],item_list[4],item_list[5],item_list[6],item_list[7],item_list[8],item_list[9],item_list[10],item_list[11],item_list[12],item_list[13]))

                
             


bot=cryptoBot()


        
crypto_links=bot.goToWeb()

other_links=bot.goToLinks(crypto_links)

bot.tokens_info(other_links)


