#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class EmptyFileError(Exception):
    pass

filenames = ["myfile.txt","nonExist","emptyFile.txt"]
for file in filenames:
    try:
        f = open(file, 'r')
        line = f.readline()
        if line == "":
            f.close()
            raise EmptyFileError("%s: is empty" % file)
    except IOError as error:
        print("%s: could not be opened: %s" % (file, error.strerror))
    except EmptyFileError as error:
        print(error)
    else:
        #没有异常时执行
        print("%s: %s" % (file, line))
    finally:
        print("Done processing", file)


