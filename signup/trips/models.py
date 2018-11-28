from django.db import models
import django.utils.timezone as timezone

# Create your models here.

class Organizations(models.Model):
	org_name = models.CharField(verbose_name="公司名稱",max_length = 50)
	FAX = models.CharField(verbose_name="傳真號碼",max_length = 20)
	class Meta:
		verbose_name_plural = "公司資訊"
	def __str__(self):
		return self.org_name
		
class Visitors(models.Model):
	name = models.CharField(verbose_name="訪客姓名",max_length = 20)
	phone_number = models.CharField(verbose_name="電話號碼",max_length = 10, default = '0912345678')
	email = models.EmailField(verbose_name="電子郵件",default='example@gmail.com')
	personal_ID = models.CharField(verbose_name="身分證字號",max_length = 10,blank = True)
	org_ID = models.ForeignKey(Organizations, on_delete=models.CASCADE, null=True,verbose_name="公司名稱")
	class Meta:
		verbose_name_plural = "個人資訊"
	def __str__(self):
		return self.name

class Visit_logs(models.Model):
    name = models.ForeignKey(Visitors, on_delete=models.CASCADE, null=True,verbose_name="訪客姓名",editable=False)
    # name = models.TextField(verbose_name="訪客姓名",max_length = 200,editable=False)
    company = models.ForeignKey(Organizations, on_delete=models.CASCADE, null=True,verbose_name="公司名稱",editable=False)
    # company = models.TextField(verbose_name="公司名稱",max_length = 30,editable=False,default="")

    class Purpose(object):
        one = 0
        two = 1

    PURPOSE_CHOICES = (
        (Purpose.one, '技術性作業'), 
        (Purpose.two, '拜訪及會議討論'),
    )

    purpose = models.PositiveSmallIntegerField(
    	verbose_name="進入目的",
        choices = PURPOSE_CHOICES,
    )


    class Visit_area(object):
        office = 0
        computer = 1

    VISIT_AREA_CHOICES = (
        (Visit_area.office, '辦公區域'),
        (Visit_area.computer, '電腦機房'),
    )

    visit_area = models.PositiveSmallIntegerField(
    	verbose_name="進出區域",
        choices = VISIT_AREA_CHOICES,
    )


    class Host(object):
        blhuang = 0
        cpchuang = 1
        yuking = 2
        lhchang = 3
        hdwu = 4
        cmchung = 5
        ktwu = 6
        cmhuang = 7
        ytlin = 8
        chyen = 9
        gracechuang = 10
        cjhsu = 11
        hsychang = 12

    HOST_CHOICES = (
        (Host.blhuang, '黃百立'),
        (Host.cpchuang, '莊峻沛'),
        (Host.yuking, '金禹天'),
        (Host.lhchang, '張麗環'),
        (Host.hdwu, '吳宏德'),
        (Host.cmchung, '鍾振明'),
        (Host.ktwu, '吳坤達'),
        (Host.cmhuang, '黃俊銘'),
        (Host.ytlin, '林彥廷'),
        (Host.chyen, '顏志宏'),
        (Host.gracechuang, '莊嘉怡'),
        (Host.cjhsu, '許純茹'),
        (Host.hsychang, '張琇茵'),  
    )

    host = models.PositiveSmallIntegerField(
    	verbose_name="接洽同仁",
        choices = HOST_CHOICES,
    )

    signature = models.TextField(max_length = 350000, default="")
    key = models.TextField(verbose_name="識別號碼",max_length=200, default=0)
    is_out = models.BooleanField(verbose_name="已簽退",default=True)
    login_time = models.DateTimeField(verbose_name="進入時間",default=timezone.now)
    logout_time = models.DateTimeField(verbose_name="離開時間",null=True)
    class Meta:
        verbose_name_plural = "訪客紀錄"
    def __str__(self):
        return str(self.name)
