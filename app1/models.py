from django.db import models
# Create your models here.
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid
import os
from datetime import datetime, timedelta
from datetime import date
from django.utils.timezone import now
import datetime
from multiselectfield import MultiSelectField

from smart_selects.db_fields import ChainedForeignKey,ChainedManyToManyField,GroupedForeignKey

class headsectormanager(models.Manager):
      def get_queryset(self):
          return super(headsectormanager,self).get_queryset().filter()


class users(models.Model):
      user_name = models.CharField(max_length=120, null=True)
      user_code = models.CharField(max_length=120, null=True)

      def __str__(self):
          return '%s' % (self.user_name,self.user_code)
class it_users(models.Model):
      username =  models.CharField(max_length=120, null=True)

      def __str__(self):
          return '%s' % (self.username,)


class hsectors(models.Model):
      sectors = models.CharField(max_length=120,null=True)
      def __str__(self):
           return '%s' % (self.sectors)

class sector(models.Model):
      hsectors = models.ForeignKey(hsectors,null=True)
      sector_name = models.CharField(max_length=120,null=True)
      def __str__(self):
          return '%s' % (self.sector_name)
def get_file_path1(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s.%s" % ( datetime.datetime.now(),uuid.uuid4(), ext)
    return os.path.join('blueprints', filename)
def get_file_path2(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s.%s" % ( datetime.datetime.now(),uuid.uuid4(), ext)
    return os.path.join('cartridges', filename)
def get_file_path3(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s.%s" % ( datetime.datetime.now(),uuid.uuid4(), ext)
    return os.path.join('spareparts', filename)
def get_file_path4(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s.%s" % ( datetime.datetime.now(),uuid.uuid4(), ext)
    return os.path.join('passrecovery', filename)
class hw_malfunction(models.Model):
      sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب', 'مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية', 'مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات', 'قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة', 'قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات', 'قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات', 'قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار', 'قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات', 'قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية', 'قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية', 'قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات', 'قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية', 'قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية', 'قطاعات الشئون القانونية'),
        ('قطاع الامن', 'قطاع الامن'),
        ('قطاع الرقابة الداخلية', 'قطاع الرقابة الداخلية'),
        )
      id= models.CharField(max_length=120,primary_key=True,default = uuid.uuid4)
      user_fullname = models.CharField(max_length=120,verbose_name='اسم المستخدم')
      hsectors = models.ForeignKey(hsectors,blank=True,null=True,verbose_name='رئاسة القطاعات')
      user_sector = models.ForeignKey(sector,blank=True,null=True,verbose_name='القطاع')
      pc_type = models.CharField(max_length=120,verbose_name='نوع الكومبيوتر')
      problem_date = models.DateTimeField(verbose_name='تاريخ المشكله')
      problem_desc = models.TextField(verbose_name='وصف المشكله')
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True)
      updated = models.DateTimeField(auto_now_add=True,null=True)
      publisher = models.ForeignKey(User,null=True)
      status = models.BooleanField(default=True)
      ip = models.CharField(blank=False,null=True,max_length=120)
      closed_by = models.CharField(blank=False, null=True, max_length=120)
      close_date = models.DateTimeField(auto_now_add=True, null=True)

      def __str__(self):
          return '%s %s %s %s %s %s ' %      (self.user_fullname,self.user_sector,self.pc_type,self.problem_date,self.problem_desc,self.timestamp,)
      def get_absolute_url(self):
          return "/app1/%s/" %(self.id)

class nw_malfunction(models.Model):
        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب', 'مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية', 'مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات', 'قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة', 'قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات', 'قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات', 'قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار', 'قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات', 'قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية', 'قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية', 'قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات', 'قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية', 'قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية', 'قطاعات الشئون القانونية'),
        ('قطاع الامن', 'قطاع الامن'),
        ('قطاع الرقابة الداخلية', 'قطاع الرقابة الداخلية'),
        )
        nettype=(('WIRE','WIRE'),('WIRELESS-CARD','WIRLESS-CARD'),('WIRELESS-USB','WIRELESS-USB'))
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
        user_fullname = models.CharField(max_length=120,verbose_name='اسم المستخدم')
        netwk_type = models.CharField(max_length=120,choices=nettype,verbose_name='نوع الشبكه')
        hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
        user_sector = models.ForeignKey(sector, blank=True, null=True, verbose_name='القطاع')
        problem_date = models.DateTimeField(verbose_name='تاريخ المشكله')
        problem_desc = models.TextField(verbose_name='وصف المشكله')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        status = models.BooleanField(default=True)
        publisher = models.ForeignKey(User,null=True)
        ip = models.CharField(blank=False,null=True,max_length=120)
        closed_by = models.CharField(blank=False, null=True, max_length=120)
        close_date = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
          return '%s %s %s %s %s' % (self.user_fullname, self.user_sector, self.netwk_type, self.problem_date, self.problem_desc)


class print_malfunction(models.Model):
        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب', 'مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية', 'مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات', 'قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة', 'قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات', 'قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات', 'قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار', 'قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات', 'قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية', 'قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية', 'قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات', 'قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية', 'قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية', 'قطاعات الشئون القانونية'),
        ('قطاع الامن', 'قطاع الامن'),
        ('قطاع الرقابة الداخلية', 'قطاع الرقابة الداخلية'),
        )
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
        user_fullname = models.CharField(max_length=120,verbose_name='اسم المستخدم')
        hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
        user_sector = models.ForeignKey(sector, blank=True, null=True, verbose_name='القطاع')
        printer_type = models.CharField(max_length=120,verbose_name='نوع الطابعه')
        problem_date = models.DateTimeField(verbose_name='تاريخ المشكله')
        problem_desc = models.TextField(verbose_name='وصف المشكله')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        publisher = models.ForeignKey(User,null=True,blank=False)
        status = models.BooleanField(default=True)
        ip = models.CharField(blank=False,null=True,max_length=120)
        closed_by = models.CharField(blank=False, null=True, max_length=120)
        close_date = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
          return '%s %s %s %s %s' % (self.user_fullname, self.user_sector, self.printer_type, self.problem_date, self.problem_desc)
        def get_absolute_url(self):
          return "/app1/%s/" %(self.id)



