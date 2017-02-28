import time

#email alert functions

def get_subject():
    return 'BLEEP BLOOP!!'

def get_body():
    return 'it worked.....'

def get_audio_file_name():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    return str(timestr + '.wav')

