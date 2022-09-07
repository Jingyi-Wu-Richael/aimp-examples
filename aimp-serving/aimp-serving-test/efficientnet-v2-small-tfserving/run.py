from __future__ import print_function

import io
import os
import time
import base64
import json
import time
import numpy as np 
import requests
import pickle
import onepanel.core.api
from onepanel.core.api.rest import ApiException
import onepanel.core.auth
from pprint import pprint

# MUST import AIMP python SDK
# import upper dir's python file
import sys
sys.path.append("../..") 
sys.path.append("..") 
import aimpInferWorkFlowSDK

#start init the aimpinferWorkFlowSDK
aimpPredict=aimpInferWorkFlowSDK.aimpInfer()
aimpPredict.namespace = 'mp'
aimpPredict.model_name = 'efficientnet-v2-small-tfserving'
aimpPredict.getAccess()
access_token=aimpPredict.api_access_token
endpoint=aimpPredict.infer_endpoint
#end init the aimpinferSDK


with open('./img.pkl','rb') as f:
    img_data = pickle.load(f)

data = {
    'instances': img_data
}

headers = {
    'onepanel-access-token': access_token,
    'Content-Type': 'application/json',
}


r = requests.post(endpoint, headers=headers, json=data)

result = r.json()

print(result)

with open('imagenet1000_clsidx_to_labels.txt') as f:
    labels = eval(f.read())
    
print(labels[np.array(result['predictions'][0]).argmax()])



