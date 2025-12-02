import ctypes,time

def Clicked():return ctypes.windll.user32.GetAsyncKeyState(0x01)and 0x8000!=0

start=time.time();clicks=[2]

print("Press Ctrl+C to terminate.")#Error should occur; there is no "try-exept-finally" protection yet.

while True:
    
    while max(clicks)>0.28:
        if Clicked():
            end=time.time()
            clicks.append(end-start);clicks=clicks[-5:]
            start=end
            while Clicked():time.sleep(0.001)
        time.sleep(0.001)
    clicks[0]=2

    heatup=time.time()
    while time.time()-heatup<0.8:
        ctypes.windll.user32.mouse_event(0x0002,0,0,0,0)
        ctypes.windll.user32.mouse_event(0x0004,0,0,0,0)
        time.sleep(0.001)
