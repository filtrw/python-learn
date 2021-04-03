from unittest import mock
import pytest
from api import API_URL, WeatherApi, Weather


@pytest.fixture
def weather_api():
    with mock.patch.object(WeatherApi, "fetch_weather") as mocked_fetch_weather:
        api = WeatherApi(API_URL)
        yield api


@pytest.fixture
def weather(weather_api):
    weather = Weather(api=weather_api)
    return weather


@pytest.fixture(params=["Moscow", "NYC", "Voronezh"])
def city(request):
    return request.param


class TestWeather:

    # @mock.patch.object(WeatherApi, "fetch_weather")
    # def test_get_temperature(self, mocked_fetch_weather):
    def test_get_temperature(self, weather_api, weather, city):
        weather_api.fetch_weather.return_value = {"temperature": 12}
        res = weather.get_temperature(city)
        assert isinstance(res, int)
        weather_api.fetch_weather.assert_called()
        weather_api.fetch_weather.assert_called_once()
        weather_api.fetch_weather.assert_called_once_with(city=city)

    # def test_get_temperature(self, weather_api):
    #     print(weather_api.fetch_weather())
    #     #mocked_fetch_weather.return_value = {"temperature": 12}
    #     weather_api.fetch_weather.return_value = {"temperature": 12}
    #     weather = Weather(api=weather_api)
    #     res = weather.get_temperature("Moscow")
    #     assert isinstance(res, int)

    # def test_get_humidity(self, mocked_fetch_weather):
    #     mocked_fetch_weather.return_value = {"humidity": 40.0}
    #     api = WeatherApi(API_URL)
    #     weather = Weather(api=api)
    #     res = weather.get_humidity("Moscow")
    #     assert isinstance(res, float)

    def test_get_humidity(self, weather_api, city):
        print(weather_api.fetch_weather())
        weather_api.fetch_weather.return_value = {"humidity": 40.0}
        weather = Weather(api=weather_api)
        res = weather.get_humidity(city)
        assert isinstance(res, float)
