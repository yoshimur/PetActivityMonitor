# PetActivityMonitor
Monitoring your pet activitiis such as eating food etc.  

Required:
Raspberry PI (Better 3 Model B+)
- Super Sonic Sensor (like XXXXXX)
- Infrared Camera (Like XXXXXX)

Optional:
- High Performance PC (if possible CUDA enables)

# Basic Concept:
This system will monitoring your Pet Activity via Super Sonic Sensor and Infrared Camera, even if you have some pets. This system recognize each pets.
- For example:
Setup this system near the Pet Food bowl, If your pet came to eat food, then Super sonic Sencor was detect your pet (cat or may be dog), and then get the picture of pet via　camera, so, in pet eat foor at night, Infrared camera can chatch the you pet image.
And then, system will recognize pet names via Deep Learning Argorizm, and store timedata to database with captured image.

When You access to Raspberry Pi WebSite, you can get your pet activitis. So, You can communicate you pet via acctivity datas.

# Initial Activity
## Get the Picture of your pets
This system is based on Deep Learning Argorithm for detect pet name. For the reason, you must first Traning the system to recognize your pets. It requires some pictures of your pets.

Initial picture must be stored images/trani/XXX Folders. And Total image must be devided by 10, 10 is batch size for this training phase.

And another limitation, current version support only Four Categry folders. Please take care of.
   
## Step1 create dataset.
First time, please run the make_train_data.py in images folders, this script generate training data set support files.

## Trainging Nural network for your purpuse.
Now start to train the Neural Network.
It is simple to run the, python train.py. It takes few minuits depend of image count and CPU power.

If you have High Performance PC (if possible CUDA enabled), Training time is make to shoot. Detail instruction as bekkow,
if you do not have High Performance PC, Don't worrry, Raspberry PI Can To Traning but to Slow.

## Tranind Nural Network to move in to Raspberry PI system
After trainig was finished, Please send all of files in python folders, include ckpt.

## Recogsize image command
To recognize image command as follow.
python predict.py imagefile

# Setup PetActivityMonitorSystem
Now, You can setup PetActivityMonitorSystem to you decided position. 
Setup is very simple, it it only put the system.

# Show Pet's Activity
You can access Raspberry PI Web Server, via PC or SmartPhone with Wifi.
connect homepage of Pet Activity Monitor, You can show your pets activities any times.
