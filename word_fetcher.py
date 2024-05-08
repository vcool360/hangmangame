import requests

def get_random_word():
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
        if response.status_code == 200:
            return response.json()[0]  # Assume one word is returned
        else:
            return "example"  # Fallback word
    except Exception as e:
        print(f"Error fetching word: {e}")
        return "example"
