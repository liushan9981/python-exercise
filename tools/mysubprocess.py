# -*- coding: utf-8 -*-
import subprocess
import sys


def test_subprocess():
    # 最普遍的用法
    child = subprocess.Popen(['ls', '/home/liushan'], bufsize=4096, shell=False,
                           stdout=subprocess.PIPE, close_fds=True, stderr=subprocess.STDOUT)
    # 实际上执行的是sleep 300，通过ps 看到的是 bach-exec 300
    # child = subprocess.Popen(['bach-run', '300'], bufsize=4096, shell=False, executable='sleep',
    #                        stdout=subprocess.PIPE, close_fds=True, stderr=subprocess.STDOUT)

    # 使用其他的shell
    # child = subprocess.Popen('ls /home/liushan', bufsize=4096, shell=True, executable='/bin/bash',
    #                        stdout=subprocess.PIPE, close_fds=True, stderr=subprocess.STDOUT)

    while child.poll() is None:
        line = child.stdout.readline()
        line = line.rstrip().decode(encoding='utf8')
        sys.stdout.write('%s ' % str(line))
        sys.stdout.flush()

