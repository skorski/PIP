import glob
import os

def main():
    print("finding files")

    for filename in glob.iglob('test-dir/**/output', recursive=True):
        absPath = os.path.abspath(filename)
        yield absPath


if __name__ == "__main__":
    files = main()
    for file in files:
        print(file)