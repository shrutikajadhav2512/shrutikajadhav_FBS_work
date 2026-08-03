def emp(id,name,sal,dept):
    data='ID:'+str(id)+'\n'
    data+='Name:'+str(name)+'\n'
    data+='Salary:'+str(sal)+'\n'
    data+='Department:'+str(dept)+'\n'
    return data
res=emp(name='sai',id=101,sal=50000,dept='DS')
print(res)