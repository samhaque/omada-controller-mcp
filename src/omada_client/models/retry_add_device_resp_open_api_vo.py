from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetryAddDeviceRespOpenApiVO")


@_attrs_define
class RetryAddDeviceRespOpenApiVO:
    """
    Attributes:
        pre_config_retry_type (int | Unset): 1: need username and pwd; 2: don't need need username and pwd
    """

    pre_config_retry_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pre_config_retry_type = self.pre_config_retry_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pre_config_retry_type is not UNSET:
            field_dict["preConfigRetryType"] = pre_config_retry_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        pre_config_retry_type = d.pop("preConfigRetryType", UNSET)

        retry_add_device_resp_open_api_vo = cls(
            pre_config_retry_type=pre_config_retry_type,
        )

        retry_add_device_resp_open_api_vo.additional_properties = d
        return retry_add_device_resp_open_api_vo

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
