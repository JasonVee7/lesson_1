import sys

print("Python Path:")
for path in sys.path:
    print(path)


print("Platform:")
print(sys.platform)


print("System Encoding:")
print(sys.getdefaultencoding())

print("Python Compiler:")
print(sys.implementation.name)
print("Python Compiler Version:")
print(sys.implementation.version)

print("Available Python Modules:")
print(sys.builtin_module_names)