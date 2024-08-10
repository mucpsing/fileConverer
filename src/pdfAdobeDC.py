import winreg as reg
import pymupdf


def is_adobe_acrobat_installed():
    try:
        # 尝试打开Adobe Acrobat的注册表项
        # 注意：这里的路径可能因Adobe Acrobat的版本和安装选项而异
        # 这里使用的是Adobe Acrobat DC的通用路径，但可能需要根据实际情况调整
        with reg.OpenKey(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Adobe\Acrobat Reader\DC\Install") as key:
            # 尝试读取版本信息
            # 注意：这里的'Version'值可能不存在或名称不同，具体取决于Adobe Acrobat的安装和版本
            version, _ = reg.QueryValueEx(key, "Version")
            print(f"Adobe Acrobat Pro DC 已安装，版本为: {version}")
            return True
    except FileNotFoundError:
        # 如果注册表项不存在，可能意味着Adobe Acrobat未安装
        print("Adobe Acrobat Pro DC 未安装。")
        return False
    except Exception as e:
        # 处理其他可能的异常
        print(f"无法检测Adobe Acrobat Pro DC的安装情况：{e}")
        return False


if __name__ == "__main__":
    pass
