# Deploy Model as REST API using Flask

## About the Project

This repository shows a simple example of deploying a image classification model as a REST API using Flask. The server is hosted on Amazon Web Service (AWS). 

The model are pretrained from [here](https://github.com/anilsathyan7/pytorch-image-classification), it can predict 11 classes : 'apple','atm card','cat','banana','bangle','battery','bottle','broom','bulb','calender','camera'.  


## Usage

To call the API, there are two methods. First method is to use the Postman application and the second one is using a Python script. 


### Method 1 - Using Postman : 
    
  
In Body -> form-data, insert KEY as 'image', choose File type and upload your image in the VALUE tab. 
    
![Postman](https://github.com/bebbieyin/Model_Deployment_API/blob/master/imgs/screenshot.PNG)
     
### Method 2 - Using Python script : 

Clone this repository and execute call.py with server url and image path as arguments. 

```
python call.py -f "image_classification/test_imgs/apple.jpeg" -url http://127.0.0.1:8000
```
