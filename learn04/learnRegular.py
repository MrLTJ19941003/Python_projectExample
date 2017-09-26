import re

def EmailCheck(EmailAdress):
    print('EmailAdress check start...')
    if re.match(r'^([a-zA-Z0-9\.\_]+)\@([a-zA-Z0-9\_]+)\.([a-zA-Z]+)$',EmailAdress):
        print('%s is yes' % EmailAdress)
    else:
        print('%s is No' % EmailAdress)
    print('EmailAdress check end')

def EmailCheckAndSpilt(EmailAdress):
    print('EmailAdress checkAndSpilt start...')
    m=re.match(r'^((\<([\w]+[\s]+[\w]+)\>)([\s]+[\w]+\.[\w]+))\@(\w)+\.([a-zA-Z]+)$',EmailAdress)
    if m:
        print('match')
        print(m.groups())
    else:
        print('Not Match')
    print('EmailAdress checkAndSpilt start...')

def spiltEmail(EmailAdress):
    s=re.split(r'[\s\@]',EmailAdress)
    print(s)

if __name__ == '__main__':
    #<Tom Paris> Bill.Gates@voyager.org
    # <Tom Paris> Tom@voyager.org
    Emailadress=input('please enter the email address: ')
    #EmailCheck(Emailadress)
    #EmailCheckAndSpilt(Emailadress)
    spiltEmail(Emailadress)