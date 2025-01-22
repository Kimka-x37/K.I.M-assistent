from random import randint, choice
import os
import time
from pygame import mixer
import webbrowser
import pyttsx3
mixer.init()
mixer.music.load("phonk.mp3")

import speech_recognition as sr
from rich import print

import wikipedia as wiki

print("[red]--[/red][yellow]Асистент[/yellow][green]K.I.M[/green][blue]--[/blue]")

tts = pyttsx3.init()
tts.setProperty('voice', 'ru')
def say(text):
    tts.say(text)
    tts.runAndWait()
    

print("[blue]Скажите помоги для списка действий[/blue]")
say("Скажите помоги для списка действий")
music_on=False
wiki.set_lang("ru")

def listen_user(text):
    while True:
            recog = sr.Recognizer()
            with sr.Microphone() as source:
                recog.adjust_for_ambient_noise(source)
                try:
                    print(f"[green]{text}[/green]...")
                    say(text)
                    audio = recog.listen(source)
                    recognized_text=str(recog.recognize_google(audio, language='ru').lower())
                    print(recognized_text)
                    return recognized_text
                except:
                    print("[red]Вы нечего на сказали пожалуйста повторите попытку [/red]")

while True:
    wwod=listen_user("Говорите")

    if "привет" in wwod or "здарова" in wwod or "хай" in wwod:
       print("--Привет--")
       say("Привет")

    elif "помоги" in wwod:
        say("Вот сейчяс виведу таблицу")
        print("""+---------------------------------------------+
|[red]привет , здарова , хай[/red]                       |
|[green]брось кости , брось куб,брось кубик[/green]          |
|[blue]брось монетку , брось монету[/blue]                 |
|[purple]кто тебя создал , кто твой создатель[/purple]         |
|[red]давай поиграем (№), давай сыграем в игру (№)[/red] |
|[yellow]всего игр №1-3[/yellow]                               |
|[yellow]включи музыку-выключи музыку[/yellow]                 |
|[blue]ютуб[/blue]                                         |
|[green]выключи компьютер[/green]                            |
|[yellow]перезагрузи компьютер[/yellow]                        |
|[purple]пока , выйти[/purple]                                 |
+---------------------------------------------+""")

    elif "брось кости" in wwod or "брось кубик" in wwod or "брось куб" in wwod:
        random_num = randint(1,6)
        print("[blue]Выпало:[/blue]",random_num)
        say(f"Выпало {random_num}")

    elif "брось монету" in wwod or "брось монетку" in wwod:
        moneta = choice(["Орел","Решка"])
        if moneta == "Орел":
            print("[blue]Выпал:[/blue]",moneta)
            say(f"Выпал {moneta}")
        else:
            print("[blue]Выпала:[/blue]", moneta)
            say(f"Выпала {moneta}")

    elif "кто тебя создал" in wwod or "кто твой создатель" in wwod:
        print("[green]Кім Жебелев[/green][blue]#[/blue][yellow]#[/yellow]")
        say("Ким Жебелев")

    elif "включи музыку" in wwod or "включи трек" in wwod or "включи funk" in wwod or "включи phonk" in wwod or "включи фонк" in wwod:
        say("включаю лютый фонк")
        mixer.music.play()

    elif "поставь на паузу музыку" in wwod or "поставь на паузу трек" in wwod or "поставь на паузу funk" in wwod or "поставь на паузу phonk" in wwod or "включи in wwod фонк" in wwod or "выключи музыку" in wwod:
        say("хорошо")
        mixer.music.pause()

    elif "сколько времени" in wwod:
        print("Сейчяс "+time.asctime())
        say(f"Сейчяс {time.asctime()}")

    elif "давай поиграем в игру 1" in wwod or "давай поиграем 1" in wwod or "давай сыграем в игру 1" in wwod or "игра один" in wwod:
        print("[yellow]                --Правила--[/yellow]")
        print("[yellow]Ты должен угадать случяйное число от 1 до 3[/yellow]")
        say("Ты должен угадать случяйное число от одного до трех")
        while True:
           otvet = listen_user("Скажите как вы думаете")
           if "один" in otvet: otvet='1'
           elif "два" in otvet: otvet = '2'
           elif "три" in otvet: otvet = '3'
           zagadanoe_chislo = str(randint(1,3))
           print("[red]Число было:[/red]",zagadanoe_chislo)
           say(f"Число было {zagadanoe_chislo}")
           if zagadanoe_chislo in otvet:
               print("[blue]Bы выйграли[/blue]")
               say("Bы выйграли")
               igratsnovo = listen_user("играть сново? |да|")
           else:
               print("[red]Bы не угадали[/red]")
               say("Bы не угадали")
               igratsnovo = listen_user("играть сново? |да|")
           if "да" in igratsnovo:
               print("Хорошо")
               say("Хорошо")
           else:
               break

    elif "давай поиграем в игру 2" in wwod or "давай поиграем 2" in wwod or "давай сыграем в игру 2" in wwod or "игра 2" in wwod:
        print("[yellow]      --Правила--[/yellow]")
        print("[yellow]Ты должен угадать орел-решка[/yellow]")
        say("Ты должен угадать орел или решка")
        while True:
           otvet = listen_user("Cкажите орёл либо решка")
           moneta = choice(["Орёл","Решка"])
           print("[green]Было:[/green]",moneta)
           say(f"Было {moneta}")
           if moneta.lower() in otvet:
               print("[blue]Bы выйграли[blue]")
               say("Bы выйграли")
               igratsnovo = listen_user("играть сново? |да|")
           else:
               print("[red]Bы не угадали[/red]")
               say("Bы не угадали")
               igratsnovo = listen_user("играть сново? |да|")
           if "да" in igratsnovo:
               print("Хорошо")
               say("Хорошо")
           else:
               break

    elif "давай поиграем в игру 3" in wwod or "давай поиграем 3" in wwod or "давай сыграем в игру 3" in wwod or "игра 3" in wwod:
        print("[yellow]      --Правила--[/yellow]")
        print("[yellow]Ты должен победить противника[/yellow]")
        say("Ты должен победить противника")
        beats = {'камень': 'ножницы', 'ножницы': 'бумага', 'бумага': 'камень'}
        while True:
           otvet = listen_user("Cкажите камень ножницы или бумага!")
           bot_item = choice(["камень","ножницы","бумага"])
           print("[green]Было у ассистента:[/green]",bot_item)
           say(f"Было у ассистента {bot_item}")

           if "камень" in otvet:
               otvet="камень"
           elif "ножницы" in otvet:
               otvet="ножницы"
           else:
               otvet="бумага"

           if beats[otvet] == bot_item:
               print("[blue]Bы выйграли[blue]")
               say("Bы выйграли")
               igratsnovo = listen_user("играть сново? |да|")
           elif beats[bot_item] == otvet:
               print("[red]Bы проиграли[/red]")
               say("Bы проиграли")
               igratsnovo = listen_user("играть сново? |да|")
           else:
               print("[red]Ничья![/red]")
               say("Ничья")
               igratsnovo = listen_user("играть сново? |да|")
           if "да" in igratsnovo:
               print("Хорошо")
               say("Хорошо")
           else:
               break

    elif "найти" in wwod or "найди" in wwod:
        try:print(wiki.summary(listen_user("Скажите что вы хотите найти")))
        except:
            print("Такой информации не существует")
            say("Такой информации не существует")

    elif "youtube" in wwod:
        say("открываю ютуб")
        webbrowser.open("https://www.youtube.com/")

    elif "семейный чат" in wwod or "чат семьи" in wwod or "семейный счёт" in wwod:
        say("открываю семейный чат")
        webbrowser.open("http://saitsimjivaleriapolydnewa.pythonanywhere.com/")

    elif "выключи компьютер" in wwod:
        wwod=listen_user("Вы точьно хотите выключить пк? да/нет")
        if "да" in wwod:
            os.system("shutdown /s /t 1")

    elif "перезагрузи компьютер" in wwod:
        wwod = listen_user("Вы точьно хотите перезагрузить пк? да/нет")
        if "да" in wwod:
            os.system("shutdown /r /t 1")

    elif "пока" in wwod or "выйти" in wwod:
        print("[red]пока[/red]")
        say("пока")
        break

    else:
        print("[red]--я не знаю что ответить--[/red]")
        say("я не знаю что ответить")
