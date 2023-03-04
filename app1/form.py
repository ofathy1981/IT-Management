from django import forms

from django.forms.models import ModelForm
from django.forms.widgets import CheckboxSelectMultiple
from django.db import models
from .models import hw_malfunction,accessory,LAW,asset_lab,junk_parts,missions,nw_malfunction,print_malfunction,analytics,search,passrecovery,cartridges,spareparts,asset_pc,asset_printer,asset_copier,asset_scanner,asset_server,asset_router,asset_rack,asset_accesspoint,asset_switch,asset_repeater,asset_stick,asset_device,asset_blueprint,searchassets,search_case

class signup_hw(forms.ModelForm):
      class Meta:
        model = hw_malfunction
        exclude = ['publisher', 'status','ip']
        fields = ('hsectors','user_sector','user_fullname',  'pc_type', 'problem_date', 'problem_desc')


      def __init__(self, *args, **kwargs):
        super(signup_hw, self).__init__(*args, **kwargs)
        self.fields['problem_date'].widget.attrs['class'] = 'datepicker'
        self.fields['problem_desc'].widget.attrs['class'] = 'tarea'

   

   #   def clean_user_fullname(self):
      #    ufullname = self.cleaned_data['user_fullname']
      #    sect = self.cleaned_data['user_sector']
       #   return ufullname



class signup_nw(forms.ModelForm):
      class Meta:
        model = nw_malfunction
        fields = ('hsectors','user_sector','user_fullname','netwk_type','problem_date','problem_desc',)
        exclude = ['publisher', 'status',]
      def __init__(self,*args,**kwargs):
          super(signup_nw, self).__init__(*args, **kwargs)
          self.fields['problem_date'].widget.attrs['class'] = 'datepicker'
          self.fields['problem_desc'].widget.attrs['class'] = 'tarea'


class signup_printer(forms.ModelForm):
      class Meta:
        model = print_malfunction
        exclude = ['publisher', 'status',]
        fields = ('hsectors','user_sector','user_fullname','printer_type', 'problem_date','problem_desc' )

      def __init__(self,*args,**kwargs):
          super(signup_printer, self).__init__(*args, **kwargs)
          self.fields['problem_date'].widget.attrs['class'] = 'datepicker'
          self.fields['problem_desc'].widget.attrs['class'] = 'tarea'


class req_analytics(forms.ModelForm):
      class Meta:
            model = analytics
            fields = ('select_sector','select_year')
      def   cleaned_data_select_sector(self):
            selected = self.cleaned_data['select_sector']
            return True
      def   cleaned_data_select_year(self):
            selected = self.cleaned_data['select_year']
            return True


      def    __init__(self, *args, **kwargs):
             super(req_analytics, self).__init__(*args, **kwargs)
class signup_cartridge(forms.ModelForm):
      class Meta:
        model = cartridges
        fields = ('hsectors','user_sector','user_fullname', 'demand_date', 'printer_type','printer_model', 'thefile')

      def __init__(self, *args, **kwargs):
        super(signup_cartridge, self).__init__(*args, **kwargs)
        self.fields['demand_date'].widget.attrs['class'] = 'datepicker'
        # self.fields['thefile'].widget.attrs['class'] = 'file'
        # self.fields['thefile'].widget.attrs['id'] = 'input-b1'
        # self.fields['thefile'].widget.attrs['name'] = 'input-b1'
        # self.fields['thefile'].widget.attrs['type'] = 'file'
        # self.fields['thefile'].widget.attrs['data-show-preview'] ='false'

class signup_spareparts(forms.ModelForm):
      class Meta:
        model = spareparts
        fields = ('hsectors','user_sector','user_fullname', 'demand_date','part_type','thefile')

      def __init__(self, *args, **kwargs):
         super(signup_spareparts, self).__init__(*args, **kwargs)
         self.fields['demand_date'].widget.attrs['class'] = 'datepicker'



class signup_passrecovery(forms.ModelForm):
      class Meta:
        model = passrecovery
        fields = ('hsectors','user_sector','user_fullname','demand_date', 'app_name', 'thefile')

      def __init__(self, *args, **kwargs):
        super(signup_passrecovery, self).__init__(*args, **kwargs)
        self.fields['demand_date'].widget.attrs['class'] = 'datepicker'

































