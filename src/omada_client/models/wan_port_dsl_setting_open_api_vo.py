from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WanPortDslSettingOpenApiVO")


@_attrs_define
class WanPortDslSettingOpenApiVO:
    """DSL settings. Only for DSL WAN.

    Attributes:
        port_uuid (str): Wan port UUID.
        location (str): Your country/region.
        isp (int): Your ISP (Internet Service Provider) from the drop-down list,Select Other to customize the settings.
        modulation_type (int): The modulation type used for your DSL connection. 0: VDSL, 1: ADSL.
        port_name (str | Unset): Wan port name.
        port_desc (str | Unset): Wan port description.
        vpi (int | Unset): The VPI(0~255) assigned by your ISP to specify the virtual path between endpoints in an ATM
            network.
        vci (int | Unset): The VCI(1~65535) assigned by your ISP to specify the virtual channel endpoints in an ATM
            network.
        encap_mode (int | Unset): Encap mode assigned by your ISP. 0: LLC, 1: VC-MUX, 2: VC/MUX, 3: 1483 Bridged IP LLC,
            4: 1483 Routed IP LLC
        mer_enable (bool | Unset): If your ISP requires MER for network connection(e.g., Sky VDSL).MER switch
            configuration, only configurable when in VDSL mode and DHCP dial-up mode.
        mer_username (str | Unset): MER username configuration, only configurable when in VDSL mode and DHCP dial-up
            mode.
        mer_password (str | Unset): MER password configuration, only configurable when in VDSL mode and DHCP dial-up
            mode.
    """

    port_uuid: str
    location: str
    isp: int
    modulation_type: int
    port_name: str | Unset = UNSET
    port_desc: str | Unset = UNSET
    vpi: int | Unset = UNSET
    vci: int | Unset = UNSET
    encap_mode: int | Unset = UNSET
    mer_enable: bool | Unset = UNSET
    mer_username: str | Unset = UNSET
    mer_password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_uuid = self.port_uuid

        location = self.location

        isp = self.isp

        modulation_type = self.modulation_type

        port_name = self.port_name

        port_desc = self.port_desc

        vpi = self.vpi

        vci = self.vci

        encap_mode = self.encap_mode

        mer_enable = self.mer_enable

        mer_username = self.mer_username

        mer_password = self.mer_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portUuid": port_uuid,
                "location": location,
                "isp": isp,
                "modulationType": modulation_type,
            }
        )
        if port_name is not UNSET:
            field_dict["portName"] = port_name
        if port_desc is not UNSET:
            field_dict["portDesc"] = port_desc
        if vpi is not UNSET:
            field_dict["vpi"] = vpi
        if vci is not UNSET:
            field_dict["vci"] = vci
        if encap_mode is not UNSET:
            field_dict["encapMode"] = encap_mode
        if mer_enable is not UNSET:
            field_dict["merEnable"] = mer_enable
        if mer_username is not UNSET:
            field_dict["merUsername"] = mer_username
        if mer_password is not UNSET:
            field_dict["merPassword"] = mer_password

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_uuid = d.pop("portUuid")

        location = d.pop("location")

        isp = d.pop("isp")

        modulation_type = d.pop("modulationType")

        port_name = d.pop("portName", UNSET)

        port_desc = d.pop("portDesc", UNSET)

        vpi = d.pop("vpi", UNSET)

        vci = d.pop("vci", UNSET)

        encap_mode = d.pop("encapMode", UNSET)

        mer_enable = d.pop("merEnable", UNSET)

        mer_username = d.pop("merUsername", UNSET)

        mer_password = d.pop("merPassword", UNSET)

        wan_port_dsl_setting_open_api_vo = cls(
            port_uuid=port_uuid,
            location=location,
            isp=isp,
            modulation_type=modulation_type,
            port_name=port_name,
            port_desc=port_desc,
            vpi=vpi,
            vci=vci,
            encap_mode=encap_mode,
            mer_enable=mer_enable,
            mer_username=mer_username,
            mer_password=mer_password,
        )

        wan_port_dsl_setting_open_api_vo.additional_properties = d
        return wan_port_dsl_setting_open_api_vo

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
