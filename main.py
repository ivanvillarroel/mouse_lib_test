import time
import mouse


def control_mouse():
    print("usando mouse")
    time.sleep(10)

    mouse.move("500", "500")
    mouse.click('left')


if __name__ == '__main__':
    control_mouse()
