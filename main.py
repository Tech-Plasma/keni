import nltk
import time
import requests
import os
import subprocess
from nltk.chat.util import Chat, reflections
from bs4 import BeautifulSoup
from DataBase import Replydb 
from DataBase.commandsDB import sendcommand
from dubbingcvs import speak
from playsound import playsound
from googlecapturing import search, gogle_open_search
from startAI import start, endai, speakPrototype
from speechtotext import continuous_speech_to_text
from googletrans import Translator
from tellmeajock import fetch_random_joke
from weatherCheck import get_weather
from evaluation import process_maths

# from rememberlastInput import remember_user_input, get_last_input
# Import TensorFlow and Keras for deep learning
# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Embedding, LSTM, GlobalMaxPooling1D
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences

# Function to create and train a simple text classification model
def train_text_classifier():
    # Example training data (replace with your own labeled data)
    texts = [
        "turn on the lights",
        "play music",
        "tell me a joke",
        "translate this sentence",
        "evaluate 2 + 2",
        "command shutdown",
    ]
    labels = [
        "turn_on_lights",
        "play_music",
        "tell_joke",
        "translate_sentence",
        "evaluate_expression",
        "system_shutdown",
        # Add corresponding labelsspeak("Hello world")
    ]

    # Tokenize and pad sequences
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(texts)
    sequences = tokenizer.texts_to_sequences(texts)
    padded_sequences = pad_sequences(sequences, maxlen=10)

    # Define and compile the model
    model = Sequential([
        Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=50, input_length=10),
        GlobalMaxPooling1D(),
        Dense(16, activation='relu'),
        Dense(len(set(labels)), activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(padded_sequences, labels, epochs=10, batch_size=1, verbose=1)

    return model, tokenizer

def check_for_unwanted_words(input_text, unwanted_words):
    input_words = input_text.lower().split()  # Convert input to lowercase and split into words
    for word in input_words:
        if word in unwanted_words:
            print(f"Warning: Detected unwanted word '{word}' in your input.")
            return True  # Return True if unwanted word found
    return False  # Return False if no unwanted words found

def get_recipe(query):
    url = f"https://www.allrecipes.com/search/results/?wt={query.replace(' ', '%20')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the first recipe title and link
    results = soup.find_all('article', class_='fixed-recipe-card')
    if results:
        first_recipe = results[0]
        title = first_recipe.find('span', class_='fixed-recipe-card__title-link').text.strip()
        link = first_recipe.find('a')['href']
        return f"Here's a recipe for {query}: {title}. You can find it here: {link}"
    else:
        return f"Sorry, I couldn't find a recipe for {query}."

def train (whattotrain,whattosay) :
    train_list = []
    with open("DataBase/replyDataBase.py", 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith('data = ['):
            # Modify the list in some way
            train_list = line.strip().split('= ')[-1]
            original_list = eval(train_list)  # Convert string representation to actual list
            original_list.append(f"""(r'{whattotrain}',
                    ['{whattosay}'])""")
            train_lines.append(f'my_list = {original_list}\n')
    with open("DataBase/replyDataBase.py", 'w') as f:
        f.writelines(train_lines)

#Translator
def translate_to_hindi(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='hi')
    return translation.text

parse=Replydb.sendData()
# Define a function to chat with the bot

def mainAI():

    start()
    try:
        parse = Replydb.sendData()
        chat = Chat(parse, reflections)
    except Exception as e:
        print(f"Error initializing Chat: {e}")
        # Handle the error appropriately, e.g., fallback to a default chat initialization

    while True:
        user_input = continuous_speech_to_text()
        # user_input=input("You: ")
        print("You : ", user_input)
        unwanted_words = ['violate', 'badword', 'fuck', 'sex', 'sala', 'harami', 'ass'] 
        if check_for_unwanted_words(user_input, unwanted_words):
            print("""I'm sorry, but that language is not appropriate. Please refrain from using such words.
            Cause It looks like you used a word that might be considered inappropriate. Let's keep the conversation respectful and friendly.
            In order to maintain a positive and respectful conversation, let's avoid using language that could be offensive or inappropriate.
            """)
            try:
                speak("""I'm sorry, but that language is not appropriate. Please refrain from using such words.
                    Cause It looks like you used a word that might be considered inappropriate. Let's keep the conversation respectful and friendly.
                    In order to maintain a positive and respectful conversation, let's avoid using language that could be offensive or inappropriate.
                    """)
            except:
                playsound("ai.mp3")
                
        else:
            comm_detect=user_input.lower().split()
            if comm_detect[0].lower() == "command":
                response = task.respond(usr_input)
            elif "Google" in comm_detect:
                comm_detect.remove("Google")
                if "search" in comm_detect:
                   comm_detect.remove("search")
                if "in" in comm_detect:
                    comm_detect.remove("in")
                to_search = " ".join(comm_detect)
                gogle_open_search(to_search)
            elif comm_detect[0].lower() == "evaluate":
                response=f"The answer is {process_maths(user_input)}"
            # elif "tell" in comm_detect and "weather" in comm_detect:
            #     city=comm_detect[-1]
            #     try:
            #         speak(get_weather(city)) 
            #     except:
            #         #playsound("ai.mp3")

            elif comm_detect[0].lower() == "translate":
                response=translate_to_hindi(response)
            elif "recipe" in comm_detect :
                response=get_recipe(comm_detect[-1])
            elif comm_detect[0].lower() == "say":
                comm_detect.remove("say")
                comm_detect.pop(-2)
                if comm_detect[-1].lower() == "hindi":
                    comm_detect.pop(-1)
                    setResp=" ".join(comm_detect)
                    response=translate_to_hindi(setResp)
                else:
                    comm_detect.pop(-1)
                    setResp=" ".join(comm_detect)
                    response=setResp
            else:    
                response = chat.respond(user_input)
            #####
            if response == 'systemshutdown':
                try:
                    speak("Have a great day sir! Good bye!")
                    print("Have a great day sir! Good bye!")
                except:
                    playsound("ai.mp3")
                    
                # speakPrototype("Have a great day sir! Good Bye!")
                time.sleep(1)
                endai()
                break
            elif response == "fingerscountstarted":
                
                try:
                    from CV.fingurescount import finger_count
                    speak(f"Number of Fingeres are {finger_count}")
                except:
                    playsound('ai.mp3')
                    
            elif response == "A.C.C.P ended":
                try:
                    speak("Ok sir! starting Air Controle Canvas Painting.")
                except:
                    playsound('ai.mp3')
                    
                import CV.AirTrackerDrow
            elif response == 'systemrestart':
                try:
                    speak("Ok, I am restarting my computer.")
                except:
                    playsound("ai.mp3")
                os.system("python3 main.py")
            elif response=="commandrepeat":
                playsound("ai.mp3")
                
            elif response == 'Yes! I know jocks also.':
                
                try:
                    speak(fetch_random_joke())
                except:
                    playsound("ai.mp3")
                    
            ####
            if response == None:
                speakggl=search(user_input)
                print("Keni: ", speakggl)
                if speakggl is not None:
                    try:
                        speak(speakggl)
                    except:
                        playsound("ai.mp3")
                        
                else:
                    try:
                        print("Keni : I dont understant what to say. Sorry for that.")
                        speak("I dont understant what to say. Sorry for that.")
                    except:
                        playsound("ai.mp3")
                        
            else: 
                print("Keni:", response)
                try:
                    speak(response)
                except:
                    playsound("ai.mp3")
                    

mainAI()
