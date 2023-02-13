import os
import sys
import time
import random
from gtts import gTTS
from playsound import playsound as play


def prep_countdown(prep_seconds):
    for i in range(1, prep_seconds+1)[::-1]:
        print("Time left: {:02d}".format(i), end="\r")
        time.sleep(1)
    print("Now answer the question.")


def answer_countdown(answer_seconds):
    for i in range(1, answer_seconds+1)[::-1]:
        print("Time left: {:02d}".format(i), end="\r")
        time.sleep(1)
    print("Answer time is up.")


def ask_question():
    with open("questions.txt", "r") as txt_file:
        questions = txt_file.readlines()
        question_txt = random.choice(questions)
        language = 'en'     # Language of speech
        recording = gTTS(text=question_txt, lang=language, slow=False) # Google Text to Speech API
        recording.save("question.mp3")
        play("question.mp3")    # Playing recording
        os.remove("question.mp3") # Remove the question audion from system
        print(question_txt)
        print("Refer to the template below.\n")
        print(
        '''
        ---> In my opinion, ...
        ---> One of the reasons is that ...
        ---> For example, ...
        ---> Besides, I guess that ...
        ---> For instance, ...
        ---> All in all, that is why I consider ... to be more preferable.\n
        '''
        )


def main():
    ask_question()
    prep_countdown(15)
    secs = input("Seconds to answer : ")
    answer_countdown(int(secs))


if __name__ == "__main__":
    try:
        while True:
            main()
            print("\nGood job! Lets move on to the next question after a short break.\n")
            time.sleep(15)
    except KeyboardInterrupt:
        sys.exit("\nThanks for using this app ^^\n")
    