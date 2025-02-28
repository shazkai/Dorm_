import requests
from bs4 import BeautifulSoup
import telegram
import asyncio

# Your Telegram bot token and chat ID
TELEGRAM_TOKEN = "7653000274:AAFKbBLtcHQLuh5JsoieTKHqyJD1qPBjTus"
CHAT_ID = "7773963333"

# Initialize the Telegram bot
bot = telegram.Bot(token=TELEGRAM_TOKEN)

async def check_listing():
    url = "https://www.stwdo.de/wohnen/aktuelle-wohnangebote"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching the page: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the header element that indicates "Keine Angebote"
    header = soup.find("header", class_="notification__header")
    
    if header and "Keine Angebote" in header.get_text(strip=True):
        print("No offers available.")
    else:
        message = "Notification: Dormitory listing might be available!"
        try:
            await bot.send_message(chat_id=CHAT_ID, text=message)
            print("Notification sent:", message)
        except Exception as e:
            print("Error sending Telegram message:", e)

async def main():
    await check_listing()

if __name__ == "__main__":
    asyncio.run(main())
