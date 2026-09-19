from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="PortMaskOpenApiVO")


@_attrs_define
class PortMaskOpenApiVO:
    """Port mask list. [portType] value of 1 is required

    Attributes:
        port (int): Port should be within the range of 0-65535
        mask (str): Port mask should be 4 hex number(0-9, A-F), e.g. 0000 or FFFF
    """

    port: int
    mask: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        mask = self.mask

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "port": port,
                "mask": mask,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port")

        mask = d.pop("mask")

        port_mask_open_api_vo = cls(
            port=port,
            mask=mask,
        )

        port_mask_open_api_vo.additional_properties = d
        return port_mask_open_api_vo

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
