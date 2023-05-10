from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Dict,
    List,
    Optional,
    TextIO,
    Tuple,
    Type,
    TypeVar,
    cast,
)

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.purchase_cargo_purchase_cargo_201_response_data import (
        PurchaseCargoPurchaseCargo201ResponseData,
    )


T = TypeVar("T", bound="PurchaseCargoPurchaseCargo201Response")


@attr.s(auto_attribs=True)
class PurchaseCargoPurchaseCargo201Response:
    """
    Attributes:
        data (PurchaseCargoPurchaseCargo201ResponseData):
    """

    data: "PurchaseCargoPurchaseCargo201ResponseData"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.purchase_cargo_purchase_cargo_201_response_data import (
            PurchaseCargoPurchaseCargo201ResponseData,
        )

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
        from ..models.purchase_cargo_purchase_cargo_201_response_data import (
            PurchaseCargoPurchaseCargo201ResponseData,
        )

        d = src_dict.copy()
        data = PurchaseCargoPurchaseCargo201ResponseData.from_dict(d.pop("data"))

        purchase_cargo_purchase_cargo_201_response = cls(
            data=data,
        )

        purchase_cargo_purchase_cargo_201_response.additional_properties = d
        return purchase_cargo_purchase_cargo_201_response

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
