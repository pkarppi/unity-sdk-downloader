import json
import subprocess
import os
from urllib.parse import urlparse
import shutil

def downloadInstallerAndUnpack(version, downloadUrl):
    il_target = f'tmp/il_{version}.il'

    # Have it already?
    if os.path.exists(il_target):
        return

    a = urlparse(downloadUrl)
    basename = os.path.basename(a.path)
    subprocess.call(["wget", "-Ptmp", downloadUrl])
    exe = f'tmp/{basename}'
    unpack_folder = "tmp/install"

    if not os.path.exists(unpack_folder):
        os.mkdir(unpack_folder)

    # Unpack
    subprocess.call(["7z", '-aoa', '-y', f'-o{unpack_folder}',  "e", exe])
    dll =  'tmp/install/UnityEditor.Android.Extensions.dll'
    
    if os.path.exists(dll):
        result = subprocess.run(['ilspycmd', '-il', dll],  stdout=subprocess.PIPE)
        with open(il_target, 'w') as f:
            f.write(result.stdout.decode("utf-8"))
    else:
        print("NOT FOUND !!!")

    # Delete install folder 
    shutil.rmtree(unpack_folder)

    # Delete exe
    os.remove(exe)


with open('windows-versions.json') as json_file:
    data = json.load(json_file)
    for release in data:
        print (release['version'])

        # Get android module 
        android =  next((module for module in release['modules'] if module['id'] == "android"), None)
        if android != None:
            downloadUrl = android['downloadUrl']
            downloadInstallerAndUnpack(release['version'], downloadUrl)

