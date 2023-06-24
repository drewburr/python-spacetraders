from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.agent import Agent
from ..models.ship_cargo import ShipCargo
from ..models.ship_modification_transaction import ShipModificationTransaction
from ..models.ship_mount import ShipMount
from ..types import Unset

T = TypeVar("T", bound="RemoveMountRemoveMount201ResponseData")


class RemoveMountRemoveMount201ResponseData(BaseModel):
    """
    Attributes:
        agent (Agent): Agent details.
        mounts (List['ShipMount']): List of installed mounts after the removal of the selected mount.
        cargo (ShipCargo): Ship cargo details.
        transaction (ShipModificationTransaction): Result of a transaction for a ship modification, such as installing a
            mount or a module.
    """

    agent: "Agent" = Field(alias="agent")
    mounts: List["ShipMount"] = Field(alias="mounts")
    cargo: "ShipCargo" = Field(alias="cargo")
    transaction: "ShipModificationTransaction" = Field(alias="transaction")
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
