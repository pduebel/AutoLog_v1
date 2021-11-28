# auto-geodasy-log-input
Utilises Google's Cloud Vision API to extract information from images of handwritten geological logs, allowing the user to edit the result before inserting it into a Microsoft Access database, for use in GEODASY logging software. Presented to user with simple tkinter GUI. Please note, that this project is a proof of concept and so may perform poorly on real world logs written in the field.

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

## Usage
    
After running the `main.py` script choose the 'Select file' button. This will open a file explorer window to allow you to specify the filepath of the image you wish to process. Then, once the image has been selected, hit the 'Process' button. This will submit the image to the Vision API for processing and may take up to a minute. If the call to the API has been selected, then processed text should appear in the text box below. You can use this text box to edit any inaccuracies in the processed text.
    
Next, use the 'Select file' button at the bottom of the window to specify the filepath to the MS Access database linked to your GEODASY software. Finally, hit the 'Input to GEODASY' button to input the data into the database. The new data should be present the next time you open your GEODASY software.
    
### Log format
    
The script uses keywords to identify the different pieces of information in the log and input them into the appropriate tables in the GEODASY database. Keywords shoud be followed by a colon `:` and then the information.
    
List of keywords:
* Project (for the project number)
* Hole (for the hole number)
* Depth (the depth in m of the top of a new strata, should be followed by a description)
* Description (for the description of the strata, at this stage this is long hand only)
* Samples (list of comma-separated samples, each sample should be made up of sample type - ES, EW, B, D, or U - and the depth it was taken at, e.g. D1.0)
* Groundwater (depth of any groundwater strikes)

An example log could comprise the following:
```
Project: LS3551
Hole: DS1
Depth: 0.0
Description: Soft sandy CLAY with coarse brick fragments. (MADE GROUND)
Depth: 0.5
Description: Firm orangey brown silty CLAY.
Depth: 2.0
Description: Very firm bluey grey silty CLAY. (LONDON CLAY)
Depth: 15.0
Description: END
Samples: ES0.3, B0.3, ES0.7, D0.7, D1.5, U2.0, U4.0, U6.5, U9.5, U12.5
Groundwater: 2.0
```
The Vision API accepts images in most major file formats including JPEG, PNG, TIFF, RAW etc. There is a [full list of supported file formats](https://cloud.google.com/vision/docs/supported-files 'Full list of supported file formats') in the documentation.
