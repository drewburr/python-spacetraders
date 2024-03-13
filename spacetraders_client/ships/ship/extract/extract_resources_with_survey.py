from spacetraders_api_client.api.fleet.extract_resources_with_survey import sync_detailed as post

from spacetraders_api_client.models import extract_resources_with_survey_response_201
Class(name='ExtractResourcesWithSurveyResponse201', module_name='extract_resources_with_survey_response_201')
required_properties = 1


# name: extract-resources-with-survey
# identifier: extract_resources_with_survey
# path: ['ships', '{shipSymbol}', 'extract', 'survey']
# tag: fleet

# path: /my/ships/{shipSymbol}/extract/survey
# method: post
# description: Use a survey when extracting resources from a waypoint. This endpoint requires a survey as the payload, which allows your ship to extract specific yields.
# 
# Send the full survey object as the payload which will be validated according to the signature. If the signature is invalid, or any properties of the survey are changed, the request will fail.
# name: extract-resources-with-survey
# requires_security: True
# summary: Extract Resources with Survey
# responses: module.endpoint.responses
# errors: []