class analytics(models.Model):
      sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب', 'مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية', 'مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات', 'قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة', 'قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات', 'قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات', 'قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار', 'قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات', 'قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية', 'قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية', 'قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات', 'قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية', 'قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية', 'قطاعات الشئون القانونية'),
        ('قطاع الامن', 'قطاع الامن'),
        ('قطاع الرقابة الداخلية', 'قطاع الرقابة الداخلية'),
        )
      years = (
          ('2018', '2018'),
          ('2019', '2019'),
          ('2020', '2020'),
          ('2021', '2021'),
          ('2022', '2022'),
          ('2023', '2023'),
          ('2024', '2024'),
          ('2025', '2025'),
          ('2026', '2026'),
          ('2027', '2027'),
          ('2028', '2028'),
          ('2029', '2029'),
          ('2030', '2030'),
          ('2031', '2031'),
          ('2032', '2032'),
          ('2033', '2033'),
          ('2034', '2034'),
          ('2035', '2035'),
          ('2036', '2036'),
          ('2037', '2037'),
          ('2038', '2038'),
          ('2039', '2039'),
          ('2040', '2040'),
          ('2041', '2041'),
          ('2042', '2042'),
          ('2043', '2043'),
          ('2044', '2044'),
          ('2045', '2045'),
          ('2046', '2046'),
          ('2047', '2047'),
          ('2048', '2048'),
          ('2049', '2049'),
          ('2050', '2050'),
          ('2051', '2051'),
          ('2052', '2052'),
          ('2053', '2053'),
          ('2054', '2054'),
          ('2055', '2055'),
          ('2056', '2056'),
          ('2057', '2057'),
          ('2058', '2058'),
          ('2059', '2059'),
          ('2060', '2060'),
          ('2061', '2061'),
          ('2062', '2062'),
          ('2063', '2063'),
          ('2064', '2064'),
          ('2065', '2065'),
          ('2066', '2066'),
          ('2067', '2067'),
          ('2068', '2068'),
          ('2069', '2069'),
          ('2070', '2070'),
          ('2071', '2071'),
          ('2072', '2072'),
          ('2073', '2073'),
          ('2074', '2074'),
          ('2075', '2075'),
          ('2076', '2076'),
          ('2077', '2077'),
          ('2078', '2078'),
          ('2079', '2079'),
          ('2080', '2080'),
          ('2081', '2081'),
          ('2082', '2082'),
          ('2083', '2083'),
          ('2084', '2084'),
          ('2085', '2085'),
          ('2086', '2086'),
          ('2087', '2087'),
          ('2088', '2088'),
          ('2089', '2089'),
          ('2090', '2090'),
          ('2091', '2091'),
          ('2092', '2092'),
          ('2093', '2093'),
          ('2094', '2094'),
          ('2095', '2095'),
          ('2096', '2096'),
          ('2097', '2097'),
          ('2098', '2098'),
          ('2099', '2099'),
          ('2100', '2100'),
          ('2101', '2101'),
      )
      select_sector = models.CharField(blank=False,max_length=120,choices=sectors,verbose_name='SectorName')
      select_year = models.CharField(blank=True, null=True,max_length=120,choices=years,verbose_name='SectorName')

      def __str__(self):
          return ( self.select_sector)

class tag:
      typechecked = models.BooleanField()
      sectchecked = models.BooleanField()
      usechecked = models.BooleanField()

class search(models.Model):
        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب', 'مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية', 'مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات', 'قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة', 'قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات', 'قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات', 'قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار', 'قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات', 'قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية', 'قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية', 'قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات', 'قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية', 'قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية', 'قطاعات الشئون القانونية'),
        ('قطاع الامن', 'قطاع الامن'),
        ('قطاع الرقابة الداخلية', 'قطاع الرقابة الداخلية'),
        )
        problem = (('HardWare','HardWare'),('Printers','Printers'),('Network','Network'))
        demand = (('Cartridge','Cartridge'),('Passrecovery','Passrecovery'),('Spareparts','Spareparts'))
        select_sector = models.CharField(blank=True,max_length=120,choices=sectors,verbose_name='SectorName')
        select_problem = models.CharField(blank=True,max_length=120,choices=problem,verbose_name='Problem Type')
        select_user = models.CharField(blank=True,max_length=120,verbose_name='اسم المستخدم')
        select_Demand = models.CharField(blank=True,max_length=120,choices=demand,verbose_name='Demand Type')
        demand_date_from = models.DateTimeField(verbose_name='تاريخ الطلب من ')
        demand_date_to = models.DateTimeField(verbose_name='تاريخ الطلب الى ')

        def __str__(self):
          return '%s %s %s %s %s %s' % (self.select_sector, self. select_problem, self.select_user,self.select_Demand,self.demand_date_from,self.demand_date_to)





class cartridges(models.Model):
        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب', 'مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية', 'مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات', 'قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة', 'قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات', 'قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات', 'قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار', 'قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات', 'قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية', 'قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية', 'قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات', 'قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية', 'قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية', 'قطاعات الشئون القانونية'),
        ('قطاع الامن', 'قطاع الامن'),
        ('قطاع الرقابة الداخلية', 'قطاع الرقابة الداخلية'),
              )
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
        user_fullname = models.CharField(max_length=120,verbose_name='اسم المستخدم')
        hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
        user_sector = models.ForeignKey(sector, blank=True, null=True, verbose_name='القطاع')
        demand_date = models.DateTimeField(verbose_name='تاريخ الطلب')
        printer_type = models.CharField(max_length=120,verbose_name='نوع الطابعه')
        printer_model = models.CharField(max_length=120,verbose_name='موديل الطابعه')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        publisher = models.ForeignKey(User,null=True)
        status = models.BooleanField(default=True)
        thefile = models.FileField(upload_to = get_file_path2,null=True,blank=True,default="NULL",verbose_name='صورة الطلب المرفق')
        ip = models.CharField(blank=False,null=True,max_length=120)
        closed_by = models.CharField(blank=False, null=True, max_length=120)
        close_date = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
          return '%s %s %s %s %s %s ' % (self.user_fullname,self.user_sector,self.demand_date,self.printer_type,self.printer_model,self.timestamp,)
        def get_absolute_url(self):
          return "/app1/%s/" %(self.id)



class   passrecovery(models.Model):
        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب', 'مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية', 'مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات', 'قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة', 'قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات', 'قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات', 'قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار', 'قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات', 'قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية', 'قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية', 'قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات', 'قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية', 'قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية', 'قطاعات الشئون القانونية'),
        ('قطاع الامن', 'قطاع الامن'),
        ('قطاع الرقابة الداخلية', 'قطاع الرقابة الداخلية'),
        )
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
        user_fullname = models.CharField(max_length=120,verbose_name='اسم المستخدم')
        hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
        user_sector = models.ForeignKey(sector, blank=True, null=True, verbose_name='القطاع')
        demand_date = models.DateTimeField(verbose_name='تاريخ طلب الاسترداد')
        app_name= models.CharField(max_length=120,verbose_name='اسم التطبيق')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        publisher = models.ForeignKey(User,null=True)
        status = models.BooleanField(default=True)
        thefile = models.FileField(upload_to = get_file_path4,null=True,default="NULL",blank=True,verbose_name='صورة الطلب المرفق')
        ip = models.CharField(blank=False,null=True,max_length=120)
        closed_by = models.CharField(blank=False, null=True, max_length=120)
        close_date = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
            return '%s %s %s %s %s %s ' % (self.user_fullname,self.user_sector,self.pc_type,self.problem_date,self.problem_desc,self.timestamp,)
        def get_absolute_url(self):
            return "/app1/%s/" %(self.id)

class spareparts(models.Model):
        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب', 'مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية', 'مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات', 'قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة', 'قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات', 'قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات', 'قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار', 'قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات', 'قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية', 'قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية', 'قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات', 'قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية', 'قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية', 'قطاعات الشئون القانونية'),
        ('قطاع الامن', 'قطاع الامن'),
        ('قطاع الرقابة الداخلية', 'قطاع الرقابة الداخلية'),
        )
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
        user_fullname = models.CharField(max_length=120, verbose_name='اسم المستخدم')
        hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
        user_sector = models.ForeignKey(sector, blank=True, null=True, verbose_name='القطاع')
        demand_date = models.DateTimeField(verbose_name='تاريخ الطلب')
        part_type = models.CharField(max_length=120, verbose_name='نوع القطعه')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        publisher = models.ForeignKey(User, null=True)
        status = models.BooleanField(default=True)
        thefile = models.FileField(upload_to = get_file_path3,null=True, blank=True, verbose_name='صورة الطلب المرفق')
        ip = models.CharField(blank=False,null=True,max_length=120)
        closed_by = models.CharField(blank=False, null=True, max_length=120)
        close_date = models.DateTimeField(auto_now_add=True,null=True)

        def __str__(self):
          return '%s %s %s %s %s %s ' % (
          self.user_fullname, self.user_sector, self.pc_type, self.problem_date, self.problem_desc, self.timestamp,)

        def get_absolute_url(self):
          return "/app1/%s/" % (self.id)



