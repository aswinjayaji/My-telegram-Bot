from datetime import datetime

def sample_response(input_text):
    user_input = str(input_text).lower()
    
    if user_input in ("hello","hi","hai"):
        return "Hello Mwonuse"
    if user_input in ("time","Time"):
        now=datetime.now() 
        return str(now.strftime("%d/%m/%y,%H:%M:%S"))
    return "I didn't understand"