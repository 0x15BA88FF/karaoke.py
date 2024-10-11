import pytest
from karaoke import Karaoke


def test_parse_valid_lrc():
    karaoke = Karaoke()
    karaoke.parse("[00:01] First lyric\n[00:02] Second lyric", clean_blanklines=False)
    assert karaoke.lyrics == ["First lyric", "Second lyric"]
    assert karaoke.lyric_index == -1


def test_get_lyric_index():
    karaoke = Karaoke()
    karaoke.parse("[00:01] First lyric\n[00:02] Second lyric")
    assert karaoke.get_lyric_index(1500) == 0  # Should return index for the first lyric
    assert (
        karaoke.get_lyric_index(2500) == 1
    )  # Should return index for the second lyric
    assert karaoke.get_lyric_index(3000) == -1  # Out of range
