from shutil import move
import os
import sys


Sorting_Folders = ["Images", "Videos", "Documents", "Executables", "Archives", "Other", "Audios"]

# create a list with only the folders in the directory
# all_folders = []
# for entry in os.scandir():
#     if entry.is_dir():
#         all_folders.append(entry)
# print("all folders: ",all_folders)

# create a list with only the files in the directory
all_files = []
for entry in os.scandir():
    if entry.is_file():
        if entry.name == os.path.basename(sys.argv[0]):
            continue
        else:
            all_files.append(entry)

# create sorting folders only if non exist
# for Sorting_folder in Sorting_Folders:
#     print("sorting folder: ", Sorting_folder)
#     for folder in all_folders:
#         print("each folder: ",folder)
#         if folder.name == Sorting_folder:
#             break
#     else:
#         os.mkdir(Sorting_folder)

# move files to appropriate places
for file in all_files:
    if file.name.endswith(".txt") or file.name.endswith(".doc") or file.name.endswith(".docx") or file.name.endswith(".htm") or file.name.endswith(".html") or file.name.endswith(".odt") or file.name.endswith(".pdf") or file.name.endswith(".xls") or file.name.endswith(".xlsx") or file.name.endswith(".ods") or file.name.endswith(".ppt") or file.name.endswith(".pptx"):
        if os.path.isdir('Documents'):
            move(file.name, f"Documents/{file.name}")
        else:
            os.mkdir('Documents')
            move(file.name, f"Documents/{file.name}")


    elif file.name.endswith(".png") or file.name.endswith(".jpg") or file.name.endswith(".jpeg") or file.name.endswith(".apng") or file.name.endswith(".avif") or file.name.endswith(".gif") or file.name.endswith(".svg") or file.name.endswith(".webp"):
        if os.path.isdir('Images'):
            move(file.name, f"Images/{file.name}")
        else:
            os.mkdir('Images')
            move(file.name, f"Images/{file.name}")

    elif file.name.endswith(".mp4") or file.name.endswith(".mov") or file.name.endswith(".avi") or file.name.endswith(".wmv") or file.name.endswith(".avchd") or file.name.endswith(".webm") or file.name.endswith(".flv"):
        if os.path.isdir('Videos'):
            move(file.name, f"Videos/{file.name}")
        else:
            os.mkdir('Videos')
            move(file.name, f"Videos/{file.name}")

    elif file.name.endswith(".zip") or file.name.endswith(".rar") or file.name.endswith(".7z") or file.name.endswith(".tar.bz2") or file.name.endswith(".tar.gz") or file.name.endswith(".zipx"):
        if os.path.isdir('Archives'):
            move(file.name, f"Archives/{file.name}")
        else:
            os.mkdir('Archives')
            move(file.name, f"Archives/{file.name}")

    elif file.name.endswith(".mp3") or file.name.endswith(".pcm") or file.name.endswith(".wav") or file.name.endswith(".aiff") or file.name.endswith(".aac") or file.name.endswith(".ogg") or file.name.endswith(".wma") or file.name.endswith(".flac") or file.name.endswith(".alac") or file.name.endswith(".mpeg"):
        if os.path.isdir('Audios'):
            move(file.name, f"Audios/{file.name}")
        else:
            os.mkdir('Audios')
            move(file.name, f"Audios/{file.name}")

    elif file.name.endswith(".exe") or file.name.endswith(".msi") or file.name.endswith(".bat") or file.name.endswith(".com") or file.name.endswith(".cmd") or file.name.endswith(".inf") or file.name.endswith(".ipa") or file.name.endswith(".osx") or file.name.endswith(".pif") or file.name.endswith(".run") or file.name.endswith(".wsh") or file.name.endswith(".appinstaller"):
        if os.path.isdir('Executables'):
            move(file.name, f"Executables/{file.name}")
        else:
            os.mkdir('Executables')
            move(file.name, f"Executables/{file.name}")

    else:
        if os.path.isdir('Other'):
            move(file.name, f"Other/{file.name}")
        else:
            os.mkdir('Other')
            move(file.name, f"Other/{file.name}")
    