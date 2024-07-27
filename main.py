from bs4 import BeautifulSoup
import requests

# URLs and class names
daily_deal_url = "https://www.digitec.ch/en/daily-deal"
price_class = "sc-812f8453-1 fMoCQC"
item_class = "sc-2e9036-0 cNsIaf sc-66a042f4-11 cQwspH"
wishlist_urls = [
    "https://www.digitec.ch/en/s1/product/logitech-mx-master-3s-wireless-mouse-20987854?ip=logi",
    "https://www.digitec.ch/en/s1/product/apple-airpods-pro-2nd-gen-magsafe-usb-c-anc-6-h-wireless-headphones-38610474"
]


def fetch_page_content(url):
    """Fetches and parses the HTML content of the given URL."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return BeautifulSoup(response.content, "html.parser")


def daily_deal(soup):
    """Prints the daily deal details."""
    print("Daily Deal:")
    item_daily = soup.find(class_=item_class).text
    price_daily = soup.find(class_=price_class).text
    early_price_daily = soup.find(class_="sc-812f8453-2 jIIOZg").text
    print(f"Item: {item_daily}, with price: {price_daily}, {early_price_daily}")

    remaining_item = soup.find(class_="sc-d5faaad1-0 dXjKKI")
    if remaining_item:
        remaining = remaining_item.text
        print(f"Remaining items: {remaining}")

    rating = soup.find('span', class_='sc-218358ee-0 XpJns sc-73d58fcc-0 hDhFCu')['aria-label']
    print(f"Rating: {rating}")


def wishlist():
    """Prints the details of items in the wishlist."""
    print("Wishlist:")
    for url in wishlist_urls:
        soup_wishlist = fetch_page_content(url)
        item = soup_wishlist.find(class_="sc-12fcbcc6-0 kHeaGZ").text
        price = soup_wishlist.find(class_="sc-168a3b5-5 dHyqgD").text
        print(f"\nItem: {item}, with price: {price}")

        discount_elem = soup_wishlist.find(class_="sc-b9b85e36-0 sc-354b679-0 cTpMKM coQedg")
        if discount_elem:
            discount = discount_elem.text
            print(f"with discount of: {discount}")

        rating_elem = soup_wishlist.find('span',
                                         class_='sc-218358ee-2 sc-218358ee-3 fQaaHM kkXSJO star_stars__LYfBH sc-2119959-1 lhohuw')
        amount_of_rating_elem = soup_wishlist.find('span', class_='sc-2119959-2 haMyov')
        if rating_elem and amount_of_rating_elem:
            rating = rating_elem['aria-label']
            amount_of_rating = amount_of_rating_elem.text
            print(f"{rating} in {amount_of_rating} ratings")


def main():
    try:
        daily_deal_soup = fetch_page_content(daily_deal_url)
        daily_deal(daily_deal_soup)
        print()
        wishlist()
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
