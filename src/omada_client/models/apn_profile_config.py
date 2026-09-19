from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApnProfileConfig")


@_attrs_define
class ApnProfileConfig:
    """
    Attributes:
        name (str): APN profile name, name should contain 1 to 64 characters.
        pdp_type (int): PdpType should be a value as follows: 0: IPv4; 1: IPv6; 2: IPv4 & IPv6.
        apn_type (int): ApnType should be a value as follows: 0: static; 1: dynamic.
        authentication (int): Authentication should be a value as follows: 0: None; 1: PAP; 2: CHAP
        apn (str | Unset): Access point name, only for apnType static, should contain 1 to 62 characters and should meet
            the following requirements:
                1. Only allow letters, numbers, hyphens and dots.
                2. Should not start with "rac", "lac", "sgsn" or "rnc" and end with ".gprs", ignoring case.
                3. Should not contain ".-", "-." and spaces.
        username (str | Unset): Username should contain 1 to 64 characters, spaces, comma, single quotation marks and
            double quotation marks are not allowed.
        password (str | Unset): Password should contain 1 to 64 characters, spaces, comma, single quotation marks and
            double quotation marks are not allowed.
        apply_to_sim (int | Unset): When the device supports Dual-SIM card, parameter [applyToSim] should be a value as
            follows: 1: apply to SIM1; 2: apply to SIM2; 3: apply to SIM1 and SIM2.
    """

    name: str
    pdp_type: int
    apn_type: int
    authentication: int
    apn: str | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    apply_to_sim: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        pdp_type = self.pdp_type

        apn_type = self.apn_type

        authentication = self.authentication

        apn = self.apn

        username = self.username

        password = self.password

        apply_to_sim = self.apply_to_sim

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "pdpType": pdp_type,
                "apnType": apn_type,
                "authentication": authentication,
            }
        )
        if apn is not UNSET:
            field_dict["apn"] = apn
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if apply_to_sim is not UNSET:
            field_dict["applyToSIM"] = apply_to_sim

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        pdp_type = d.pop("pdpType")

        apn_type = d.pop("apnType")

        authentication = d.pop("authentication")

        apn = d.pop("apn", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        apply_to_sim = d.pop("applyToSIM", UNSET)

        apn_profile_config = cls(
            name=name,
            pdp_type=pdp_type,
            apn_type=apn_type,
            authentication=authentication,
            apn=apn,
            username=username,
            password=password,
            apply_to_sim=apply_to_sim,
        )

        apn_profile_config.additional_properties = d
        return apn_profile_config

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
