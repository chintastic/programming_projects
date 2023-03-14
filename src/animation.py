import os, time
os.system('cls')
filenames = ['frame1.txt', 'frame2.txt']
frames = []

for name in filenames:
    with open(name, 'r', encoding='utf8') as f:
        frames.append(f.readlines())

for frame in frames:
    print(''.join(frame))
    time.sleep(1)
    os.system('cls')