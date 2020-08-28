
from cx_Freeze import *
import sys

includefiles = ['mana.ico']
excludes = []
packages = []
base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

shortcut_table = [
    ("DesktopShortcut", #Shortcut
    "DesktopFolder", #Directory_
    "Student_manage_system_db_2", #Name
    "TARGETDIR", #component_
    "[TARGETDIR]\Student_manage_system_db_2.exe", # Target
    None, #Arguments
    None, #Description
    None, #Hotkey
    None, #Icon
    None, #IconIndex
    None, #showCmd
    "TARGETDIR", #wkdir
    )
]

msi_data = {"Shortcut": shortcut_table}

#Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}


setup(
    version="0.1",
    description = "Stuent Management System Developed by MMM",
    author = "MMM",
    name = "Student Management System",
    options = {'build_exe': {'include_files': includefiles}, "bdist_msi": bdist_msi_options, },
    executables = [
        Executable(
            script = "Student_manage_system_db_2.py",
            base = base,
            icon = "mana.ico",

            )
    ]
)

