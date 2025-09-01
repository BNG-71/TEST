import platform
b = platform.architecture()[0]
if b == '64bit':
    import nv8
else:
    print("32bit Not Supported!")
