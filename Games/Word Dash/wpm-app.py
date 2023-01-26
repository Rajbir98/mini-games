import curses
from curses import wrapper
import time
from random import randint

subjects = ["I", "He", "She", "Jack", "Jim", "Tim", "Bob", "Jane", "Mia", "We", "They", "You all", "The group", "The team", "The quick brown fox", "A lazy dog"]
verbs = ["jumped", "ran", "leaped", "hopped", "skipped", "galloped", "trotted", "dashed"]
objects = ["over the fence", "through the field", "across the stream", "down the road", "up the hill", "around the corner", "into the forest", "out of the cave"]
adverbs = ["quickly", "happily", "eagerly", "calmly","loudly","softly","angrily","sadly"]
adjectives = ["exciting", "interesting", "bizarre", "funny","sad","happy","angry","calm"]

title = """
         __          __              _   _____               _      _
         \ \        / /             | | |  __ \             | |    | |
          \ \  /\  / /___   _ __  __| | | |  | |  __ _  ___ | |__  | |
           \ \/  \/ // _ \ | '__|/ _` | | |  | | / _` |/ __|| '_ \ | |
            \  /\  /| (_) || |  | (_| | | |__| || (_| |\__ \| | | ||_|
             \/  \/  \___/ |_|   \__,_| |_____/  \__,_||___/|_| |_|(_)
"""

button_next = """
                                _  _            _
                               | \| | ___ __ __| |_
                               | .` |/ -_)\ \ /|  _|
                               |_|\_|\___|/_\_\ \__|
"""

def gen_sen():
    verb = verbs[randint(0, len(verbs)-1)]
    if verb in ["jumped", "leaped", "hopped", "skipped", "galloped"]:
        adverb = adverbs[randint(0, len(adverbs)-1)]
        return subjects[randint(0, len(subjects)-1)] + " " + verb + " " + adverb + " " + objects[randint(0, len(objects)-1)]
    else:
        return subjects[randint(0, len(subjects)-1)] + " " + verb + " " + objects[randint(0, len(objects)-1)]



def main_menu(stdscr):
    stdscr.clear()

    stdscr.addstr(curses.LINES // 2 - 6, 16, title, curses.A_BOLD)
    stdscr.addstr(curses.LINES // 2 + 6 , 26, "Press any key to continue.", curses.A_ITALIC)

    stdscr.refresh()
    key = stdscr.getch()
    if key == 27:
        exit()

def game(stdscr):
    countdown(stdscr)
    tp_txt = gen_sen()
    txt = []
    wpm = 0
    time.sleep(0.2)
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = int((len(txt) // (time_elapsed / 60)) / 5)

        stdscr.clear()

        stdscr.addstr(curses.LINES // 2, (curses.COLS // 2) - len(tp_txt)//2, tp_txt)
        stdscr.addstr(curses.LINES // 2 + 3, (curses.COLS // 2) - len(tp_txt)//2, f"WPM: {wpm}")

        for i, char in enumerate(txt):
            check = char == tp_txt[i]
            stdscr.addstr(curses.LINES // 2, (curses.COLS // 2) - len(tp_txt)//2 + i, char, curses.color_pair(int(check)+1))

        stdscr.refresh()

        if "".join(txt) == tp_txt or len(txt) == len(tp_txt):
            stdscr.nodelay(False)
            return wpm
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(txt) > 0:
                txt.pop()
        elif not len(key) > 1:
            if ord(key) == 27:
                stdscr.nodelay(False)
                return wpm
                break

        if len(txt) < len(tp_txt) and (key.isalpha() or key in ["SHF_PADENTER", "CTL_PADENTER"] or not len(key) > 1 and ord(key) in (ord('.'), ord(' '), ord('!'), ord('?'))):
            if key in ["SHF_PADENTER", "CTL_PADENTER"]:
                if key == "SHF_PADENTER":
                    txt.append("'")
                elif key == "CTL_PADENTER":
                    txt.append('"')
            else:
                txt.append(key)

def countdown(stdscr):
     for i in range(3):
        stdscr.clear()
        stdscr.addstr(curses.LINES // 2, (curses.COLS // 2) - 1, str(i+1), curses.A_BOLD)
        stdscr.refresh()
        time.sleep(1)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.A_INVIS)
    curses.init_pair(2, curses.COLOR_GREEN, curses.A_INVIS)

    main_menu(stdscr)
    wpm = game(stdscr)
    while True:
        text = f"Your WPM was {wpm}"
        stdscr.clear()
        stdscr.addstr(curses.LINES // 2 - 4, 16, button_next, curses.A_BOLD)
        stdscr.addstr(curses.LINES // 2 + 5, (curses.COLS // 2) - len(text)//2 + 1, text, curses.A_BOLD)
        stdscr.refresh()
        key = stdscr.getkey()
        if ord(key) == 27:
            main_menu(stdscr)
        if ord(key) == ord("\n"):
            wpm = game(stdscr)

wrapper(main)

