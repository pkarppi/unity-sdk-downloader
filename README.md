# unity-sdk-downloader

Download and extract `UnitySetup-Android-Support-for-Editor-*.exe`, decompile `UnityEditor.Android.Extensions.dll` and search for android JDK, NDK and SDK versions.

## Requirements

* Python 3
* [`7z` from 7zip](https://www.7-zip.org/)
* [`ilspycmd` from icsharpcode/ILSpy](https://github.com/icsharpcode/ILSpy)

## Usage

```bash
python3 fetch.py
python3 resolve.py
```

Results are stored in `versions.yml`

## License

[MIT](LICENSE.md) © [Petteri Karppinen](https://github.com/pkarppi)
