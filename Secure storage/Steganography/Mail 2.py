#API="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"
# ------------------
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'

api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
type = 'classic'
status = 'sent'
start_date = '2023-02-05T21:20:30+01:00'
end_date = '2023-02-06T21:07:00+01:00'
limit = 10
offset = 0

try:
    api_response = api_instance.get_email_campaigns(type=type, status=status, start_date=start_date, end_date=end_date, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->get_email_campaigns: %s\n" % e)