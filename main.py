import gtts
from playsound import playsound
gave_right_answer = False
while not gave_right_answer:
    answer = input("Can I have more candy?")
    good_responses = ["yes", "sure", "ok", "i guess", "all right"]
    if answer.lower() in good_responses:
        #answer lower for capitalization purposes
        gave_right_answer = True

celebrate = "Yummy I will eat candy!"
speaker1 = gtts.gTTS(celebrate)
speaker1.save("celebrate.mp3")
repeat = "again and again"
speaker2 = gtts.gTTS(repeat)
speaker2.save("repeat.mp3")
playsound("celebrate.mp3")
for repeat_count in range(5):
    playsound("repeat.mp3")