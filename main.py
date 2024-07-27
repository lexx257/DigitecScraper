from bs4 import BeautifulSoup
import requests
try:
    dailyDeal = "https://www.digitec.ch/en/daily-deal"
    span = "sc-812f8453-1 fMoCQC"
    spanName = "sc-2e9036-0 cNsIaf sc-66a042f4-11 cQwspH"
    Wishlist = ["https://www.digitec.ch/en/s1/product/logitech-mx-master-3s-wireless-mouse-20987854?ip=logi"]
    soup = BeautifulSoup(requests.get(dailyDeal).content, "html.parser")

    print("Daily Deal:")
    itemDaily = soup.find(class_=spanName).text
    priceDaily = soup.find(class_=span).text
    earlyPriceDaily = soup.find(class_="sc-812f8453-2 jIIOZg").text
    print(f"Item: {itemDaily}, with price: {priceDaily}, {earlyPriceDaily}")
    if soup.find(class_="sc-d5faaad1-0 dXjKKI"):
        remaining = soup.find(class_="sc-d5faaad1-0 dXjKKI").text
        print(f"Remaining items: {remaining}")


    print("Whislist:")
    for item in Wishlist:
        soup = BeautifulSoup(requests.get(item).content, "html.parser")
        item = soup.find(class_="sc-12fcbcc6-0 kHeaGZ").text
        price = soup.find(class_="sc-168a3b5-5 dHyqgD").text
        print(f"Item: {item}, with price: {price}")
        if soup.find(class_="sc-b9b85e36-0 sc-354b679-0 cTpMKM coQedg"):
            discount = soup.find(class_="sc-b9b85e36-0 sc-354b679-0 cTpMKM coQedg").text
            print(f"with discount of: {discount}")
except Exception as e:
    print(f"Error occurred: {e}")



