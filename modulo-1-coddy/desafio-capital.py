def get_capital(country_capitals, country_name):
    country_capitals = country_capitals
    print(country_capitals)
    return country_capitals[country_name]


print(get_capital({"Norway": "Oslo", "Sweden": "Stockho"}, "Norway"))
