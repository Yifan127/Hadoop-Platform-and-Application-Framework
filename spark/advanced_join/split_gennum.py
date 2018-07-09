def split_show_views(line):
    key_value = line.split(",")
    show = key_value[0]
    views = key_value[1]
    return (show, views)
