def oxford_comma(items):
    if len(items) > 2:
        last_index = len(items)-1
        first_section_list = items[0:last_index]
        first_section_string = ", ".join(first_section_list)
        last_item_string = items[-1]
        combined_strings_list = [first_section_string, last_item_string]
        string = ", and ".join(combined_strings_list)
    else:
        string = " and ".join(items)
    return string