class search1(forms.ModelForm):
      class Meta:
            model = search
            fields = ('select_sector',)


class search2(forms.ModelForm):
      class Meta:
            model = search
            fields = ('select_problem',)

class search3(forms.ModelForm):
      class Meta:
            model = search
            fields = ('select_user',)

class search4(forms.ModelForm):
      class Meta:
            model = search
            fields = ('select_sector',)

class search8(forms.ModelForm):
      class Meta:
            model = search
            fields = ('demand_date_from','demand_date_to')
      def __init__(self, *args, **kwargs):
        super(search8, self).__init__(*args, **kwargs)
        self.fields['demand_date_from'].widget.attrs['class'] = 'datepicker'
        self.fields['demand_date_to'].widget.attrs['class'] = 'datepicker'

class search6(forms.ModelForm):
      class Meta:
            model = search
            fields = ('select_Demand',)


class add_pc(forms.ModelForm):
      accessories=(('DVD','DVD'),('CD','CD'))
      #accessory = forms.CharField(widget=forms.CheckboxSelectMultiple)
      code = forms.CharField(disabled=True,required=False,label='گود الموظڤ')
      class Meta:
        model = asset_pc
        exclude = ['publisher', 'status']
        fields = ('bransh','hsectors','user_sector','user_fullname','code', 'pc_type','pc_model','ram_type','ram_size','processor_type','harddisk_size','monitor_type','monitor_size','accessory' ,'os_version_oem','os_version','os_license','office_version','networking','joined','notes',)
      def __init__(self, *args, **kwargs):
        super(add_pc, self).__init__(*args, **kwargs)
        self.fields['user_fullname'].widget.attrs['class'] = 'col-md-6 mb-3'
       # self.fields['user_sector'].widget.attrs['class'] = 'col-md-6 mb-3'
        self.fields['notes'].widget.attrs['class'] = 'tarea'
        self.fields['code'].widget.attrs['class'] = 'col-md-3 mb-3'

      #  self.fields['user_head_sector'].widget.attrs['class'] = 'dropdown-divider'

      # self.fields['accessory'].widget = CheckboxSelectMultiple()
     #   self.fields['accessory'].queryset= accessory.objects.all()

#
class add_lab(forms.ModelForm):
    code = forms.CharField(disabled=True,required=False,label='گود الموظڤ')

    class Meta:
        model = asset_lab
        exclude = ['publisher', 'status']
        fields = ('bransh','user_sector','hsectors','user_fullname','code','lab_vendor','lab_model', 'os_version', 'os_version_oem','lab_serial', 'notes',)

    def __init__(self, *args, **kwargs):
        super(add_lab, self).__init__(*args, **kwargs)
        self.fields['user_fullname'].widget.attrs['class'] = 'col-md-6 mb-3'
        self.fields['user_sector'].widget.attrs['class'] = 'col-md-6 mb-3'
        self.fields['notes'].widget.attrs['class'] = 'tarea'
        self.fields['code'].widget.attrs['class'] = 'col-md-3 mb-3'


class add_printer(forms.ModelForm):
      code = forms.CharField(disabled=True,required=False, label='گود الموظڤ')

      class Meta:
        model = asset_printer
        exclude = ['publisher', 'status']
        fields = ('bransh','hsectors','user_sector','user_fullname','code','printer_model','conn_type','printer_type','cartridge_number','black_number','color_number', 'notes')
      def __init__(self, *args, **kwargs):
        super(add_printer, self).__init__(*args, **kwargs)
        self.fields['notes'].widget.attrs['class'] = 'tarea'
        self.fields['code'].widget.attrs['class'] = 'col-md-3 mb-3'
        self.fields['black_number'].widget.attrs['class'] = 'col-md-4 mb-3'
        self.fields['color_number'].widget.attrs['class'] = 'col-md-4 mb-3'


