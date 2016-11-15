from distutils.core import setup
import py2exe

Mydata_files = [('images', ['icon.ico']), ('', ['freesansbold.ttf'])]

setup(
    windows=[{
        "script": "pJing.py",
        "icon_resources": [(0, "icon.ico")],
        "dest_base": "pJing"
    }],
    data_files=Mydata_files
)
