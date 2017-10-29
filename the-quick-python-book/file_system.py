#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import glob # old UNIX function that did pattern matching
import shutil
# module shutil: offers a number of high-level operations on files and collections of files.
#In particular, functions are provided which support file copying and removal

#当前工作目录
old_pwd = os.getcwd()
print(os.getcwd())
print('curdir: ',os.curdir)
print('pardir: ',os.pardir)
print('listdir: ',os.listdir(os.curdir))
#更改当前工作目录
os.chdir("/home/sam/workspace")
print('新的当前目录:',os.getcwd())
print(os.listdir(os.curdir))
os.chdir(old_pwd)

#路径操作
print(type(os.getcwd()))
path1 = os.path.join(os.getcwd(),'bin/foo','utils','disktools','beauty.jpg')
print(os.path.join(os.getcwd(),'bin/foo','utils','disktools'))
print(os.path.join(os.getcwd(),'bin/foo','utils','disktools').split('/'))
print(os.path.split(os.path.join(os.getcwd(),'bin/foo','utils','disktools')))
print(os.path.basename(path1))
print(os.path.dirname(path1))
print(os.path.splitext(path1))
#环境变量扩展
print(os.path.expandvars('$HOME/workspace'))
print(os.path.expandvars('$QTDIR/workspace'))

workspace_dir = os.path.expandvars('$HOME/workspace')
print(os.path.exists(path1))
print('exists: ',os.path.exists(workspace_dir))
print('isdir: ',os.path.isdir(workspace_dir))
print('isfile: ',os.path.isfile(workspace_dir))

print(glob.glob('*'))
print(glob.glob('f*.py'))
print(glob.glob('f?.txt'))
print(glob.glob('f[0-9].txt'))
#文件重命名
os.rename('f1.txt', 'f9.txt')
print(glob.glob('*.txt'))
#复制文件
open('f9_copy.txt','wb').write( open('f9.txt','rb').read() )
print(glob.glob('*.txt'))
os.rename('f9_copy.txt','f1.txt')
os.remove('f9.txt')

#目录操作
os.makedirs('a/b', exist_ok=True)
os.removedirs('a/b')
os.makedirs('a/b', exist_ok=True)
print(glob.glob('*'))
shutil.rmtree('a')
#遍历目录，含子目录
for root, dirs, files in os.walk('/home/sam/workspace/python-demo'):
    print("{0} has {1} files,{2}".format(root, len(files), dirs))


