import matplotlib.pyplot as plt
import numpy as np
import json

coco_part_names = ['Nose','LEye','REye','LEar','REar','LShoulder','RShoulder','LElbow','RElbow','LWrist','RWrist','LHip','RHip','LKnee','RKnee','LAnkle','RAnkle']
colors = ['r', 'r', 'r', 'r', 'r', 'y', 'y', 'y', 'y', 'y', 'y', 'g', 'g', 'g','g','g','g']
pairs = [[0,1],[0,2],[1,3],[2,4],[5,6],[5,7],[7,9],[6,8],[8,10],[11,12],[11,13],[13,15],[12,14],[14,16],[6,12],[5,11]]
 
with open('../output/violencia/1/vid1id1.json') as json_file:
    data = json.load(json_file)

    for item in data['pontos']:
        fig = plt.figure(figsize=(640/10,480/10),dpi=10)        
        for element in item:

            plt.plot( item[element][0], item[element][1], marker='o', color='r',markersize=22) 
        
        plt.show()
        print('a')


# plt.axis('off')
# ax = plt.gca()
# ax.set_xlim([0,width])
# ax.set_ylim([height,0])
# extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
# if not os.path.exists(visdir): 
# os.mkdir(visdir)

# fig.savefig(os.path.join(visdir,str(args.video_index)+"tmp.png"), pad_inches = 0.0, bbox_inches=extent, dpi=13)
# plt.close()