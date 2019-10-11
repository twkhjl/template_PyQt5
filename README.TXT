參考資料:
https://stackoverflow.com/questions/54168748/qt-creator-fails-to-open-on-windows-10-no-qt-platform-plugin-could-be-initializ
https://stackoverflow.com/questions/51324754/python-3-6-x-pyinstaller-gives-error-no-module-named-pyqt5-sip
https://github.com/pyinstaller/pyinstaller/issues/4293
https://github.com/pyinstaller/pyinstaller/blob/master/PyInstaller/loader/rthooks/pyi_rth_pyqt5.py
https://github.com/pyinstaller/pyinstaller/issues/2573
https://www.jianshu.com/p/73d41faaf469

安裝PyQt5可參考:

https://dotblogs.com.tw/zeus83157/2018/06/23/011440
*請參考如何安裝即可!!!!

pip install pyqt5
(我安裝時是使用pip3 install pyqt5,不知有無差別)
pip install pyqt5-tools


designer.exe路徑(會因python安裝路徑不同而有差別):
C:\python\Lib\site-packages\pyqt5_tools\Qt\bin\designer.exe

designer是PyQt5的gui編輯器.
實際使用請參考:
https://www.youtube.com/watch?v=UjxQRdmvC1k
http://bmharwani.com/blog/python-gui-tutorial-1-pyqt5-using-qt-designer/




此資料夾為空白的Pyqt5模板,
用於建立新專案的模板之用.

updateUI.bat:
使用designer.exe編輯完UI_main.ui後,
可執行此檔案快速產生UI_main.py
若UI_main.ui檔有變更名稱,此檔案也需編輯修改名稱

deploy.bat:
可將程式碼編譯為可執行檔(.exe)
此檔案的路徑預設為:
C:\python\Lib\site-packages\PyQt5\Qt\bin
若python安裝路徑不同則需做修改


*需先安裝pyinstaller
*python安裝路徑在deploy.bat預設為c:\python,
若路徑不同請編輯此檔案修改python路徑

exec.bat:
用於測試.exe檔是否運作正常.
亦可使用vscode的命令列去運行
dist\main.exe

-----------------------------

dist\platforms\qwindows.dll
有可能會需要更新,

可從以下路徑"複製"新檔案
(不是蓋過以下路徑的檔案!!!!!
qwindows.dll要以下方路徑的為準!!!!
python路徑視實際安裝路徑做修改):

C:\python\Lib\site-packages\PyQt5\Qt\plugins\platforms

