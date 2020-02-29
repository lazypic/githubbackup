#!/usr/bin/env python
import os

def main():
    cwd = os.getcwd()
    for d in os.listdir(cwd):
        if d == ".git":
            continue
        repo = cwd+"/"+d
        if not os.path.isdir(repo):
            continue
        os.chdir(repo)
        os.system("git pull")

if __name__ == "__main__":
    main()