1.在windows下安装pycrypto模块时，报错未找到'cl.exe'
  解决方法：
  安装对应的VC++ 库
2.安装VC++库后报错'cl.exe' failed out with status 2
  查看日志是报错目录下的inttypes.h里面intmax_t报错
  解决办法：
  把intmax_t和uintmax_t替换未int,安装好pycrypto后可以替换回去（不知道是否会有其他影响，所以暂时先替换回去）