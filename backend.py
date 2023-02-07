import requests

API_KEY = "6474b74e0d979275321b21546f31332e"


def get_data(place, forecast_days=None, forecast_type=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if forecast_type == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if forecast_type == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Calgary"))
