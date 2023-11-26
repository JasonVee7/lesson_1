import sys

print("Python Version Checker")
print("You are currently using Python", sys.version.split()[0])


print("Installed Python versions:")
for path in sys.path:
    if "python" in path.lower():
        print(path)
