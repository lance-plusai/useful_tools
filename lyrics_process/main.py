import os
from bs4 import UnicodeDammit
import re

RE_ROW_OF_NUMBERS = re.compile(r'^[\s\t]?\d+\s?$')


def main():
    lyrics_dir = '/Users/hyl/Documents/英语/咱们裸熊/第一季'
    for root_dir, dirs, files in os.walk(lyrics_dir):
        for file in files:
            if file.endswith('.srt'):
                parse_lyrics(os.path.join(root_dir, file))


def parse_lyrics(lyrics_file_path):
    with open(lyrics_file_path, 'rb') as f:
        lyrics_content = f.read()
    suggestion = UnicodeDammit(lyrics_content)
    encoding = suggestion.original_encoding
    if encoding.startswith('utf-16'):
        encoding = 'utf-16'

    decode_content = lyrics_content.decode(encoding)
    lines = decode_content.splitlines()
    total_line = len(lines)
    new_lines = []
    del_idx = 0
    for i in range(total_line):
        line = lines[i]
        if RE_ROW_OF_NUMBERS.match(line):
            next_idx = i + 3
            if next_idx >= total_line - 1:
                next_idx = total_line - 1
            en_line = lines[next_idx]
            if en_line and not RE_ROW_OF_NUMBERS.match(en_line):
                del_idx = next_idx
        if del_idx != i:
            new_lines.append(line)
    with open(lyrics_file_path, 'w') as f:
        f.write('\n'.join(new_lines))


if __name__ == '__main__':
    main()
