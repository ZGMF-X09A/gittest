with open('D:/gittest/pythoncoding/basic/hello.py', 'r') as f:
    for line in f.readlines():
        print(line.strip())
        
with open('D:/gittest/pythoncoding/basic/hello2.py', 'w') as f:
    f.write('Hello, World!')