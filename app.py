#!/usr/bin/env python3
"""
ReelRecommend: offline movie and TV-show recommendation system
"""
from pathlib import Path
import webbrowser
import time

HERE = Path(__file__).resolve().parent
PAGE = HERE / "index.html"

def main():
    if not PAGE.exists():
        print("ERROR: index.html is missing. Keep it in the same folder.")
        raise SystemExit(1)
        
    url = PAGE.as_uri()
    print("=" * 58)
    print(" REELRECOMMEND - MOVIE & SHOW RECOMMENDATION SYSTEM ")
    print("=" * 58)
    print("Opening the movie and TV-show catalogue in your browser...")
    print("Choose genres, search titles, and mark shows as watched.")
    print("Your preferences and watch history are saved locally.")
    print("To stop: close this terminal window.")
    time.sleep(0.5)
    webbrowser.open(url)
    print("\nIf the browser did not open, copy this file link:")
    print(url)

if __name__ == "__main__":
    main()
