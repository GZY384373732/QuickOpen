import configparser

def configReader():
    cf = configparser.ConfigParser(allow_no_value=True)
    cf.read("config.ini", encoding='utf-8')

    #一个[]称为一个section
    # sec = cf.sections()
    # print(sec)

    #section下面的键称为option,整个键值对称为item
    # options = cf.options("Softs")
    # print(options)
    items = cf.items("Softs")
    # print(items[0])
    # print(cf.get("Softs","QQ"))

    #根据函数需要,提前转换为dict返回
    dt = dict(zip([k for k,v in items],[v for k,v in items]))
    return dt

# configReader()

def configAppend(k,v):
    cf = configparser.ConfigParser(allow_no_value=True)
    cf.read("config.ini", encoding='utf-8')
    cf.set("Softs",k,v)
    cf.write(open("config.ini","r+"))


# configAppend("test","test1")