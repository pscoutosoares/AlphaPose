import subprocess
import psutil

def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

if __name__ == "__main__":

    for i in range(1,146):
        index = ''
        if(i<10):
            index = '00'+str(i)
        elif(i<100):
            index = '0'+str(i)
        else:
            index = str(i)
        proc = process = subprocess.Popen("python video_demo.py --video samples/com_violencia/"+index+".wmv --outdir output/com_violencia/"+str(i)+"/  --sp --fast_inference False --nms 0.7 --conf 0.09",shell=True)

        try:
            proc.wait(timeout=300)
        except subprocess.TimeoutExpired:
            kill(proc.pid)
