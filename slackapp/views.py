from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .slack_events import verify_slack_signature, client
import json

@csrf_exempt
def slack_events(request):
    if request.method == 'POST':
        # Verify the request is from Slack
        if not verify_slack_signature(request):
            return HttpResponse(status=403)
        
        # Parse the request body
        data = json.loads(request.body)
        
        # URL verification challenge
        if 'challenge' in data:
            return JsonResponse({'challenge': data['challenge']})
        
        # Handle events
        if 'event' in data:
            event = data['event']
            
            # Handle app mention
            if event.get('type') == 'app_mention':
                channel = event['channel']
                text = event['text']
                
                # Respond to mention
                client.chat_postMessage(
                    channel=channel,
                    text=f"Hello! You mentioned me and said: {text}"
                )
            
            # Handle direct messages
            elif event.get('type') == 'message' and event.get('channel_type') == 'im':
                channel = event['channel']
                text = event.get('text', '')
                
                # Respond to DM
                client.chat_postMessage(
                    channel=channel,
                    text=f"Hi there! I received your message: {text}"
                )
        
        return HttpResponse(status=200)
    return HttpResponse(status=405)