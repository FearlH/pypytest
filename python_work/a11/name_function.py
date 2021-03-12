def get_formatted_name(firstname,lastname,middlename=""):
    if middlename:
        full_name=f"{firstname} {middlename} {lastname}"
    else:
        full_name=f"{firstname} {lastname}"
    return full_name.title()
