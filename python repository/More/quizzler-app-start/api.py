import requests

response = requests.get(url = "https://opentdb.com/api.php?amount=10")
response.raise_for_status()
data = response.json()

question_text = str(data["response_code"]["result"]["question"])

print(question_text)