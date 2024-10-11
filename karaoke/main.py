import re
import functools
from typing import List
from typing import Tuple
from typing import Callable


def debug(func):
    """A decorator that logs the function call details."""

    @property
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}()")
        print(f"Arguments: {args}, {kwargs}")

        try:
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned: {result}")
            return result
        except Exception as e:
            print(f"Exception in {func.__name__}: {e}")
            raise

    return wrapper


class Karaoke:
    def __init__(self) -> None:
        self.__lyric_index: int = -1
        self.__callbacks: Tuple[Callable, ...]
        self.__lrc_data: List[Tuple[int, str]] = []

    @debug
    def lrc_data(self) -> List[Tuple[int, str]]:
        return self.__lrc_data

    @debug
    def callbacks(self) -> Tuple[Callable, ...]:
        return self.__callbacks

    @property
    def lyrics(self) -> List:
        """Get a list of all lyrics in the LRC (without timestamps)"""
        return [lyric[1] for lyric in self.__lrc_data]

    @property
    def lyric_index(self) -> int:
        """
        Get the index of the current active lyric
        [-1]: undefined state (karaoke has not began or failed to get index)
        [0:]: play state (karaoke has began)
        """
        return self.__lyric_index

    @property
    def current_lyric(self) -> str:
        """Get the current active lyric"""
        return self.__lrc_data[self.__lyric_index][1]

    def check(self, lrc: str) -> None:
        """
        Validate LRC structure
        [Not implemented yet...]
        """
        if not lrc:
            raise ValueError("Invalid LRC data.")

    def clean(self, lrc: str, clean_blanklines: bool) -> str:
        """Clean and re-format LRC"""
        lines = []
        timestamp_pattern = r"(\[(\d{2}):?(\d{2})(:\d{2})?(\.\d{2})?\])\s*"

        for line in lrc.splitlines():
            if not clean_blanklines or line.strip():
                lines.append(re.sub(timestamp_pattern, r"\1", line).strip())

        return "\n".join(lines).strip()

    def timestamp_to_ms(self, timestamp) -> int:
        """Convert timestamp/seek string to milliseconds"""
        timestamp = re.sub(f"[{re.escape('()[]{} ')}]", "", timestamp).split(":")
        timestamp = ["0"] * (3 - len(timestamp)) + timestamp
        HH, MM, SS = map(float, timestamp)
        return int((HH * 3600 + MM * 60 + SS) * 1000)

    def parse(self, lrc: str, clean_blanklines: bool = False) -> None:
        """Parse LRC into an internal structure"""
        self.check(lrc)
        self.__lrc_data = []
        self.__lyric_index = -1
        lrc = self.clean(lrc, clean_blanklines)
        for line in lrc.splitlines():
            pattern = r"^\[(.*?)\](.*)$"
            match = re.match(pattern, line)
            if match:
                timestamp, lyric = match.groups()
                self.__lrc_data.append((self.timestamp_to_ms(timestamp), lyric))

    def get_lyric_index(self, target_time: int) -> int:
        """Get the index of a lyric by target time"""
        start_times = [start_time[0] for start_time in self.__lrc_data]
        for idx, start_time in enumerate(start_times):
            if (
                target_time >= start_time
                and idx == len(start_times) - 1
                or target_time <= start_times[idx + 1]
            ):
                return idx
        return -1

    def seek(self, target_time: int) -> None:
        """Set active lyric index and trigger observer callback"""
        prev_lyric_index = self.__lyric_index
        self.__lyric_index = self.get_lyric_index(target_time)
        if not self.__lyric_index == prev_lyric_index:
            [callback() for callback in self.__callbacks]

    def on_lyric_change(self, *callbacks: Callable):
        """Add callback function(s) to watchlist"""
        self.__callbacks = callbacks
