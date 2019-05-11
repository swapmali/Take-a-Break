import time
import webbrowser

if __name__ == '__main__':
    print('@author: Swapnil Mali')
    fp = open('video_link.txt', 'r')
    link = fp.read()

    try:
        my_break = int(input('\nEnter your break time (in min):  '))
        print('\nBreak time set to: {}\n'
              'link to open set to: {}'
              '\n\n#Be Productive!! '.format(time.strftime('%Hhr %Mmin %Ssec', time.gmtime(my_break*60)), link))
        while True:
            time.sleep(my_break * 60)
            webbrowser.open(link)
    except ValueError:
        print('Please try again with valid input.')
