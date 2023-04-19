from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

prices = []
websites = ['Worten', 'MediaMarkt', 'NOS', 'Apple']

while True:
    driver.get("https://www.worten.pt/produtos/iphone-14-pro-max-apple-6-7-256-gb-dourado-7644351")
    time.sleep(3)
    worten_element = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div/div[9]/div/div/section/div/div/div[2]/div[1]/div[2]/div/div[1]/span/span/span/span/span/span[2]/span[1]')
    worten_price = worten_element.text.replace("€", "")
    prices.append(float(worten_price))
    print(f'O preço na Worten está a {worten_price}')

    driver.get("https://mediamarkt.pt/products/apple-iphone-14-pro-max-dourado-smartphone-6-7-256gb-a16-bionic")
    time.sleep(3)
    media_element = driver.find_element(By.XPATH, '//*[@id="AddToCartForm"]/div[1]/div[26]/span/div/div[2]')
    media_price = media_element.text.strip().replace("€", "")
    prices.append(float(media_price))
    print(f'O preço na MediaMarkt está a {media_price}')

    driver.get("https://lojaonline.nos.pt/produto/apple-iphone-14-pro-max-5g-256gb-preto-sideral-256gb-48796")
    time.sleep(3)
    NOS_element = driver.find_element(By.XPATH, '//*[@id="one-panel"]/div[1]/div/h3')
    NOS_price = NOS_element.text.strip()
    NOS_price = NOS_price.replace(".", "")
    NOS_price = NOS_price.replace(",", ".")
    NOS_price = NOS_price.split(".")[0]
    prices.append(float(NOS_price))
    print(f'O preço na NOS está a {NOS_price}')

    driver.get('https://www.apple.com/pt/iphone-14-pro/')
    time.sleep(3)
    try:
        apple_element = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/p[1]/span')
        apple_price = apple_element.text.strip().replace("€", "")
        prices.append(float(apple_price))
        print(f'O preço na Apple está a {apple_price}')
    except:
        apple_price = "N/A"
        print(f'O preço na Apple não está disponível')

    lowest_price = min(prices)
    lowest_price_website = websites[prices.index(lowest_price)]
    print(f'O preço mais baixo é: {lowest_price:.of}€ e é na {lowest_price_website}')
    prices.clear()
