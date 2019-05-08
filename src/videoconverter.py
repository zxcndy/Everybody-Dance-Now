import cv2
from pytube import YouTube
from pathlib import Path


save_dir = Path('./')
save_dir.mkdir(exist_ok=True)

img_dir = save_dir.joinpath('images')
img_dir.mkdir(exist_ok=True)

# Bruno Mars - That's What I Like
yt = YouTube('https://www.youtube.com/watch?v=PMivT7MJ41M')
yt.streams.first().download(save_dir, 'mv')


#convert into png files
cap = cv2.VideoCapture(str(save_dir.joinpath('mv.mp4')))
i = 0
while(cap.isOpened()):
    flag, frame = cap.read()
    if flag == False or i == 1000:
        break
    cv2.imwrite(str(img_dir.joinpath(f'img_{i:04d}.png')), frame)
    i += 1