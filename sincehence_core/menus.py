# from pprint import pprint
# from django.apps import apps
# from django.conf import settings
# from django.shortcuts import render
# from django.urls import reverse, reverse_lazy
# from django.utils.module_loading import import_string
# from django.contrib.auth.decorators import login_required
# from django.contrib.contenttypes.models import ContentType
# from django.templatetags.static import static
# # from core.models import (
# #     Category
# # )
from django.urls import reverse
from sincehence_core.helper import (
    pages,
    # categories,
    model_with_field,

)
from django.core.cache import cache





# def category_menus(request):
#     all_cat = categories().filter(add_to_cat_menu = True, sites__id = request.site.id) 
#     menu_items = []
#     for cat in all_cat:
#         if cat.have_items:         
#             item_dict = {
#                 'title' : cat.title,
#                 'url' : cat.get_absolute_url(),
#                 'data_set': False,
#                 'icon' : cat.icon
                
#             }
#             menu_items.append(item_dict)
        
#     return menu_items

def page_menus(request):
    
    menu_items = cache.get('sh_page_menu_items')
    if menu_items is not None:
        return menu_items
    
    all_page = pages().filter(add_to_page_menu = True, sites__id = request.site.id)     
    menu_items = []
    for p in all_page:
        item_dict = {
            'title' : p.title,
            'url' : p.get_absolute_url(), 
            'data_set': False  
        }
        menu_items.append(item_dict)    
    cache.set('sh_page_menu_items', menu_items, timeout=60 * 60)
        
    return menu_items




def footer_menu(request):
    
    menu_items = cache.get('sh_footer_menu_items')
    if menu_items is not None:
        return menu_items
    
    
    
    objects_with_footer_menu = []
    for model in model_with_field('add_to_footer_menu'):
        objects_with_footer_menu += model.objects.filter(add_to_footer_menu=True, sites__id = request.site.id).order_by('title')        
    menu_items = []     
    
    
    for obj in objects_with_footer_menu:
        item_dict = {
            'title' : obj.title,
            'url' : obj.get_absolute_url(),  
            'data_set': False 
        }
        menu_items.append(item_dict)      
        
        
    menu_items.append(
        {'title': 'Blog', 'url': reverse('sincehence_core:latest_blogs'), 'data_set': False},        
        ) 
    
    menu_items.append(
        {'title': 'Contact Us', 'url': reverse('sincehence_core:contact'), 'data_set': False},        
        ) 
    
    #Add more manual above this line ====================#        
    nav_one = []
    nav_two = []
    nav_three = []
    nav_four = []     

    for mi in menu_items:        
        if len(nav_one) <= round(len(menu_items)/4)-1:
            nav_one.append(mi)
        elif len(nav_two) <= round(len(menu_items)/4)-1:            
            nav_two.append(mi)            
        elif len(nav_three) <= round(len(menu_items)/4)-1:            
            nav_three.append(mi)
        else:
            nav_four.append(mi)             
      
    menu_pack = []    
    menu_pack.append(
        {'title': 'Navigation', 'url': '#navone', 'data_set': nav_one},        
        )         
    menu_pack.append(
        {'title': 'Continued', 'url': '#navtwo', 'data_set': nav_two},        
        )    
    menu_pack.append(
        {'title': 'Continued', 'url': '#navthree', 'data_set': nav_three},        
        )        
    menu_pack.append(
        {'title': 'Continued', 'url': '#navfour', 'data_set': nav_four},        
        ) 
    
    cache.set('sh_footer_menu_items', menu_pack, timeout=60 * 60)
    
        
    return menu_pack

def header_menu(request):
    
    menu_items = cache.get('sh_header_menu_items')
    if menu_items is not None:
        return menu_items
    
    
    objects_with_header_menu = []

    for model in model_with_field('add_to_header_menu'):     
        objects_with_header_menu += model.objects.filter(add_to_header_menu=True, sites__id = request.site.id).order_by('title')
        
    menu_items = [] 
    menu_items.append(
        {'title': 'Home', 'url': '/', 'data_set': False},        
        )     
    
    menu_items.append(
        {'title': 'Page', 'url': False, 'data_set': page_menus(request) },        
        ) 
    for obj in objects_with_header_menu:
        have_items = getattr(obj, 'have_items', None)
        if (have_items and obj.have_items) or obj.add_to_header_menu:
            item_dict = {
                'title': obj.title,
                'url': obj.get_absolute_url(),
                'data_set': False
            }
            menu_items.append(item_dict)
            
    menu_items.append(
        {'title': 'Blog', 'url': reverse('sincehence_core:latest_blogs'), 'data_set': False},        
        )    
    
    menu_items.append(
        {'title': 'Contact', 'url': reverse('sincehence_core:contact'), 'data_set': False},        
        ) 
    
    cache.set('sh_header_menu_items', menu_items, timeout=60 * 60)
        
    return menu_items



    



    