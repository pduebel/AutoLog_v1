# auto-geodasy-log-input
Utilises Google's Cloud Vision API to extract information from images of handwritten geological logs, allowing the user to edit the result before inserting it into a Microsoft Access database, for use in GEODASY logging software. Presented to user with simple tkinter GUI.

## Screenshots
<figure>
  <figcaption>Test image of basic example of handwritten log.</figcaption>
  <img width="390" alt="Test image of basic example of handwritten log" src="https://user-images.githubusercontent.com/56090238/143719948-23b9c129-bf7a-4128-8f89-cf60afab935b.png">
</figure>
<figure>
  <figcaption>Program interface.<figcaption>
  <img width="337" alt="Screenshot of program interface" src="https://user-images.githubusercontent.com/56090238/143720108-532f0130-d156-48cc-a4f1-299afb3ca318.png">
</figure>
    
## Getting started

Requirements:
* Git
* Python
* google-cloud-vision library
* Google Cloud Vision API key
    
In order to use this code clone the repository with the following command:
```
git clone https://github.com/pduebel/auto-geodasy-log-input.git
```

Next create a virtual environment and install the `google-cloud-vision` library, for example by using the following code:
```
python3 -m venv venv
venv\Scripts\activate
pip install google-cloud-vision
```
For more information about installing the library please reder to the [documentation](https://pypi.org/project/google-cloud-vision/ 'google-cloud-vision library documentation') 
    
**IMPORTANT:** In order for the code to run you will need to set up the Vision API and aquire an API key. To do this follow the [official quick start guide](https://cloud.google.com/vision/docs/setup 'Google CLoud Vision API Quickstart Guide'). Once you have everything set up save the API key as a json in the directory with the name `API-key.json`.
    
Then to start the program run the `main.py` script using:
```
python3 main.py
```
