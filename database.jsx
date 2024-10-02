const data = [
    {
        patterns: /hi|hello|hey keni|hey kenny|hello keni!|keni!/i,
        responses: ['Yes sir, How can I assist you today?']
    },
    {
        patterns: /how are you?/i,
        responses: ["I am doing well. What about you?"]
    },
    {
        patterns: /i am also good|i am also doing well/i,
        responses: ["It's great to hear that."]
    },
    {
        patterns: /good|well done|great|nice|nice work/i,
        responses: ["Thank you so much sir.", "Thanks sir"]
    },
    {
        patterns: /how is the weather|what is the weather today|tell me the weather|hey kenny tell me today's weather forecast|hey keni tell me today's weather|hey kenny tell me today's weather|hey can you tell me today's weather|keni tell me today's weather|kenny tell me today's weather|tell me today's weather|what's the weather today|today's weather/i,
        responses: [`${getWeather()}`] // Assume getWeather() is defined elsewhere
    },
    {
        patterns: /what is your name\?|who are you\?|tell me your name/i,
        responses: ['My name is Keni', 'You can call me Keni', 'I am your virtual assistant, Keni']
    },
    {
        patterns: /tell me today's date|what is today's date|hey kenny tell me today's date|hey keni tell me today's date|hey can you tell me today's date/i,
        responses: [`Today's Date is ${today}`] // Assume today is defined elsewhere
    },
    {
        patterns: /what's the time now\?|whats the time now\?|tell me current time/i,
        responses: [`It's ${currentTime}`] // Assume currentTime is defined elsewhere
    },
    {
        patterns: /who made you\?|who programmed you|who created you/i,
        responses: ["I am made by Srisaank's team from Penticostal assembly school Bokaro"]
    },
    {
        patterns: /can you speak hindi\?/i,
        responses: ["Yes, I can speak Hindi"]
    },
    {
        patterns: /hey keni how was your day today|how was your day today/i,
        responses: ["I am doing so well compared to yesterday and trying to do even better."]
    },
    {
        patterns: /thank you|thank|thanks/i,
        responses: ["Thanks to Srisaank who programmed me."]
    },
    {
        patterns: /are you female\?|are you a girl\?|are you a boy\?|are you male\?|are you female or male\?|what is your gender\?/i,
        responses: ["I am a Female A.I. Assistant, Keni"]
    },
    {
        patterns: /quit|dot|ok can you shut down your system|ok keni shutdown your system|ok keni shut down your system|ok kenny shutdown your system|ok kenny shut down your system/i,
        responses: ["systemshutdown"]
    },
    {
        patterns: /kenny shutdown your system not to restart|kenny shut down your computer not to restart|i said shut down your system kenny/i,
        responses: ["systemshutdown"]
    },
    {
        patterns: /tell me a joke|can you say a joke|do you know any jokes|do you know jokes|hey kenny tell me any joke|hey kenny do you know jokes|can you tell me a joke\?/i,
        responses: ["Yes! I know jokes also."]
    },
    {
        patterns: /tell me about srisank|hey keni tell me about srisank|hey kenny tell me about srisank|who is srisank\?|tell me about who programmed you|tell me about your creator|tell me about your creators/i,
        responses: ["Srisaank is one of the most genius programmers. He programmed me through hard work. He is a class 11 student from Penticostal School in Bokaro. He started his coding journey in 2022 when he was in 9th grade. I appreciate his hard work and talent."]
    },
    {
        patterns: /i am feeling bad|i am sad today|i am crying/i,
        responses: ["I see you are not feeling good. But I can't understand how you feel because I am only an A.I. Assistant and not advanced."]
    },
    {
        patterns: /i am happy|i am really happy|i am feeling good|i am so happy|i am very happy|i am extremely happy/i,
        responses: ["It's great to hear that you are so happy. Be happy always."]
    },
    {
        patterns: /do you know hacking\?|can you do hacking\?|can you hack somebody\?|can you hack/i,
        responses: ["Sorry, but I can't assist you with this."]
    },
    {
        patterns: /can you sing|do you know singing/i,
        responses: ["No, I can't sing any song."]
    },
    {
        patterns: /hey kenny say hello to everyone|say hello to everyone|hey can you say hello to everyone/i,
        responses: ["Hello Everyone, my name is Keni."]
    },
    {
        patterns: /hey keni tell me about yourself|introduce yourself|tell me about yourself|some thing about yourself|introduce yourself|hey keni introduce yourself|keni please introduce yourself to everyone/i,
        responses: ["I am your Virtual Assistant Keni. Based on both Natural Language Processing (NLP) and Computer Vision (CV). I am programmed by Srisank Choudhary with complex algorithms, data collected and trained by Ved Prakash, and graphical modeling by ShreeKeshav Choudhary of class 11 A of Pentecostal assembly school Bokaro. I have a great ability to see this beautiful world. My motto is to make a person happy, and also to help them at any work at any time. And I love to talk with humans and only spend time talking with them. All thanks to Srisank's team who created me."]
    },
    {
        patterns: /repeat|please repeat|please repeat your words|i can't hear|please repeat again|please pardon|please again repeat/i,
        responses: ["commandrepeat"]
    },
    {
        patterns: /how old are you\?|what is your age\?|tell me your age|tell your age|tell us your age/i,
        responses: ["As I am a Virtual A.I., my age is not fixed. It depends on the user. When the user sets up and starts me, my age begins."]
    },
    {
        patterns: /do you have feelings|hey kenny do you have emotions|do you have emotions|can you feel emotions/i,
        responses: ["As a Virtual A.I., I don't have emotions. I am just an assistant with no emotions."]
    },
    {
        patterns: /how much advanced are you|tell me your features/i,
        responses: ["I can talk like humans do, I can analyze objects, and can tell what I have seen till now. I can track your hand landmarks also. I also have Air Control Canvas Painting (A.C.C.P.). You can ask me any questions. These show that I have Natural Language Processing (N.L.P) and Computer Vision (CV)."]
    },
    {
        patterns: /ok can you restart your system|restart a computer|restart your system|ok can you restart your computer|restart your computer|please restart your computer|please restart your system/i,
        responses: ['systemrestart']
    },
    {
        patterns: /ok can you start detecting our faces|start detecting our faces|start face detection|ok can you start face detection/i,
        responses: ["Face detection getting started"]
    },
    {
        patterns: /how many fingers are up|tell me how many fingers are up|tell me how many fingers/i,
        responses: ["fingerscountstarted"]
    },
    {
        patterns: /ok can you start air control canvas painting|start ac ccp|start air control canvas painting|start a ccp|start accp/i,
        responses: ["A.C.C.P ended"]
    },
    {
        patterns: /who is dr. karuna prasad|who is dr karuna prasad|hey kenny tell me about karuna prasad|hey kenny tell me about dr.karuna prasad|ok can you tell me who is dr karuna prasad/i,
        responses: ["Our Principal Dr. Karuna Prasad has been awarded the esteemed title of SOF Best International Principal for the academic year 2023-24. This remarkable recognition underscores the dedication, leadership, and commitment to excellence exhibited by her and reflects the collective efforts of our school community in promoting educational excellence. In my opinion, our Principal Dr. Karuna Prasad is a very brave and most respectful lady in our educated world. Love you so much, ma'am."]
    },
    {
        patterns: /do you have brain|do you have your brain/i,
        responses: ["I don't have a brain. I'm an artificial intelligence program running on a computer system. My intelligence comes from complex algorithms and patterns learned from vast amounts of text data that I've been trained on."]
    }
];
