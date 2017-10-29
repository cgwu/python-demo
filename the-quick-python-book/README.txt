重新导入模块:
>>> import imp
>>> imp.reload(module_name)

python 在centos下找不到tkinter,解决办法:

yum update python
yum install tkinter
yum -y install tcl-devel tk-devel

另外，python在3版本之后，Tkinter变成了tkinter，
python 2.x 为import Tkinter
python 3.x 为import tkinter

