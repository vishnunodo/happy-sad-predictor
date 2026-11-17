sentence = input("Enter a sentence: ")

happy_words = ["happy", "joy", "good", "great", "love", "awesome", "excited"]
sad_words = ["sad", "bad", "cry", "hate", "sorry", "upset", "lonely"]

happy_count = 0
sad_count = 0

words = sentence.lower().split()

for word in words:
    if word in happy_words:
        happy_count += 1
    elif word in sad_words:
        sad_count += 1

if happy_count > sad_count:
    print("Prediction: Happy ")
elif sad_count > happy_count:
    print("Prediction: Sad ")
else:
    print("Prediction: Neutral ")
