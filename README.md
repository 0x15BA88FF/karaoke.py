# Karaoke.py

## Overview

**Karaoke** is a lightweight Python library designed to facilitate interactions
with song LRC (Lyric) files. It allows for easy parsing, management, and
retrieval of song lyrics along with their corresponding timestamps.

## Installation

To use the Karaoke library, simply clone the repository or download the
`karaoke.py` file and include it in your project.

```bash
git clone https://github.com/pascall-de-creator/karaoke.py
```

## Features

- **Parsing LRC Files:** Load and parse LRC formatted lyrics, extracting
  timestamps and lyrics.
- **Timestamp Management:** Convert timestamps from LRC format to milliseconds
  for precise timing.
- **Current Lyric Tracking:** Keep track of the current lyric based on a given
  timestamp.

## Usage

### Importing the Library

```python
from karaoke import Karaoke
```

### Creating an Instance

```python
karaoke = Karaoke()
```

### Parsing LRC Data

To parse LRC data, use the `parse` method:

```python
lrc_data = """
[00:01.00]Line 1
[00:05.00]Line 2
[00:10.00]Line 3
"""

karaoke.parse(lrc_data)
```

### Accessing Lyrics

You can access all the lyrics using the `lyrics` property:

```python
all_lyrics = karaoke.lyrics
print(all_lyrics)  # Output: ['Line 1', 'Line 2', 'Line 3']
```

### Getting Current Lyric

To get the currently active lyric based on the timestamp set, use the
`current_lyric` property:

```python
karaoke.set_current_lyric(6000)  # Set current time to 6 seconds
print(karaoke.current_lyric)  # Output: 'Line 2'
```

### Clean and Validate LRC Data

The `check` method validates the LRC data:

```python
karaoke.check(lrc_data)  # Raises ValueError if the data is invalid
```

The `clean` method can be used to clean up LRC data by removing blank lines:

```python
cleaned_lrc = karaoke.clean(lrc_data, clean_blanklines=True)
```

### Timestamp Conversion

Convert LRC timestamp to milliseconds with:

```python
ms = karaoke.timestamp_to_ms("[00:01.00]")  # Output: 1000
```

### Finding Lyric Index

To find the index of a lyric based on the target time:

```python
index = karaoke.find_lyric_index(6000)  # Output: 1
```

## Class Reference

### `Karaoke`

#### Properties

- `lyrics`: Returns a list of all lyrics.
- `lyric_index`: Returns the index of the currently active lyric.
- `current_lyric`: Returns the currently active lyric.

#### Methods

- `check(lrc: str)`: Validates the provided LRC data.
- `clean(lrc: str, clean_blanklines: bool)`: Cleans the LRC data by removing
  timestamps or blank lines.
- `timestamp_to_ms(timestamp: str) -> int`: Converts LRC timestamp to milliseconds.
- `parse(lrc: str, clean_blanklines: bool = False)`: Parses the LRC data into an
  internal structure.
- `find_lyric_index(target_time: int) -> int`: Finds the index of the lyric that
  corresponds to a given time.
- `set_current_lyric(target_time: int)`: Sets the current lyric based on a
  target time.

## Example

Here's a complete example demonstrating the library's functionality:

```python
from karaoke import Karaoke

karaoke = Karaoke()

lrc_data = """
[00:01.00]Line 1
[00:05.00]Line 2
[00:10.00]Line 3
"""

karaoke.parse(lrc_data)

karaoke.set_current_lyric(6000)  # Set current time to 6 seconds
print(karaoke.current_lyric)  # Output: 'Line 2'
```

## Conclusion

The Karaoke library is a simple yet powerful tool for managing song lyrics and
their timestamps. Its clean API and lightweight structure make it easy to
integrate into various projects. Enjoy your karaoke sessions!