class accessory(models.Model):
      accessory = models.CharField(blank=False,null=True,max_length=120,)
      def __str__(self):
          return '%s' % (self.accessory)


class asset_pc(models.Model):
      id= models.CharField(max_length=120,primary_key=True,default = uuid.uuid4)
      branshes=(('الفواله','الفواله'),('المهندسيين','المهندسيين'),('جاردن سيتى','جاردن سيتى'),('سيتى بنك','سيتى بنك'),('قصر النيل','قصر النيل'),('التوفيقيه','التوفيقيه'),)
      pctype=(('compatible','compatible'),('Brand','Brand'))
      ramtype=(('SDRAM','SDRAM'),('DDRAM','DDRAM'),('DDRAM2','DDRAM2'),('DDRAM3','DDRAM3'),('DDRAM4','DDRAM4'),)
      ramsize=(('128M','128M'),('256M','256M'),('512M','512M'),('756M','756M'),('1G','1G'),('1.128G',''),('1.256G','1.256G'),('1.512G','1.512G'),('1.768G','1.768G'),('2G','2G'),('2.128G','2.128G'),('2.256G','2.256G'),('2.512G','2.512G'),('2.768G','2.768G'),('3G','3G'),('3.128G','3.128G'),('3.256G','3.256G'),('3.512G','3.512G'),('3.768G','3.768G'),('4G','4G'),('4.128G','4.128G'),('4.256G','4.256G'),('4.512G','4.512G'),('4.768G','4.768G'),('5G','5G'),('6G','6G'),('7G','7G'),('8G','8G'))
      proctype=(('celeron','celeron'),('Pentium','Pentium'),('PentiumD','PentiumD'),('Pentium4','Pentium4'),('DualCore','DualCore'),('Core2Duo','Core2Duo'),('CoreI3','CoreI3'),('CoreI5','CoreI5'),('CoreI7','CoreI7'),('',''),)
      montype=(('CRT','CRT'),('LCD','LCD'),('LED','LED'),)
      os=(('NONE','NONE'),('WINDOWS XP','WINDOWS XP'),('WINDOWS 7','WINDOWS 7'),('WINDOWS 8','WINDOWS 8'),('WINDOWS 10','WINDOWS 10'),('LINUX','LINUX'),('MS-DOS','MS-DOS'))
      os_license=(('Licensed','Licensed'),('No License','No License'),)
      office=(('OFFICE 2003','OFFICE 2003'),('OFFICE 2007','OFFICE 2007'),('OFFICE 2010','OFFICE 2010'),('OFFICE 2013','OFFICE 2013'),('OFFICE 2016','OFFICE 2016'))
      accessories=(('DVD-ROM','DVD-ROM'),('CD-ROM','CD-ROM'),('KEYBOARD/MOUSE','KEYBOARD/MOUSE'),('DVD-RW','DVD-RW'),('FLASH-MEM','FLASH-MEM'),)

      user_fullname = models.CharField(max_length=120,verbose_name='اسم المستخدم')
      hsectors = models.ForeignKey(hsectors,blank=True,null=True,verbose_name='رئاسة القطاعات')
      user_sector = models.ForeignKey(sector,blank=True,null=True,verbose_name='القطاع')
      os_version = models.CharField(blank=False,null=True,max_length=120,choices=os,verbose_name='نسخة نظام التشغيل الحاليه')
      os_version_oem = models.CharField(blank=True,null=True,max_length=120,default="None",choices=os,verbose_name='OEM OS LABELED VERSION')

      os_license = models.CharField(blank=False,null=True,max_length=120,choices=os_license,verbose_name='ترخيص نظام التشغيل ')
      office_version = models.CharField(blank=False,null=True,max_length=120,choices=office,verbose_name='نسخة الاوڤيس')
      accessory = MultiSelectField(blank=False,max_length=120,null=True,choices=accessories,verbose_name='الملحقات')

      #accessory = models.ManyToManyField(accessory,blank=False,max_length=120,verbose_name='الملحقات')
      #user_sector = ChainedForeignKey('sector',chained_field="hectors",chained_model_field="hsectors",null=True,verbose_name='القطاع')
      bransh = models.CharField(blank=False,null=True,max_length=120,choices=branshes,verbose_name='اسم الفرع')
      pc_type = models.CharField(max_length=120,choices=pctype,verbose_name='نوع الجهاز',editable=True)
      pc_model = models.CharField(max_length=120,verbose_name='موديل الجهاز')
      ram_type= models.CharField(max_length=120,choices=ramtype,verbose_name='نوع الذاكره')
      ram_size= models.CharField(max_length=120,choices=ramsize,verbose_name='حجم الذاكره ')
      processor_type= models.CharField(max_length=120,choices=proctype,verbose_name='نوع المعالج')
      harddisk_size= models.CharField(max_length=120,verbose_name='حجم وحدة التخزين')
      monitor_type= models.CharField(max_length=120,choices=montype,verbose_name='نوع الشاشه الجهاز')
      monitor_size= models.CharField(max_length=120,verbose_name='حجم الشاشه')
      nettype=(('WIRE','WIRE'),('WIRELESS-STICK','WIRELESS-STICK'),('WIRELESS-CARD','WIRELESS-CARD'),('NO-CONNECTION','NO-CONNECTION'))
      networking = models.CharField(blank=False,null=True,max_length=120,choices=nettype,verbose_name='نوع الشپگه')
      domain=(('JOINED','JOINED'),('UNJOINED','UNJOINED'),)
      joined = models.CharField(blank=True, null=True,max_length=120,choices=domain,verbose_name='الرپط پالدومين')
      notes = models.TextField(blank=True, null=True,verbose_name='ملاحظات')
      timestamp = models.DateTimeField(auto_now_add=True,null=True)
      updated = models.DateTimeField(auto_now_add=True,null=True)
      updater = models.CharField(blank=False, null=True, max_length=120)  
      publisher = models.ForeignKey(User,null=True)
      status = models.BooleanField(default=True)
      ip = models.CharField(blank=False,null=True,max_length=120)
      def __str__(self):
          return '%s %s %s %s %s %s ' % (self.user_fullname,self.user_sector,self.user_head_sector,self.pc_type,self.timestamp,)
      def get_absolute_url(self):
          return "/app1/%s/" %(self.id)


