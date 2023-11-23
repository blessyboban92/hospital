
from django.shortcuts import render, redirect
from django.contrib import auth, messages

from .models import *
def addbrand(request):
    brands = list(BrandMaster.objects.all())
    brands.reverse()
    context = {
        'brands': brands
    }
    return render(request, 'brand.html', context)

def add_brand(request):
    brands = BrandMaster.objects.all()
    if request.method == "POST":
        brandname= request.POST['brandname']
        branddescription = request.POST['branddescription']
        Brands = BrandMaster(brandname=brandname, branddescription=branddescription)
        Brands.save()
        messages.info(request, "Brand added Successfully")
        return redirect('hiapp:add_brand')
    context = {
        'brands': brands
    }
    return render(request,'brand.html',context)
def delete_brand(request,brandid):
        brands=BrandMaster.objects.get(id=brandid)
        brands.delete()
        messages.info(request,"Brand Deleted Successfully")
        return redirect('hiapp:add_brand')
def update_brand(request,brandid):
    brands = BrandMaster.objects.get(id=brandid)
    brands.brandname= request.POST['brandname']
    brands.branddescription = request.POST['branddescription']
    brands.save()
    messages.info(request,"Brand updated successfully")
    return redirect('hiapp:add_brand')
def edit_brand(request,brandid):
    sel_brands=BrandMaster.objects.get(id=brandid)
    brands=BrandMaster.objects.all()
    context = {
        'sel_brands':sel_brands,
        'brands':brands
    }
    return render(request, 'brand.html', context)
def addcategory(request):
    categories = list(CategoryMaster.objects.all())
    categories.reverse()
    context = {
        'categories': categories
    }
    return render(request,'category.html',context)
def add_category(request):
    categories = CategoryMaster.objects.all()
    if request.method == "POST":
        categoryname= request.POST['categoryname']
        categorydescription = request.POST['categorydescription']
        Categories = CategoryMaster(categoryname=categoryname, categorydescription=categorydescription)
        Categories.save()
        messages.info(request, "Category added Successfully")
        return redirect('hiapp:add_category')
    context = {
        'categories': categories
    }
    return render(request,'category.html',context)
def delete_category(request,categoryid):
    categories=CategoryMaster.objects.get(id=categoryid)
    categories.delete()
    messages.info(request,"Category Deleted Successfully")
    return redirect('hiapp:add_category')
def update_category(request,categoryid):
    categories = CategoryMaster.objects.get(id=categoryid)
    categories.categoryname= request.POST['categoryname']
    categories.categorydescription = request.POST['categorydescription']
    categories.save()
    messages.info(request,"Category updated successfully")
    return redirect('hiapp:add_category')
def edit_category(request,categoryid):
    sel_categories=CategoryMaster.objects.get(id=categoryid)
    categories=CategoryMaster.objects.all()
    context = {
        'sel_categories':sel_categories,
        'categories':categories
    }
    return render(request, 'category.html', context)
def additem(request):
    categories = CategoryMaster.objects.all()
    brands = BrandMaster.objects.all()
    item_list = list(ItemMaster.objects.all())
    item_list.reverse()
    context = {
        'categories': categories,
        'brands': brands,
        'item_list':item_list,
    }
    return render(request,'item.html',context)
def add_item(request):
    categories = CategoryMaster.objects.all()
    brands = BrandMaster.objects.all()
    item_list = list(ItemMaster.objects.all())
    item_list.reverse()
    if request.method == "POST":
        itemname =request.POST['itemname']
        itemcode =request.POST['itemcode']
        category_id = request.POST['category']
        salestax=request.POST['salestax']
        mrp = request.POST['mrp']
        barcode = request.POST['barcode']
        hsncode = request.POST['hsncode']
        unit = request.POST['unit']
        brand_id = request.POST['brand']
        purchasetax = request.POST['purchasetax']
        item = ItemMaster(itemname=itemname,itemcode=itemcode,category_id=category_id,salestax=salestax,mrp=mrp,barcode=barcode,hsncode=hsncode,unit=unit,brand_id=brand_id,purchasetax=purchasetax)
        item.save()
        messages.info(request,"Item added Successfully")
        return redirect('hiapp:add_item')
    context={
            'item_list' : item_list,
            'categories' :categories,
            'brands' :brands
    }
    return render(request,"item.html",context)
def delete_item(request,itemid):
        items = ItemMaster.objects.get(id=itemid)
        items.delete()
        messages.info(request, "Item Deleted Successfully")
        return redirect('hiapp:add_item')
def update_item(request, itemid):
    items = ItemMaster.objects.get(id=itemid)
    items.itemname = request.POST['itemname']
    items.itemcode = request.POST['itemcode']
    items.category_id = request.POST['category']
    items.salestax = request.POST['salestax']
    items.mrp = request.POST['mrp']
    items.barcode = request.POST['barcode']
    items.hsncode = request.POST['hsncode']
    items.unit = request.POST['unit']
    items.brand_id = request.POST['brand']
    items.purchasetax = request.POST['purchasetax']
    items.save()
    messages.info(request, "Item updated successfully")
    return redirect('hiapp:add_item')

def edit_item(request, itemid):
    sel_items = ItemMaster.objects.get(id=itemid)
    items = ItemMaster.objects.all()
    context = {
        'sel_items': sel_items,
        'items': items,
        'categories': CategoryMaster.objects.all(),
        'brands': BrandMaster.objects.all(),
    }
    return render(request, 'item.html', context)



