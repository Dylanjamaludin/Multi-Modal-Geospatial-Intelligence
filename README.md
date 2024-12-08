<img src="https://github.com/Dylanjamaludin/Multi-Modal-Geospatial-Intelligence/blob/main/Interface/splashScreen/image%201%402x.png" width="100%" height="auto">

# Multi-Modal Geospatial Intelligence

## Objective

Develop a geospatial intelligence application using multi-modal models (Segment Anything Model, OpenAl's CLIP, QA) for zero-shot classification in computer vision tasks, leveraging geospatial datasets like RSICD.

## Key Requirements

1. Integration of Multi-Modal Models
    - Combine vision and language models for accurate classifications and responses.
2. Zero-Shot Classification
    - Leverage the zero-shot classification capabilities of multi-modal models for real-time insights.
3. Geospatial Data Utilization
    - Efficiently process and analyze geospatial datasets to extract valuable insights.
4. User-Friendly Interface
    - Create an intuitive interface for easy navigation and understanding of results.

## Impact

 This project has the potential to revolutionize geospatial data processing and analysis in various sectors like environmental monitoring, urban planning, and disaster management. It can also inspire the development of similar applications in other domains.

## Interface Image

<img width="1552" alt="Screen Shot 2024-12-08 at 12 14 13 PM" src="https://github.com/user-attachments/assets/a1c1b351-18ee-4bab-af8b-a80e77c3e22f">


## Demo Videos

Example of GeoINT's prompt generation!

https://github.com/user-attachments/assets/1219e6c6-9c0f-4627-b87e-fdf274ca5a11

Example of Preview in File Explorer Window!

https://github.com/user-attachments/assets/3ad8acb8-a99b-4262-bc1a-1412bc334fb2

Example of TileServer Graphing Abilites!

https://github.com/user-attachments/assets/2419ffc0-06c7-4b90-8d6a-3e4fe2e28b63

Examples of adding/deleting images to the File Explorer Window!

https://github.com/user-attachments/assets/fc3f7b71-e119-49f3-a92c-34ce60a5f9a2

https://github.com/user-attachments/assets/566618e6-1433-40ca-8e15-a4e573244580

Example of creating/opening chats 

https://github.com/user-attachments/assets/0ab041f0-4373-4976-9e3f-6925b058dd60




## Setting Up the Application: 
Create a python virtual environment, python 3.11 or greater 

The virtual environment must be created in the same directory as  the “interface”  folder. 

Activate that python virtual environment

Using the terminal enter the interface file cd Interface

Install all the packages required for the application by running this command: pip install -r requirements.txt 

Install python-dotenv module by running this command: pip install python-dotenv

Create a .env file inside the interface folder

Add your api key from Replicate (Might have to create an account) to that .env file as shown below. 

REPLICATE_API_KEY = ”######################################”

## To run the application
Run Interface.py
python Interface.py: 
## Python Description files/folders:
The ‘feather’, ‘feather(2.5px)’, and’ feather(3px)’ folders holds the application’s icons, and are sourced from https://feathericons.com/. 

The ‘loadingSvg’ folder holds all the loading animations for the application and are sourced from https://loading.io/ 

The ‘splashScreen’ folder holds the splash screen image that is displayed when the application is booting. 

chat_history_dock.py: Manages the chat sessions within GUI. Allows users to start new chats, open existing ones and remove chats from their history. Contains customized widgets related to the Chat History Window.

chatbox_file.py:  Allows users to interact with Llava. Contains customized widgets related to the chat interface. 

component_file.py: Contains all the styled components/widgets that fit the application's theme.

file_explorer_dock.py: The file explorer dock allows users to upload an image, remove and image, and keep track of what image is currently being viewed in the current conversation. Contains customized widgets related to the File Explorer Window

interface.py: This file calls the main window of the application, it instantiates all of the custom widgets and places all widgets in its rightful location. 

interactive_map_dock.py: Allows users to screenshot, and capture satellite images, and view GeoTiff Images in their rightful location. Contains the widgets related to the Interactive Map Window. Contains localtileserver package built by Bane Sullivan.

image_preview_dock.py: Contains a custom widget for displaying images. Handles image scaling and interactive functionalities. Contains the widgets related to the Current Image Window and the File Explorer Window
model_runnable.py: Integrates multimodal model using a replicate API.

current model application is using: llava-v1.6-vicuna-13b

## Limitations:

If a user tries to pass a file larger than 20 MB through Replicate’s API it will return an error: Prediction interrupted; please retry (code: PA). We believe this is due us setting the file as input in the request body leading to Replicate’s API enforcing limits on the size of the request.
