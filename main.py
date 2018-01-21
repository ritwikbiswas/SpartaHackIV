from firebase import firebase
import RPi.GPIO as GPIO
import time

chan = 15

# GPIO.setup(chan, GPIO.out)

minbank = ['minute', 'minutes']
secbank = ['second', 'seconds']

fb = firebase.FirebaseApplication('https://voice-recognition-spartahacks.firebaseio.com/', None)

def start(c=chan, t=1):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(c,GPIO.OUT)
    GPIO.output(c,GPIO.HIGH)
    time.sleep(t)
    GPIO.output(c, GPIO.LOW)
    GPIO.cleanup()


def button(r, listen):
    minute = 0
    second = 0
    t = False
    rbank = r.lower().split()
    if 'start' in rbank:
        for i, word in enumerate(rbank):
            if word in minbank:
                minute = int(rbank[i - 1])
                t = True
            if word in secbank:
                second = int(rbank[i - 1])
                t = True
        if not t:
            second = 5
            '''
            fb.post('/voice', "Ok. How long should I run for?".format(minute, second))
            print("Ok. How long should I run for? \n".format(minute, second))
            while listen == r:
                r = fb.get('/text', None)
                time.sleep(.5)
            listen = r
            print(r)
            bank = r.lower().split()
            for i, word in enumerate(rbank):
                try:
                    if word in minbank:
                        minute = int(rbank[i - 1])
                        t = True
                    if word in secbank:
                        second = int(rbank[i - 1])
                        t = True
                except ValueError:
                    fb.post('/voice', "Sorry, I didn't understand. Please try again.")
                    print("Sorry, I didn't understand. Please try again. \n")
                    return None
            if not t:
                fb.post('/voice', "Sorry, I didn't understand. Please try again.")
                print("Sorry, I didn't understand. Please try again. \n")
                return None
            '''
        if not minute:
            if second == 1:
                fb.post('/voice', "Alright. Starting blender for 1 second.")
                print("Alright. Starting blender for 1 second. \n")
            else:
                fb.post('/voice', "Alright. Starting blender for {} seconds.".format(second))
                print("Alright. Starting blender for {} seconds. \n".format(second))
            time.sleep(3)
            start(chan, 60*minute+second)
            return None
        if not second:
            if minute == 1:
                fb.post('/voice', "Alright. Starting blender for 1 minute.")
                print("Alright. Starting blender for 1 minute. \n")
            else:
                fb.post('/voice', "Alright. Starting blender for {} minutes.".format(minute))
                print("Alright. Starting blender for {} minutes. \n".format(minute))
            time.sleep(3)
            start(chan, 60*minute+second)
            return None
        if minute == 1:
            if second == 1:
                fb.post('/voice', "Alright. Starting blender for 1 minute and 1 second.")
                print("Alright. Starting blender for 1 minute and 1 second. \n")
            else:
                fb.post('/voice', "Alright. Starting blender for 1 minute and {} seconds.".format(second))
                print("Alright. Starting blender for 1 minute and {} seconds. \n".format(second))
            time.sleep(3)
            start(chan, 60*minute+second)
            return None
        if second == 1:
            fb.post('/voice', "Alright. Starting blender for {} minutes and 1 second.".format(minute))
            print("Alright. Starting blender for {} minutes and 1 second. \n".format(minute))
            time.sleep(3)
            start(chan, 60*minute+second)
            return None
        else:
            fb.post('/voice', "Alright. Starting blender for {} minutes and {} seconds.".format(minute, second))
            print("Alright. Starting blender for {} minutes and {} seconds. \n".format(minute, second))
            time.sleep(3)
            start(chan, 60*minute+second)
            return None
    if 'stop' in rbank:
        #GPIO.output(15, GPIO.LOW)
        GPIO.cleanup()
        fb.post('/voice', "Stopped.")
        print("Stopped. \n")
        return None
    else:
        fb.post('/voice', "Sorry, I didn't understand. Please try again.")
        print("Sorry, I didn't understand. Please try again. \n")
        return None


def main():
    listen = ""
    while True:
        result = fb.get('/text', None)
        if result == listen:
            time.sleep(.5)
        else:
            listen = result
            print(result)
            button(result, listen)


main()
