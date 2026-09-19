from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.instances_vo import InstancesVO


T = TypeVar("T", bound="SpanningTreeSettingVO")


@_attrs_define
class SpanningTreeSettingVO:
    """SpanningTree Setting

    Attributes:
        priority (int): Priority should be within the range of 0–240
        ext_path_cost (int): ExtPathCost should be within the range of 0–2000000
        int_path_cost (int): IntPathCost should be within the range of 0–2000000
        edge_port (bool): Indicates whether edge port is enabled
        p_2_p_link (int): P2pLink should be within the range of 0-2
        mcheck (bool | Unset): Indicates whether mcheck is enabled
        loop_protect (bool | Unset): Indicates whether loop protect is enabled
        root_protect (bool | Unset): Indicates whether root protect is enabled
        tc_guard (bool | Unset): Indicates whether tcGuard is enabled
        bpdu_protect (bool | Unset): Indicates whether bpdu protect is enabled
        bpdu_filter (bool | Unset): Indicates whether bpdu filter is enabled
        bpdu_forward (bool | Unset): Indicates whether bpdu forward is enabled
        instance_enable (bool | Unset): Indicates whether instance is enabled
        instances (list[InstancesVO] | Unset): Instances
    """

    priority: int
    ext_path_cost: int
    int_path_cost: int
    edge_port: bool
    p_2_p_link: int
    mcheck: bool | Unset = UNSET
    loop_protect: bool | Unset = UNSET
    root_protect: bool | Unset = UNSET
    tc_guard: bool | Unset = UNSET
    bpdu_protect: bool | Unset = UNSET
    bpdu_filter: bool | Unset = UNSET
    bpdu_forward: bool | Unset = UNSET
    instance_enable: bool | Unset = UNSET
    instances: list[InstancesVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        priority = self.priority

        ext_path_cost = self.ext_path_cost

        int_path_cost = self.int_path_cost

        edge_port = self.edge_port

        p_2_p_link = self.p_2_p_link

        mcheck = self.mcheck

        loop_protect = self.loop_protect

        root_protect = self.root_protect

        tc_guard = self.tc_guard

        bpdu_protect = self.bpdu_protect

        bpdu_filter = self.bpdu_filter

        bpdu_forward = self.bpdu_forward

        instance_enable = self.instance_enable

        instances: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.instances, Unset):
            instances = []
            for instances_item_data in self.instances:
                instances_item = instances_item_data.to_dict()
                instances.append(instances_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "priority": priority,
                "extPathCost": ext_path_cost,
                "intPathCost": int_path_cost,
                "edgePort": edge_port,
                "p2pLink": p_2_p_link,
            }
        )
        if mcheck is not UNSET:
            field_dict["mcheck"] = mcheck
        if loop_protect is not UNSET:
            field_dict["loopProtect"] = loop_protect
        if root_protect is not UNSET:
            field_dict["rootProtect"] = root_protect
        if tc_guard is not UNSET:
            field_dict["tcGuard"] = tc_guard
        if bpdu_protect is not UNSET:
            field_dict["bpduProtect"] = bpdu_protect
        if bpdu_filter is not UNSET:
            field_dict["bpduFilter"] = bpdu_filter
        if bpdu_forward is not UNSET:
            field_dict["bpduForward"] = bpdu_forward
        if instance_enable is not UNSET:
            field_dict["instanceEnable"] = instance_enable
        if instances is not UNSET:
            field_dict["instances"] = instances

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.instances_vo import InstancesVO

        d = dict(src_dict)
        priority = d.pop("priority")

        ext_path_cost = d.pop("extPathCost")

        int_path_cost = d.pop("intPathCost")

        edge_port = d.pop("edgePort")

        p_2_p_link = d.pop("p2pLink")

        mcheck = d.pop("mcheck", UNSET)

        loop_protect = d.pop("loopProtect", UNSET)

        root_protect = d.pop("rootProtect", UNSET)

        tc_guard = d.pop("tcGuard", UNSET)

        bpdu_protect = d.pop("bpduProtect", UNSET)

        bpdu_filter = d.pop("bpduFilter", UNSET)

        bpdu_forward = d.pop("bpduForward", UNSET)

        instance_enable = d.pop("instanceEnable", UNSET)

        _instances = d.pop("instances", UNSET)
        instances: list[InstancesVO] | Unset = UNSET
        if _instances is not UNSET:
            instances = []
            for instances_item_data in _instances:
                instances_item = InstancesVO.from_dict(instances_item_data)

                instances.append(instances_item)

        spanning_tree_setting_vo = cls(
            priority=priority,
            ext_path_cost=ext_path_cost,
            int_path_cost=int_path_cost,
            edge_port=edge_port,
            p_2_p_link=p_2_p_link,
            mcheck=mcheck,
            loop_protect=loop_protect,
            root_protect=root_protect,
            tc_guard=tc_guard,
            bpdu_protect=bpdu_protect,
            bpdu_filter=bpdu_filter,
            bpdu_forward=bpdu_forward,
            instance_enable=instance_enable,
            instances=instances,
        )

        spanning_tree_setting_vo.additional_properties = d
        return spanning_tree_setting_vo

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
