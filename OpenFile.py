fpath = r'强解普通策略数据迁移到NGE说明.docx'

with open(fpath,"r") as file:
    print(file.read())
# read and write

def getConfig(filePath):
    with open(filePath, 'r',encoding="utf8") as f:
        return f.read()

def setConfig(filePath,content):
    with open(filePath, 'w',encoding="utf8") as f:
        return f.write(content)
