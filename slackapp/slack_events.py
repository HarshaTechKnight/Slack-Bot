import hmac
import hashlib
import json
import time
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from slack_sdk import WebClient

client = WebClient(token=settings.SLACK_BOT_TOKEN)

def verify_slack_signature(request):
    # Get the timestamp and signature from the request headers
    slack_signature = request.headers.get('X-Slack-Signature', '')
    slack_timestamp = request.headers.get('X-Slack-Request-Timestamp', '')
    
    # Verify timestamp is recent (prevent replay attacks)
    if abs(time.time() - int(slack_timestamp)) > 60 * 5:
        return False
    
    # Create the basestring
    basestring = f"v0:{slack_timestamp}:{request.body.decode('utf-8')}"
    
    # Create signature
    my_signature = 'v0=' + hmac.new(
        settings.SLACK_SIGNING_SECRET.encode('utf-8'),
        basestring.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    
    # Compare signatures
    return hmac.compare_digest(my_signature, slack_signature)