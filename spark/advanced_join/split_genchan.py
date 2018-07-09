def split_show_channel(line):
    key_value = line.split(",")
    show = key_value[0]
    channel = key_value[1]
    return (show, channel)
