sql='insert into ?,?,?'
print(sql)
arg=[]
arg.append('sss')
arg.append('sss1')
arg.append('sss2')
sql=sql.replace('?','%s'), arg


print(sql)