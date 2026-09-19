from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ModelTypeInfoOpenApiVO")


@_attrs_define
class ModelTypeInfoOpenApiVO:
    """Model type information.

    Attributes:
        show_model (str): Model complex displayed on the front end, you can also get this field throw: "Get the model of
            the specified site"
        compound_model (str): Model complex used on the backend, you can also get this field throw: "Get the model of
            the specified site"
    """

    show_model: str
    compound_model: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        show_model = self.show_model

        compound_model = self.compound_model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "showModel": show_model,
                "compoundModel": compound_model,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        show_model = d.pop("showModel")

        compound_model = d.pop("compoundModel")

        model_type_info_open_api_vo = cls(
            show_model=show_model,
            compound_model=compound_model,
        )

        model_type_info_open_api_vo.additional_properties = d
        return model_type_info_open_api_vo

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
