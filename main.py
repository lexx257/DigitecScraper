from bs4 import BeautifulSoup
import requests
dailyDeal = "https://www.digitec.ch/en/daily-deal"
span = "sc-812f8453-1 fMoCQC"
spanName = "sc-2e9036-0 cNsIaf sc-66a042f4-11 cQwspH"

soup = BeautifulSoup(requests.get(dailyDeal).content, "html.parser")

print("Daily Deal:")
print(soup.find(class_=spanName).text)
print(soup.find(class_=span).text)

print("Whislist:")


#soup.find(class_="sc-168a3b5-5 dHyqgD")
#print(soup.find(class_="sc-168a3b5-5 dHyqgD").text)
#print(soup.find(class_="sc-12fcbcc6-0 kHeaGZ").text)
