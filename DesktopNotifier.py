﻿# git-practice
from plyer import notification
from random_word import RandomWords

r=RandomWords()

word=r.get_random_word()g

title='Greetings logophile!'
message=f"Your word is {word}; find the meaning,have fun :)"
            

notification.notify(title=title,
                    message=message,
                    app_icon=None,
                    timeout=10,
                    toast=False)


