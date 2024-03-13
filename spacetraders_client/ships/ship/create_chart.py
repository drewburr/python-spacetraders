from spacetraders_api_client.api.fleet.create_chart import sync_detailed as post

from spacetraders_api_client.models import create_chart_response_201
Class(name='CreateChartResponse201', module_name='create_chart_response_201')
required_properties = 1


# name: create-chart
# identifier: create_chart
# path: ['ships', '{shipSymbol}', 'chart']
# tag: fleet

# path: /my/ships/{shipSymbol}/chart
# method: post
# description: Command a ship to chart the waypoint at its current location.
# 
# Most waypoints in the universe are uncharted by default. These waypoints have their traits hidden until they have been charted by a ship.
# 
# Charting a waypoint will record your agent as the one who created the chart, and all other agents would also be able to see the waypoint's traits.
# name: create-chart
# requires_security: True
# summary: Create Chart
# responses: module.endpoint.responses
# errors: []

