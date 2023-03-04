from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include,url

urlpatterns = [

    url(r'^$', views.index,name='index'),
    url(r'^main/', views.main,name='main'),
   url(r'^pc/', views.pc, name='pc'),
    url(r'^spare/', views.spare, name='spareparts'),
    url(r'^cart/', views.cartridge, name='cartridge'),
    url(r'^passwd/', views.passrec, name='passrecovery'),
    url(r'^netwk/', views.netwk, name='netwk'),
    url(r'^printer/', views.printer, name='printer'),
    url(r'^success/', views.success, name='success'),
    url(r'^add_success/', views.asset_add_success, name='asset_add_success'),
    url(r'^add_success/', views.asset_add_success, name='asset_add_success'),

    url(r'^trans_success/', views.trans_success, name='trans_success'),
    url(r'^update_success/', views.asset_update_success, name='asset_update_success'),
    url(r'^remove_success/', views.asset_remove_success, name='asset_remove_success'),


    url(r'^dsuccess/', views.demandsuccess, name='demandsuccess'),
    url(r'^rest/', views.rest, name='rest'),
    url(r'^(?P<id>[0-9a-f-]+)/$', views.detail, name='detail'),
    url(r'^pr/(?P<id>[0-9a-f-]+)/$', views.prdetail, name='prdetail'),
    url(r'^nw/(?P<id>[0-9a-f-]+)/$', views.nwdetail, name='nwdetail'),
    url(r'^cartridges/(?P<id>[0-9a-f-]+)/$', views.cartridgedetail, name='cartridgedetail'),
    url(r'^pass/(?P<id>[0-9a-f-]+)/$', views.passdetail, name='passdetail'),
    url(r'^spares/(?P<id>[0-9a-f-]+)/$', views.sparepartsdetail, name='sparepartsdetail'),
    url(r'^(?P<id>[0-9a-f-]+)/det/$', views.user_detail, name='user_detail'),
    url(r'^(?P<id>[0-9a-f-]+)/det1/$', views.user_detail1, name='user_detail1'),
    url(r'^(?P<id>[0-9a-f-]+)/det2/$', views.user_detail2, name='user_detail2'),
    url(r'^(?P<id>[0-9a-f-]+)/det3/$', views.user_detail3, name='user_detail3'),
    url(r'^(?P<id>[0-9a-f-]+)/det4/$', views.user_detail4, name='user_detail4'),
    url(r'^(?P<id>[0-9a-f-]+)/det5/$', views.user_detail5, name='user_detail5'),

    url(r'^p_det/', views.prob_detail,name='prob_detail'),
    url(r'^p_det1/', views.prob_detail1,name='prob_detail1'),
    url(r'^p_det2/', views.prob_detail2,name='prob_detail2'),
    url(r'^p_det3/', views.prob_detail3,name='prob_detail3'),
    url(r'^p_det4/', views.prob_detail4,name='prob_detail4'),
    url(r'^p_det5/', views.prob_detail5,name='prob_detail5'),

    url(r'^u_p_det5/', views.user_prob_detail5, name='user_prob_detail5'),
    url(r'^u_p_det4/', views.user_prob_detail4, name='user_prob_detail4'),
    url(r'^u_p_det3/', views.user_prob_detail3, name='user_prob_detail3'),
    url(r'^u_p_det2/', views.user_prob_detail2, name='user_prob_detail2'),

    url(r'^u_p_det1/', views.user_prob_detail1,name='user_prob_detail1'),
    url(r'^u_p_det/', views.user_prob_detail,name='user_prob_detail'),
    url(r'^(?P<id>[0-9a-f-]+)/remove/$', views.remove, name='remove'),

    url(r'^(?P<id>[0-9a-f-]+)/remove1/$', views.pc_remove1, name='pc_remove1'),
    url(r'^(?P<id>[0-9a-f-]+)/remove1/$', views.pc_remove1, name='pc_remove1'),
    url(r'^(?P<id>[0-9a-f-]+)/remove2/$', views.printer_remove2, name='printer_remove2'),
    url(r'^(?P<id>[0-9a-f-]+)/remove3/$', views.scanner_remove3, name='scanner_remove3'),
    url(r'^(?P<id>[0-9a-f-]+)/remove4/$', views.copier_remove4, name='copier_remove4'),

    url(r'^(?P<id>[0-9a-f-]+)/solved/$', views.solved, name='solved'),
    url(r'^(?P<id>[0-9a-f-]+)/solved1/$', views.solved1, name='solved1'),
    url(r'^(?P<id>[0-9a-f-]+)/solved2/$', views.solved2, name='solved2'),
    url(r'^(?P<id>[0-9a-f-]+)/solved3/$', views.solved3, name='solved3'),
    url(r'^(?P<id>[0-9a-f-]+)/solved4/$', views.solved4, name='solved4'),
    url(r'^(?P<id>[0-9a-f-]+)/solved5/$', views.solved5, name='solved5'),

    url(r'^analytics/', views.analytics, name='analytics'),
    url(r'^analytics1/', views.analytics1, name='analytics1'),

    #url(r'^analytics/#contac', views.analytics1, name='analytics1'),
    url(r'^search/', views.search, name='search'),
    url(r'^searchp/', views.searchp, name='searchp'),
    url(r'^searchd/', views.searchd, name='searchd'),
    url(r'^computers_list_ordered/',views.computers_list_ordered,name='computers_list_ordered'),
    url(r'^searchasst/', views.searchasst, name='searchasst'),
    url(r'^searchasst2/', views.searchasst2, name='searchasst2'),

    url(r'^assets/', views.assets, name='assets'),
    url(r'^asset-pc/', views.add_asset_pc, name='add_asset_pc'),
    url(r'^computers_det/', views.computers_detail, name='computers_detail'),
    url(r'^(?P<id>[0-9a-f-]+)/comp_det/$', views.computer_detail, name='computer_detail'),
    url(r'^(?P<id>[0-9a-f-]+)/pc-update/$', views.pc_update, name='pc_update'),
    url(r'^(?P<id>[0-9a-f-]+)/printer-update/$', views.printer_update, name='printer_update'),
    url(r'^(?P<id>[0-9a-f-]+)/scanner-update/$', views.scanner_update, name='scanner_update'),
    url(r'^(?P<id>[0-9a-f-]+)/copier-update/$', views.copier_update, name='copier_update'),

    url(r'^comp_list/', views.computers_list, name='computers_list'),
    url(r'^asset-printer/', views.add_asset_printer, name='add_asset_printer'),
    url(r'^printers_det/', views.printers_detail, name='printers_detail'),
    url(r'^(?P<id>[0-9a-f-]+)/print_det/$', views.printer_detail, name='printer_detail'),
    url(r'^print_list/', views.printers_list, name='printers_list'),
    url(r'^asset-scan/', views.add_asset_scanner, name='add_asset_scanner'),
    url(r'^scanners_det/', views.scanners_detail, name='scanners_detail'),
    url(r'^(?P<id>[0-9a-f-]+)/scan_det/$', views.scanner_detail, name='scanner_detail'),
    url(r'^scan_list/', views.scanners_list, name='scanners_list'),
    url(r'^asset-copier/', views.add_asset_copier, name='add_asset_copier'),
    url(r'^copiers_det/', views.copiers_detail, name='copiers_detail'),
    url(r'^(?P<id>[0-9a-f-]+)/copis_det/$', views.copier_detail, name='copier_detail'),
    url(r'^copis_list/', views.copiers_list, name='copiers_list'),


    url(r'^asset-server/', views.add_asset_server, name='add_asset_server'),
    url(r'^(?P<id>[0-9a-f-]+)/server-update/$', views.server_update, name='server_update'),
    url(r'^(?P<id>[0-9a-f-]+)/remove1server/$', views.server_remove1, name='server_remove1'),
    url(r'^servers_det/', views.servers_detail, name='servers_detail'),
    url(r'^(?P<id>[0-9a-f-]+)/server_det/$', views.server_detail, name='server_detail'),
    url(r'^server_list/', views.servers_list, name='servers_list'),

    url(r'^(?P<id>[0-9a-f-]+)/switch-update/$', views.switch_update, name='switch_update'),
    url(r'^(?P<id>[0-9a-f-]+)/remove1switch/$', views.switch_remove1, name='switch_remove1'),
    url(r'^switchs_det/', views.switchs_detail, name='switchs_detail'),
    url(r'^(?P<id>[0-9a-f-]+)/switch_det/$', views.switch_detail, name='switch_detail'),
    url(r'^switch_list/', views.switchs_list, name='switchs_list'),

    url(r'^(?P<id>[0-9a-f-]+)/accesspoint-update/$', views.accesspoint_update, name='accesspoint_update'),
    url(r'^(?P<id>[0-9a-f-]+)/remove1accesspoint/$', views.accesspoint_remove1, name='accesspoint_remove1'),
    url(r'^accesspoints_det/', views.accesspoints_detail, name='accesspoints_detail'),
    url(r'^(?P<id>[0-9a-f-]+)/accesspoint_det/$', views.accesspoint_detail, name='accesspoint_detail'),
    url(r'^accesspoint_list/', views.accesspoints_list, name='accesspoints_list'),

    url(r'^(?P<id>[0-9a-f-]+)/stick-update/$', views.stick_update, name='stick_update'),
    url(r'^(?P<id>[0-9a-f-]+)/remove1stick/$', views.stick_remove1, name='stick_remove1'),
    url(r'^sticks_det/', views.sticks_detail, name='sticks_detail'),
    url(r'^(?P<id>[0-9a-f-]+)/stick_det/$', views.stick_detail, name='stick_detail'),
    url(r'^stick_list/', views.sticks_list, name='sticks_list'),

    url(r'^(?P<id>[0-9a-f-]+)/router-update/$', views.router_update, name='router_update'),
    url(r'^(?P<id>[0-9a-f-]+)/remove1router/$', views.router_remove1, name='router_remove1'),
    url(r'^routers_det/', views.routers_detail, name='routers_detail'),
    url(r'^(?P<id>[0-9a-f-]+)/router_det/$', views.router_detail, name='router_detail'),
    url(r'^router_list/', views.routers_list, name='routers_list'),

    url(r'^(?P<id>[0-9a-f-]+)/repeater-update/$', views.repeater_update, name='repeater_update'),
    url(r'^(?P<id>[0-9a-f-]+)/remove1repeater/$', views.repeater_remove1, name='repeater_remove1'),
    url(r'^repeaters_det/', views.repeaters_detail, name='repeaters_detail'),
    url(r'^(?P<id>[0-9a-f-]+)/repeater_det/$', views.repeater_detail, name='repeater_detail'),
    url(r'^repeater_list/', views.repeaters_list, name='repeaters_list'),

    url(r'^(?P<id>[0-9a-f-]+)/rack-update/$', views.rack_update, name='rack_update'),
    url(r'^(?P<id>[0-9a-f-]+)/remove1rack/$', views.rack_remove1, name='rack_remove1'),
    url(r'^racks_det/', views.racks_detail, name='racks_detail'),
    url(r'^(?P<id>[0-9a-f-]+)/rack_det/$', views.rack_detail, name='rack_detail'),
    url(r'^rack_list/', views.racks_list, name='racks_list'),

    url(r'^(?P<id>[0-9a-f-]+)/device-update/$', views.device_update, name='device_update'),
    url(r'^(?P<id>[0-9a-f-]+)/remove1device/$', views.device_remove1, name='device_remove1'),
    url(r'^devices_det/', views.devices_detail, name='devices_detail'),
    url(r'^(?P<id>[0-9a-f-]+)/device_det/$', views.device_detail, name='device_detail'),
    url(r'^device_list/', views.devices_list, name='devices_list'),

    url(r'^asset-switch/', views.add_asset_switch, name='add_asset_switch'),
    url(r'^asset-accesspoint/', views.add_asset_accesspoint, name='add_asset_accesspoint'),
    url(r'^asset-stick/', views.add_asset_stick, name='add_asset_stick'),
    url(r'^asset-router/', views.add_asset_router, name='add_asset_router'),
    url(r'^asset-repeater/', views.add_asset_repeater, name='add_asset_repeater'),
    url(r'^asset-rack/', views.add_asset_rack, name='add_asset_rack'),
    url(r'^asset-device/', views.add_asset_device, name='add_asset_device'),
    url(r'^asset-blueprint/', views.add_asset_blueprint, name='add_asset_blueprint'),
    url(r'^(?P<id>[0-9a-f-]+)/blueprint-update/$', views.blueprint_update, name='blueprint_update'),
    url(r'^(?P<id>[0-9a-f-]+)/remove1blueprint/$', views.blueprint_remove1, name='blueprint_remove1'),
    url(r'^blueprints_det/', views.blueprints_detail, name='blueprints_detail'),
    url(r'^(?P<id>[0-9a-f-]+)/blueprint_det/$', views.blueprint_detail, name='blueprint_detail'),
    url(r'^blueprint_list/', views.blueprints_list, name='blueprints_list'),
    url(r'^reps/', views.reports, name='reports'),

    url(r'^(?P<id>[0-9a-f-]+)/remove1lab/$', views.lab_remove1, name='lab_remove1'),
    url(r'^(?P<id>[0-9a-f-]+)/lab-update/$', views.lab_update, name='lab_update'),
    url(r'^asset-lab/', views.add_asset_lab, name='add_asset_lab'),
    url(r'^(?P<id>[0-9a-f-]+)/lab_det/$', views.lab_detail, name='lab_detail'),
    url(r'^lab_list/', views.labs_list, name='labs_list'),
    url(r'^labs_det/', views.labs_detail, name='labs_detail'),
    url(r'^(?P<id>\d+)/lab_det/$', views.lab_detail, name='lab_detail'),
   # url(r'^get_signups/', views.get_signups, name='get_signups'),
    url(r'^chaining/', include('smart_selects.urls')),

    url(r'^(?P<id>[0-9a-f-]+)/remove1junk/$', views.junk_remove1, name='junk_remove1'),
    url(r'^(?P<id>[0-9a-f-]+)/junk-update/$', views.junk_update, name='junk_update'),
    url(r'^add-junk/', views.add_new_junk, name='add_new_junk'),
    url(r'^(?P<id>\d+)/junk_det/$', views.junk_detail, name='junk_detail'),
    url(r'^junk_list/', views.junks_list, name='junks_list'),
    url(r'^junks_det/', views.junks_detail, name='junks_detail'),
    url(r'^(?P<id>[0-9a-f-]+)/junk_det/$', views.junk_detail, name='junk_detail'),
    url(r'^ajax/getusercode/$', views.getusercode, name='getusercode'),
    url(r'^(?P<id>[0-9a-f-]+)/junk-trans/$', views.trans_the_junk, name='trans_the_junk'),
    url(r'^adminsrep/', views.adminsrep, name='adminsrep'),
    url(r'^addmissions/', views.add_mission, name='add_mission'),
    url(r'^listmissions/', views.list_mission, name='list_mission'),
    url(r'^missionsmain/', views.mission_main, name='mission_main'),
    url(r'^law-notes/', views.law_affairs, name='law_affairs'),
    url(r'^law-main/', views.law_affairs_main, name='law_affairs_main'),
    url(r'^law-list/', views.law_affairs_list, name='law_affairs_list'),
    url(r'^(?P<id>\d+)/lawaffairsupdate/$', views.law_affairs_update, name='law_affairs_update'),
    url(r'^lawadd_success/', views.law_add_success, name='law_add_success'),
    url(r'^searchcases/', views.searchcases, name='searchcases'),
    url(r'^restlaw/', views.restlaw, name='restlaw'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#(?P<pk>\d+)
