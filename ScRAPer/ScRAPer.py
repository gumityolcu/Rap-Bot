from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Scraper():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.i=0
        self.lyrics = []
    def get_songs(self):
        self.driver.get("http://ohhla.com/YFA_eminem.html")
        table = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/table/tbody/tr[2]/td")
        links = table.find_elements_by_tag_name("a")
        count = 0
        while self.i< len(links):
            #print(self.driver.window_handles)
            self.driver.get("http://ohhla.com/YFA_eminem.html")
            table = self.driver.find_element_by_xpath(
                "/html/body/div[2]/div[2]/div[2]/div/table/tbody/tr[2]/td")

            links = table.find_elements_by_tag_name("a")
            #print(len(links))
            #if links[self.i].text!= "BUY NOW!" and "#" not in links[self.i].get_attribute("href"):
            try:
                if ".txt" in links[self.i].get_attribute("href"):#links[self.i].text!= "BUY NOW!" and "#" not in :
                    print(links[self.i].text)
                    links[self.i].click()
                    self.lyrics.append(self.driver.find_element_by_xpath("/html/body/div[4]/pre").text)
                    self.driver.back()
                self.i += 1
            except Exception:
                print(links[self.i])
                self.i += 1

        print(len(self.lyrics))
        f = open("/Users/macbook/Desktop/eminem-lyrics.txt", "w+")
        for m in self.lyrics:
            f.write(m)
        f.close()

bot= Scraper()
bot.get_songs()