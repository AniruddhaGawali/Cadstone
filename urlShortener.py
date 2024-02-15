import pyshorteners

long_url = input("Enter the URL to shorten:")

type_tiny = pyshorteners.Shortener()

short_url = type_tiny.tinyurl.short(long_url)

print(f"The short URL is: {short_url}")