#coding:utf-8
from django.db import models

from .model import BaseModel

from datetime import datetime



class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='yonghuzhanghao'


    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='yonghuzhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuzhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='用户账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    yonghuxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    pquestion=models.CharField ( max_length=255, null=True, unique=False, verbose_name='密保问题' )
    panswer=models.CharField ( max_length=255, null=True, unique=False, verbose_name='密保答案' )
    status=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='状态' )
    '''
    yonghuzhanghao=VARCHAR
    mima=VARCHAR
    yonghuxingming=VARCHAR
    xingbie=VARCHAR
    touxiang=Text
    lianxidianhua=VARCHAR
    pquestion=VARCHAR
    panswer=VARCHAR
    status=Integer
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'
class paotui(BaseModel):
    __doc__ = u'''paotui'''
    __tablename__ = 'paotui'

    __loginUser__='paotuizhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='paotuizhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    paotuizhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='跑腿账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    paotuixingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='跑腿姓名' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    pquestion=models.CharField ( max_length=255, null=True, unique=False, verbose_name='密保问题' )
    panswer=models.CharField ( max_length=255, null=True, unique=False, verbose_name='密保答案' )
    status=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='状态' )
    '''
    paotuizhanghao=VARCHAR
    mima=VARCHAR
    paotuixingming=VARCHAR
    touxiang=Text
    xingbie=VARCHAR
    lianxidianhua=VARCHAR
    pquestion=VARCHAR
    panswer=VARCHAR
    status=Integer
    '''
    class Meta:
        db_table = 'paotui'
        verbose_name = verbose_name_plural = '跑腿'
class shangpinfenlei(BaseModel):
    __doc__ = u'''shangpinfenlei'''
    __tablename__ = 'shangpinfenlei'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shangpinfenlei=models.CharField ( max_length=255,null=False,unique=True, verbose_name='商品分类' )
    '''
    shangpinfenlei=VARCHAR
    '''
    class Meta:
        db_table = 'shangpinfenlei'
        verbose_name = verbose_name_plural = '商品分类'
class shangpinxinxi(BaseModel):
    __doc__ = u'''shangpinxinxi'''
    __tablename__ = 'shangpinxinxi'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='用协'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shangpinbianma=models.CharField ( max_length=255, null=True,unique=True, verbose_name='商品编码' )
    shangpinmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    shangpinfenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品分类' )
    shangpintupian=models.TextField   (  null=True, unique=False, verbose_name='商品图片' )
    shangpinguige=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品规格' )
    shangpinjiage=models.FloatField   (  null=True, unique=False, verbose_name='商品价格' )
    shangpinxiangqing=models.TextField   (  null=True, unique=False, verbose_name='商品详情' )
    shangpinzhuangtai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品状态' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户姓名' )
    clicktime=models.DateTimeField  (auto_now=True,  null=True, unique=False, verbose_name='最近点击时间' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    discussnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='评论数' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    shangpinbianma=VARCHAR
    shangpinmingcheng=VARCHAR
    shangpinfenlei=VARCHAR
    shangpintupian=Text
    shangpinguige=VARCHAR
    shangpinjiage=Float
    shangpinxiangqing=Text
    shangpinzhuangtai=VARCHAR
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    clicktime=DateTime
    clicknum=Integer
    discussnum=Integer
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'shangpinxinxi'
        verbose_name = verbose_name_plural = '商品信息'
class shangpingoumai(BaseModel):
    __doc__ = u'''shangpingoumai'''
    __tablename__ = 'shangpingoumai'



    __authTables__={'yonghuzhanghao':'yonghu','goumaizhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shangpinmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    shangpinfenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品分类' )
    shangpintupian=models.TextField   (  null=True, unique=False, verbose_name='商品图片' )
    shangpinjiage=models.FloatField   (  null=True, unique=False, verbose_name='购买价格' )
    goumaixiangqing=models.TextField   (  null=True, unique=False, verbose_name='购买详情' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户姓名' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    shouhuodizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='收货地址' )
    goumaizhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='购买账号' )
    goumaixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='购买姓名' )
    zhuangtai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='状态' )
    ispay=models.CharField ( max_length=255, null=True, unique=False,default='未支付', verbose_name='是否支付' )
    '''
    shangpinmingcheng=VARCHAR
    shangpinfenlei=VARCHAR
    shangpintupian=Text
    shangpinjiage=Float
    goumaixiangqing=Text
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    lianxidianhua=VARCHAR
    shouhuodizhi=VARCHAR
    goumaizhanghao=VARCHAR
    goumaixingming=VARCHAR
    zhuangtai=VARCHAR
    ispay=VARCHAR
    '''
    class Meta:
        db_table = 'shangpingoumai'
        verbose_name = verbose_name_plural = '商品购买'
class dingdanxinxi(BaseModel):
    __doc__ = u'''dingdanxinxi'''
    __tablename__ = 'dingdanxinxi'



    __authTables__={'goumaizhanghao':'yonghu','paotuizhanghao':'paotui','yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shangpinmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    shangpintupian=models.TextField   (  null=True, unique=False, verbose_name='商品图片' )
    goumaizhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='购买账号' )
    goumaixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='购买姓名' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    shouhuodizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='收货地址' )
    fahuoshijian=models.DateField   (  null=True, unique=False, verbose_name='发货时间' )
    fahuoxiangqing=models.TextField   (  null=True, unique=False, verbose_name='发货详情' )
    paotuizhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='跑腿账号' )
    paotuixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='跑腿姓名' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户姓名' )
    fahuozhuangtai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='发货状态' )
    '''
    shangpinmingcheng=VARCHAR
    shangpintupian=Text
    goumaizhanghao=VARCHAR
    goumaixingming=VARCHAR
    lianxidianhua=VARCHAR
    shouhuodizhi=VARCHAR
    fahuoshijian=Date
    fahuoxiangqing=Text
    paotuizhanghao=VARCHAR
    paotuixingming=VARCHAR
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    fahuozhuangtai=VARCHAR
    '''
    class Meta:
        db_table = 'dingdanxinxi'
        verbose_name = verbose_name_plural = '订单信息'
class dingdanpeisong(BaseModel):
    __doc__ = u'''dingdanpeisong'''
    __tablename__ = 'dingdanpeisong'



    __authTables__={'goumaizhanghao':'yonghu','paotuizhanghao':'paotui','yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shangpinmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    shangpintupian=models.TextField   (  null=True, unique=False, verbose_name='商品图片' )
    goumaizhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='购买账号' )
    goumaixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='购买姓名' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    shouhuodizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='配送地址' )
    peisongzhuangtai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='配送状态' )
    peisongshijian=models.DateField   (  null=True, unique=False, verbose_name='配送时间' )
    paotuizhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='跑腿账号' )
    paotuixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='跑腿姓名' )
    beizhu=models.TextField   (  null=True, unique=False, verbose_name='备注' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户姓名' )
    '''
    shangpinmingcheng=VARCHAR
    shangpintupian=Text
    goumaizhanghao=VARCHAR
    goumaixingming=VARCHAR
    lianxidianhua=VARCHAR
    shouhuodizhi=VARCHAR
    peisongzhuangtai=VARCHAR
    peisongshijian=Date
    paotuizhanghao=VARCHAR
    paotuixingming=VARCHAR
    beizhu=Text
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    '''
    class Meta:
        db_table = 'dingdanpeisong'
        verbose_name = verbose_name_plural = '订单配送'
class tixianxinxi(BaseModel):
    __doc__ = u'''tixianxinxi'''
    __tablename__ = 'tixianxinxi'



    __authTables__={'yonghuzhanghao':'yonghu','goumaizhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shangpinmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    shangpintupian=models.TextField   (  null=True, unique=False, verbose_name='商品图片' )
    shangpinjiage=models.FloatField   (  null=True, unique=False, verbose_name='资金' )
    tixianjine=models.CharField ( max_length=255, null=True, unique=False, verbose_name='提现金额' )
    tixianbeizhu=models.TextField   (  null=True, unique=False, verbose_name='提现备注' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户姓名' )
    goumaizhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='购买账号' )
    goumaixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='购买姓名' )
    '''
    shangpinmingcheng=VARCHAR
    shangpintupian=Text
    shangpinjiage=Float
    tixianjine=VARCHAR
    tixianbeizhu=Text
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    goumaizhanghao=VARCHAR
    goumaixingming=VARCHAR
    '''
    class Meta:
        db_table = 'tixianxinxi'
        verbose_name = verbose_name_plural = '提现信息'
class chatmessage(BaseModel):
    __doc__ = u'''chatmessage'''
    __tablename__ = 'chatmessage'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    uid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户ID' )
    fid=models.BigIntegerField  ( null=False, unique=False, verbose_name='好友用户ID' )
    content=models.CharField ( max_length=255, null=True, unique=False, verbose_name='内容' )
    format=models.IntegerField  (  null=True, unique=False, verbose_name='格式(1:文字，2:图片)' )
    isread=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='消息已读(0:未读，1:已读)' )
    '''
    uid=BigInteger
    fid=BigInteger
    content=VARCHAR
    format=Integer
    isread=Integer
    '''
    class Meta:
        db_table = 'chatmessage'
        verbose_name = verbose_name_plural = '消息表'
class friend(BaseModel):
    __doc__ = u'''friend'''
    __tablename__ = 'friend'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    uid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户ID' )
    fid=models.BigIntegerField  ( null=False, unique=False, verbose_name='好友用户ID' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='名称' )
    picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
    role=models.CharField ( max_length=255, null=True, unique=False, verbose_name='角色' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='表名' )
    alias=models.CharField ( max_length=255, null=True, unique=False, verbose_name='别名' )
    type=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='类型(0:好友申请，1:好友，2:消息)' )
    '''
    uid=BigInteger
    fid=BigInteger
    name=VARCHAR
    picture=Text
    role=VARCHAR
    tablename=VARCHAR
    alias=VARCHAR
    type=Integer
    '''
    class Meta:
        db_table = 'friend'
        verbose_name = verbose_name_plural = '好友表'
class chat(BaseModel):
    __doc__ = u'''chat'''
    __tablename__ = 'chat'



    __authTables__={}
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    adminid=models.BigIntegerField  (  null=True, unique=False, verbose_name='管理员id' )
    ask=models.TextField   (  null=True, unique=False, verbose_name='提问' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复' )
    isreply=models.IntegerField  (  null=True, unique=False, verbose_name='是否回复' )
    isread=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='已读/未读(1:已读,0:未读)' )
    uname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户头像' )
    uimage=models.TextField   (  null=True, unique=False, verbose_name='用户名' )
    type=models.IntegerField  (  null=True, unique=False,default='1', verbose_name='内容类型(1:文本,2:图片,3:视频,4:文件,5:表情)' )
    '''
    userid=BigInteger
    adminid=BigInteger
    ask=Text
    reply=Text
    isreply=Integer
    isread=Integer
    uname=VARCHAR
    uimage=Text
    type=Integer
    '''
    class Meta:
        db_table = 'chat'
        verbose_name = verbose_name_plural = '智能客服'
class forum(BaseModel):
    __doc__ = u'''forum'''
    __tablename__ = 'forum'



    __authTables__={}
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255, null=True, unique=False, verbose_name='帖子标题' )
    content=models.TextField   ( null=False, unique=False, verbose_name='帖子内容' )
    parentid=models.BigIntegerField  (  null=True, unique=False, verbose_name='父节点id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    username=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    isdone=models.CharField ( max_length=255, null=True, unique=False, verbose_name='状态' )
    istop=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='是否置顶' )
    toptime=models.DateTimeField  (  null=True, unique=False, verbose_name='置顶时间' )
    typename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='分类名称' )
    cover=models.TextField   (  null=True, unique=False, verbose_name='封面' )
    isanon=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='是否匿名(1:是,0:否)' )
    delflag=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='是否删除(1:是,0:否)' )
    '''
    title=VARCHAR
    content=Text
    parentid=BigInteger
    userid=BigInteger
    username=VARCHAR
    avatarurl=Text
    isdone=VARCHAR
    istop=Integer
    toptime=DateTime
    typename=VARCHAR
    cover=Text
    isanon=Integer
    delflag=Integer
    '''
    class Meta:
        db_table = 'forum'
        verbose_name = verbose_name_plural = '留言信息'
class forumtype(BaseModel):
    __doc__ = u'''forumtype'''
    __tablename__ = 'forumtype'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    typename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='分类名称' )
    '''
    typename=VARCHAR
    '''
    class Meta:
        db_table = 'forumtype'
        verbose_name = verbose_name_plural = '留言信息类型'
class forumreport(BaseModel):
    __doc__ = u'''forumreport'''
    __tablename__ = 'forumreport'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    forumid=models.BigIntegerField  (  null=True, unique=False, verbose_name='论坛id' )
    title=models.CharField ( max_length=255, null=True, unique=False, verbose_name='帖子标题' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='举报用户id' )
    username=models.CharField ( max_length=255, null=True, unique=False, verbose_name='举报用户名' )
    reporteduserid=models.BigIntegerField  ( null=False, unique=False, verbose_name='被举报用户id' )
    reportedusername=models.CharField ( max_length=255, null=True, unique=False, verbose_name='被举报用户名' )
    reason=models.TextField   ( null=False, unique=False, verbose_name='举报原因' )
    picture=models.TextField   (  null=True, unique=False, verbose_name='图片补充' )
    handleadvise=models.TextField   (  null=True, unique=False, verbose_name='处理建议' )
    status=models.CharField ( max_length=255, null=True, unique=False,default='处理中', verbose_name='状态' )
    reporttype=models.CharField ( max_length=255, null=True, unique=False,default='主题帖举报', verbose_name='举报类型' )
    '''
    forumid=BigInteger
    title=VARCHAR
    userid=BigInteger
    username=VARCHAR
    reporteduserid=BigInteger
    reportedusername=VARCHAR
    reason=Text
    picture=Text
    handleadvise=Text
    status=VARCHAR
    reporttype=VARCHAR
    '''
    class Meta:
        db_table = 'forumreport'
        verbose_name = verbose_name_plural = '留言信息举报'
class newstype(BaseModel):
    __doc__ = u'''newstype'''
    __tablename__ = 'newstype'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    typename=models.CharField ( max_length=255,null=False, unique=False, verbose_name='分类名称' )
    '''
    typename=VARCHAR
    '''
    class Meta:
        db_table = 'newstype'
        verbose_name = verbose_name_plural = '公告资讯分类'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    __thumbsUp__='是'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='是'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    typename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='分类名称' )
    name=models.CharField ( max_length=255, null=True, unique=False, verbose_name='发布人' )
    headportrait=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    clicktime=models.DateTimeField  (auto_now=True,  null=True, unique=False, verbose_name='最近点击时间' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    typename=VARCHAR
    name=VARCHAR
    headportrait=Text
    clicknum=Integer
    clicktime=DateTime
    thumbsupnum=Integer
    crazilynum=Integer
    storeupnum=Integer
    picture=Text
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '公告资讯'
class storeup(BaseModel):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    refid=models.BigIntegerField  (  null=True, unique=False, verbose_name='商品id' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='表名' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='名称' )
    picture=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    type=models.CharField ( max_length=255, null=True, unique=False,default='1', verbose_name='类型' )
    inteltype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='推荐类型' )
    remark=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    '''
    userid=BigInteger
    refid=BigInteger
    tablename=VARCHAR
    name=VARCHAR
    picture=Text
    type=VARCHAR
    inteltype=VARCHAR
    remark=VARCHAR
    '''
    class Meta:
        db_table = 'storeup'
        verbose_name = verbose_name_plural = '收藏表'
class aboutus(BaseModel):
    __doc__ = u'''aboutus'''
    __tablename__ = 'aboutus'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    subtitle=models.CharField ( max_length=255, null=True, unique=False, verbose_name='副标题' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    picture1=models.TextField   (  null=True, unique=False, verbose_name='图片1' )
    picture2=models.TextField   (  null=True, unique=False, verbose_name='图片2' )
    picture3=models.TextField   (  null=True, unique=False, verbose_name='图片3' )
    '''
    title=VARCHAR
    subtitle=VARCHAR
    content=Text
    picture1=Text
    picture2=Text
    picture3=Text
    '''
    class Meta:
        db_table = 'aboutus'
        verbose_name = verbose_name_plural = '关于我们'
class systemintro(BaseModel):
    __doc__ = u'''systemintro'''
    __tablename__ = 'systemintro'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    subtitle=models.CharField ( max_length=255, null=True, unique=False, verbose_name='副标题' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    picture1=models.TextField   (  null=True, unique=False, verbose_name='图片1' )
    picture2=models.TextField   (  null=True, unique=False, verbose_name='图片2' )
    picture3=models.TextField   (  null=True, unique=False, verbose_name='图片3' )
    '''
    title=VARCHAR
    subtitle=VARCHAR
    content=Text
    picture1=Text
    picture2=Text
    picture3=Text
    '''
    class Meta:
        db_table = 'systemintro'
        verbose_name = verbose_name_plural = '系统简介'
class discussshangpinxinxi(BaseModel):
    __doc__ = u'''discussshangpinxinxi'''
    __tablename__ = 'discussshangpinxinxi'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    istop=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='置顶(1:置顶,0:非置顶)' )
    tuserids=models.TextField   (  null=True, unique=False, verbose_name='赞用户ids' )
    cuserids=models.TextField   (  null=True, unique=False, verbose_name='踩用户ids' )
    '''
    refid=BigInteger
    userid=BigInteger
    avatarurl=Text
    nickname=VARCHAR
    content=Text
    reply=Text
    thumbsupnum=Integer
    crazilynum=Integer
    istop=Integer
    tuserids=Text
    cuserids=Text
    '''
    class Meta:
        db_table = 'discussshangpinxinxi'
        verbose_name = verbose_name_plural = '商品信息评论表'