class asset_printer(models.Model):
        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب', 'مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية', 'مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات', 'قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة', 'قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات', 'قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات', 'قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار', 'قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات', 'قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية', 'قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية', 'قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات', 'قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية', 'قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية', 'قطاعات الشئون القانونية'),
        ('قطاع الامن', 'قطاع الامن'),
        ('قطاع الرقابة الداخلية', 'قطاع الرقابة الداخلية'),
        )
        branshes = (
        ('الفواله', 'الفواله'), ('المهندسيين', 'المهندسيين'), ('جاردن سيتى', 'جاردن سيتى'), ('سيتى بنك', 'سيتى بنك'),
        ('قصر النيل', 'قصر النيل'), ('التوفيقيه', 'التوفيقيه'),)
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)

        contype =(('USB','USB'),('ETHERNET','ETHERNET'),('USB+ETHERNET','USB+ETHERNET'),('LTP-PORT','LTP-PORT'),)
        user_fullname = models.CharField(max_length=120, verbose_name='اسم المستخدم')
        hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
        user_sector = models.ForeignKey(sector, blank=True, null=True, verbose_name='القطاع')
        printtype=(('LaserJet','LaserJet'),('OfficeJet','OfficeJet'),('DeskJet','DeskJet'),('InkJet','InkJet'),('MFP','MFP'))
        conntype=(('PARALLEL(ltp)','PARALLEL(ltp)'),('USB','USB'),('ETHERNET','ETHERNET'),('WIRELESS','WIRELESS'),('USB & ETHERNET','USB & ETHERNET'),('USB+ETHERNET+PARALLEL','USB+ETHERNET+PARALLEL'))
        bransh = models.CharField(blank=False,null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
        printer_type = models.CharField(max_length=120,choices=printtype, verbose_name='نوع الطابعه')
        conn_type = models.CharField(max_length=120,choices=conntype,default="NULL" ,verbose_name='نوع التوصيل')
        printer_model = models.CharField(max_length=120, verbose_name='موديل الطابعه')
        cartridge_number = models.CharField(blank=True,max_length=120, verbose_name='رقم عبوة الحبر ')
        black_number = models.CharField(blank=True, null=True,max_length=120, verbose_name='رقم عبوة الحبر الاسود ')
        color_number = models.CharField(blank=True, null=True,max_length=120, verbose_name='رقم عبوة الحبر الالوان')

        notes = models.TextField(blank=True, null=True,verbose_name='ملاحظات')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        updater = models.CharField(blank=False, null=True, max_length=120)
        publisher = models.ForeignKey(User, null=True)
        status = models.BooleanField(default=True)
        ip = models.CharField(blank=False,null=True,max_length=120)
        def __str__(self):
            return '%s %s %s %s %s %s ' % (self.user_fullname, self.user_sector, self.printer_type, self.timestamp,)

        def get_absolute_url(self):
            return "/app1/%s/" % (self.id)

class asset_scanner(models.Model):
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)

        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب', 'مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية', 'مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات', 'قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة', 'قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات', 'قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات', 'قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار', 'قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات', 'قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية', 'قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية', 'قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات', 'قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية', 'قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية', 'قطاعات الشئون القانونية'),
        ('قطاع الامن', 'قطاع الامن'),
        ('قطاع الرقابة الداخلية', 'قطاع الرقابة الداخلية'),
        )
        branshes = (
        ('الفواله', 'الفواله'), ('المهندسيين', 'المهندسيين'), ('جاردن سيتى', 'جاردن سيتى'), ('سيتى بنك', 'سيتى بنك'),
        ('قصر النيل', 'قصر النيل'), ('التوفيقيه', 'التوفيقيه'),)
        scantype=(('LowSpeedNormal','LowSpeedNormal'),('HighSpeedMultiScan','HighSpeedMultiScan'),)
        user_fullname = models.CharField(max_length=120, verbose_name='اسم المستخدم')
        hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
        user_sector = models.ForeignKey(sector, blank=True, null=True, verbose_name='القطاع')
        bransh = models.CharField(blank=False, max_length=120, choices=branshes, verbose_name='اسم الفرع')
        scanner_model = models.CharField(max_length=120, verbose_name='موديل الماسح الضوئى')
        scanner_type = models.CharField(max_length=120,default="Null", choices=scantype,verbose_name='نوع الماسح الضوئى')
        notes = models.TextField(blank=True, null=True,verbose_name='ملاحظات')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        updater = models.CharField(blank=False, null=True, max_length=120)
        publisher = models.ForeignKey(User, null=True)
        status = models.BooleanField(default=True)
        ip = models.CharField(blank=False,null=True,max_length=120)
        def __str__(self):
            return '%s %s %s %s %s %s ' % (self.user_fullname, self.user_sector, self.printer_type, self.timestamp,)

        def get_absolute_url(self):
            return "/app1/%s/" % (self.id)

class asset_copier(models.Model):
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)

        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب', 'مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية', 'مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات', 'قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة', 'قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات', 'قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات', 'قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار', 'قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات', 'قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية', 'قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية', 'قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات', 'قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية', 'قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية', 'قطاعات الشئون القانونية'),
        ('قطاع الامن', 'قطاع الامن'),
        ('قطاع الرقابة الداخلية', 'قطاع الرقابة الداخلية'),
        )
        branshes = (
        ('الفواله', 'الفواله'), ('المهندسيين', 'المهندسيين'), ('جاردن سيتى', 'جاردن سيتى'), ('سيتى بنك', 'سيتى بنك'),
        ('قصر النيل', 'قصر النيل'), ('التوفيقيه', 'التوفيقيه'),)
        copiertype =(('USB','USB'),('ETHERNET','ETHERNET'),('USB+ETHERNET','USB+ETHERNET'),('NO-DATA-CONNECTION','NO-DATA-CONNECTION'),)
        hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
        user_sector = models.ForeignKey(sector, blank=True, null=True, verbose_name='القطاع')
        bransh = models.CharField(blank=True,null=True,max_length=120, choices=branshes, verbose_name='اسم الفرع')
        copier_model = models.CharField(max_length=120, verbose_name='موديل ماكينة التصوير')
        cartridge_number = models.CharField(max_length=120, verbose_name='رقم عبوة الحبر ')
        conn_type = models.CharField(blank=True,null=True,max_length=120, default="NO-DATA-CONNECTION",choices=copiertype, verbose_name='نوع التوصيل الشبكى')
        notes = models.TextField(blank=True, null=True,verbose_name='ملاحظات')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        updater = models.CharField(blank=False, null=True, max_length=120)
        publisher = models.ForeignKey(User, null=True)
        status = models.BooleanField(default=True)
        ip = models.CharField(blank=False,null=True,max_length=120)
        def __str__(self):
            return '%s %s %s %s %s %s ' % (self.user_fullname, self.user_sector, self.printer_type, self.timestamp,)

        def get_absolute_url(self):
            return "/app1/%s/" % (self.id)
#---------------------------------------------------------------------------------
#*********************************************************************************
class asset_server(models.Model):
      id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)

      branshes = (
            ('الفواله', 'الفواله'), ('المهندسيين', 'المهندسيين'), ('جاردن سيتى', 'جاردن سيتى'), ('سيتى بنك', 'سيتى بنك'),
            ('قصر النيل', 'قصر النيل'), ('التوفيقيه', 'التوفيقيه'),)
      floores = (
        ('التاسع', 'التاسع'), ('الثامن', 'الثامن'), ('العاشر', 'العاشر'), ('السابع', 'السابع'),
        ('الرابع', 'الرابع'), ('الحادى عشر', 'الحادى عشر'),('الاول', 'الاول'))
      bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
      floor = models.CharField(blank=True, null=True, max_length=120, choices=floores, verbose_name='رقم الطابق')
      server_vendor = models.CharField(max_length=120, verbose_name='المصنع ')
      server_model = models.CharField(max_length=120, verbose_name='الموديل ')
      montype = (('CRT', 'CRT'), ('LCD', 'LCD'), ('LED', 'LED'),)
      monitor_type = models.CharField(blank=True, null=True,max_length=120, choices=montype, verbose_name='نوع الشاشه الجهاز')
      ram_size = models.CharField(max_length=120, verbose_name='الذاكره ')

      monitor_size = models.CharField(blank=True, null=True,max_length=120, verbose_name='حچم وموديل الشاشه ')
      processor = models.CharField(max_length=120, verbose_name='المعالج ',null=True)
      harddisk_size = models.CharField(max_length=120, verbose_name='حجم التخزين ')
      created = models.DateTimeField(auto_now_add=True,null=True)
      updated = models.DateTimeField(auto_now_add=True,null=True)
      updater = models.CharField(blank=False, null=True, max_length=120)  
      publisher = models.ForeignKey(User, null=True)
      status = models.BooleanField(default=True)
      ip = models.CharField(blank=False, null=True, max_length=120)

      def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.server_model, self.server_vendor, self.bransh, self.floor,self.ram_size,self.harddisk_size,self.processor)

      def get_absolute_url(self):
        return "/app1/%s/" % (self.id)




      #---------------------------------------------------------------------------------
