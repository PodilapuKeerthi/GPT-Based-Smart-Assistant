import openai
import pyttsx3
import speech_recognition as sr
import webbrowser
from apikey import api_data  # Assuming api_data contains your OpenAI API key

# Set OpenAI API key
openai.api_key = api_data

# Text-to-speech engine setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get OpenAI response
def Reply(question):
    completion = openai.ChatCompletion.create(
        model="gpt-4",  # Ensure you are using the correct model identifier
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant'},
            {'role': 'user', 'content': question}
        ],
        max_tokens=200
    )
    answer = completion.choices[0].message['content']
    return answer

# Speech recognition setup
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening .......')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing ....')
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")
    except Exception as e:
        print("Say that again .....")
        return "None"
    return query

# Main loop
if __name__ == '__main__':
    while True:
        query = takeCommand().lower()
        if query == 'none':
            continue
        
        ans = Reply(query)
        print(ans)
        speak(ans)
        
        # Specific Browser Related Tasks
        if "Open youtube" in query:
            webbrowser.open('www.youtube.com')
        if "Open Google" in query:
            webbrowser.open('www.google.com')
        if "bye" in query:
            break
