from django.db import models

# Create your models here.


class BookInfoManager(models.Manager):
    def all(self):
        return self.filter(is_delete=False)

"""
insert into tb_books(btitle,bpub_date,bread,bcomment,is_delete) values
"""
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, null=False, verbose_name='图书标题')
    bpub_date = models.DateField(verbose_name='发行日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    books = BookInfoManager()

    class Meta:
        db_table = 'tb_book'
        verbose_name = '图书'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.btitle

    def my_date(self):
        return self.bpub_date.strftime('%Y.%m.%d')

    my_date.short_description = '自定义发布时间'
    my_date.admin_order_field = 'bpud_date'


"""insert into tb_heros(hname,hgender,hbook_id,hcomment,is_delete) values"""
class HeroInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female'),
        (2, 'mid')
    )

    hname = models.CharField(max_length=20, null=False, verbose_name='英雄名字')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hbook = models.ForeignKey(BookInfo, verbose_name='所属图书')
    hcomment = models.CharField(max_length=200 ,null=True, verbose_name='描述')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_hero'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname

    def book_read(self):
        return self.hbook.bread

    book_read.short_description = '所属图书阅读量'
    book_read.admin_order_field = 'hbook.bread'



















"""insert into tb_book(btitle,bpub_date,bread,bcomment,is_delete) values
('射雕英雄传','1980-5-1',12,34,0),
('天龙八部','1986-7-24',36,40,0),
('笑傲江湖','1995-12-24',20,80,0),
('雪山飞狐','1987-11-11',58,24,0);



insert into tb_hero(hname,hgender,hbook_id,hcomment,is_delete) values
('郭靖',1,1,'降龙十八掌',0),
('黄蓉',0,1,'打狗棍法',0),
('黄药师',1,1,'弹指神通',0),
('欧阳锋',1,1,'蛤蟆功',0),
('梅超风',0,1,'九阴白骨爪',0),
('乔峰',1,2,'降龙十八掌',0),
('段誉',1,2,'六脉神剑',0),
('虚竹',1,2,'天山六阳掌',0),
('王语嫣',0,2,'神仙姐姐',0),
('令狐冲',1,3,'独孤九剑',0),
('任盈盈',0,3,'弹琴',0),
('岳不群',1,3,'华山剑法',0),
('东方不败',0,3,'葵花宝典',0),
('胡斐',1,4,'胡家刀法',0),
('苗若兰',0,4,'黄衣',0),
('程灵素',0,4,'医术',0),
('袁紫衣',0,4,'六合拳',0);

''




"""