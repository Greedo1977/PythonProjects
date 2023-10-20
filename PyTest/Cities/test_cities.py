from CitiesCountry import formatted_cities_country


def test_city_country_with_pop():
    formatted = formatted_cities_country('chile', 'santiago', 5_000_000)
    assert formatted == 'Santiago, Chile - population 5000000'


def test_city_country_no_pop():
    formatted = formatted_cities_country('chile', 'santiago')
    assert formatted == 'Santiago, Chile'


