import requests
API_Key = '5881028'

# Generate your personal key at website www.openweathermap.org.
# You need to register first, next get on API keys and see your.


base_url = "http://www.boredapi.com/api/activity?type=recreational?key=5881028"

random_activity = requests.get(base_url).json()

print(random_activity)

# another working API_key: cb771e45ac79a4e8e2205c0ce66ff633