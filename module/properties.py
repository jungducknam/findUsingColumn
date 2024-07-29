def getAttributes():
    attributes = {}
    with open('./info.txt', 'r', encoding='utf-8') as file:
        content = file.read().strip()
        items = content.split(',')
        for item in items:
            key, value = item.split('=')
            attributes[key.strip()] = value.strip()
    return attributes
