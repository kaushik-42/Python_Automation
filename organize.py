import os
SUBDIRECTORIES = {
    "Documents": ['.pdf', '.txt', '.rtf'],
    "AUDIO": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png']
}


def pickDirectory(value):
    for category, sub in SUBDIRECTORIES.items():
        for s in sub:
            if(s == value):
                return category
    return 'MISC'


# print(pickDirectory('.pdf'))


def organizeDIr():
    for item in os.scandir(): # scandir is a function which is used to run through all the available files in that path!
        if item.is_dir != True:
            continue
        filepath = path(item)
        filetype = filepath.suffix.lower()
        directory = pickDirectory(filetype)
        dpath = path(directory)
        if dpath.is_dir() != True:
            dpath.mkdir()
        filepath.rename(dpath.joinpath(filepath))


organizeDIr()
