from spacetraders_api_client.api.fleet.create_survey import sync_detailed as post

from spacetraders_api_client.models import create_survey_response_201

# name: create-survey
# identifier: create_survey
# path: ['my', 'ships', '{shipSymbol}', 'survey']
# tag: fleet

# path: /my/ships/{shipSymbol}/survey
# method: post
# description: Create surveys on a waypoint that can be extracted such as asteroid fields. A survey focuses on specific types of deposits from the extracted location. When ships extract using this survey, they are guaranteed to procure a high amount of one of the goods in the survey.
# 
# In order to use a survey, send the entire survey details in the body of the extract request.
# 
# Each survey may have multiple deposits, and if a symbol shows up more than once, that indicates a higher chance of extracting that resource.
# 
# Your ship will enter a cooldown after surveying in which it is unable to perform certain actions. Surveys will eventually expire after a period of time or will be exhausted after being extracted several times based on the survey's size. Multiple ships can use the same survey for extraction.
# 
# A ship must have the `Surveyor` mount installed in order to use this function.
# name: create-survey
# requires_security: True
# summary: Create Survey
# responses: module.endpoint.responses
# errors: []

