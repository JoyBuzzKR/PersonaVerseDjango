import json
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import MyBeanieDocument
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
async def post_mybeanie(request):
    if request.method == 'POST':
        # Parse JSON body
        body = json.loads(request.body)

        doc = await MyBeanieDocument(**body).insert()
        
        response_data = {
            "message": "success",
            "data": {
                "_id": str(doc.id),
                "title": doc.title,
                "description": doc.description,
                "created_at": doc.created_at.isoformat()
            }
        }
        
        return HttpResponse(
            json.dumps(response_data), 
            content_type='application/json'
        )

    return HttpResponseNotAllowed(["POST"])