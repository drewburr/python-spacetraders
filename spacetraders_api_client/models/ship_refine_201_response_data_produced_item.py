from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field


T = TypeVar("T", bound="ShipRefine201ResponseDataProducedItem")


@_attrs_define
class ShipRefine201ResponseDataProducedItem:
    """
    Attributes:
        trade_symbol (str): Symbol of the good.
        units (int): Amount of units of the good.
    """

    trade_symbol: str
    units: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        trade_symbol = self.trade_symbol

        units = self.units

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tradeSymbol": trade_symbol,
                "units": units,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        trade_symbol = d.pop("tradeSymbol")

        units = d.pop("units")

        ship_refine_201_response_data_produced_item = cls(
            trade_symbol=trade_symbol,
            units=units,
        )

        ship_refine_201_response_data_produced_item.additional_properties = d
        return ship_refine_201_response_data_produced_item

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