class add_copier(forms.ModelForm):
      class Meta:
        model = asset_copier
        exclude = ['publisher', 'status']
        fields = ( 'bransh','hsectors','user_sector','copier_model','cartridge_number','conn_type','notes',)
      def __init__(self, *args, **kwargs):
        super(add_copier, self).__init__(*args, **kwargs)
        self.fields['notes'].widget.attrs['class'] = 'tarea'


class add_scanner(forms.ModelForm):
      code = forms.CharField(disabled=True,required=False, label='گود الموظڤ')

      class Meta:
        model = asset_scanner
        exclude = ['publisher', 'status']
        fields = ('bransh','hsectors','user_sector','user_fullname','code',  'scanner_model','scanner_type','notes')
      def __init__(self, *args, **kwargs):
        super(add_scanner, self).__init__(*args, **kwargs)
        self.fields['notes'].widget.attrs['class'] = 'tarea'
        self.fields['code'].widget.attrs['class'] = 'col-md-3 mb-3'

#******************************************************************************************
class add_server(forms.ModelForm):
      class Meta:
        model = asset_server
        exclude = ['publisher', 'ip','created']
        fields = ('floor', 'bransh', 'server_vendor', 'server_model', 'ram_size','harddisk_size','processor','monitor_type','monitor_size')
      def __init__(self, *args, **kwargs):
        super(add_server, self).__init__(*args, **kwargs)




#******************************************************************************************
class add_switch(forms.ModelForm):
      class Meta:
        model = asset_switch
        exclude = ['publisher', 'ip']
        fields = ('floor', 'bransh', 'switch_vendor', 'switch_model', 'port_numbers',)

      def __init__(self, *args, **kwargs):
        super(add_switch, self).__init__(*args, **kwargs)





#******************************************************************************************
class add_accesspoint(forms.ModelForm):
      class Meta:
        model = asset_accesspoint
        exclude = ['publisher', 'ip']
        fields = ('bransh','floor' , 'accesspoint_vendor', 'accesspoint_model',)

      def __init__(self, *args, **kwargs):
        super(add_accesspoint, self).__init__(*args, **kwargs)






#******************************************************************************************
class add_stick(forms.ModelForm):
      class Meta:
        model = asset_stick
        exclude = ['publisher', 'ip']
        fields = ('floor', 'bransh', 'stick_vendor', 'stick_model','user_fullname','user_sector')

      def __init__(self, *args, **kwargs):
        super(add_stick, self).__init__(*args, **kwargs)

#******************************************************************************************
class add_router(forms.ModelForm):
      class Meta:
        model = asset_router
        exclude = ['publisher', 'ip']
        fields = ('floor', 'bransh', 'router_vendor', 'router_model',)

      def __init__(self, *args, **kwargs):
        super(add_router, self).__init__(*args, **kwargs)

#******************************************************************************************
class add_repeater(forms.ModelForm):
      class Meta:
        model = asset_repeater
        exclude = ['publisher', 'ip']
        fields = ('floor', 'bransh', 'repeater_vendor', 'repeater_model',)

      def __init__(self, *args, **kwargs):
        super(add_repeater, self).__init__(*args, **kwargs)

#******************************************************************************************
class add_rack(forms.ModelForm):
      class Meta:
        model = asset_rack
        exclude = ['publisher', 'ip']
        fields = ('floor', 'bransh', 'rack_type',)

      def __init__(self, *args, **kwargs):
        super(add_rack, self).__init__(*args, **kwargs)

#******************************************************************************************

class add_device(forms.ModelForm):
      class Meta:
        model = asset_device
        exclude = ['publisher', 'ip']
        fields = ('floor', 'bransh', 'device_name', 'device_desc',)

      def __init__(self, *args, **kwargs):
        super(add_device, self).__init__(*args, **kwargs)
        self.fields['device_desc'].widget.attrs['class'] = 'tarea'

