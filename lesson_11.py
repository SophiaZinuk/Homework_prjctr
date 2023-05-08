import requests

res_monobank = requests.get('https://api.monobank.ua/bank/currency')
# print(res_monobank.status_code)
# print(type(res_monobank.status_code))
# print(res_monobank.elapsed)
# print(res_monobank.text)
# print(res_monobank.headers)
# for i in res_monobank.headers:
#     print(i)
# print(res_monobank.json())
# for obj in res_monobank.json():
#     print(f'Object is {obj}, \nType is {type(obj)}', end = '\n\n' )


def cur_mono_fanc():
    currencies = {
        980: '🇺🇦',
        840: '🇺🇸',
        978: "🇪🇺",
    }
    my_rates = []
    for obj in res_monobank.json():
        if obj['currencyCodeA'] in currencies and obj['currencyCodeA'] not in my_rates:
            my_rates.append(obj)

    for obj in my_rates:
        print(
            f"Країна: {currencies[obj['currencyCodeA']]} Купівля {obj['rateBuy']} Продаж: {obj['rateSell']}")


def currencies_privat():
    res_privatbank = requests.get(
        'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
    match res_privatbank.status_code:
        case 200:
            for obj in res_privatbank.json():
                print(
                    f"Country: {obj['ccy']}, Buy: {obj['buy']}, Sale: {obj['sale']}")
        case _:
            print(f'Eror in status code: {res_privatbank.status_code}')

# Practice

# Вивести всіх космонавтів(кількість і імена) http://api.open-notify.org/astros.json


def try_astros():
    astros = requests.get("http://api.open-notify.org/astros.json")
    people = astros.json()['people']
    all_astronauts = 0
    for obj in people:
        print(obj['name'])
        all_astronauts += 1
    print(f'There are now {all_astronauts} astronauts in space')

# Create a program that will ask user to search a word. Search this word in Giphy (use their API). Return links to these GIFs as a result
def giphy_search():
    query = input("Your search query: ")
    link = "api.giphy.com/v1/stickers/search?api_key=0eZR3ldiNCYN17CCClsZYG9co2AiFfxp&q=" + str(query) + "&bundle=sticker_layering"
    giphy_search = requests.get("https://" + link)
    try:
        match giphy_search.status_code:
            case 200:
                giphy_search0 = giphy_search.json()
                print(giphy_search0["data"][0]["url"])
            case _:
                print(f'Eror in status code: {giphy_search.status_code}')
    except Exception as ex:
        print("Something goes wrong... \nTry another data.", ex)


# Взяти API-weather, розпарсити і вивезти погоду від користувача
# (вводить локацію, по цій локації повернеться погода, вологість і тд) https://openweathermap.org


def get_weather_now():
    city = input("Enter your city: ")
    city = city.strip()
    city = city.capitalize()

    link = "https://api.openweathermap.org/data/2.5/weather?q=" + \
    str(city) + "&APPID=17bca265e627a17f9bbfe31c9e698730"

    res0 = requests.get(f"{link}")
    match res0.status_code:
        case 404:
            print('Page not found. \nTry another data.')
        case 200:
            result = res0.json()
            print(f"The weather is {result['weather'][0]['main']}, \nTemperature: {round(result['main']['temp'] - 273.15, 2)}, feels like {round(result['main']['feels_like'] - 273.15, 2)}; \nWind speed: {result['wind']['speed']}")
        case _:
            print('Something goes wrong... \nTry another data.')



