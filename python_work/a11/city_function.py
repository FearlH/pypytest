def city_name(city,country,populaton=""):
    city=city.title()
    country=country.title()
    if populaton:    
        city_name=f"{city},{country} - population {populaton}"
    else:
        city_name=f"{city},{country}"

    return city_name