#******************************************************************************************
class add_blueprint(forms.ModelForm):
      class Meta:
        model =  asset_blueprint
        exclude = ['publisher', 'ip']
        fields = ('name','floor', 'bransh', 'image', 'imagesrc',)

      def __init__(self, *args, **kwargs):
        super(add_blueprint, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'file'


#******************************************************************************************
class add_junk(forms.ModelForm):
      code = forms.CharField(disabled=True,label='گود الموظڤ',required=False)

      class Meta:
        model = junk_parts
        exclude = ['publisher', 'status']
        fields = ('bransh','hsectors','user_sector','junk_user','code','junk_type','junk_brand', 'damadge_type','notes',)

      def __init__(self, *args, **kwargs):
        super(add_junk, self).__init__(*args, **kwargs)
        self.fields['user_sector'].widget.attrs['class'] = 'col-md-6 mb-3'
        self.fields['notes'].widget.attrs['class'] = 'tarea'
        self.fields['code'].widget.attrs['class'] = 'col-md-3 mb-3'


#******************************************************************************************
class trans_junk(forms.ModelForm):
        class Meta:
            model = junk_parts
            exclude = ['publisher', 'status','timestamp','pstatus']
            fields = ('transto',)

        def __init__(self, *args, **kwargs):
            super(trans_junk, self).__init__(*args, **kwargs)



        def cleaned_data_transto(self):
            transto = self.cleaned_data['transto']
            return True






#******************************************************************************************
# class searchassetmain(forms.ModelForm):
#     class Meta:
#         model = searchassets
#         fields = ('','','','','','','',)

# ******************************************************************************************
class searchassetmain(forms.ModelForm):
    class Meta:
        model = searchassets
        fields = ('select_bransh', 'select_hsectors', 'select_sector', 'select_user')

class selectobj(forms.ModelForm):
    class Meta:
        model = searchassets
        fields = ('select_object',)


class searchassetcomputers(forms.ModelForm):
    class Meta:
        model = searchassets
        fields = ('pc_model', 'os_license', 'processor_type', 'harddisk_size', 'joined', 'monitor_type',)


class searchassetlabs(forms.ModelForm):
    class Meta:
        model = searchassets
        fields = ('lab_model', 'lab_vendor')


class searchassetprinters(forms.ModelForm):
    class Meta:
        model = searchassets
        fields = ('printer_type', 'printer_model')


class searchassetscanners(forms.ModelForm):
    class Meta:
        model = searchassets
        fields = ('scanner_type', 'scanner_model')


class searchassetcopiers(forms.ModelForm):
    class Meta:
        model = searchassets
        fields = ('conn_type', 'copier_model')

class record_mission(forms.ModelForm):
    class Meta:
        model = missions
        fields = ('it_name','mission1','m1_place','m1_bransh','m1_out_premisis','mission2','m2_place','m2_bransh','m2_out_premisis','mission3','m3_place','m3_bransh','m3_out_premisis','mission4','m4_place','m4_bransh','m4_out_premisis','mission5','m5_place','m5_bransh','m5_out_premisis',)
       # it_partners = forms.ModelMultipleChoiceField(widget=SelectMultiple(), label='گود الموظڤ', required=False)

    def __init__(self, *args, **kwargs):
        super(record_mission, self).__init__(*args, **kwargs)
        #self.fields['it_partners'].widget.attrs['class'] = '


















#--------
class add_law_note(forms.ModelForm):
      class Meta:
        model = LAW
        exclude = ['publisher', 'timestamp', 'ip']
        fields = ('case_name', 'case_type', 'court_name', 'case_start_date', 'lawyer_name', 'about_case','last_case_update',)

      def __init__(self, *args, **kwargs):
        super(add_law_note, self).__init__(*args, **kwargs)
        self.fields['case_start_date'].widget.attrs['class'] = 'datepicker'
        self.fields['about_case'].widget.attrs['class'] = 'tarea'


class update_law_note(forms.ModelForm):
    class Meta:
        model = LAW
        exclude = ['publisher', 'timestamp', 'ip']
        fields = ( 'last_case_update',)

    def __init__(self, *args, **kwargs):
        super(update_law_note, self).__init__(*args, **kwargs)
        self.fields['last_case_update'].widget.attrs['readonly'] = 'True'

class searchlaw(forms.ModelForm):
    class Meta:
        model = search_case
        fields = ( 'case_name','court_name','lawyer_name',)

    def __init__(self, *args, **kwargs):
        super(searchlaw, self).__init__(*args, **kwargs)
        #self.fields['last_case_update'].widget.attrs['readonly'] = 'True'