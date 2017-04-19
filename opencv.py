#coding=utf-8
#qpy:kivy

from jnius import autoclass
from jnius import cast

#part 1
'''
Stack=autoclass('java.util.Stack')
stack=Stack()
stack.push('Hello')
stack.push('World')
print stack.pop()
print stack.pop()
'''

#part2

System=autoclass('java.lang.System')
#System.out.println("hello world")
System.loadLibrary('/data/app/org.opencv.engine-1/lib/arm64/libopencv_java3.so')


#part3
'''
DisplayMetrics = autoclass('android.util.DisplayMetrics')
metrics = DisplayMetrics()
print 'DPI', metrics.getDeviceDensity()
'''

#part4
'''
Format=autoclass('java.text.SimpleDateFormat')
Date=autoclass('java.util.Date')
fm=Format('HH:mm:ss')
dt=Date()
print fm.format(dt)
'''

#part5
'''
PythonActivity=autoclass('org.renpy.android.PythonActivity')
Intent=autoclass('android.content.Intent')
Uri=autoclass('android.net.Uri')

intent=Intent()
intent.setAction(Intent.ACTION_VIEW)
intent.setData(Uri.parse('http://kivy.org'))
currentActivity=cast('android.app.Activity',PythonActivity.mActivity)
currentActivity.startActivity(intent)
'''