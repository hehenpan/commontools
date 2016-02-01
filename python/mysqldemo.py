import os
import MySQLdb
import random

def get():
	conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='MjU5YjE3ZGUw',port=3306)
	cur=conn.cursor()
	sql="select * from mae.dockerfile_template_info"
	'''
	value=[1,'hi rollen']
    cur.execute('insert into test values(%s,%s)',value)
	'''
	while True:
		cur.execute(sql)
		result=cur.fetchone()
		print result

		
def insert():
	conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='YTk3NWNjMWMy',port=3306)
	cur=conn.cursor()
	count=0
	sql='insert into mytest.image_info(image_id,project_id,git_tag,image_md5)values(%s,%s,%s,%s)'
	for item in range(0,1000000,1):
		value=(str(random.random()),"project_id","git_tag","image_md5")
		cur.execute(sql,value)
		conn.commit()
		count=count+1
		if count%1000==0:
			print count
	cur.close()
	conn.close()
	#
	
if __name__=='__main__':
	#get()
	insert()
	print 'hello'