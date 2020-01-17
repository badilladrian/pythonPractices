#!/usr/bin/env python3.8

from urllib.request import urlopen
import sys

url = "http://sixty-north.com/c/t.txt"

def fetch_words(url):
    """Fetch a list of words from a URL.
    Args:
        URL
    Return:
        List of words from the URL.txt"""
    with urlopen (url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_words(story_words):
    for word in story_words:
        print(word)


def main(url):
    words = fetch_words(url)
    print_words(words)


if __name__ == '__main__':
    #main(sys.argv[1]) # the system arguments [0] name of the script, then [1] whichever we passed and so on
    main(url)


