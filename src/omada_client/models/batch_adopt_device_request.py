from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchAdoptDeviceRequest")


@_attrs_define
class BatchAdoptDeviceRequest:
    """
    Attributes:
        username (str | Unset): Adopt device username. It should contain 1 to 64 characters.
        password (str | Unset): Adopt device password. It should contain 1 to 64 characters.
        macs (list[str] | Unset): MAC list of devices. E.g. AA-BB-CC-DD-11-22
    """

    username: str | Unset = UNSET
    password: str | Unset = UNSET
    macs: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        macs: list[str] | Unset = UNSET
        if not isinstance(self.macs, Unset):
            macs = self.macs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if macs is not UNSET:
            field_dict["macs"] = macs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        macs = cast(list[str], d.pop("macs", UNSET))

        batch_adopt_device_request = cls(
            username=username,
            password=password,
            macs=macs,
        )

        batch_adopt_device_request.additional_properties = d
        return batch_adopt_device_request

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
