from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.construction import Construction
    from ..models.ship_cargo import ShipCargo


T = TypeVar("T", bound="SupplyConstructionResponse201Data")


@_attrs_define
class SupplyConstructionResponse201Data:
    """
    Attributes:
        construction (Construction): The construction details of a waypoint.
        cargo (ShipCargo): Ship cargo details.
    """

    construction: "Construction"
    cargo: "ShipCargo"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        construction = self.construction.to_dict()

        cargo = self.cargo.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "construction": construction,
                "cargo": cargo,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.construction import Construction
        from ..models.ship_cargo import ShipCargo

        d = src_dict.copy()
        construction = Construction.from_dict(d.pop("construction"))

        cargo = ShipCargo.from_dict(d.pop("cargo"))

        supply_construction_response_201_data = cls(
            construction=construction,
            cargo=cargo,
        )

        supply_construction_response_201_data.additional_properties = d
        return supply_construction_response_201_data

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
