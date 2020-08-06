import glob
import re
import os

files = glob.glob("tmp/*il")
files.sort()

for f in files:
    basename = os.path.basename(f)
    version = f.replace('il_', '').replace('.il', '').replace('tmp/', '')

    with open(f) as il_file:
        print(version + ':')
        content = il_file.read()
        sdk_tools_version = None
        sdk_build_tools_version = None
        sdk_platform_tools_version = None
        sdk_platform_version = None
        ndk_version = None
        ndk_full = None

        m = re.search(r'kMinAndroidSDKToolsVersion = "([0-9\.]+)"', content)
        if (m is not None):
            sdk_tools_version = m.group(1)
        else: 
            m = re.search(r'kMinAndroidSDKToolsVersion = [a-z0-9]+\((\d+)\)', content)
            if (m is not None):
                sdk_tools_version = m.group(1)

        m = re.search(r'kMinAndroidSDKBuildToolsVersion = "([0-9\.]+)"', content)
        if (m is not None):
            sdk_build_tools_version = m.group(1)
        else:
            m = re.search(r'kMinAndroidSDKBuildToolsVersion = [a-z0-9]+\((\d+)\)', content)
            if (m is not None):
                sdk_build_tools_version = m.group(1)

        m = re.search(r'kMinAndroidSDKPlatformToolsVersion = [a-z0-9]+\((\d+)\)', content)
        if (m is not None):
            sdk_platform_tools_version = m.group(1)
        else:
            m = re.search(r'kMinAndroidSDKPlatformToolsVersion = [a-z0-9]+\((\d+)\)', content)
            if (m is not None):
                sdk_platform_tools_version = m.group(1)

        m = re.search(r'kMinAndroidSDKPlatformVersion = [a-z0-9]+\((\d+)\)', content)
        if (m is not None):
            sdk_platform_version = m.group(1)
        else:
            m = re.search(r'kMinAndroidSDKPlatformVersion = [a-z0-9]+\((\d+)\)', content)
            if (m is not None):
                sdk_platform_version = m.group(1)

        m = re.search(r'string k_Version = "([0-9a-z]+)"', content)
        if (m is not None):
            ndk_version = m.group(1)
        else:
            m = re.search(r'AndroidNdkVersion = "([0-9a-z\.]+)"', content)
            if (m is not None):
                ndk_version = m.group(1)

        m = re.search(r"ldc\.i4\.s (\d+)[\0-\377[:nonascii:]]*.*ldc.i4.(\d+)[\0-\377[:nonascii:]]*.*?ldc\.i4 (\d+)[\n].*", content)
        if (m is not None):
            ndk_full = m.group(1) + '.' + m.group(2) + '.' +  m.group(3)
        else:
            ndk_full = ''

        print("  sdk_tools_version: " + sdk_tools_version)
        print("  sdk_build_tools_version: " + sdk_build_tools_version)
        print("  sdk_platform_tools_version: " + sdk_platform_tools_version)
        print("  sdk_platform_version: " + sdk_platform_version)
        print("  ndk_version: " + ndk_version)
        print("  ndk_full: " + ndk_full)

    
