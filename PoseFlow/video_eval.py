import glob 
import shutil
import os, sys
from tqdm import tqdm


num_vid = 1
container = 1
for i in tqdm(range (1,53)):
    dir_list = glob.glob("../output/sem_violencia/sem_violencia/vid"+str(i)+"id*")
    if not os.path.exists("../resultado/sem_violencia/"+str(container)): 
        os.mkdir("../resultado/sem_violencia/"+str(container))

    for index, x in enumerate(dir_list):
        shutil.copy(x,"../resultado/sem_violencia/"+str(container))
    
    num_vid +=1
    if num_vid == 5:
        container +=1
        num_vid = 1
