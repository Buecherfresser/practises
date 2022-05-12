import random
import time
import tkinter as tk

#root = tk.Tk()

letters = input("Welche Buchstaben willst du üben?")
text = ""
for i in range(int(input("Wie viele Wörter willst du tippen?"))):
    fiveletters = ""
    for m in range(5):
        fiveletters = fiveletters + letters[random.randint(0, len(letters) - 1)]
    text += fiveletters + " "
#label = tk.Label(root, text = text)
#label.pack(padx=20, pady=20)
#root.mainloop()
print(text)
time1 = time.time()
typedText = input()

typedText = typedText.split(' ')
text = text.split(' ')
counter = 0
for i in range(len(text) - 1):
    if typedText[i] != text[i]:
        counter += 1
timefinal = time.time() - time1
print('You mistyped ' + str(counter) + " words and needed " + str(round(timefinal, 2)) + " seconds with "
      + str(round(len(text) * 60 / timefinal, 1)) + " wpm.")
