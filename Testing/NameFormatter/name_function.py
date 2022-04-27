
# def formatName(first_name, last_name):
#     formated = f"{first_name} {last_name}"
#     return formated.title()
    

def formatName(first_name, last_name, middle_name=''):
    if middle_name:
        formated = f"{first_name} {middle_name} {last_name}"
    else:
        formated = f"{first_name} {last_name}"    
    return formated.title()
