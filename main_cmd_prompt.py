import time
import webbrowser
from pygame import mixer
import sys

if __name__ == '__main__':
    print('@author: Swapnil Mali')         # author credits

    fp = open('video_link.txt', 'r')
    link = fp.read()

    try:
        my_break = int(input('\nEnter your break time (in min):  '))
        print('\nBreak time set to: {}\n'
              'link to open set to: {}'
              '\n\n#Be Productive!! '.format(time.strftime('%Hhr %Mmin %Ssec', time.gmtime(my_break*60)), link))
        mixer.init()        # used for playing audio at start and end
        session_id = 1      # counter for work sessions completed

        # until user ends program don't stop taking breaks
        while True:
            sys.stdout.write('\nSession {} Started: '.format(session_id))
            mixer.music.load("sounds\start.mp3")
            mixer.music.play()
            time.sleep(2)

            # this prints after what time next break is
            for remaining in range(my_break-2, -1, -1):
                sys.stdout.write("\r")
                if remaining != 0:
                    sys.stdout.write("Next Break in {:2d}sec.".format(remaining))
                else:
                    sys.stdout.write("{} Session Completed".format(session_id))
                sys.stdout.flush()
                time.sleep(1)

            # break time
            print("\nIt's time for a 5 min break!")
         ##   webbrowser.open(link)

            # prints after what time this break ends
            for remaining in range(5, -1, -1):
                sys.stdout.write("\r")
                if remaining != 0:
                    sys.stdout.write("Break ends in {:2d}sec.".format(remaining))
                else:
                    sys.stdout.write("{} Session Completed".format(session_id))
                sys.stdout.flush()
                time.sleep(1)

            # plays end music
            mixer.music.load("sounds\end1.mp3")
            mixer.music.play()
            time.sleep(2)

            session_id += 1
            sys.stdout.write("\r")
            sys.stdout.flush()

    except ValueError:
        print('Please try again with valid input.')