#*********************************************************************************
class asset_switch(models.Model):
        branshes = (
          ('الفواله', 'الفواله'), ('المهندسيين', 'المهندسيين'), ('جاردن سيتى', 'جاردن سيتى'), ('سيتى بنك', 'سيتى بنك'),
          ('قصر النيل', 'قصر النيل'), ('التوفيقيه', 'التوفيقيه'),)
        floores = (
          ('التاسع', 'التاسع'), ('الثامن', 'الثامن'), ('العاشر', 'العاشر'), ('السابع', 'السابع'),
          ('الرابع', 'الرابع'), ('الحادى عشر', 'الحادى عشر'), ('الاول', 'الاول'))
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)

        bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
        floor = models.CharField(blank=True, null=True, max_length=120, choices=floores, verbose_name='رقم الطابق')
        switch_vendor = models.CharField(max_length=120, verbose_name='المصنع ')
        switch_model = models.CharField(max_length=120, verbose_name='الموديل ')
        port_numbers = models.CharField(max_length=120, verbose_name='عدد المنافذ ')
        publisher = models.ForeignKey(User, null=True)
        ip = models.CharField(blank=False, null=True, max_length=120)
        created = models.DateTimeField(auto_now_add=True, null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        updater = models.CharField(blank=False, null=True, max_length=120)  

        def __str__(self):
          return '%s %s %s %s ' % (
            self.bransh, self.floor, self.switch_model, self.switch_vendor,)



        def get_absolute_url(self):
          return "/app1/%s/" % (self.id)



#---------------------------------------------------------------------------------
#*********************************************************************************
class asset_accesspoint(models.Model):
          branshes = (
            ('الفواله', 'الفواله'), ('المهندسيين', 'المهندسيين'), ('جاردن سيتى', 'جاردن سيتى'),
            ('سيتى بنك', 'سيتى بنك'),
            ('قصر النيل', 'قصر النيل'), ('التوفيقيه', 'التوفيقيه'),)
          floores = (
            ('التاسع', 'التاسع'), ('الثامن', 'الثامن'), ('العاشر', 'العاشر'), ('السابع', 'السابع'),
            ('الرابع', 'الرابع'), ('الحادى عشر', 'الحادى عشر'), ('الاول', 'الاول'))
          id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)

          bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
          floor = models.CharField(blank=True, null=True, max_length=120, choices=floores, verbose_name='رقم الطابق')
          accesspoint_vendor = models.CharField(max_length=120, verbose_name='المصنع ')
          accesspoint_model = models.CharField(max_length=120, verbose_name='الموديل ')
          publisher = models.ForeignKey(User, null=True)
          ip = models.CharField(blank=False, null=True, max_length=120)
          created = models.DateTimeField(auto_now_add=True, null=True)
          updated = models.DateTimeField(auto_now_add=True,null=True)
          updater = models.CharField(blank=False, null=True, max_length=120)  
          def __str__(self):
            return '%s %s %s %s ' % (self.bransh, self.floor, self.accesspoint_model, self.accesspoint_vendor,)

          def get_absolute_url(self):
            return "/app1/%s/" % (self.id)



#---------------------------------------------------------------------------------
#*********************************************************************************
class asset_stick(models.Model):
        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب', 'مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية', 'مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات', 'قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة', 'قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات', 'قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات', 'قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار', 'قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات', 'قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية', 'قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية', 'قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات', 'قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية', 'قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية', 'قطاعات الشئون القانونية'),
        ('قطاع الامن', 'قطاع الامن'),
        ('قطاع الرقابة الداخلية', 'قطاع الرقابة الداخلية'),
        )
        user_fullname = models.CharField(max_length=120,verbose_name='اسم المستخدم',default="NULL")
        user_sector = models.CharField(blank=False,editable=True,max_length=120,choices=sectors,verbose_name='رئاسة القطاعات',default="NULL")
        branshes = (
        ('الفواله', 'الفواله'), ('المهندسيين', 'المهندسيين'), ('جاردن سيتى', 'جاردن سيتى'),
        ('سيتى بنك', 'سيتى بنك'),
        ('قصر النيل', 'قصر النيل'), ('التوفيقيه', 'التوفيقيه'),)
        floores = (
        ('التاسع', 'التاسع'), ('الثامن', 'الثامن'), ('العاشر', 'العاشر'), ('السابع', 'السابع'),
        ('الرابع', 'الرابع'), ('الحادى عشر', 'الحادى عشر'), ('الاول', 'الاول'))
        bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
        floor = models.CharField(blank=True, null=True, max_length=120, choices=floores, verbose_name='رقم الطابق')
        stick_vendor = models.CharField(max_length=120, verbose_name='المصنع ')
        stick_model = models.CharField(max_length=120, verbose_name='الموديل ')
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
        publisher = models.ForeignKey(User, null=True)
        ip = models.CharField(blank=False, null=True, max_length=120)
        created = models.DateTimeField(auto_now_add=True, null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        updater = models.CharField(blank=False, null=True, max_length=120)
        def __str__(self):
            return '%s %s %s %s ' % ( self.bransh, self.floor, self.stick_model, self.stick_vendor,)

        def get_absolute_url(self):
            return "/app1/%s/" % (self.id)





            #---------------------------------------------------------------------------------
#*********************************************************************************
class asset_router(models.Model):
              branshes = (
                ('الفواله', 'الفواله'), ('المهندسيين', 'المهندسيين'), ('جاردن سيتى', 'جاردن سيتى'),
                ('سيتى بنك', 'سيتى بنك'),
                ('قصر النيل', 'قصر النيل'), ('التوفيقيه', 'التوفيقيه'),)
              floores = (
                ('التاسع', 'التاسع'), ('الثامن', 'الثامن'), ('العاشر', 'العاشر'), ('السابع', 'السابع'),
                ('الرابع', 'الرابع'), ('الحادى عشر', 'الحادى عشر'), ('الاول', 'الاول'))
              bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes,
                                        verbose_name='اسم الفرع')
              id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
              floor = models.CharField(blank=True, null=True, max_length=120, choices=floores, verbose_name='رقم الطابق')
              router_vendor = models.CharField(max_length=120, verbose_name='المصنع ')
              router_model = models.CharField(max_length=120, verbose_name='الموديل ')
              publisher = models.ForeignKey(User, null=True)
              ip = models.CharField(blank=False, null=True, max_length=120)
              created = models.DateTimeField(auto_now_add=True, null=True)
              updated = models.DateTimeField(auto_now_add=True,null=True)
              updater = models.CharField(blank=False, null=True, max_length=120)  
              def __str__(self):
                return '%s %s %s %s ' % ( self.bransh, self.floor, self.router_model, self.router_vendor,)
              def get_absolute_url(self):
                return "/app1/%s/" % (self.id)







              #---------------------------------------------------------------------------------
