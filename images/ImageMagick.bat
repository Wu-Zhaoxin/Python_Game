@echo off
echo ImageMagick fix libpng warning: iCCP: Not recognizing known sRGB profile ......
echo Search PNG in subdirs and process ...
set fn=C:\Program Files\ImageMagick-7.0.9-Q16\imdisplay.exe
for /f "tokens=*" %%i in ('dir/s/b *.png') do "C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\imdisplay.exe" "%%i" -strip "%%i"
pause