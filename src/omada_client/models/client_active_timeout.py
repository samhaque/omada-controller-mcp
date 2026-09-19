from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ClientActiveTimeout")


@_attrs_define
class ClientActiveTimeout:
    """
    Attributes:
        client_active_timeout_min (int): Client Active Timeout should be within the range of 3-10 minutes
    """

    client_active_timeout_min: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_active_timeout_min = self.client_active_timeout_min

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientActiveTimeoutMin": client_active_timeout_min,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        client_active_timeout_min = d.pop("clientActiveTimeoutMin")

        client_active_timeout = cls(
            client_active_timeout_min=client_active_timeout_min,
        )

        client_active_timeout.additional_properties = d
        return client_active_timeout

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
