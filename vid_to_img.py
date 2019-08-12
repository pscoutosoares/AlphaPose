import cv2
import os
from tqdm import tqdm

def video_to_frames(video, path_output_dir):
    # extract frames from a video and save to directory as 'x.png' where 
    # x is the frame index
    vidcap = cv2.VideoCapture(video)
    count = 0
    while vidcap.isOpened():
        success, image = vidcap.read()
        if success:
            cv2.imwrite(os.path.join(path_output_dir, '%d.jpg') % count, image)
            count += 1
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()

if __name__ == "__main__":
   
    #for i in tqdm(range(1,53)):
    #    index = ''
    ##   if(i<10):
    #        index = '00'+str(i)
    #    elif(i<100):
    #        index = '0'+str(i)
    #    else:
    #        index = str(i)

    #if not os.path.exists("output/sem_violencia/"+str(i)+"/vis/"):
    #    os.mkdir("output/sem_violencia/"+str(i)+"/vis/")
    ##video_to_frames("samples/violencia/"+index+".wmv", "output/violencia/"+str(i)+"/vis/")
    video_to_frames("samples/sem_violencia/033.wmv", "output/sem_violencia/33/vis/")
        