import subprocess
import psutil
from tqdm import tqdm
import glob

def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

if __name__ == "__main__":

    vec = []
    for i in tqdm(range(1,2)):
        if i == 77:
            continue
        #dir_list = glob.glob("../output/violencia/violencia/vid"+str(i)+"id*.avi")
        #if not dir_list:
        vec.append(i)
        path = "../output/violencia/"+ str(i)
        proc = subprocess.Popen("python tracker-general.py --imgdir "+path+"/vis --in_json "+path+"/alphapose-results.json --out_json "+path+"/alphapose-results-forvis-tracked.json    --visdir ../output/tmp/violencia/  --video_index "+str(i) ,shell=True)
        try:
            proc.wait(timeout=5000)
        except subprocess.TimeoutExpired:
            kill(proc.pid)
   
    # print(vec)
    # print("Agora para sem violencia ")
    
    # vec = []
    # for i in tqdm( range(1,53)):
    #     dir_list = glob.glob("../output/sem_violencia/sem_violencia/vid"+str(i)+"id*.avi")
    #     if not dir_list:
    #         vec.append(i)
    #         path = "../output/sem_violencia/"+str(i)
    #         proc = subprocess.Popen("python tracker-general.py --imgdir "+path+"/vis --in_json "+path+"/alphapose-results.json --out_json "+path+"/alphapose-results-forvis-tracked.json    --visdir ../output/sem_violencia/sem_violencia/ --video_index "+str(i) ,shell=True)
    #         try:
    #             proc.wait(timeout=5000)
    #         except subprocess.TimeoutExpired:
    #             kill(proc.pid)



#python tracker-general.py --imgdir ../output/violencia/1/vis/0.jpg --in_json ../output/violencia/1/alphapose-results.json --out_json ../output/violencia/1/alphapose-results-forvis-tracked.json    --visdir ../output/violencia/1/ 