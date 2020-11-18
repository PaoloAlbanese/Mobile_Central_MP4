from django.shortcuts import render
from .forms import AddProductForm,\
    AddBrandForm, AddSideForm, ProdList, EditProductForm
from products.models import Product, Category, CaroPics
from django.contrib.auth.decorators import login_required

# We're in prodMgt views.


@login_required(redirect_field_name='next', login_url='signin')
def AddProduct(request):
    pName = ""
    AddProd = ()
    subForm = ""
    Dear = ""

    if request.user.is_authenticated and request.user.first_name:
        Dear = str(request.user.first_name)
    if request.method == 'POST':
        print(request.POST)
        if 'subForm' in request.POST:
            subForm = request.POST['subForm']

        print('quale is: ', subForm)

        if subForm == 'prod':

            try:
                pForm = AddProductForm(request.POST, request.FILES)

                if pForm.is_valid():
                    pForm.save()

                    AddProd = pForm.instance
                    pName = AddProd.name

            except:
                pForm = AddProductForm()

    else:
        pForm = AddProductForm()

    context = {
        'pForm': pForm,
        'pName': pName,
        'AddProd': AddProd,
        'Dear': Dear,

    }
    return render(request, 'prodMgt/addProduct.html', context)


@login_required(redirect_field_name='next', login_url='signin')
def AddBrand(request):
    AddBrand = ()
    bForm = AddBrandForm()
    Dear = ""
    bName = ""
    subForm = ""

    if request.user.is_authenticated and request.user.first_name:
        Dear = str(request.user.first_name)
    if request.method == 'POST':
        print(request.POST)
        if 'subForm' in request.POST:
            subForm = request.POST['subForm']

        if subForm == 'brand':
            try:
                bForm = AddBrandForm(request.POST)

                if bForm.is_valid():
                    bForm.save()
                    AddBrand = bForm.instance
                    bName = AddBrand.name
            except:
                bForm = AddBrandForm()

    else:

        bForm = AddBrandForm()

    context = {

        'AddBrand': AddBrand,
        'bForm': bForm,
        'bName': bName,
        'Dear': Dear,
    }
    return render(request, 'prodMgt/addBrand.html', context)


@login_required(redirect_field_name='next', login_url='signin')
def AddSidePic(request):
    AddSidePic = ()
    cProduct = ""
    cForm = AddSideForm()
    lookupProd = ProdList()
    caropics = ()
    subForm = ""
    Dear = ""

    if request.user.is_authenticated and request.user.first_name:
        Dear = str(request.user.first_name)
    if request.method == 'POST':
        print(request.POST)
        if 'subForm' in request.POST:
            subForm = request.POST['subForm']

        if subForm == 'sidepic':
            try:
                cForm = AddSideForm(request.POST, request.FILES)

                if cForm.is_valid():
                    cForm.save()
                    AddSidePic = cForm.instance
                    cProduct = AddSidePic.product
            except:
                cForm = AddSideForm()

    else:
        cForm = AddSideForm()

    context = {
        'AddSidePic': AddSidePic,
        'cProduct': cProduct,
        'cForm': cForm,
        'lookupProd': lookupProd,
        'caropics': caropics,
        'Dear': Dear,
    }
    return render(request, 'prodMgt/addSidePicture.html', context)