#*********************************************************************************
class asset_repeater(models.Model):
                branshes = (
                  ('الفواله', 'الفواله'), ('المهندسيين', 'المهندسيين'), ('جاردن سيتى', 'جاردن سيتى'),
                  ('سيتى بنك', 'سيتى بنك'),
                  ('قصر النيل', 'قصر النيل'), ('التوفيقيه', 'التوفيقيه'),)
                floores = (
                  ('التاسع', 'التاسع'), ('الثامن', 'الثامن'), ('العاشر', 'العاشر'), ('السابع', 'السابع'),
                  ('الرابع', 'الرابع'), ('الحادى عشر', 'الحادى عشر'), ('الاول', 'الاول'))
                bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes,
                                          verbose_name='اسم الفرع')
                floor = models.CharField(blank=True, null=True, max_length=120, choices=floores,
                                         verbose_name='رقم الطابق')
                id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
                repeater_vendor = models.CharField(max_length=120, verbose_name='المصنع ')
                repeater_model = models.CharField(max_length=120, verbose_name='الموديل ')
                publisher = models.ForeignKey(User, null=True)
                status = models.BooleanField(default=True)
                ip = models.CharField(blank=False, null=True, max_length=120)
                created = models.DateTimeField(auto_now_add=True, null=True)
                updated = models.DateTimeField(auto_now_add=True,null=True)
                updater = models.CharField(blank=False, null=True, max_length=120)  
                def __str__(self):
                  return '%s %s %s %s ' % (self.bransh, self.floor, self.repeater_model, self.repeater_vendor,)


                def get_absolute_url(self):
                  return "/app1/%s/" % (self.id)






#---------------------------------------------------------------------------------
#*********************************************************************************
class asset_rack(models.Model):
                  branshes = (
                    ('الفواله', 'الفواله'), ('المهندسيين', 'المهندسيين'), ('جاردن سيتى', 'جاردن سيتى'),
                    ('سيتى بنك', 'سيتى بنك'),
                    ('قصر النيل', 'قصر النيل'), ('التوفيقيه', 'التوفيقيه'),)
                  floores = (
                    ('التاسع', 'التاسع'), ('الثامن', 'الثامن'), ('العاشر', 'العاشر'), ('السابع', 'السابع'),
                    ('الرابع', 'الرابع'), ('الحادى عشر', 'الحادى عشر'), ('الاول', 'الاول'))
                  racktype = (
                    ('Wall_Mounted', 'Wall_Mounted'), ('STAND_ALONE', 'STAND_ALONE'), ('STAND_ALONE_SMALL', 'STAND_ALONE_SMALL'),)
                  id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
                  bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes,verbose_name='اسم الفرع')
                  floor = models.CharField(blank=True, null=True, max_length=120, choices=floores,verbose_name='رقم الطابق')
                  rack_type= models.CharField(blank=True, null=True, max_length=120, choices=racktype,verbose_name='نوع الراك')
                  publisher = models.ForeignKey(User, null=True)
                  status = models.BooleanField(default=True)
                  ip = models.CharField(blank=False, null=True, max_length=120)
                  created = models.DateTimeField(auto_now_add=True, null=True)
                  updated = models.DateTimeField(auto_now_add=True,null=True)
                  updater = models.CharField(blank=False, null=True, max_length=120)  
                  def __str__(self):
                    return '%s %s %s  ' % ( self.bransh, self.floor, self.rack_type,)



                  def get_absolute_url(self):
                    return "/app1/%s/" % (self.id)




#---------------------------------------------------------------------------------
#*********************************************************************************
class asset_device(models.Model):
                    id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)

                    branshes = (
                      ('الفواله', 'الفواله'), ('المهندسيين', 'المهندسيين'), ('جاردن سيتى', 'جاردن سيتى'),
                      ('سيتى بنك', 'سيتى بنك'),
                      ('قصر النيل', 'قصر النيل'), ('التوفيقيه', 'التوفيقيه'),)
                    floores = (
                      ('التاسع', 'التاسع'), ('الثامن', 'الثامن'), ('العاشر', 'العاشر'), ('السابع', 'السابع'),
                      ('الرابع', 'الرابع'), ('الحادى عشر', 'الحادى عشر'), ('الاول', 'الاول'))
                    id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)

                    bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes,
                                              verbose_name='اسم الفرع')
                    floor = models.CharField(blank=True, null=True, max_length=120, choices=floores,
                                             verbose_name='رقم الطابق')
                    device_name = models.CharField(max_length=120, verbose_name='اسم الجهاز ')
                    device_desc =  models.TextField(verbose_name='وصف الجهاز')
                    publisher = models.ForeignKey(User, null=True)
                    ip = models.CharField(blank=False, null=True, max_length=120)
                    created = models.DateTimeField(auto_now_add=True, null=True)
                    updated = models.DateTimeField(auto_now_add=True,null=True)
                    updater = models.CharField(blank=False, null=True, max_length=120)  
                    def __str__(self):
                      return '%s %s %s %s ' % (self.bransh, self.floor, self.device_name, self.device_desc,)

                    def get_absolute_url(self):
                      return "/app1/%s/" % (self.id)




#---------------------------------------------------------------------------------
#*********************************************************************************
class asset_blueprint(models.Model):
      id= models.CharField(max_length=120,primary_key=True,default = uuid.uuid4)

      branshes = (('الفواله', 'الفواله'), ('المهندسيين', 'المهندسيين'), ('جاردن سيتى', 'جاردن سيتى'),
                 ('سيتى بنك', 'سيتى بنك'),
                 ('قصر النيل', 'قصر النيل'), ('التوفيقيه', 'التوفيقيه'),)
      floores = (('التاسع', 'التاسع'), ('الثامن', 'الثامن'), ('العاشر', 'العاشر'), ('السابع', 'السابع'),
                ('الرابع', 'الرابع'), ('الحادى عشر', 'الحادى عشر'), ('الاول', 'الاول'))
      bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes,verbose_name='اسم الفرع')
      floor = models.CharField(blank=True, null=True, max_length=120, choices=floores,verbose_name='رقم الطابق')
      name = models.CharField(blank=False, null=True, max_length=120,verbose_name='اسم المخطط')
      ip = models.CharField(blank=False, null=True, max_length=120)
      publisher = models.ForeignKey(User, null=True)
      image = models.FileField(upload_to = get_file_path1,null=True,blank=True,verbose_name='صورة المخطط')
      imagesrc = models.FileField(null=True,blank=True,verbose_name='ملف المصدر')
      created = models.DateTimeField(auto_now_add=True, null=True)
      updated = models.DateTimeField(auto_now_add=True,null=True)
      updater = models.CharField(blank=False, null=True, max_length=120)
      def __str__(self):
        return '%s %s %s %s ' % (self.bransh, self.floor, self.image, self.imagesrc,)

      def get_absolute_url(self):
        return "/app1/%s/" % (self.id)






        #---------------------------------------------------------------------------------
#*********************************************************************************

