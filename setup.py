import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os","pyttsx3.drivers","pyttsx3.drivers.dummy","pyttsx3.drivers.espeak","pyttsx3.drivers.nsss","pyttsx3.drivers.sapi5","pyttsx3.drivers._espeak"],"include_files":[ "datasets","heart.ico","datasets/cleveland.csv"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="HDP SYSTEM",
    version="1.0",
    description="heart Disease Prediction System",
    options={"build_exe": build_exe_options},
    author="Mr. Ezekiel",
    executables=[Executable("heart_disease_pred.py", base=base,icon='heart.ico')],
)