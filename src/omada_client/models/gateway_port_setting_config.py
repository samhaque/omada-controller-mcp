from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dsl_settings import DslSettings


T = TypeVar("T", bound="GatewayPortSettingConfig")


@_attrs_define
class GatewayPortSettingConfig:
    """
    Attributes:
        link_speed (int | Unset): Port link speed should be a value as follows: 0: Auto; 1: 10M; 2: 100M; 3: 1000M; 4:
            2500M; 5: 10G; 6: 5G
        duplex (int | Unset): Port duplex mode should be a value as follows: 0: Auto; 1: Half; 2: Full
        mirror_enable (bool | Unset): Port enabled mirror or not
        mirrored_ports (list[int] | Unset): Mirrored Ports Set
        mirror_mode (int | Unset): Port mirror mode should be a value as follow: 0: ingress; 1: egress; 2: ingress and
            egress.
        pvid (int | Unset): Pvid(only for lan port.)
        flow_control (bool | Unset): Enable flow control or not.(When the port supports flow control.)
        status (int | Unset): Enable port or not, status should be a value as follows: 0: disable; 1: enable.(When the
            port supports status.)
        poe_mode (int | Unset): Enter a value as follows: 0: off; 1: 802.3at/af.
        dsl_settings (DslSettings | Unset): DSL port configurations.
        tag_set (list[str] | Unset): Tag ID Set
    """

    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    mirror_enable: bool | Unset = UNSET
    mirrored_ports: list[int] | Unset = UNSET
    mirror_mode: int | Unset = UNSET
    pvid: int | Unset = UNSET
    flow_control: bool | Unset = UNSET
    status: int | Unset = UNSET
    poe_mode: int | Unset = UNSET
    dsl_settings: DslSettings | Unset = UNSET
    tag_set: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        link_speed = self.link_speed

        duplex = self.duplex

        mirror_enable = self.mirror_enable

        mirrored_ports: list[int] | Unset = UNSET
        if not isinstance(self.mirrored_ports, Unset):
            mirrored_ports = self.mirrored_ports

        mirror_mode = self.mirror_mode

        pvid = self.pvid

        flow_control = self.flow_control

        status = self.status

        poe_mode = self.poe_mode

        dsl_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dsl_settings, Unset):
            dsl_settings = self.dsl_settings.to_dict()

        tag_set: list[str] | Unset = UNSET
        if not isinstance(self.tag_set, Unset):
            tag_set = self.tag_set

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if mirror_enable is not UNSET:
            field_dict["mirrorEnable"] = mirror_enable
        if mirrored_ports is not UNSET:
            field_dict["mirroredPorts"] = mirrored_ports
        if mirror_mode is not UNSET:
            field_dict["mirrorMode"] = mirror_mode
        if pvid is not UNSET:
            field_dict["pvid"] = pvid
        if flow_control is not UNSET:
            field_dict["flowControl"] = flow_control
        if status is not UNSET:
            field_dict["status"] = status
        if poe_mode is not UNSET:
            field_dict["poeMode"] = poe_mode
        if dsl_settings is not UNSET:
            field_dict["dslSettings"] = dsl_settings
        if tag_set is not UNSET:
            field_dict["tagSet"] = tag_set

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dsl_settings import DslSettings

        d = dict(src_dict)
        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        mirror_enable = d.pop("mirrorEnable", UNSET)

        mirrored_ports = cast(list[int], d.pop("mirroredPorts", UNSET))

        mirror_mode = d.pop("mirrorMode", UNSET)

        pvid = d.pop("pvid", UNSET)

        flow_control = d.pop("flowControl", UNSET)

        status = d.pop("status", UNSET)

        poe_mode = d.pop("poeMode", UNSET)

        _dsl_settings = d.pop("dslSettings", UNSET)
        dsl_settings: DslSettings | Unset
        if isinstance(_dsl_settings, Unset):
            dsl_settings = UNSET
        else:
            dsl_settings = DslSettings.from_dict(_dsl_settings)

        tag_set = cast(list[str], d.pop("tagSet", UNSET))

        gateway_port_setting_config = cls(
            link_speed=link_speed,
            duplex=duplex,
            mirror_enable=mirror_enable,
            mirrored_ports=mirrored_ports,
            mirror_mode=mirror_mode,
            pvid=pvid,
            flow_control=flow_control,
            status=status,
            poe_mode=poe_mode,
            dsl_settings=dsl_settings,
            tag_set=tag_set,
        )

        gateway_port_setting_config.additional_properties = d
        return gateway_port_setting_config

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
