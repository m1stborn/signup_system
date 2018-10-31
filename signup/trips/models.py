from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class Visit_logs(models.Model):
    name = models.TextField(max_length = 200)
    company = models.TextField(max_length = 30)

    class Purpose(object):
        one = 0
        two = 1
        three = 2
        four = 3
        five = 4

    PURPOSE_CHOICES = (
        (Purpose.one, '例行維護'), 
        (Purpose.two, '故障檢修'),  
        (Purpose.three, '設備安裝'),
        (Purpose.four, '環境施工'),
        (Purpose.five, '商務拜訪'),
    )

    purpose = models.PositiveSmallIntegerField(
        choices = PURPOSE_CHOICES,
    )


    class Visit_area(object):
        office = 0
        seminar = 1
        work = 2
        computer = 3

    VISIT_AREA_CHOICES = (
        (Visit_area.office, '辦公室'), 
        (Visit_area.seminar, '研討室'),  
        (Visit_area.work, '工作區'),
        (Visit_area.computer, '電腦機房'),
    )

    visit_area = models.PositiveSmallIntegerField(
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
        choices = HOST_CHOICES,
    )

    signature = models.TextField(max_length = 350000, default="")
    key = models.TextField(max_length=200, default=0)
    is_out = models.BooleanField(default=True)
    login_time = models.DateTimeField(default=timezone.now)
    logout_time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

class Organizations(models.Model):
	org_name = models.CharField(max_length = 50)
	FAX = models.CharField(max_length = 20)
	def __str__(self):
		return self.org_name
		
class Visitors(models.Model):
	name = models.CharField(max_length = 20)
	phone_number = models.CharField(max_length = 10, default = '0912345678')
	email = models.EmailField(default='example@gmail.com')
	personal_ID = models.CharField(max_length = 10,blank = True)
	org_ID = models.ForeignKey(Organizations, on_delete=models.CASCADE, null=True)
	def __str__(self):
		return self.name
