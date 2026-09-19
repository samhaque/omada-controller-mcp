from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_data_vo import OswDataVO
    from ..models.osw_dev_cap_vo import OswDevCapVO
    from ..models.osw_lag_status_vo import OswLagStatusVO
    from ..models.port_vo import PortVO


T = TypeVar("T", bound="OswStackDataVOOswDataVO")


@_attrs_define
class OswStackDataVOOswDataVO:
    """stackOswData

    Attributes:
        stack_id (str | Unset):
        stack_name (str | Unset):
        model (str | Unset): Model of device,for example:EAP225
        model_version (str | Unset): Model version of device,for example:3.0
        show_model (str | Unset): Model complex shown in the front end.Ap：model+(country)+modelVersion,EAP225(EU) v3.0
            Gateway/Switch：model+modelVersion,Osg v3.0
        master_mac (str | Unset):
        un_selectedable_ports (list[PortVO] | Unset): The unSelectedable ports of the device.
        stack_status (int | Unset):
        abnormal_reason (int | Unset):
        member (list[OswDataVO] | Unset):
        lags (list[OswLagStatusVO] | Unset):
        support_custom_dhcp_option (bool | Unset):
        support_dhcp_range (bool | Unset):
        support_vrf (bool | Unset):
        support_auto_add_vlan (bool | Unset):
        dev_cap (OswDevCapVO | Unset): Capability of device
        custom_standard_ports (list[str] | Unset): The standard ports that has some vlan not included in port vlan.
        custom_lag_ids (list[int] | Unset): The lag ids that has some vlan not included in port vlan.
        support_layout (bool | Unset): Whether the device supports reporting port layout information.
    """

    stack_id: str | Unset = UNSET
    stack_name: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    show_model: str | Unset = UNSET
    master_mac: str | Unset = UNSET
    un_selectedable_ports: list[PortVO] | Unset = UNSET
    stack_status: int | Unset = UNSET
    abnormal_reason: int | Unset = UNSET
    member: list[OswDataVO] | Unset = UNSET
    lags: list[OswLagStatusVO] | Unset = UNSET
    support_custom_dhcp_option: bool | Unset = UNSET
    support_dhcp_range: bool | Unset = UNSET
    support_vrf: bool | Unset = UNSET
    support_auto_add_vlan: bool | Unset = UNSET
    dev_cap: OswDevCapVO | Unset = UNSET
    custom_standard_ports: list[str] | Unset = UNSET
    custom_lag_ids: list[int] | Unset = UNSET
    support_layout: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stack_id = self.stack_id

        stack_name = self.stack_name

        model = self.model

        model_version = self.model_version

        show_model = self.show_model

        master_mac = self.master_mac

        un_selectedable_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.un_selectedable_ports, Unset):
            un_selectedable_ports = []
            for un_selectedable_ports_item_data in self.un_selectedable_ports:
                un_selectedable_ports_item = un_selectedable_ports_item_data.to_dict()
                un_selectedable_ports.append(un_selectedable_ports_item)

        stack_status = self.stack_status

        abnormal_reason = self.abnormal_reason

        member: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.member, Unset):
            member = []
            for member_item_data in self.member:
                member_item = member_item_data.to_dict()
                member.append(member_item)

        lags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lags, Unset):
            lags = []
            for lags_item_data in self.lags:
                lags_item = lags_item_data.to_dict()
                lags.append(lags_item)

        support_custom_dhcp_option = self.support_custom_dhcp_option

        support_dhcp_range = self.support_dhcp_range

        support_vrf = self.support_vrf

        support_auto_add_vlan = self.support_auto_add_vlan

        dev_cap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dev_cap, Unset):
            dev_cap = self.dev_cap.to_dict()

        custom_standard_ports: list[str] | Unset = UNSET
        if not isinstance(self.custom_standard_ports, Unset):
            custom_standard_ports = self.custom_standard_ports

        custom_lag_ids: list[int] | Unset = UNSET
        if not isinstance(self.custom_lag_ids, Unset):
            custom_lag_ids = self.custom_lag_ids

        support_layout = self.support_layout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if stack_name is not UNSET:
            field_dict["stackName"] = stack_name
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if master_mac is not UNSET:
            field_dict["masterMac"] = master_mac
        if un_selectedable_ports is not UNSET:
            field_dict["unSelectedablePorts"] = un_selectedable_ports
        if stack_status is not UNSET:
            field_dict["stackStatus"] = stack_status
        if abnormal_reason is not UNSET:
            field_dict["abnormalReason"] = abnormal_reason
        if member is not UNSET:
            field_dict["member"] = member
        if lags is not UNSET:
            field_dict["lags"] = lags
        if support_custom_dhcp_option is not UNSET:
            field_dict["supportCustomDhcpOption"] = support_custom_dhcp_option
        if support_dhcp_range is not UNSET:
            field_dict["supportDhcpRange"] = support_dhcp_range
        if support_vrf is not UNSET:
            field_dict["supportVrf"] = support_vrf
        if support_auto_add_vlan is not UNSET:
            field_dict["supportAutoAddVlan"] = support_auto_add_vlan
        if dev_cap is not UNSET:
            field_dict["devCap"] = dev_cap
        if custom_standard_ports is not UNSET:
            field_dict["customStandardPorts"] = custom_standard_ports
        if custom_lag_ids is not UNSET:
            field_dict["customLagIds"] = custom_lag_ids
        if support_layout is not UNSET:
            field_dict["supportLayout"] = support_layout

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_data_vo import OswDataVO
        from ..models.osw_dev_cap_vo import OswDevCapVO
        from ..models.osw_lag_status_vo import OswLagStatusVO
        from ..models.port_vo import PortVO

        d = dict(src_dict)
        stack_id = d.pop("stackId", UNSET)

        stack_name = d.pop("stackName", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        show_model = d.pop("showModel", UNSET)

        master_mac = d.pop("masterMac", UNSET)

        _un_selectedable_ports = d.pop("unSelectedablePorts", UNSET)
        un_selectedable_ports: list[PortVO] | Unset = UNSET
        if _un_selectedable_ports is not UNSET:
            un_selectedable_ports = []
            for un_selectedable_ports_item_data in _un_selectedable_ports:
                un_selectedable_ports_item = PortVO.from_dict(
                    un_selectedable_ports_item_data
                )

                un_selectedable_ports.append(un_selectedable_ports_item)

        stack_status = d.pop("stackStatus", UNSET)

        abnormal_reason = d.pop("abnormalReason", UNSET)

        _member = d.pop("member", UNSET)
        member: list[OswDataVO] | Unset = UNSET
        if _member is not UNSET:
            member = []
            for member_item_data in _member:
                member_item = OswDataVO.from_dict(member_item_data)

                member.append(member_item)

        _lags = d.pop("lags", UNSET)
        lags: list[OswLagStatusVO] | Unset = UNSET
        if _lags is not UNSET:
            lags = []
            for lags_item_data in _lags:
                lags_item = OswLagStatusVO.from_dict(lags_item_data)

                lags.append(lags_item)

        support_custom_dhcp_option = d.pop("supportCustomDhcpOption", UNSET)

        support_dhcp_range = d.pop("supportDhcpRange", UNSET)

        support_vrf = d.pop("supportVrf", UNSET)

        support_auto_add_vlan = d.pop("supportAutoAddVlan", UNSET)

        _dev_cap = d.pop("devCap", UNSET)
        dev_cap: OswDevCapVO | Unset
        if isinstance(_dev_cap, Unset):
            dev_cap = UNSET
        else:
            dev_cap = OswDevCapVO.from_dict(_dev_cap)

        custom_standard_ports = cast(list[str], d.pop("customStandardPorts", UNSET))

        custom_lag_ids = cast(list[int], d.pop("customLagIds", UNSET))

        support_layout = d.pop("supportLayout", UNSET)

        osw_stack_data_vo_osw_data_vo = cls(
            stack_id=stack_id,
            stack_name=stack_name,
            model=model,
            model_version=model_version,
            show_model=show_model,
            master_mac=master_mac,
            un_selectedable_ports=un_selectedable_ports,
            stack_status=stack_status,
            abnormal_reason=abnormal_reason,
            member=member,
            lags=lags,
            support_custom_dhcp_option=support_custom_dhcp_option,
            support_dhcp_range=support_dhcp_range,
            support_vrf=support_vrf,
            support_auto_add_vlan=support_auto_add_vlan,
            dev_cap=dev_cap,
            custom_standard_ports=custom_standard_ports,
            custom_lag_ids=custom_lag_ids,
            support_layout=support_layout,
        )

        osw_stack_data_vo_osw_data_vo.additional_properties = d
        return osw_stack_data_vo_osw_data_vo

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
