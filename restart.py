import json
import subprocess                                                                                                                              


with open('/run/hive/gpu-stats.json','r') as json_file:                                                                                        
    data = json.load(json_file)                                                                                                                
    load = set([float(gpu) for gpu in data['load']])                                                                                           

if len(load) == 1 and list(load)[0] == 0:                                                                                                      
    subprocess.run(["miner", "stop"])                                                                                                          
    subprocess.run(["miner", "start"])

