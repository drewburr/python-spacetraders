from typing import (
    Any,
    Dict,
    List,
    TypeVar,
)

from pydantic import BaseModel, Field

from ..models.extraction_yield import ExtractionYield
from ..types import Unset

T = TypeVar("T", bound="Extraction")


class Extraction(BaseModel):
    """Extraction details.

    Attributes:
        ship_symbol (str): Symbol of the ship that executed the extraction.
        yield_ (ExtractionYield): A yield from the extraction operation.
    """

    ship_symbol: str = Field(alias="shipSymbol")
    yield_: "ExtractionYield" = Field(alias="yield")
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
