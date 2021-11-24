def handwr_recog(API_key, log_img):

    import io
    import os
    import string
    from google.cloud import vision
    #you have to have this API-key (donloaded from the google vision projects
    #bit) in order for this to  work, pinngs it off to google using your account
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= API_key
    os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = 'roots.pem'
    client = vision.ImageAnnotatorClient()

    path = log_img

    with io.open(path, 'rb') as image_file:
            content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)
    
    #this gives you the text from the picture as one big long string
    text_string = response.full_text_annotation.text

    return text_string
