from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.waypoint_modifier_symbol import WaypointModifierSymbol

T = TypeVar("T", bound="WaypointModifier")


@_attrs_define
class WaypointModifier:
    """
    Attributes:
        symbol (WaypointModifierSymbol): The unique identifier of the modifier.
        name (str): The name of the trait.
        description (str): A description of the trait.
    """

    symbol: WaypointModifierSymbol
    name: str
    description: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        symbol = self.symbol.value

        name = self.name

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "name": name,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        symbol = WaypointModifierSymbol(d.pop("symbol"))

        name = d.pop("name")

        description = d.pop("description")

        waypoint_modifier = cls(
            symbol=symbol,
            name=name,
            description=description,
        )

        waypoint_modifier.additional_properties = d
        return waypoint_modifier

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