@login_required(redirect_field_name='next', login_url='signin')
def EditProduct(request):
    EditProd = ()
    eName = ""
    eForm = EditProductForm()
    lookupProd = ProdList()
    dpForm = ()
    subForm = ""
    Dear = ""
    selprodId = ""
    pDeleted = ""
    theresPic = ""
    p_to_change = ""
    pChanged = ""

    if request.user.is_authenticated and request.user.first_name:
        Dear = str(request.user.first_name)
    if request.method == 'POST':
        if 'subForm' in request.POST:
            subForm = request.POST['subForm']

        if subForm == 'findProd':
            theProd = request.POST['lookupProd']
            selProd = Product.objects.get(id=theProd)
            EditProd = EditProductForm(instance=selProd)
            eForm = EditProd
            selprodId = theProd

        elif subForm == 'editProd':

            try:
                eForm = EditProductForm(request.POST, request.FILES)
                if 'with_prod_id' in request.POST:
                    with_prod_id = request.POST['with_prod_id']
                    pickprod = Product.objects.get(id=with_prod_id)
                else:
                    theProd = request.POST['name']
                    pickprod = Product.objects.get(name=theProd)

                if 'p_to_del' in request.POST:
                    pDeleted = str(pickprod)
                    pickprod.delete()

                elif 'p_to_del' not in request.POST:

                    p_to_change = Product.objects.get(id=pickprod.id)
                    eName = str(pickprod)
                    if 'name' in request.POST:

                        p_to_change.name = request.POST['name']
                        pChanged = p_to_change
                    if 'price' in request.POST:
                        p_to_change.price = request.POST['price']
                        pChanged = p_to_change
                    if 'description' in request.POST:
                        p_to_change.description = request.POST['description']
                        pChanged = p_to_change
                    if 'stock' in request.POST:
                        p_to_change.stock = request.POST['stock']
                        pChanged = p_to_change
                    if 'available' in request.POST:
                        if 'available' in request.POST:
                            available = request.POST['available']
                            if available == 'on':
                                p_to_change.available = True
                                pChanged = p_to_change
                    else:
                        p_to_change.available = False
                    if 'latest' in request.POST:
                        latest = request.POST['latest']
                        if latest == 'on':
                            p_to_change.latest = True
                            pChanged = p_to_change
                    else:
                        p_to_change.latest = False
                    if 'best' in request.POST:
                        best = request.POST['best']
                        if best == 'on':
                            p_to_change.best = True
                            pChanged = p_to_change
                    else:
                        p_to_change.best = False

                    if 'category' in request.POST:
                        upCategory = request.POST['category']
                        pickCateg = Category.objects.get(id=upCategory)
                        p_to_change.category = pickCateg
                        pChanged = p_to_change

                    if 'image' in request.FILES:
                        upImage = request.FILES['image']
                        p_to_change.image = upImage
                        theresPic = str(p_to_change)
                        pChanged = p_to_change
                    p_to_change.save()

            except Exception as e:
                raise e

    else:

        eForm = AddProductForm()
        dpForm = ()

    context = {

        'eForm': eForm,
        'EditProd': EditProd,
        'eName': eName,
        'lookupProd': lookupProd,
        'dpForm': dpForm,
        'Dear': Dear,
        'selprodId': selprodId,
        'pDeleted': pDeleted,
        'theresPic': theresPic,
        'p_to_change': p_to_change,
        'pChanged': pChanged,

    }
    return render(request, 'prodMgt/editProduct.html', context)


@login_required(redirect_field_name='next', login_url='signin')
def DelSidePic(request):
    lookupProd = ProdList()
    caropics = ()
    selSideProd = ""
    sidePicDeletion = ""
    pic_to_del = ""
    subForm = ""
    TheSidePic = ""
    Dear = ""

    if request.user.is_authenticated and request.user.first_name:
        Dear = str(request.user.first_name)
    if request.method == 'POST':
        if 'subForm' in request.POST:
            subForm = request.POST['subForm']
        if 'pic_to_del' in request.POST:
            pic_to_del = request.POST['pic_to_del']

        if subForm == 'findSideProd':
            theProd = request.POST['lookupProd']
            selSideProd = Product.objects.get(id=theProd)
            caropics = CaroPics.objects.filter(product=selSideProd)

        if pic_to_del:

            TheSidePic = CaroPics.objects.get(id=pic_to_del)
            TheSidePic.delete()
            sidePicDeletion = "deleted"

    context = {
        'lookupProd': lookupProd,
        'caropics': caropics,
        'selSideProd': selSideProd,
        'sidePicDeletion': sidePicDeletion,
        'TheSidePic': TheSidePic,
        'Dear': Dear,
    }
    return render(request, 'prodMgt/deleteSidePicture.html', context)
