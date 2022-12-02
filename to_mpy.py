#!/usr/bin/env python3
import argparse
import os
import os.path
import shutil

# argparser = argparse.ArgumentParser(description="Compile all .py files to .mpy recursively")
# argparser.add_argument("-o", "--out", help="output directory (default: input dir)")
# argparser.add_argument("--target", help="select MicroPython target config")
# argparser.add_argument("dir", help="input directory")
# args = argparser.parse_args()

TARGET_OPTS = {
    "unix": "",
    "baremetal": "",
}

args_dir = "app"
args_out = "mpy_app"

if not args_out:
    args_out = args_dir

path_prefix_len = len(args_dir) + 1

for path, subdirs, files in os.walk(args_dir):
    for f in files:
        if f.endswith(".py"):
            fpath = path + "/" + f
            # print(fpath)
            out_fpath = args_out + "/" + fpath[path_prefix_len:-3] + ".mpy"
            out_dir = os.path.dirname(out_fpath)
            if not os.path.isdir(out_dir):
                os.makedirs(out_dir)
            cmd = "mpy-cross -v -s %s %s -o %s" % (
                fpath[path_prefix_len:],
                fpath,
                out_fpath,
            )
            # print(cmd)
            res = os.system(cmd)
            assert res == 0
        else:
            fpath = path + "/" + f
            out_fpath = args_out + "/" + fpath[path_prefix_len:-3]
            _out = args_out + "/" + fpath[path_prefix_len:]
            out_dir = os.path.dirname(out_fpath)
            if not os.path.isdir(out_dir):
                if fpath[0:2] != out_dir[0:2]:
                    os.makedirs(out_dir)
            shutil.copy(fpath, _out)
