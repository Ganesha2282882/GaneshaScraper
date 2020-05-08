import requests as req
print("==~== Ganesha Scraper - A free and open source web scraper. ==~==")
print("=~ Quick Links to copy ~=")
print("http://www.google.com")
print("http://www.microsoft.com")
print("http://www.w3schools.com")
while True:
    print("URL to scrape:")
    url = input()
    r = req.get(url)
    cont = r.content
    print("⚙ Scraping . . . ")
    print("Status Code:", r.status_code)
    print("Writing output 1% . . .", end=" ")
    fobj = open("output", "wb")
    fobj.write(cont)
    fobj.close()
    print("done.")
    print("Thank you for using Ganesha Scraper!")
