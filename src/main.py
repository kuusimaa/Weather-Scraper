import requests
from bs4 import BeautifulSoup


# Scrapes www.foreca.fi
def scrape_foreca(city):
    forecast = []
    BASE_URL = "https://www.foreca.fi/Finland/"

    res = requests.get(f"{BASE_URL}{city}/10vrk")
    res.encoding = "utf-8"
    print(f"Now scraping: {BASE_URL}{city}/10vrk")

    soup = BeautifulSoup(res.text, "html.parser")
    days = soup.find_all(class_="day")
    for day in days:
        forecast.append({
            "date": day.find("h5").get_text(),
            "weather": day.find(class_="fluid")["title"],
            "max": day.find(class_="tx").get_text(),
            "min": day.find(class_="tn").get_text()
        })
    return forecast


# Prints the forecast.
def print_forecast(forecast):
    for d in forecast:
        print(f"{d['date']} {d['weather']} {d['max']} {d['min']}")


def main():
    city = input("Give the name of the city you want to see forecast on: ")
    forecast = scrape_foreca(city)
    print_forecast(forecast)


if __name__ == "__main__":
    main()