class asset_lab(models.Model):
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
        branshes=(('الفواله','الفواله'),('المهندسيين','المهندسيين'),('جاردن سيتى','جاردن سيتى'),('سيتى بنك','سيتى بنك'),('قصر النيل','قصر النيل'),('التوفيقيه','التوفيقيه'),)
        os = (('WINDOWS XP', 'WINDOWS XP'), ('WINDOWS 7', 'WINDOWS 7'), ('WINDOWS 8', 'WINDOWS 8'),
              ('WINDOWS 10', 'WINDOWS 10'), ('LINUX', 'LINUX'), ('MS-DOS', 'MS-DOS'))
        user_fullname = models.CharField(max_length=120,verbose_name='اسم المستخدم')
        user_sector = models.ForeignKey(sector,blank=False,max_length=120,null=True,verbose_name='القطاع')
        hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
        os_version = models.CharField(blank=False, null=True, max_length=120, choices=os,verbose_name='نسخة نظام التشغيل الحاليه')
        os_version_oem = models.CharField(blank=False, null=True, max_length=120, choices=os,verbose_name='OEM OS LABELED VERSION')
        bransh = models.CharField(blank=False,null=True,max_length=120,choices=branshes,verbose_name='اسم الفرع')
        lab_model = models.CharField(max_length=120,verbose_name='موديل الجهاز')
        lab_vendor = models.CharField(max_length=120,verbose_name='اسم الشركه المصنعه')
        lab_serial = models.CharField(max_length=120,verbose_name='الرقم التسلسلى للجهاز')
        notes = models.TextField(blank=True, null=True,verbose_name='ملاحظات')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        updater = models.CharField(blank=False, null=True, max_length=120)
        publisher = models.ForeignKey(User,null=True)
        status = models.BooleanField(default=True)
        ip = models.CharField(blank=False,null=True,max_length=120)
        def __str__(self):
          return '%s %s %s %s %s %s ' % (self.user_fullname,self.user_sector,self.hsectors,self.lab_type,self.timestamp,)
        def get_absolute_url(self):
          return "/app1/%s/" %(self.id)


#---------------------------------------------------------------------------
class junk_parts(models.Model):
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
        branshes=(('الفواله','الفواله'),('المهندسيين','المهندسيين'),('جاردن سيتى','جاردن سيتى'),('سيتى بنك','سيتى بنك'),('قصر النيل','قصر النيل'),('التوفيقيه','التوفيقيه'),)
        jtype = (('COMPUTER', 'COMPUTER'), ('PRINTER', 'PRINTER'), ('SCANNER', 'SCANNER'), ('SWITCH', 'SWITCH'), ('ROUTER', 'ROUTER'), ('ACCESSPOINT', 'ACCESSPOINT'), ('SERVER', 'SERVER'), ('REPEATER', 'REPEATER'), ('KEYBORAD', 'KEYBORAD'), ('MOUSE', 'MOUSE'),('POWER CABLE', 'POWER CABLE'), ('NETWORK CARD', 'NETWORK CARD'),('POWER SUPPLY', 'POWER SUPPLY'),('MONITOR', 'MONITOR'),('OTHER', 'OTHER'),)
        places =(('الفواله','الفواله'),('المهندسيين','المهندسيين'),('جاردن سيتى','جاردن سيتى'),('سيتى بنك','سيتى بنك'),('قصر النيل','قصر النيل'),('التوفيقيه','التوفيقيه'),('مخزن','مخزن'))
        cplaces =(('پالمقر','پالمقر'),('چهه اخرى','چهه اخرى'))
        junk_type = models.CharField(max_length=120,choices=jtype,verbose_name='نوع القطعه التالڤه')
        junk_brand  = models.CharField(max_length=120,blank=True,verbose_name='اسم وموديل القطعه')
        damadge_type = models.CharField(max_length=120,blank=True,verbose_name='نوع التلڤ')
        user_sector = models.ForeignKey(sector,blank=True,null=True,max_length=120,verbose_name=' القطاع')
        hsectors = models.ForeignKey(hsectors,blank=True, null=True, verbose_name='رئاسة القطاعات')
        junk_user = models.CharField(max_length=120,blank=True,verbose_name='اسم المستخدم')
        bransh = models.CharField(blank=False,null=True,max_length=120,choices=branshes,verbose_name='اسم الفرع')
        notes = models.TextField(blank=True, null=True,verbose_name='ملاحظات')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        updater = models.CharField(blank=False, null=True, max_length=120)
        publisher = models.ForeignKey(User,null=True)
        pstatus = models.BooleanField(default=True)
        ip = models.CharField(blank=False,null=True,max_length=120)
        cplace = models.CharField(max_length=120,blank=True,choices=cplaces,default='پالمقر',verbose_name='المگان الحالى')
        transto= models.CharField(max_length=120,blank=True,choices=places,verbose_name='نقل الى')
        def __str__(self):
          return '%s  ' % (self.timestamp)
        def get_absolute_url(self):
          return "/app1/%s/" %(self.id)




#----------------------------------------------------------------------------------------------
class searchassets(models.Model):
    branshes = (
        ('الفواله', 'الفواله'), ('المهندسيين', 'المهندسيين'), ('جاردن سيتى', 'جاردن سيتى'), ('سيتى بنك', 'سيتى بنك'),
        ('قصر النيل', 'قصر النيل'), ('التوفيقيه', 'التوفيقيه'),)
    objects = (('COMPUTERS', 'COMPUTERS'), ('LABTOPS', 'LABTOPS'), ('PRINTERS', 'PRINTERS'), ('SCANNERS', 'SCANNERS'),
               ('COPIERS', 'COPIERS'))
    select_bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
    select_hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
    select_sector = models.ForeignKey(sector, blank=True, null=True, max_length=120, verbose_name=' القطاع')
    select_user = models.CharField(blank=True,null=True ,max_length=120, verbose_name='اسم المستخدم')
    select_object = models.CharField(blank=True,null=True, max_length=120, choices=objects, verbose_name='نوع الاصل')
#-------------------computers
    proctype = (('celeron', 'celeron'), ('Pentium', 'Pentium'), ('PentiumD', 'PentiumD'), ('Pentium4', 'Pentium4'),
                ('DualCore', 'DualCore'), ('Core2Duo', 'Core2Duo'), ('CoreI3', 'CoreI3'), ('CoreI5', 'CoreI5'),
                ('CoreI7', 'CoreI7'), ('', ''),)
    processor_type = models.CharField(blank=True, null=True,max_length=120, choices=proctype, verbose_name='نوع المعالج')
    domain = (('JOINED', 'JOINED'), ('UNJOINED', 'UNJOINED'),)
    joined = models.CharField(blank=True, null=True, max_length=120, choices=domain, verbose_name='الرپط پالدومين')
    harddisk_size = models.CharField(blank=True, null=True,max_length=120, verbose_name='حجم وحدة التخزين')
    pc_model = models.CharField(blank=True, null=True,max_length=120, verbose_name='موديل الجهاز')
    montype = (('CRT', 'CRT'), ('LCD', 'LCD'), ('LED', 'LED'),)
    monitor_type = models.CharField(blank=True, null=True,max_length=120, choices=montype, verbose_name='نوع الشاشه الجهاز')
    os_license = (('Licensed', 'Licensed'), ('No License', 'No License'),)
    os_license = models.CharField(blank=True, null=True, max_length=120, choices=os_license,verbose_name='ترخيص نظام التشغيل ')

#-------------------labs
    lab_model = models.CharField(blank=True, null=True,max_length=120, verbose_name='موديل الجهاز')
    lab_vendor = models.CharField(blank=True, null=True,max_length=120, verbose_name='اسم الشركه المصنعه')
