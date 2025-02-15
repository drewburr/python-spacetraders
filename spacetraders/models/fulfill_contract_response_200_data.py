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
    from ..models.agent import Agent
    from ..models.contract import Contract


T = TypeVar("T", bound="FulfillContractResponse200Data")


@_attrs_define
class FulfillContractResponse200Data:
    """
    Attributes:
        agent (Agent): Agent details.
        contract (Contract): Contract details.
    """

    agent: "Agent"
    contract: "Contract"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        agent = self.agent.to_dict()

        contract = self.contract.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent": agent,
                "contract": contract,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.agent import Agent
        from ..models.contract import Contract

        d = src_dict.copy()
        agent = Agent.from_dict(d.pop("agent"))

        contract = Contract.from_dict(d.pop("contract"))

        fulfill_contract_response_200_data = cls(
            agent=agent,
            contract=contract,
        )

        fulfill_contract_response_200_data.additional_properties = d
        return fulfill_contract_response_200_data

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
