import glob
i = '1'
x = glob.glob("../output/violencia/violencia/vid"+i+"id*.avi")
for i, teste  in enumerate(x):
    print (str(i)+"id -> "+teste)

    