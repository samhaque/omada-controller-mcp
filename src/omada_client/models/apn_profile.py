from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApnProfile")


@_attrs_define
class ApnProfile:
    """
    Attributes:
        name (str): APN profile name, name should contain 1 to 64 characters.
        pdp_type (int): PdpType should be a value as follows: 0: IPv4; 1: IPv6; 2: IPv4 & IPv6.
        apn_type (int): ApnType should be a value as follows: 0: static; 1: dynamic.
        authentication (int): Authentication should be a value as follows: 0: None; 1: PAP; 2: CHAP
        id (str | Unset): APN profile ID
        apn (str | Unset): Access point name, only for apnType static, should contain 1 to 64 characters and should meet
            the following requirements:
                1. Should not start with "rac", "lac", "sgsn" or "rnc" and end with ".gprs", ignoring case.
                2. Should not contain ".*.", ".-", "-." and spaces.
                3. Should not contain any of the characters #!$%^&*(),:;"'|\\@.
        username (str | Unset): Username should contain 1 to 64 characters, spaces, comma, single quotation marks and
            double quotation marks are not allowed.
        password (str | Unset): Password should contain 1 to 64 characters, spaces, comma, single quotation marks and
            double quotation marks are not allowed.
        build_in (bool | Unset): Indicates whether this APN profile is a built-in APN profile for SIM card.
        apply_to_sim (int | Unset): 1: apply to SIM1; 2: apply to SIM2; 3: apply to SIM1 and SIM2.
    """

    name: str
    pdp_type: int
    apn_type: int
    authentication: int
    id: str | Unset = UNSET
    apn: str | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    build_in: bool | Unset = UNSET
    apply_to_sim: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        pdp_type = self.pdp_type

        apn_type = self.apn_type

        authentication = self.authentication

        id = self.id

        apn = self.apn

        username = self.username

        password = self.password

        build_in = self.build_in

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
        if id is not UNSET:
            field_dict["id"] = id
        if apn is not UNSET:
            field_dict["apn"] = apn
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if build_in is not UNSET:
            field_dict["buildIn"] = build_in
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

        id = d.pop("id", UNSET)

        apn = d.pop("apn", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        build_in = d.pop("buildIn", UNSET)

        apply_to_sim = d.pop("applyToSIM", UNSET)

        apn_profile = cls(
            name=name,
            pdp_type=pdp_type,
            apn_type=apn_type,
            authentication=authentication,
            id=id,
            apn=apn,
            username=username,
            password=password,
            build_in=build_in,
            apply_to_sim=apply_to_sim,
        )

        apn_profile.additional_properties = d
        return apn_profile

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
