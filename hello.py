"""
echo "# cs102" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/vsevolodfomin/cs102.git
git push -u origin master
"""

def message():
    a = int(1)
    b = int(2)
    c = (a, b)
    print((a, b))

if __name__ == "__main__":
    message()
