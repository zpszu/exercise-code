#（函数）

def city(city_name, country_name, population=''):
    if population:
        city_info = city_name.title() + ", " + country_name.title() + ' - ' + \
                    ' population ' + str(population)
    else:
        city_info = city_name.title() + ", " + country_name.title()
    return city_info




(调用）
import unittest
from test import city

class CityTest(unittest.TestCase):

    def test_city_country(self):
        city_information = city('shanghai', 'china')
        self.assertEquals = (city_information,
                             'Shanghai, China')

    def test_city_country_population(self):
        city_information = city('shanghai', 'china', 500000)
        self.assertEquals = (city_information,
                             'Shanghai, China - population 500000')


unittest.main()
