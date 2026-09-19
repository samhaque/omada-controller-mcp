from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dot_1x_port_info_open_api_vo import Dot1XPortInfoOpenApiVO


T = TypeVar("T", bound="Dot1XSwitchInfoOpenApiVO")


@_attrs_define
class Dot1XSwitchInfoOpenApiVO:
    """
    Attributes:
        name (str | Unset): Switch name
        mac (str | Unset): Switch MAC address
        model (str | Unset): Switch model
        version (str | Unset): Switch firmwareVersion
        status (str | Unset): Device status
        status_category (int | Unset): Device status category, 0: Disconnected, 1: Connected, 2: Pending,3: Heartbeat
            Missed, 4: Isolated
        added_in_advanced (bool | Unset): Whether the device is added offline
        ports (list[Dot1XPortInfoOpenApiVO] | Unset): Switch port information
        support_vrf (bool | Unset): Whether the switch supports VRF
        account_vrf_id (str | Unset): Account VRF ID
        auth_vrf_id (str | Unset): Auth VRF ID
        support_single_mab_auth (bool | Unset): Whether the switch supports single MAB Authentication.If not supported,
            it will not take effect when configuring single MAB authentication for the port of the switch.
        port_configured (bool | Unset): Is there any port configured with 802.1x or MAB authentication.
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    model: str | Unset = UNSET
    version: str | Unset = UNSET
    status: str | Unset = UNSET
    status_category: int | Unset = UNSET
    added_in_advanced: bool | Unset = UNSET
    ports: list[Dot1XPortInfoOpenApiVO] | Unset = UNSET
    support_vrf: bool | Unset = UNSET
    account_vrf_id: str | Unset = UNSET
    auth_vrf_id: str | Unset = UNSET
    support_single_mab_auth: bool | Unset = UNSET
    port_configured: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        model = self.model

        version = self.version

        status = self.status

        status_category = self.status_category

        added_in_advanced = self.added_in_advanced

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        support_vrf = self.support_vrf

        account_vrf_id = self.account_vrf_id

        auth_vrf_id = self.auth_vrf_id

        support_single_mab_auth = self.support_single_mab_auth

        port_configured = self.port_configured

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if model is not UNSET:
            field_dict["model"] = model
        if version is not UNSET:
            field_dict["version"] = version
        if status is not UNSET:
            field_dict["status"] = status
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if added_in_advanced is not UNSET:
            field_dict["addedInAdvanced"] = added_in_advanced
        if ports is not UNSET:
            field_dict["ports"] = ports
        if support_vrf is not UNSET:
            field_dict["supportVrf"] = support_vrf
        if account_vrf_id is not UNSET:
            field_dict["accountVrfId"] = account_vrf_id
        if auth_vrf_id is not UNSET:
            field_dict["authVrfId"] = auth_vrf_id
        if support_single_mab_auth is not UNSET:
            field_dict["supportSingleMabAuth"] = support_single_mab_auth
        if port_configured is not UNSET:
            field_dict["portConfigured"] = port_configured

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dot_1x_port_info_open_api_vo import (
            Dot1XPortInfoOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        model = d.pop("model", UNSET)

        version = d.pop("version", UNSET)

        status = d.pop("status", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        added_in_advanced = d.pop("addedInAdvanced", UNSET)

        _ports = d.pop("ports", UNSET)
        ports: list[Dot1XPortInfoOpenApiVO] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = Dot1XPortInfoOpenApiVO.from_dict(ports_item_data)

                ports.append(ports_item)

        support_vrf = d.pop("supportVrf", UNSET)

        account_vrf_id = d.pop("accountVrfId", UNSET)

        auth_vrf_id = d.pop("authVrfId", UNSET)

        support_single_mab_auth = d.pop("supportSingleMabAuth", UNSET)

        port_configured = d.pop("portConfigured", UNSET)

        dot_1x_switch_info_open_api_vo = cls(
            name=name,
            mac=mac,
            model=model,
            version=version,
            status=status,
            status_category=status_category,
            added_in_advanced=added_in_advanced,
            ports=ports,
            support_vrf=support_vrf,
            account_vrf_id=account_vrf_id,
            auth_vrf_id=auth_vrf_id,
            support_single_mab_auth=support_single_mab_auth,
            port_configured=port_configured,
        )

        dot_1x_switch_info_open_api_vo.additional_properties = d
        return dot_1x_switch_info_open_api_vo

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
