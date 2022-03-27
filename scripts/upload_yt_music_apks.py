import os
os.chdir("..")
os.chdir("api")
os.chdir("v1")
os.chdir("music")

for path_1 in os.listdir():
    if path_1.endswith(".apk"):
        print(path_1)
        os.system(f"git add -f {path_1}")
        os.system(f"git commit -m 'Added /api/v1/music/{path_1}'")
        os.system("git push")
    else:
        os.chdir(path_1)  # 4.02 ...
        for path_2 in os.listdir():
            if path_2.endswith(".apk"):
                print(f"{path_1} , {path_2}")
                os.system(f"git add -f {path_2}")
                os.system(
                    f"git commit -m 'Added /api/v1/music/{path_1}/{path_2}'")
                os.system("git push")
            os.chdir("stock")
            for path_3 in os.listdir():
                print(f"{path_1}, {path_2} , {path_3}")
                os.system(f"git add -f {path_3}")
                os.system(
                    f"git commit -m 'Added /api/v1/music/{path_1}/stock/{path_3}'")
            os.chdir("..")
        os.chdir("..")
