import tkinter as tk
from tkinter import ttk, messagebox
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


def daily_deal(soup, daily_deal_frame):
    """Displays the daily deal details in the UI."""
    try:
        item_daily = soup.find(class_=item_class).text
        price_daily = soup.find(class_=price_class).text
        early_price_daily = soup.find(class_="sc-812f8453-2 jIIOZg").text

        item_label = ttk.Label(daily_deal_frame, text=f"Item: {item_daily}")
        price_label = ttk.Label(daily_deal_frame, text=f"Price: {price_daily} (Early Price: {early_price_daily})")

        item_label.pack()
        price_label.pack()

        remaining_item = soup.find(class_="sc-d5faaad1-0 dXjKKI")
        if remaining_item:
            remaining = remaining_item.text
            remaining_label = ttk.Label(daily_deal_frame, text=f"Remaining items: {remaining}")
            remaining_label.pack()

        rating = soup.find('span', class_='sc-218358ee-0 XpJns sc-73d58fcc-0 hDhFCu')['aria-label']
        rating_label = ttk.Label(daily_deal_frame, text=f"Rating: {rating}")
        rating_label.pack()

    except Exception as e:
        messagebox.showerror("Error", f"Failed to load daily deal: {e}")


def wishlist(wishlist_frame):
    """Displays the wishlist items details in the UI."""
    for url in wishlist_urls:
        try:
            soup_wishlist = fetch_page_content(url)
            item = soup_wishlist.find(class_="sc-12fcbcc6-0 kHeaGZ").text
            price = soup_wishlist.find(class_="sc-168a3b5-5 dHyqgD").text

            item_label = ttk.Label(wishlist_frame, text=f"Item: {item}")
            price_label = ttk.Label(wishlist_frame, text=f"Price: {price}")

            item_label.pack()
            price_label.pack()

            discount_elem = soup_wishlist.find(class_="sc-b9b85e36-0 sc-354b679-0 cTpMKM coQedg")
            if discount_elem:
                discount = discount_elem.text
                discount_label = ttk.Label(wishlist_frame, text=f"Discount: {discount}")
                discount_label.pack()

            rating_elem = soup_wishlist.find('span',
                                             class_='sc-218358ee-2 sc-218358ee-3 fQaaHM kkXSJO star_stars__LYfBH sc-2119959-1 lhohuw')
            amount_of_rating_elem = soup_wishlist.find('span', class_='sc-2119959-2 haMyov')
            if rating_elem and amount_of_rating_elem:
                rating = rating_elem['aria-label']
                amount_of_rating = amount_of_rating_elem.text
                rating_label = ttk.Label(wishlist_frame, text=f"{rating} in {amount_of_rating} ratings")
                rating_label.pack()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load wishlist item: {e}")


def load_data():
    try:
        daily_deal_soup = fetch_page_content(daily_deal_url)
        daily_deal(daily_deal_soup, daily_deal_frame)
        wishlist(wishlist_frame)
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {e}")


# Setting up the UI
root = tk.Tk()
root.title("Daily Deal and Wishlist")

# Create frames
daily_deal_frame = ttk.Frame(root, padding="10")
wishlist_frame = ttk.Frame(root, padding="10")

daily_deal_frame.pack(side="top", fill="both", expand=True)
wishlist_frame.pack(side="top", fill="both", expand=True)

# Add title labels
daily_deal_title = ttk.Label(daily_deal_frame, text="Daily Deal", font=("Helvetica", 16))
wishlist_title = ttk.Label(wishlist_frame, text="Wishlist", font=("Helvetica", 16))

daily_deal_title.pack()
wishlist_title.pack()

# Load data
load_data()

root.mainloop()
