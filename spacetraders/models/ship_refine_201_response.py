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
    from ..models.ship_refine_201_response_data import ShipRefine201ResponseData


T = TypeVar("T", bound="ShipRefine201Response")


@_attrs_define
class ShipRefine201Response:
    """
    Attributes:
        data (ShipRefine201ResponseData):
    """

    data: "ShipRefine201ResponseData"
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
        from ..models.ship_refine_201_response_data import ShipRefine201ResponseData

        d = src_dict.copy()
        data = ShipRefine201ResponseData.from_dict(d.pop("data"))

        ship_refine_201_response = cls(
            data=data,
        )

        ship_refine_201_response.additional_properties = d
        return ship_refine_201_response

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
