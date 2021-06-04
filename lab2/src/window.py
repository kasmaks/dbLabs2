import win32gui
import ctypes


def get_name_of_active_window():
    w = win32gui
    return w.GetWindowText(w.GetForegroundWindow())


def change_window_title(login):
    ctypes.windll.kernel32.SetConsoleTitleW(login)
    return True



