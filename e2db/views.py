from django.http import HttpResponse

def qr(request):
    from e2db.utils import qr_page
    
    param = request.GET.get('q', '')
    result = qr_page(param)
    return HttpResponse(result)
