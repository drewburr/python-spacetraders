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
    from ..models.purchase_ship_response_201_data import PurchaseShipResponse201Data


T = TypeVar("T", bound="PurchaseShipResponse201")


@_attrs_define
class PurchaseShipResponse201:
    """
    Attributes:
        data (PurchaseShipResponse201Data):
    """

    data: "PurchaseShipResponse201Data"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.purchase_ship_response_201_data import PurchaseShipResponse201Data

        d = src_dict.copy()
        data = PurchaseShipResponse201Data.from_dict(d.pop("data"))

        purchase_ship_response_201 = cls(
            data=data,
        )

        purchase_ship_response_201.additional_properties = d
        return purchase_ship_response_201

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
