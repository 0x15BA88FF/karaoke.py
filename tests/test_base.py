import pytest
from karaoke import Karaoke


def test_initial_state():
    karaoke = Karaoke()
    assert karaoke.lyric_index == -1
    assert karaoke.lyrics == []
    assert karaoke.current_lyric is None


def test_check_invalid_lrc():
    karaoke = Karaoke()
    with pytest.raises(ValueError, match="Invalid LRC data."):
        karaoke.check("")


def test_clean_lrc():
    karaoke = Karaoke()
    cleaned = karaoke.clean("[00:01] Lyric 1\n\n[00:02] Lyric 2", clean_blanklines=True)
    assert cleaned == "[00:01] Lyric 1\n[00:02] Lyric 2"


def test_timestamp_to_ms():
    karaoke = Karaoke()
    assert karaoke.timestamp_to_ms("[00:01:50]") == 110000
    assert karaoke.timestamp_to_ms("[00:02]") == 2000
