def formatted_cities_country(country, city, population = None):

    if population:
        formatted_cities = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted_cities = f"{city.title()}, {country.title()}"

    return formatted_cities