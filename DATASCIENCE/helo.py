import requests
import emoji
import cowsay

# Use requests to get a random fun fact from an API
response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
fact = response.json()["text"]

# Use emoji to add an emoji
message = emoji.emojize(f":light_bulb: Did you know? {fact}")

# Use cowsay to have a cow tell you the fact
cowsay.cow(message)