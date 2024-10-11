from karaoke import Karaoke
from time import sleep

sample_lrc = """"
[00:00.00]Hello World

[00:11.50]I've been searching for a sign,
[00:14.00]In the chaos of my mind.
[00:16.50]Every dream feels so far away,
[00:19.00]But I keep on finding my way.

[00:23.50]Hello World, can you hear me?
[00:26.00]I'm breaking through, setting free.
[00:28.50]With every step, I'm alive,
[00:31.00]In this moment, I will thrive.

[00:35.50]Through the shadows, I will run,
[00:38.00]Chasing rays of the rising sun.
[00:40.50]All the colors start to blend,
[00:43.00]This journey's just around the bend.

[00:47.50]Hello World, can you see me?
[00:50.00]I'm finding hope, just believe me.
[00:52.50]With every heartbeat, I'm alive,
[00:55.00]In this moment, I will thrive.

[00:59.50]Hello World, I'm here to stay,
[01:02.00]With open arms, I'll find my way.
[01:04.50]Every challenge, every fall,
[01:07.00]Hello World, I'm ready for it all.
"""

termaoke_machine = Karaoke()
termaoke_machine.parse(sample_lrc)


def show_lyric():
    print(termaoke_machine.current_lyric)


termaoke_machine.on_lyric_change(show_lyric)

time = 0
while True:
    termaoke_machine.seek(time)
    sleep(0.5)
    time += 500
