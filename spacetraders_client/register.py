from spacetraders_api_client.api.default.register import sync_detailed as post

from spacetraders_api_client.models import register_response_201
Class(name='RegisterResponse201', module_name='register_response_201')
required_properties = 1


# name: register
# identifier: register
# path: ['register']
# tag: default

# path: /register
# method: post
# description: Creates a new agent and ties it to an account. 
# The agent symbol must consist of a 3-14 character string, and will be used to represent your agent. This symbol will prefix the symbol of every ship you own. Agent symbols will be cast to all uppercase characters.
# 
# This new agent will be tied to a starting faction of your choice, which determines your starting location, and will be granted an authorization token, a contract with their starting faction, a command ship that can fly across space with advanced capabilities, a small probe ship that can be used for reconnaissance, and 150,000 credits.
# 
# > #### Keep your token safe and secure
# >
# > Save your token during the alpha phase. There is no way to regenerate this token without starting a new agent. In the future you will be able to generate and manage your tokens from the SpaceTraders website.
# 
# If you are new to SpaceTraders, It is recommended to register with the COSMIC faction, a faction that is well connected to the rest of the universe. After registering, you should try our interactive [quickstart guide](https://docs.spacetraders.io/quickstart/new-game) which will walk you through basic API requests in just a few minutes.
# name: register
# requires_security: False
# summary: Register New Agent
# responses: module.endpoint.responses
# errors: []

