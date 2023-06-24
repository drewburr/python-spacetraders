from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.agent import Agent
from ..models.market_transaction import MarketTransaction
from ..models.ship_fuel import ShipFuel
from ..types import Unset

T = TypeVar("T", bound="RefuelShipResponse200Data")


class RefuelShipResponse200Data(BaseModel):
    """
    Attributes:
        agent (Agent): Agent details.
        fuel (ShipFuel): Details of the ship's fuel tanks including how much fuel was consumed during the last transit
            or action.
        transaction (MarketTransaction): Result of a transaction with a market.
    """

    agent: "Agent" = Field(alias="agent")
    fuel: "ShipFuel" = Field(alias="fuel")
    transaction: "MarketTransaction" = Field(alias="transaction")
    additional_properties: Dict[str, Any] = {}

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

    def dict(self, *args, **kwargs):
        output = super().dict(*args, **kwargs)
        return {k: v for k, v in output.items() if not isinstance(v, Unset)}

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