#-------------------printers
    printtype = (
    ('LaserJet', 'LaserJet'), ('OfficeJet', 'OfficeJet'), ('DeskJet', 'DeskJet'), ('InkJet', 'InkJet'), ('MFP', 'MFP'))
    printer_type = models.CharField(blank=True, null=True,max_length=120, choices=printtype, verbose_name='نوع الطابعه')
    printer_model = models.CharField(blank=True, null=True,max_length=120, verbose_name='موديل الطابعه')

    #--------------------scanners
    scantype = (('LowSpeedNormal', 'LowSpeedNormal'), ('HighSpeedMultiScan', 'HighSpeedMultiScan'),)
    scanner_type = models.CharField(blank=True, null=True,max_length=120, default="Null", choices=scantype, verbose_name='نوع الماسح الضوئى')
    scanner_model = models.CharField(blank=True, null=True,max_length=120, verbose_name='موديل الماسح الضوئى')

    #--------------------copiers
    copier_model = models.CharField(blank=True, null=True,max_length=120, verbose_name='موديل ماكينة التصوير')
    copiertype = (('USB', 'USB'), ('ETHERNET', 'ETHERNET'), ('USB+ETHERNET', 'USB+ETHERNET'),
                  ('NO-DATA-CONNECTION', 'NO-DATA-CONNECTION'),)
    conn_type = models.CharField(blank=True, null=True, max_length=120, default="NO-DATA-CONNECTION",choices=copiertype, verbose_name='نوع التوصيل الشبكى')


def __str__(self):
    return '%s %s %s %s' % (self.select_sector, self.select_hsectors, self.select_user,select_object)
#---------------------------------------------------------------------------------------------------------------
class missions(models.Model):
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)

        branshes = (
        ('الفواله', 'الفواله'), ('المهندسيين', 'المهندسيين'), ('جاردن سيتى', 'جاردن سيتى'), ('سيتى بنك', 'سيتى بنك'),
        ('قصر النيل', 'قصر النيل'), ('التوفيقيه', 'التوفيقيه'),)


        places = (
        ('الفواله', 'الفواله'), ('المهندسيين', 'المهندسيين'), ('جاردن سيتى', 'جاردن سيتى'), ('سيتى بنك', 'سيتى بنك'),
        ('قصر النيل', 'قصر النيل'), ('التوفيقيه', 'التوفيقيه'), ('مخزن', 'مخزن'))
        places = (('داخل الشرگه', 'داخل الشرگه'), ('چهه اخرى', 'چهه اخرى'))

        partners = (
                    (' محمد احمد ','محمد احمد '),(' عبد المنعم رفعت ','عبد المنعم رفعت '),(' أحمد سعيد ','أحمد سعيد '),(' وائل علاء الدين ','وائل علاء الدين '),(' مصطفى نادى ','مصطفى نادى '),(' احمد رفقى ','احمد رفقى '),

                    (' وائل الطويل ','وائل الطويل '),(' اسلام عبد الوهاب ','اسلام عبد الوهاب '),(' أحمد حجازى ','أحمد حجازى '),(' أحمد صلاح ','أحمد صلاح '),(' رامز سمير ','رامز سمير '),(' أحمد عبيد  ','أحمد عبيد  '),

                    (' أحمد إبراهيم ','أحمد إبراهيم '),(' محمد جاد ','محمد جاد '),(' ياسمين الجوهرى ','ياسمين الجوهرى '),(' اميرة عبد العال ','اميرة عبد العال '),(' مها محمد ','مها محمد '),(' أمجد أبو السعود ','أمجد أبو السعود '),

                    (' أسامة فتحى ','أسامة فتحى '),(' محمد مصطفى ','محمد مصطفى '),(' دينا سراج ','دينا سراج '),(' محمد شعبان ','محمد شعبان '),(' هانى مصطفى ','هانى مصطفى '),(' محمد جاد  ','محمد جاد  '),(' محمد احمد ','محمد احمد '),

                    (' احمد عصام ','احمد عصام '),(' إسلام عبد الوهاب ','إسلام عبد الوهاب '))









        mission1 = models.TextField(max_length=120,blank=True, verbose_name='المهامه الاولى')
        mission2 = models.TextField(max_length=120, blank=True,verbose_name='المهامه الثانيه')
        mission3 = models.TextField(max_length=120, blank=True,verbose_name='المهامه الثالثه')
        mission4 = models.TextField(max_length=120, blank=True,verbose_name='المهامه الراپعه')
        mission5 = models.TextField(max_length=120,blank=True, verbose_name='المهامه الخامسه')
        it_name = models.ForeignKey(it_users,max_length=120, blank=True, verbose_name='الاسم')
        it_partners = models.CharField(max_length=120,blank=True,choices=partners,default='داخل الشرگه',verbose_name='المشترگين ڤى الاعمال ')
        m1_bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
        m2_bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
        m3_bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
        m4_bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
        m5_bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')

        m1_out_premisis = models.CharField(max_length=120, blank=True, verbose_name='چهة خارچ الشرگه')
        m2_out_premisis = models.CharField(max_length=120, blank=True, verbose_name='چهة خارچ الشرگه')
        m3_out_premisis = models.CharField(max_length=120, blank=True, verbose_name='چهة خارچ الشرگه')
        m4_out_premisis = models.CharField(max_length=120, blank=True, verbose_name='چهة خارچ الشرگه')
        m5_out_premisis = models.CharField(max_length=120, blank=True, verbose_name='چهة خارچ الشرگه')
        m1_place = models.CharField(max_length=120,blank=True,choices=places,default='داخل الشرگه',verbose_name='المگان ')
        m2_place = models.CharField(max_length=120,blank=True,choices=places,default='داخل الشرگه',verbose_name='المگان ')
        m3_place = models.CharField(max_length=120,blank=True,choices=places,default='داخل الشرگه',verbose_name='المگان ')
        m4_place = models.CharField(max_length=120,blank=True,choices=places,default='داخل الشرگه',verbose_name='المگان ')
        m5_place = models.CharField(max_length=120,blank=True,choices=places,default='داخل الشرگه',verbose_name='المگان ')
        timestamp = models.DateTimeField(auto_now_add=True, null=True)
        publisher = models.ForeignKey(User, null=True)
        ip = models.CharField(blank=False, null=True, max_length=120)


        def __str__(self):
            return '%s  ' % (self.timestamp)

        def get_absolute_url(self):
            return "/app1/%s/" % (self.id)
#=================================================================
class LAW(models.Model):

        case_name = models.CharField(max_length=120, verbose_name='اسم القضيه')
        case_type = models.CharField(blank=True, max_length=120, null=True, verbose_name='نوع القضيه')
        court_name = models.CharField( blank=True, null=True,max_length=120, verbose_name='المحگمه المتداول پها القضيه')
        case_start_date = models.DateTimeField(blank=True, null=True, max_length=120, verbose_name=' تاريخ پدا القضيه ')
        lawyer_name = models.CharField(blank=True, null=True, max_length=120, verbose_name='اسم المحامى متولى القضيه')
        about_case = models.TextField(blank=True, null=True, max_length=120,  verbose_name='نپذه عن القضيه')
        last_case_update = models.TextField(max_length=2048, verbose_name='اخر تحديث للقضيه')
        timestamp = models.DateTimeField(auto_now_add=True, null=True)
        updated = models.DateTimeField(auto_now_add=True, null=True)
        publisher = models.ForeignKey(User, null=True)
        status = models.BooleanField(default=True)
        ip = models.CharField(blank=True, null=True, max_length=120)

        def __str__(self):
            return '%s' % (self.timestamp,)

        def get_absolute_url(self):
            return "/app1/%s/" % (self.id)
#------------------------------------------------------------------------------
class search_case(models.Model):
    case_name = models.CharField(blank=True, max_length=120,verbose_name='الپحث پاسم القضيه')
    lawyer_name = models.CharField(blank=True, max_length=120,verbose_name=' الپحث پاسم المحامى')
    court_name = models.CharField(blank=True, max_length=120, verbose_name='الپحث پاسم المحگمه ')


    def __str__(self):
        return '%s %s %s ' % ( self.case_name, self.lawyer_name, self.court_name,)

