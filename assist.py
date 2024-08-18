import speech_recognition as sr
import pyttsx3
import requests
from bs4 import BeautifulSoup

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return None

def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    result_div = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
    results = [result.get_text() for result in result_div[:3]]
    return results

def process_command(command):
    if 'hello' in command:
        speak("Hello sajid I am jarvis ! How can I help you today?")
    elif 'your name' in command:
        speak("I am your voice assistant.")
    elif 'search' in command:
        search_query = command.replace('search', '').strip()
        speak(f"Searching Google for {search_query}")
        results = google_search(search_query)
        if results:
            speak("Here are the top results I found:")
            for result in results:
                speak(result)
        else:
            speak("I couldn't find any results.")
    elif 'exit' in command:
        speak("Goodbye!")
        return False
    else:
        speak("Sorry, I didn't understand that.")
    return True

def main():
    speak("Hello! I am your voice assistant. How can I help you today?")
    while True:
        command = listen()
        if command:
            if not process_command(command):
                break

if __name__ == "__main__":
    main()
