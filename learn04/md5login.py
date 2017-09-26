import hashlib,getpass
db={
    #'michael': 'e10adc3949ba59abbe56e057f20f883e',
    #'bob': '878ef96e86145580c38c87f0410ad153',
    #'alice': '99b1c2188db85afee403b1536010c2c9'
}
MD5='the-Salt'
class userlib(object):
    def get_md5(self,password):
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        return md5.hexdigest()

    def calc_md5(self,password):
        return self.get_md5(password+MD5)

    def register(self,username, password):
        try:
            db[username] = self.calc_md5(password + username)
        except:
            return False
        return True

    def login(self,user, password):
        password=self.calc_md5(password+user)
        for x in db:
            if user==x and password==db[x]:
                return True
            else:
                return '%s not found' % user

if __name__ == '__main__':

    def do_login():
        username = input('please your username:')
        password = input('password:')
        user = userlib()
        re = user.login(username, password)
        if re:
            print('login success. welcome %s' % username)

    def do_register():
        username = input('please your username:')
        password = input('password:')
        user = userlib()
        code = user.register(username, password)
        print(code)
        if code:
            print('注册成功！')
            print('login start...')
            do_login()
        else:
            print('注册失败！')
            print('register restart...')
            do_register()
print('register start...')
do_register()

