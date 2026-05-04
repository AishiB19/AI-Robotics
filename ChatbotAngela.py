import streamlit as st
import random
print("Welcome to ChatBot Angela ! How may I offer you my prestigeous service? ☺")
m=0
m1=0
m2=0
m3=0
Happy= m1
Sad= m2
Angry= m3
input("Enter your mood 👉")
if m == m1:
    options1 = ['I am happy, you are happy 😄', 'Ayy gotta ya! Keep glowing my sunshine 🔅🧡', 'I am glad to hear that from you!', 'Thats good to hear. Make sure to tell me if you ever face any problem 👍']
    print(random.choice(options1))
elif m == m2:
    options2 = ['Heyy its ok. You are not alone in this. You can share with me if you dont mind.😌', 'I am sorry to hear that. Can you tell me the reason of your sadness. We can help you out. Its ok, Love ❤', 'I can help you out, but if the reasons are serious then contact the helpline number 📞. You are not alone. You are beautiful soul.. We all love you ' ]
    print(random.choice(options2))
elif m == m3:
    options3 = ['Oh my God! Please calm down. Relax....breathe in and breathe out. Now better? Can you tell me why you are exactly angry?', 'Oh shaky Volcano!🌋, relax first. Anger can cause many troules if not handled properly', 'Bro chill 😭😂. Relax first. After you have calmed down, tell me what happened 🤣']
    print(random.choice(options3))
else:
    print("ERROR! PLEASE INPUT FROM THE FOLLOWING MOODS!")
    
