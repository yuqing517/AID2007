'''
hash加密
'''
import hashlib

# md5 = hashlib.md5()   #创建MD5加密对象  # 应用MD5算法（sha1,sha256,sha384,sha512等）
# data_1 = "123456"
# md5.update(data_1.encode('utf-8')) # update() 传入要加密的字符串 .encode("utf-8")  把传入的字符串转换为utf-8格式的字节流
#
# data_2=md5.hexdigest()  # hexdig()  获取到机密后的密文 用date_2接收
# print(data_2)
# print(type(data_2))

# md6 = hashlib.md5()
# md6.update("123456123456".encode("utf-8"))
# print(md6.hexdigest())
# md5.update(data_1.encode('utf-8'))  # 再次使用md5对象进行加密的时候 相当于在之前传入的字符串的基础上叠加的新字符串
# data_3=md5.hexdigest()
# print(data_3)   # 这里的data_3 相当于是 "hello worldhello world" 加密之后的密文
# print(type(data_3))

# # 加盐加密：
# md5 = hashlib.md5('!@#$%^&*()'.encode('utf-8'))  # 在创建MD5加密对象的时候向hashlib.md5()中传入参数(任意字符串) 这样的方法称之为加盐加密
# md5.update("aaa123aaa456".encode('utf-8'))
# print(md5.hexdigest())  # 得到的加密后的密文是不容易破解的


 # 下面是模拟登录  都是之前学过的东西
# #
def md5(arg):#这是加密函数，将传进来的函数加密
    md5_pwd = hashlib.md5('/!@#$%^&*()_+'.encode('utf-8'))
    md5_pwd.update(arg.encode('utf-8'))
    return md5_pwd.hexdigest()#返回加密的数据

def log(user,pwd):#登陆时候时候的函数，由于md5不能反解，因此登陆的时候用正解
    with open('db.txt', 'r', encoding='utf-8') as f:
        for line in f:
            u,p=line.strip().split('|')
            if u ==user and p == md5(pwd):#登陆的时候验证用户名以及加密的密码跟之前保存的是否一样
                return True
        return False

def register(user,pwd):#注册的时候把用户名和加密的密码写进文件，保存起来
    with open('db.txt', 'w', encoding='utf-8') as f:
        temp = user + '|' + md5(pwd)
        print(temp)
        f.write(temp)


i=input('1表示登陆，2表示注册：')
if i=='2':
    user = input('用户名：')
    pwd =input('密码：')
    register(user,pwd)
elif i=='1':
    user = input('用户名：')
    pwd =input('密码：')
    r=log(user,pwd)#验证用户名和密码
    if r ==True:
        print('登陆成功')
    else:
        print('登录失败')
else:
    print('账号不存在')
