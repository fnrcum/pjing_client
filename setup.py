from distutils.core import setup
import py2exe

Mydata_files = [('images', ['icon.ico']), ('', ['freesansbold.ttf']), ('', ['msvcp90.dll'])]

setup(
    # options={'py2exe': {'bundle_files': 3, 'compressed': True, "includes": ["sip"]}},
    windows=[{
        "script": "pJing.py",
        "icon_resources": [(1, "icon.ico")],
        "dest_base": "pJing"
    }],
    data_files=Mydata_files
)
