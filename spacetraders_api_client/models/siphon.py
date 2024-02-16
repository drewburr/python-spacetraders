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
    from ..models.siphon_yield import SiphonYield


T = TypeVar("T", bound="Siphon")


@_attrs_define
class Siphon:
    """Siphon details.

    Attributes:
        ship_symbol (str): Symbol of the ship that executed the siphon.
        yield_ (SiphonYield): A yield from the siphon operation.
    """

    ship_symbol: str
    yield_: "SiphonYield"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        ship_symbol = self.ship_symbol
        yield_ = self.yield_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shipSymbol": ship_symbol,
                "yield": yield_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.siphon_yield import SiphonYield

        d = src_dict.copy()
        ship_symbol = d.pop("shipSymbol")

        yield_ = SiphonYield.from_dict(d.pop("yield"))

        siphon = cls(
            ship_symbol=ship_symbol,
            yield_=yield_,
        )

        siphon.additional_properties = d
        return siphon

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
