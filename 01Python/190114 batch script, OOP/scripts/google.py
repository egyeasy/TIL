import webbrowser
import sys

url = "https://www.google.co.kr/search?q="

keyword = ' '.join(sys.argv[1:])

webbrowser.open(url + keyword)