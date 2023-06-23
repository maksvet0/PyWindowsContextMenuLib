import os
import time


class WindowsContextMenuLib:
    def add_folder(self, folder_name):
        if folder_name is None or folder_name == '' or folder_name == ' ':
            print("WindowsContextMenuLib error: folder_name is None or ' '")
        else:
            try:
                os.system(f'reg add "HKEY_CLASSES_ROOT\*\shell\\{folder_name}"')
            except PermissionError:
                print('WindowsContextMenuLib error: none permission.Please run this app for admin')
            except Exception as e:
                print(f'WindowsContextMenuLib error: {e}')


if __name__ == '__main__':
    wcml = WindowsContextMenuLib()
    wcml.add_folder('HelloWorld')
    time.sleep(1000)
