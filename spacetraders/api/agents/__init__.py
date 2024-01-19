""" Contains methods for accessing the API """

from . import get_agent, get_agents, get_my_agent


class Agents:
    get_my_agent = get_my_agent
    get_agents = get_agents
    get_agent = get_agent


__all__ = "Agents"
