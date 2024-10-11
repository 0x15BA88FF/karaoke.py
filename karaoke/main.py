import re
from typing import List, Tuple


class Karaoke:
    def __init__(self) -> None:
        self.__lyric_index: int = 0
        self.__lrc_data: List[Tuple[int, str]] = []

    @property
    def lyrics(self) -> List:
        return [lyric[1] for lyric in self.__lrc_data]

    @property
    def lyric_index(self) -> int:
        return self.__lyric_index

    @property
    def current_lyric(self) -> str:
        return self.__lrc_data[self.__lyric_index][1]

    def check(self, lrc: str) -> None:
        if not lrc:
            raise ValueError("Invalid LRC data.")

    def clean(self, lrc: str, clean_blanklines: bool) -> str:
        lines = []
        timestamp_pattern = r"(\[(\d{2}):?(\d{2})(:\d{2})?(\.\d{2})?\])\s*"

        for line in lrc.splitlines():
            if not clean_blanklines or line.strip():
                lines.append(re.sub(timestamp_pattern, r"\1", line).strip())

        return "\n".join(lines).strip()

    def timestamp_to_ms(self, timestamp) -> int:
        timestamp = re.sub(f"[{re.escape('()[]{} ')}]", "", timestamp).split(":")
        timestamp = ["0"] * (3 - len(timestamp)) + timestamp
        HH, MM, SS = map(float, timestamp)
        return int((HH * 3600 + MM * 60 + SS) * 1000)

    def parse(self, lrc: str, clean_blanklines: bool = False) -> None:
        self.check(lrc)
        self.__lrc_data = []
        self.__lyric_index = 0
        lrc = self.clean(lrc, clean_blanklines)
        for line in lrc.splitlines():
            pattern = r"^\[(.*?)\](.*)$"
            match = re.match(pattern, line)
            if match:
                timestamp, lyric = match.groups()
                self.__lrc_data.append((self.timestamp_to_ms(timestamp), lyric))

    def find_lyric_index(self, target_time: int) -> int:
        start_times = [start_time[0] for start_time in self.__lrc_data]
        for idx, start_time in enumerate(start_times):
            if target_time >= start_time and target_time <= start_times[idx + 1]:
                return idx
        return -1

    def set_current_lyric(self, target_time: int) -> None:
        self.__lyric_index = self.find_lyric_index(target_time)
