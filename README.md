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

## Trainging Nural network for your purpuse.
If you have High Performance PC (if possible CUDA enabled), Training time is make to shoot. Detail instruction as bekkow,

if you do not have High Performance PC, Don't worrry, Raspberry PI Can To Traning but to Slow.

## Tranind Nural Network to move in to Raspberry PI system
Traned Neural Network system is key item for this system, So, copy it data to Raspberry PI correct directory.

## Setup system parameter for your environment

# Setup PetActivityMonitorSystem
Now, You can setup PetActivityMonitorSystem to you decided position. 
Setup is very simple, it it only put the system.

# Show Pet's Activity
You can access Raspberry PI Web Server, via PC or SmartPhone with Wifi.
connect homepage of Pet Activity Monitor, You can show your pets activities any times.
