import time
import sys
import pyttsx3
import datetime
import webbrowser
import contextlib
with contextlib.redirect_stdout(None):
    from pygame import mixer

def log_session(break_time_in_min):
    ts = datetime.datetime.now().timestamp()
    readable = datetime.datetime.fromtimestamp(ts).isoformat()
    # print(readable)
    fp = open('log.txt', '+a')
    index = file_len('log.txt')

    log = '\n' + str(index) + '\t' + readable + '\t' + str(break_time_in_min*60)
    fp.write(log)
    fp.close()


def file_len(fname):
    try:
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1
    except UnboundLocalError:
        return 1


if __name__ == '__main__':
    print('@author: Swapnil Mali')         # author credits

    fp = open('video_link.txt', 'r')
    link, user = fp.read().split()
    # for text to speech
    speaker = pyttsx3.init()

    try:
        my_break = int(input('\nEnter your break time (in min):  '))
        print('\nBreak time set to: {}'
              '\n\n#Be Productive!! \n'.format(time.strftime('%Hhr %Mmin %Ssec', time.gmtime(my_break*60))))
        mixer.init()        # used for playing audio at start and end
        session_id = 1      # counter for work sessions completed

        # until user ends program don't stop taking breaks
        while True:
            sys.stdout.write('Session {} Started: '.format(session_id))

            speaker.say('\nSession {} Started: '.format(session_id))
            speaker.runAndWait()

            # plays start music
            mixer.music.load("sounds\start.mp3")
            mixer.music.play()
            time.sleep(2)

            # this prints after what time next break is
            for remaining in range(my_break-2, -1, -1):
                sys.stdout.write("\r")
                if remaining != 0:
                    sys.stdout.write("Next Break in {:2d} sec".format(remaining))
                else:
                    sys.stdout.write("Session {} Completed ".format(session_id))
                sys.stdout.flush()
                time.sleep(1)

            # plays end music
            """
            mixer.music.load("sounds\end.mp3")
            mixer.music.play()
            time.sleep(2)
            """
            session_id += 1
            log_session(my_break)

            sys.stdout.write("\r")
            sys.stdout.flush()


            # break time starts from here
            speaker.say("It's time for a 5 min break {}".format(user))
            speaker.runAndWait()
            # sys.stdout.write("\nIt's time for a 5 min break!")
            # time.sleep(2)
            # sys.stdout.flush()
            # webbrowser.open(link)

            # prints after what time this break ends
            for remaining in range(5, -1, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Break ends in {:2d} sec".format(remaining))
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write("\r")
            sys.stdout.write('')
            sys.stdout.flush()

            # plays break end music
            mixer.music.load("sounds\end1.mp3")
            mixer.music.play()
            time.sleep(4)

            speaker.say("{} It's time to get back to work!".format(user))
            speaker.runAndWait()

    except ValueError:
        print('Please try again with valid input.')
