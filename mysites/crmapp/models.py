from django.db import models

# Create your models here.

#基础对象
class BaseObject(models.Model):
	"""docstring for BaseObject"""
	#def __init__(self, arg):
	#	super(BaseObject, self).__init__()
	#	self.arg = arg
	#ID=models.IntegerField(default=1)
	Code=models.CharField(max_length=10,default='default code')
	Name=models.CharField(max_length=10,default='default name')
	CreateTime=models.DateTimeField(u'新建时间',auto_now_add=True,editable=True)	
	ModifyTime=models.DateTimeField(u'修改时间',auto_now_add=True,editable=True)
	Remark=models.CharField(max_length=1000)

	class Meta:
        abstract = True

#用户
class User(BaseObject):
	"""docstring for User"""
	#def __init__(self, arg):
	#	super(User, self).__init__()
	#	self.arg = arg
	PassWord=models.CharField(max_length=20,default='123')

#联系人，针对于客户在联系人
class Contacts(BaseObject):
	"""docstring for ClassName"""
	#def __init__(self, arg):
	#	super(ClassName, self).__init__()
	#	self.arg = arg
	Phone=models.IntegerField()
	#联系人所属客户
	Client=models.ForeignKey(Client, related_name = 'Client')
	#该联系人角色
	Role=models.CharField(max_length=100)
	#Remark特殊点
	#职位
	Position=models.CharField(max_length=100)
	WeChat=models.CharField(max_length=100)
	QQ=models.CharField(max_length=50)
	Email=models.EmailField(
        _('email address'), max_length=255, unique=True, db_index=True)
	#关联联系人
	Contacts=models.ForeignKey(self,related_name='RelationContacts')

		
#跟进记录
class FollowRecord(BaseObject):
	"""docstring for FollowRecord"""
	#def __init__(self, arg):
	#	super(FollowRecord, self).__init__()
	#	self.arg = arg
	RecordText=	models.CharField(max_length=1000)
	RecordUser=models.ForeignKey(User, related_name = 'Records')
	#这次跟进在联系人
	Contacts=models.ForeignKey(Contacts,related_name='ContactsRecords')
		
#客户
class Client(BaseObject):
	"""docstring for Client"""
	#def __init__(self, arg):
	#	super(Client, self).__init__()
	#	self.arg = arg
	CompanyName=models.CharField(max_length=50)
	#所属销售
	Owner=models.ForeignKey(User, related_name = 'Clients')
	#所属行业
	Industry=models.CharField(max_length=100)
	#意向产品
	IntentionalProducts=models.CharField(max_length=100)
	#购买点数
	PurchasePoint=models.IntegerField()
	#跟进记录
	FollowRecord=models.CharField(max_length=1000)
	#关联客户
	Clients=models.ForeignKey(self,related_name='RelationClients')
	#项目进程
	ProjectProcess=models.CharField(max_length=100)
	#联系人--在新增客户时可以新增多个联系人
	Contacts=models.ForeignKey(Contacts,related_name='ContactsRecords')
	#地址
	Address=models.CharField(max_length=1000)


		
