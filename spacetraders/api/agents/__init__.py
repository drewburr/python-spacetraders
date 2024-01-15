""" Contains methods for accessing the API """


from .get_agent import asyncio_detailed as get_agent_asyncio
from .get_agent import sync_detailed as get_agent
from .get_agents import asyncio_detailed as get_agents_asyncio
from .get_agents import sync_detailed as get_agents
from .get_my_agent import asyncio_detailed as get_my_agent_asyncio
from .get_my_agent import sync_detailed as get_my_agent


class Agents:
    get_my_agent = get_my_agent
    get_agents = get_agents
    get_agent = get_agent


class AsyncAgents:
    get_my_agent = get_my_agent_asyncio
    get_agents = get_agents_asyncio
    get_agent = get_agent_asyncio


__all__ = ("Agents", "AsyncAgents")
