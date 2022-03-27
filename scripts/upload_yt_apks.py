import os
os.chdir("..")
os.chdir("api")

for path_1 in os.listdir():
    os.chdir(path_1)
    os.chdir("apks")
    for path_2 in os.listdir():  # v 16.29.39
        os.chdir(path_2)
        for path_3 in os.listdir():  # root , nonroot
            os.chdir(path_3)
            for path_4 in os.listdir():  # arch, language, theme
                # use -f so it ignores .gitignore
                print(f"{path_1}, {path_2}, {path_3}, {path_4}")
                os.system(f"git add -f {path_4}")
                os.system(
                    f"git commit -m 'Added /api/{path_1}/apks/{path_2}/{path_3}/{path_4}/'")
                os.system("git push")
            os.chdir("..")
        os.chdir("..")
    os.chdir("../..")
