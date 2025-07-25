import streamlit as st
from bs4 import BeautifulSoup
import requests
import smtplib

# ====== EMAIL CREDENTIALS (⚠️ KEEP PRIVATE) ======
EMAIL_ADDRESS = ""
EMAIL_PASSWORD = ""
SMTP_ADDRESS = ""

# ====== Streamlit UI ======
st.title("📦 Amazon Price Tracker (India Accurate)")

url = st.text_input("Enter Amazon Product URL:")
target_price = st.number_input("Notify me if price drops below:", min_value=1.0, step=0.5)
track_btn = st.button("Track Price")

if track_btn and url:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
        ),
        "Accept-Language": "en-IN,en;q=0.9"
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract title
        title_tag = soup.find(id="productTitle")
        if not title_tag:
            st.error("❌ Product title not found.")
            st.stop()
        title = title_tag.get_text().strip()

        # Try all known ID/class selectors for actual price
        price_selectors = [
            {"id": "priceblock_dealprice"},
            {"id": "priceblock_ourprice"},
            {"id": "priceblock_saleprice"},
            {"class_": "a-price-whole"},
        ]

        price_as_float = None
        for sel in price_selectors:
            price_tag = soup.find(**sel)
            if price_tag:
                try:
                    price_text = price_tag.get_text().strip()
                    price_as_float = float(price_text.replace("₹", "").replace(",", ""))
                    break
                except:
                    continue

        # If still not found, fallback: try all a-offscreen spans inside buy box
        if price_as_float is None:
            buybox = soup.find(id="corePriceDisplay_desktop_feature_div") or soup
            for tag in buybox.find_all("span", class_="a-offscreen"):
                try:
                    price_text = tag.get_text().strip()
                    price_as_float = float(price_text.replace("₹", "").replace(",", ""))
                    break
                except:
                    continue

        if price_as_float is None:
            st.error("❌ Could not find the current price.")
            st.stop()

        st.subheader(f"📘 {title}")
        st.write(f"💰 Current Price: **₹{price_as_float}**")

        # Send email if price drops
        if price_as_float < target_price:
            message = f"{title} is now available for ₹{price_as_float}!\n{url}"

            with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
                connection.starttls()
                connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL_ADDRESS,
                    to_addrs=EMAIL_ADDRESS,
                    msg=f"Subject:Amazon Price Alert!\n\n{message}".encode("utf-8")
                )

            st.success("✅ Email sent! Product is below your target price.")
        else:
            st.info("ℹ️ Product is still above your target price.")

    except Exception as e:
        st.error(f"❌ Error occurred: {e}")
