1.Doctor通过网页可以扫药品条码进行开药
2.根据库存通知药品厂商自动进药并配送过来
3.病人用户需要通过密码，或者指纹验证才能获取信息
4.Doctor看病人信息也需要病人验证
5.Doctor可以不通过验证看到已经开的处方，申请单，但是不能看到对应的病人
6.Doctor和病人及时聊天通讯，并进行对应管理，Doctor对自己病人进行管理，病人对自己的Doctors进行管理，家庭医生概念
7.采用密码器进行数据加密和验证？
8.病人录入自己的或者家人就诊信息功能
9.医生录入数据时，需要取得病人的同意，通过即时通讯取得同意
10.客户反馈系统



业务数据：

Record(录入记录):
	ID
	ClientID
	DoctorID
	IsSelfRecord(是否病人自己录入)
	CreateTime
	TreatTime(就诊时间)
	ModifyTime
	DeptID
	OrganizationID



DAs(记录明细):
	ID
	RecordID
	MediID(商品名ID)
	MediChemID(通用名ID)
	EachQuantity(每次用量)
	DoseUnit(计量单位)
	Quantity(数量)
	CalcUnit(计算单位)
	Frequency(频率)
	Useage(用法)

ImageRecord(记录对应图片):
	ID
	RecordID
	Image


基础数据：

Doctors(医生):
	ID
	Code
	Name
	IDCard
	Phone
	Email
	WeChat
	Age
	Sex
	Organization
	Dept
	FingerPrint
	PassWord
	CreateTime
	LastLogTime
	IsForbidden
	Remark



Clients(客户):								
	ID
	Code
	Name
	IDCard
	YBCard
	Phone
	Email
	WeChat
	Age
	Sex
	FingerPrint(指纹)
	PassWord
	Cipher(密码器)
	CreateTime
	LastLogTime
	Remark


Address(联系地址，发货地址):
	ID
	ClientID
	Address
	Contacts(联系人)
	Phone
	CreateTime
	Remark

Organization(机构):
	ID
	Code
	Name
	Phone
	ManagersID(管理人标识)
	Address
	CreateTime
	ModifyTime
	Remark



Dept(科室):
	ID
	Code
	Name
	Phone
	ManagersID
	Address
	CreateTime
	ModifyTime
	Remark


DrugStore(药房):
	ID
	Code
	Name
	Phone
	ManagersID
	Address
	CreateTime
	ModifyTime
	Remark


Medi(药品):
	ID
	MediChemID(通用名)
	Code(国药准字)
	Name
	Spec
	ProducerID(厂家)
	GuidePrice(指导价)
	DoseUnit(最小单位)
	DoseFactor(计量系数)
	OtpaUnit(门诊单位)
	OtpaPack(门诊包装系数)
	InpaUnit(住院单位)
	InpaPack(住院包装系数)
	HouseUnit(药库单位)
	HousePack(药库包装系数)
	Instructions(说明书)
	CreateTime
	ModifyTime
	Remark


MediChem(药品化学性质):
	ID
	Name(通用名)
	MediForm(药品剂型)


WordData(词汇字典)：
	ID
	MainID(字典目录)
	Name
	Remark


WordMain(字典目录)：
	ID
	Name