import pytest
from karaoke import Karaoke


def test_on_lyric_change():
    karaoke = Karaoke()
    callback_called = False

    def callback():
        nonlocal callback_called
        callback_called = True

    karaoke.on_lyric_change(callback)
    assert karaoke.callbacks == (callback,)

    karaoke.seek(
        0
    )  # Assuming no lyrics are present, this should not trigger the callback
    assert not callback_called

    # Add lyrics and seek to trigger the callback (this part may require proper setup)
    karaoke.parse("[00:00] First lyric\n[00:01] Second lyric")
    karaoke.seek(0)
    assert callback_called
