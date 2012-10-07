import sublime, sublime_plugin
import ctypes, re

#------------------------------------------------------------------------------
class WindowManager:

	EnumWindows = ctypes.windll.user32.EnumWindows
	EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
	IsWindowVisible = ctypes.windll.user32.IsWindowVisible
	GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
	GetWindowText = ctypes.windll.user32.GetWindowTextW
	GetClassName = ctypes.windll.user32.GetClassNameW
	SetForegroundWindow = ctypes.windll.user32.SetForegroundWindow
	KeyboardEvent = ctypes.windll.user32.keybd_event
	MessageBox = ctypes.windll.user32.MessageBoxA

	def __init__(self):
		self.current_window_handle = None

	def __enum_windows_callback(self, hwnd, lParam):
		if WindowManager.IsWindowVisible(hwnd):
			length = WindowManager.GetWindowTextLength(hwnd) + 1
			ubuffer = ctypes.create_unicode_buffer(length)
			WindowManager.GetWindowText(hwnd, ubuffer, length)
			window_text = ubuffer.value
			ubuffer2 = ctypes.create_unicode_buffer(256)
			WindowManager.GetClassName(hwnd, ubuffer2, len(ubuffer2))
			window_class_name = ubuffer2.value
			char_pointer = ctypes.cast(lParam, ctypes.c_char_p)
			pattern = char_pointer.value
			if (window_class_name == u'SunAwtFrame') and (re.match(pattern, window_text) != None):
				self.current_window_handle = hwnd
				return False # If we wanted every matching window, then we should NOT return false here (this line should be commented out)
		return True

	def find_matching_window(self, pattern):
		self.current_window_handle = None
		WindowManager.EnumWindows(WindowManager.EnumWindowsProc(self.__enum_windows_callback), ctypes.c_char_p(pattern))
		return self.current_window_handle

	def set_foreground_window(self):
		if self.current_window_handle != None:
			WindowManager.SetForegroundWindow(self.current_window_handle)

	def send_ctrl_plus_key_to_current_window(self, key):
		if self.current_window_handle != None:
			WindowManager.KeyboardEvent(0x11, 0, 0, 0) # CTRL is down
			WindowManager.KeyboardEvent(ord(key), 0, 0, 0) # key is down
			WindowManager.KeyboardEvent(ord(key), 0, 0x0002, 0) # key is up
			WindowManager.KeyboardEvent(0x11, 0, 0x0002, 0) # CTRL is up

#------------------------------------------------------------------------------
class RunProcessingSketchOnWindowsCommand(sublime_plugin.ApplicationCommand):

	def __init__(self):
		self.matching_windows = []
		self.first_matching_window = None

	def run(self):
		wndmgr = WindowManager()
		# Matches windows whose name matches a pattern like this: "<sketch> | Processing <version>"
		wndmgr.find_matching_window(".+ \| Processing .+")
		wndmgr.set_foreground_window()
		wndmgr.send_ctrl_plus_key_to_current_window('R')
		# DEBUG: MessageBox(None, str(wndmgr.current_window_handle), 'Plugin message', 0)
