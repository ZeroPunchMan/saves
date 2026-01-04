class SavePath:
    def __init__(self, src, dst, desc) -> None:
        self.src = src
        self.dst = dst
        self.desc = desc


sourcePath = {
    SavePath(
        "C:/ProgramData/Steam/ZumasRevenge/users",
        "./zumas_revenge/users",
        "ZumasRevenge",
    ),
    SavePath(
        "C:/Program Files (x86)/Steam/userdata/339055594/219990/remote",
        "./GD/remote",
        "GrimDawn",
    ),
}

# for test 
# sourcePath = [ 
#     SavePath("D:/test/abc", "./abc", "abc"),
#     SavePath("D:/test/def", "./def", "def"),
#     SavePath("D:/test/xyz", "./xyz", "xyz"),
# ]

import os
import shutil
import filecmp


def DirDeepCmp(cmp: filecmp.dircmp):
    if len(cmp.diff_files) != 0 or len(cmp.left_only) != 0 or len(cmp.right_only) != 0:
        return False
    else:
        for subCmp in cmp.subdirs.values():
            if DirDeepCmp(subCmp) == False:
                return False

    return True


for s in sourcePath:
    if os.path.isdir(s.src) == True:
        print("+++找到存档 {0}+++".format(s.desc))
        if os.path.isdir(s.dst) == True:
            cmp = filecmp.dircmp(s.src, s.dst)
            if DirDeepCmp(cmp) == True:
                print("\t***文件相同,跳过")
                continue
            else:
                print("\t***删除旧文件")
                shutil.rmtree(s.dst)

        shutil.copytree(s.src, s.dst)
        print("\t~~~~复制完成 {0}~~~~".format(s.desc))
    else:
        print("!!!未找到存档: {0}!!!".format(s.desc))

# need commit?
c = input("提交?(y/n)")
if c == "y" or c == "Y":
    info = input("提交日志:")
    os.system("git add .")
    cmd = 'git commit -m "{0}"'.format(info)
    os.system(cmd)
else:
    os.system("echo no commit")

os.system("pause")
