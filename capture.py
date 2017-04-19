#coding=utf-8
#qpy:console
#qpy:2

from androidhelper import Android as D
d=D()
import time

d.recorderCaptureVideo('/sdcard/qpy/test.3gp')
time.sleep(3600)
d.recorderStop()