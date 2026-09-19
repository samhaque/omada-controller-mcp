from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.ont_eth_port_dto_priority_policy import OntEthPortDTOPriorityPolicy
from ..models.ont_eth_port_dto_qin_q import OntEthPortDTOQinQ
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ont_eth_port_igmp_forward_dto import OntEthPortIGMPForwardDTO
    from ..models.ont_eth_port_vlan_config_dto import OntEthPortVlanConfigDTO


T = TypeVar("T", bound="OntEthPortDTO")


@_attrs_define
class OntEthPortDTO:
    """
    Attributes:
        port_id (int): Port ID
        vlan_config (OntEthPortVlanConfigDTO | Unset): Configure the VLAN TAG processing mode of the ONT port
        priority_policy (OntEthPortDTOPriorityPolicy | Unset): Priority policy should be a value as
            follows:UNCONCERN,ASSIGNED,COPY_COS
        igmp_forward (OntEthPortIGMPForwardDTO | Unset): IgmpForward
        max_mac_count (int | Unset): MaxMacCount should be within the range of 0 to 255
        qin_q (OntEthPortDTOQinQ | Unset): QinQ mode,qinQ should be a value as follows:UNCONCERN;DISABLE;ENABLE
        tls_vlan (str | Unset): Tls vlan
    """

    port_id: int
    vlan_config: OntEthPortVlanConfigDTO | Unset = UNSET
    priority_policy: OntEthPortDTOPriorityPolicy | Unset = UNSET
    igmp_forward: OntEthPortIGMPForwardDTO | Unset = UNSET
    max_mac_count: int | Unset = UNSET
    qin_q: OntEthPortDTOQinQ | Unset = UNSET
    tls_vlan: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_id = self.port_id

        vlan_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vlan_config, Unset):
            vlan_config = self.vlan_config.to_dict()

        priority_policy: str | Unset = UNSET
        if not isinstance(self.priority_policy, Unset):
            priority_policy = self.priority_policy.value

        igmp_forward: dict[str, Any] | Unset = UNSET
        if not isinstance(self.igmp_forward, Unset):
            igmp_forward = self.igmp_forward.to_dict()

        max_mac_count = self.max_mac_count

        qin_q: str | Unset = UNSET
        if not isinstance(self.qin_q, Unset):
            qin_q = self.qin_q.value

        tls_vlan = self.tls_vlan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portId": port_id,
            }
        )
        if vlan_config is not UNSET:
            field_dict["vlanConfig"] = vlan_config
        if priority_policy is not UNSET:
            field_dict["priorityPolicy"] = priority_policy
        if igmp_forward is not UNSET:
            field_dict["igmpForward"] = igmp_forward
        if max_mac_count is not UNSET:
            field_dict["maxMacCount"] = max_mac_count
        if qin_q is not UNSET:
            field_dict["qinQ"] = qin_q
        if tls_vlan is not UNSET:
            field_dict["tlsVlan"] = tls_vlan

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ont_eth_port_igmp_forward_dto import (
            OntEthPortIGMPForwardDTO,
        )
        from ..models.ont_eth_port_vlan_config_dto import (
            OntEthPortVlanConfigDTO,
        )

        d = dict(src_dict)
        port_id = d.pop("portId")

        _vlan_config = d.pop("vlanConfig", UNSET)
        vlan_config: OntEthPortVlanConfigDTO | Unset
        if isinstance(_vlan_config, Unset):
            vlan_config = UNSET
        else:
            vlan_config = OntEthPortVlanConfigDTO.from_dict(_vlan_config)

        _priority_policy = d.pop("priorityPolicy", UNSET)
        priority_policy: OntEthPortDTOPriorityPolicy | Unset
        if isinstance(_priority_policy, Unset):
            priority_policy = UNSET
        else:
            priority_policy = OntEthPortDTOPriorityPolicy(_priority_policy)

        _igmp_forward = d.pop("igmpForward", UNSET)
        igmp_forward: OntEthPortIGMPForwardDTO | Unset
        if isinstance(_igmp_forward, Unset):
            igmp_forward = UNSET
        else:
            igmp_forward = OntEthPortIGMPForwardDTO.from_dict(_igmp_forward)

        max_mac_count = d.pop("maxMacCount", UNSET)

        _qin_q = d.pop("qinQ", UNSET)
        qin_q: OntEthPortDTOQinQ | Unset
        if isinstance(_qin_q, Unset):
            qin_q = UNSET
        else:
            qin_q = OntEthPortDTOQinQ(_qin_q)

        tls_vlan = d.pop("tlsVlan", UNSET)

        ont_eth_port_dto = cls(
            port_id=port_id,
            vlan_config=vlan_config,
            priority_policy=priority_policy,
            igmp_forward=igmp_forward,
            max_mac_count=max_mac_count,
            qin_q=qin_q,
            tls_vlan=tls_vlan,
        )

        ont_eth_port_dto.additional_properties = d
        return ont_eth_port_dto

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
