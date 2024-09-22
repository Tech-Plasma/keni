import datetime
from weatherCheck import get_weather
current_time = datetime.datetime.now().strftime("%H:%M:%S")
today = datetime.date.today()
data = [
    ('hi|hello|hey keni|hey kenny|hello keni!|keni!', ['Yes sir, How can I assist you today?']),
    ('how are you?', ["I am doing well. What about you?"]),
    ("i am also good|i am also doing well", ["It's greate to here that."]),
    ('good|well done|great|nice|nice work',["Thank you soo much sir.","Thank's sir"]),
    ("how is the weather|what is the weather today|tell me the weather|hey kenny tell me today's weather forcast|hey keni tell me today's weather|hey kenny tell me today's weather|hey can you tell me today's weather|keni tell me today's weather|kenny tell me today's weather|tell me today's weather|what's the weather today|todays weather", [f"{get_weather()}"]),
    ('what is your name?|who are you?|tell me your name', ['My name is Keni', 'You can call me Keni', 'I am your virtual assistant, Keni']),
    ("tell me today's date|what is today's date|hey kenny tell me today's date|hey keni tell me today's date|hey can you tell me today's date", [f"Todays Date is {today}"]),
    ("what's the time now?|whats the time now?|tell me current time", [f"It's {current_time}"]),
    ('who made you?|who programmed you|who created you', ["I am made by Srisaank's team from Penticostal assembly school Bokaro"]),
    ('can you speak hindi?', ["Yes, I can speak hindi"]),
    ("hey keni how was your day today|how was your day today",["I am doing so well then yesterday and trying to do more better."]),
    ("thank you|thank|thank's", ["Thank's to srisaank who programmed me."]),
    ('are you female?|are you a girl?|are you a boy?|are you main?|are you female or mail?|what is your gender?', ["I am Femail A.I. Assistant, Keni"]),
    ('quit|dot|ok can you shut down your system|ok keni shutdown your system|ok keni shut down your system|ok keny shutdown youe system|ok keny shut down your system', ["systemshutdown"]),
    ("kenny shutdown your system not to restart|kenny shut down your computer normalt to restart|i said shut down your system kenny", ["systemshutdown"]),
    ('tell me a joke|can you say a joke|do you know any jock|do you know jock|hey kenny tell me any jock|hey kenny do you know jocks|can you tell me a joke?', ["Yes! I know jocks also."]),
    ('tell me about srisank|hey keni tell me about srisank|hey kenny tell me abut srisank|who is srisank?|tell me about who programmed you|tell me about your creator|tell me about your creators',["Srisaank is one of the most genious programmer, He also programmed me by duing hardwork. He is class 11th Penticostal School student from bokaro. He started his coding journey since 2022 when he was at 9th class. I also appriciate his hardwork mindset and talents. His ideas are super great. And his journy of coding is really painfull. A normal student can't do it. He is really a genious person."]),
    ('i am feeling bad|i am sad today|i am crying', ["I see, you are not feeling good. But I kant understand how you feels because I am only an A.I. Assistant and also not advanced"]),
    ('i am happy|i am really happy|i am feeling good|i am so happy|i am very happy|i am extremely happy', ["It's greate to hear that you are soo happy, be happy always."]),
    ("do you know hacking?|can you do hacking?|can you hack some body|can you hack", ["Sorry, but I can't assist you with this."]),
    ("can you sing|do you know singing", ["No, I can't sing any song"]),
    ("hey kenny say hello to everyone|say hello to everyone|hey can you say hello to everyone", ["Hello Everyone, my name is Keni"]),
    ("hey keni tell me about your self|introduce yourself|tell me about your self|tell us about your self|some thing about your self|introduse your self|hey keni introduce your self|keni please introduce your self to everyone", ["I am your Virtual Assistant Keni. Baised on both Natural Language Processing (NLP) and Computer Vision (CV). I am programmed by Srisank Choudhary with complex algorithms, Data collected and trained by Ved Prakash and GUIX and Graphical modelling by ShreeKeshav Choudhary of class 11 A of Pentecostal assembly school Bokaro. I have a great ability to see this beautifull world. My moto is to make a person happy, and also to help him or her at any work at any time. And I love to tock with humains and only spend time to tock with them. All thanks to Srisank's team who create me."]),
    ("repeat|please repeat|please repeat your words|i can't hear|please repeat again|please pardon|please again repeat", ["commandrepeat"]),
    ("How old are you?|what is your age?|tell me your age|tell your age|tell us your age", ["As I am a Virtual A.I., My age is not fixed. It depends upon the user. When user setup and start me my age begains."]),
    ("do you have feelings|hey kenny do you have emotions|do you have emotions|can you feel emotions", ["As an Virtual A.I. I don't have emotions. I am just an assistant with no emotions"]),
    ("how much advance you are|tell me your features", ["I can tock like humains do, I can analyse objects and can tell what I had seened till now. And I can track your hand landmark also. I also have Air Controle Canvas Painting (A.C.C.P.). You can ask me any questions. These shows that I have Natural Language Processing (N.L.P) and Computer Vision (CV)"]),
    ("ok can you restart your system|restart a computer|restart your system|ok can you restart your computer|restart your computer|please restart your computer|please restart your system", ['systemrestart']),
    ("ok can you start detecting our faces|start detecting our faces|start face detection|ok can you start face detection", ["face detection getting started"]),
    ("how many fingers are up|tell me how many fingers ar up|tell me how many fingers", ["fingerscountstarted"]),
    ("ok can you start air control canvas painting|start ac ccp|start air controle canvas painting|start a ccp|start accp", ["A.C.C.P ended"]),
    ("who is dr. karuna prasad|who is dr karuna prasad|hey kenny tell me about karuna prasad|hey kenny tell me about dr.karuna prasad|ok can you tell me who is dr karuna prasad", ["Our Principal Dr. Karuna Prasad, in being awarded the esteemed title of SOF Best International Principal for the academic year 2023-24. This remarkable recognition underscores the dedication, leadership, and commitment to excellence exhibited by her and reflects the collective efforts of our school community in promoting educational excellence. In my openion, Our Principal Dr. Karuna Prasad is very brave and most respectfull lady in our educated world. Love you soo much ma'am."]),
    ("do you have brain|do you have your brain", ["I don't have a brain.  I'm an artificial intelligence program running on a computer system. My intelligence comes from complex algorithms and patterns learned from vast amounts of text data that I've been trained on."]),
    
]
def sendData():
    return data
