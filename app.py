from flask import Flask, request, jsonify
import torch
from torchvision import transforms
from PIL import Image

app = Flask(__name__)

def load_model(model_path,device):
    model = torch.load(model_path)
    model.to(device)
    model.eval()
    return model

# get the query image from requests
def get_input():
    return request.files['image']

# preprocess image before sending to model
def preprocess_img(img):
    preprocess=transforms.Compose([
                transforms.Resize(size=256),
                transforms.CenterCrop(size=224),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406],
                                        [0.229, 0.224, 0.225])
            ])

    return preprocess(img)

@app.route('/api',methods=['POST'])
def predict():

    data = get_input()

    with torch.no_grad():
        img=Image.open(data).convert('RGB')
        inputs=preprocess_img(img).unsqueeze(0)
        outputs = model(inputs).to(device)
        _, preds = torch.max(outputs, 1)    
        label=class_labels[preds]

    output = {'predicted':label}
    
    return jsonify(output) # return json of output
        
if __name__ == '__main__':
    
    # define the class names
    class_labels =['apple','atm card','cat','banana','bangle','battery','bottle','broom','bulb','calender','camera']

    # load the pretrained model 
    MODEL_PATH='image_classification/models/resnet18.pth'
    device = 'cpu'

    model = load_model(MODEL_PATH,device)
    
    # run the server
    app.run(port=8000, debug=True)