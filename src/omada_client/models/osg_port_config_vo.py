from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dsl_settings_vo import DslSettingsVO
    from ..models.osg_link_vo import OsgLinkVO
    from ..models.osg_port_band_ctrl_vo import OsgPortBandCtrlVO
    from ..models.osg_port_stat_vo import OsgPortStatVO
    from ..models.osg_port_storm_ctrl_vo import OsgPortStormCtrlVO
    from ..models.osg_pv_id_name_vo import OsgPvIdNameVO


T = TypeVar("T", bound="OsgPortConfigVO")


@_attrs_define
class OsgPortConfigVO:
    """
    Attributes:
        port (int):
        port_list (list[int] | Unset):
        link_speed (int | Unset):
        duplex (int | Unset):
        port_cap (list[OsgLinkVO] | Unset):
        support_mirror (bool | Unset):
        mirror_enable (bool | Unset):
        mirrored_ports (list[int] | Unset):
        mirror_mode (int | Unset):
        pvid (int | Unset):
        available_pvids (list[int] | Unset):
        available_pvid_names (list[OsgPvIdNameVO] | Unset):
        port_stat (OsgPortStatVO | Unset):
        flow_control (bool | Unset):
        support_flow_control (bool | Unset):
        status (int | Unset):
        support_port_control (bool | Unset):
        support_loopback_control (bool | Unset):
        loopback_control (int | Unset):
        support_port_isolation (bool | Unset):
        port_isolation_enable (bool | Unset):
        support_band_width_ctrl (bool | Unset):
        band_width_ctrl_type (int | Unset):
        band_ctrl (OsgPortBandCtrlVO | Unset):
        storm_ctrl (OsgPortStormCtrlVO | Unset):
        resource (int | Unset):
        dsl_settings (DslSettingsVO | Unset):
        port_support_poe (bool | Unset):
        poe_mode (int | Unset):
        tag_set (list[str] | Unset):
    """

    port: int
    port_list: list[int] | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    port_cap: list[OsgLinkVO] | Unset = UNSET
    support_mirror: bool | Unset = UNSET
    mirror_enable: bool | Unset = UNSET
    mirrored_ports: list[int] | Unset = UNSET
    mirror_mode: int | Unset = UNSET
    pvid: int | Unset = UNSET
    available_pvids: list[int] | Unset = UNSET
    available_pvid_names: list[OsgPvIdNameVO] | Unset = UNSET
    port_stat: OsgPortStatVO | Unset = UNSET
    flow_control: bool | Unset = UNSET
    support_flow_control: bool | Unset = UNSET
    status: int | Unset = UNSET
    support_port_control: bool | Unset = UNSET
    support_loopback_control: bool | Unset = UNSET
    loopback_control: int | Unset = UNSET
    support_port_isolation: bool | Unset = UNSET
    port_isolation_enable: bool | Unset = UNSET
    support_band_width_ctrl: bool | Unset = UNSET
    band_width_ctrl_type: int | Unset = UNSET
    band_ctrl: OsgPortBandCtrlVO | Unset = UNSET
    storm_ctrl: OsgPortStormCtrlVO | Unset = UNSET
    resource: int | Unset = UNSET
    dsl_settings: DslSettingsVO | Unset = UNSET
    port_support_poe: bool | Unset = UNSET
    poe_mode: int | Unset = UNSET
    tag_set: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        port_list: list[int] | Unset = UNSET
        if not isinstance(self.port_list, Unset):
            port_list = self.port_list

        link_speed = self.link_speed

        duplex = self.duplex

        port_cap: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_cap, Unset):
            port_cap = []
            for port_cap_item_data in self.port_cap:
                port_cap_item = port_cap_item_data.to_dict()
                port_cap.append(port_cap_item)

        support_mirror = self.support_mirror

        mirror_enable = self.mirror_enable

        mirrored_ports: list[int] | Unset = UNSET
        if not isinstance(self.mirrored_ports, Unset):
            mirrored_ports = self.mirrored_ports

        mirror_mode = self.mirror_mode

        pvid = self.pvid

        available_pvids: list[int] | Unset = UNSET
        if not isinstance(self.available_pvids, Unset):
            available_pvids = self.available_pvids

        available_pvid_names: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.available_pvid_names, Unset):
            available_pvid_names = []
            for available_pvid_names_item_data in self.available_pvid_names:
                available_pvid_names_item = available_pvid_names_item_data.to_dict()
                available_pvid_names.append(available_pvid_names_item)

        port_stat: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port_stat, Unset):
            port_stat = self.port_stat.to_dict()

        flow_control = self.flow_control

        support_flow_control = self.support_flow_control

        status = self.status

        support_port_control = self.support_port_control

        support_loopback_control = self.support_loopback_control

        loopback_control = self.loopback_control

        support_port_isolation = self.support_port_isolation

        port_isolation_enable = self.port_isolation_enable

        support_band_width_ctrl = self.support_band_width_ctrl

        band_width_ctrl_type = self.band_width_ctrl_type

        band_ctrl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.band_ctrl, Unset):
            band_ctrl = self.band_ctrl.to_dict()

        storm_ctrl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storm_ctrl, Unset):
            storm_ctrl = self.storm_ctrl.to_dict()

        resource = self.resource

        dsl_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dsl_settings, Unset):
            dsl_settings = self.dsl_settings.to_dict()

        port_support_poe = self.port_support_poe

        poe_mode = self.poe_mode

        tag_set: list[str] | Unset = UNSET
        if not isinstance(self.tag_set, Unset):
            tag_set = self.tag_set

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "port": port,
            }
        )
        if port_list is not UNSET:
            field_dict["portList"] = port_list
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if port_cap is not UNSET:
            field_dict["portCap"] = port_cap
        if support_mirror is not UNSET:
            field_dict["supportMirror"] = support_mirror
        if mirror_enable is not UNSET:
            field_dict["mirrorEnable"] = mirror_enable
        if mirrored_ports is not UNSET:
            field_dict["mirroredPorts"] = mirrored_ports
        if mirror_mode is not UNSET:
            field_dict["mirrorMode"] = mirror_mode
        if pvid is not UNSET:
            field_dict["pvid"] = pvid
        if available_pvids is not UNSET:
            field_dict["availablePvids"] = available_pvids
        if available_pvid_names is not UNSET:
            field_dict["availablePvidNames"] = available_pvid_names
        if port_stat is not UNSET:
            field_dict["portStat"] = port_stat
        if flow_control is not UNSET:
            field_dict["flowControl"] = flow_control
        if support_flow_control is not UNSET:
            field_dict["supportFlowControl"] = support_flow_control
        if status is not UNSET:
            field_dict["status"] = status
        if support_port_control is not UNSET:
            field_dict["supportPortControl"] = support_port_control
        if support_loopback_control is not UNSET:
            field_dict["supportLoopbackControl"] = support_loopback_control
        if loopback_control is not UNSET:
            field_dict["loopbackControl"] = loopback_control
        if support_port_isolation is not UNSET:
            field_dict["supportPortIsolation"] = support_port_isolation
        if port_isolation_enable is not UNSET:
            field_dict["portIsolationEnable"] = port_isolation_enable
        if support_band_width_ctrl is not UNSET:
            field_dict["supportBandWidthCtrl"] = support_band_width_ctrl
        if band_width_ctrl_type is not UNSET:
            field_dict["bandWidthCtrlType"] = band_width_ctrl_type
        if band_ctrl is not UNSET:
            field_dict["bandCtrl"] = band_ctrl
        if storm_ctrl is not UNSET:
            field_dict["stormCtrl"] = storm_ctrl
        if resource is not UNSET:
            field_dict["resource"] = resource
        if dsl_settings is not UNSET:
            field_dict["dslSettings"] = dsl_settings
        if port_support_poe is not UNSET:
            field_dict["portSupportPoe"] = port_support_poe
        if poe_mode is not UNSET:
            field_dict["poeMode"] = poe_mode
        if tag_set is not UNSET:
            field_dict["tagSet"] = tag_set

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dsl_settings_vo import DslSettingsVO
        from ..models.osg_link_vo import OsgLinkVO
        from ..models.osg_port_band_ctrl_vo import OsgPortBandCtrlVO
        from ..models.osg_port_stat_vo import OsgPortStatVO
        from ..models.osg_port_storm_ctrl_vo import OsgPortStormCtrlVO
        from ..models.osg_pv_id_name_vo import OsgPvIdNameVO

        d = dict(src_dict)
        port = d.pop("port")

        port_list = cast(list[int], d.pop("portList", UNSET))

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        _port_cap = d.pop("portCap", UNSET)
        port_cap: list[OsgLinkVO] | Unset = UNSET
        if _port_cap is not UNSET:
            port_cap = []
            for port_cap_item_data in _port_cap:
                port_cap_item = OsgLinkVO.from_dict(port_cap_item_data)

                port_cap.append(port_cap_item)

        support_mirror = d.pop("supportMirror", UNSET)

        mirror_enable = d.pop("mirrorEnable", UNSET)

        mirrored_ports = cast(list[int], d.pop("mirroredPorts", UNSET))

        mirror_mode = d.pop("mirrorMode", UNSET)

        pvid = d.pop("pvid", UNSET)

        available_pvids = cast(list[int], d.pop("availablePvids", UNSET))

        _available_pvid_names = d.pop("availablePvidNames", UNSET)
        available_pvid_names: list[OsgPvIdNameVO] | Unset = UNSET
        if _available_pvid_names is not UNSET:
            available_pvid_names = []
            for available_pvid_names_item_data in _available_pvid_names:
                available_pvid_names_item = OsgPvIdNameVO.from_dict(
                    available_pvid_names_item_data
                )

                available_pvid_names.append(available_pvid_names_item)

        _port_stat = d.pop("portStat", UNSET)
        port_stat: OsgPortStatVO | Unset
        if isinstance(_port_stat, Unset):
            port_stat = UNSET
        else:
            port_stat = OsgPortStatVO.from_dict(_port_stat)

        flow_control = d.pop("flowControl", UNSET)

        support_flow_control = d.pop("supportFlowControl", UNSET)

        status = d.pop("status", UNSET)

        support_port_control = d.pop("supportPortControl", UNSET)

        support_loopback_control = d.pop("supportLoopbackControl", UNSET)

        loopback_control = d.pop("loopbackControl", UNSET)

        support_port_isolation = d.pop("supportPortIsolation", UNSET)

        port_isolation_enable = d.pop("portIsolationEnable", UNSET)

        support_band_width_ctrl = d.pop("supportBandWidthCtrl", UNSET)

        band_width_ctrl_type = d.pop("bandWidthCtrlType", UNSET)

        _band_ctrl = d.pop("bandCtrl", UNSET)
        band_ctrl: OsgPortBandCtrlVO | Unset
        if isinstance(_band_ctrl, Unset):
            band_ctrl = UNSET
        else:
            band_ctrl = OsgPortBandCtrlVO.from_dict(_band_ctrl)

        _storm_ctrl = d.pop("stormCtrl", UNSET)
        storm_ctrl: OsgPortStormCtrlVO | Unset
        if isinstance(_storm_ctrl, Unset):
            storm_ctrl = UNSET
        else:
            storm_ctrl = OsgPortStormCtrlVO.from_dict(_storm_ctrl)

        resource = d.pop("resource", UNSET)

        _dsl_settings = d.pop("dslSettings", UNSET)
        dsl_settings: DslSettingsVO | Unset
        if isinstance(_dsl_settings, Unset):
            dsl_settings = UNSET
        else:
            dsl_settings = DslSettingsVO.from_dict(_dsl_settings)

        port_support_poe = d.pop("portSupportPoe", UNSET)

        poe_mode = d.pop("poeMode", UNSET)

        tag_set = cast(list[str], d.pop("tagSet", UNSET))

        osg_port_config_vo = cls(
            port=port,
            port_list=port_list,
            link_speed=link_speed,
            duplex=duplex,
            port_cap=port_cap,
            support_mirror=support_mirror,
            mirror_enable=mirror_enable,
            mirrored_ports=mirrored_ports,
            mirror_mode=mirror_mode,
            pvid=pvid,
            available_pvids=available_pvids,
            available_pvid_names=available_pvid_names,
            port_stat=port_stat,
            flow_control=flow_control,
            support_flow_control=support_flow_control,
            status=status,
            support_port_control=support_port_control,
            support_loopback_control=support_loopback_control,
            loopback_control=loopback_control,
            support_port_isolation=support_port_isolation,
            port_isolation_enable=port_isolation_enable,
            support_band_width_ctrl=support_band_width_ctrl,
            band_width_ctrl_type=band_width_ctrl_type,
            band_ctrl=band_ctrl,
            storm_ctrl=storm_ctrl,
            resource=resource,
            dsl_settings=dsl_settings,
            port_support_poe=port_support_poe,
            poe_mode=poe_mode,
            tag_set=tag_set,
        )

        osg_port_config_vo.additional_properties = d
        return osg_port_config_vo

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
