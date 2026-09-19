from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswQosConfigVO")


@_attrs_define
class OswQosConfigVO:
    """Switch qos config

    Attributes:
        dscp_dot_1_p_mapping_id (str): Dscp Dot1p Mapping ID
        dot_1_p_queue_mapping_id (str): Dot1p Queue Mapping ID
        queue_scheduler_id (str): Queue Scheduler ID
        dscp_dot_1_p_mapping_name (str | Unset): Dscp Dot1p Mapping Name
        dot_1_p_queue_mapping_name (str | Unset): Dot1p Queue Mapping Name
        queue_scheduler_name (str | Unset): Queue Scheduler Name
    """

    dscp_dot_1_p_mapping_id: str
    dot_1_p_queue_mapping_id: str
    queue_scheduler_id: str
    dscp_dot_1_p_mapping_name: str | Unset = UNSET
    dot_1_p_queue_mapping_name: str | Unset = UNSET
    queue_scheduler_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dscp_dot_1_p_mapping_id = self.dscp_dot_1_p_mapping_id

        dot_1_p_queue_mapping_id = self.dot_1_p_queue_mapping_id

        queue_scheduler_id = self.queue_scheduler_id

        dscp_dot_1_p_mapping_name = self.dscp_dot_1_p_mapping_name

        dot_1_p_queue_mapping_name = self.dot_1_p_queue_mapping_name

        queue_scheduler_name = self.queue_scheduler_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dscpDot1pMappingId": dscp_dot_1_p_mapping_id,
                "dot1pQueueMappingId": dot_1_p_queue_mapping_id,
                "queueSchedulerId": queue_scheduler_id,
            }
        )
        if dscp_dot_1_p_mapping_name is not UNSET:
            field_dict["dscpDot1pMappingName"] = dscp_dot_1_p_mapping_name
        if dot_1_p_queue_mapping_name is not UNSET:
            field_dict["dot1pQueueMappingName"] = dot_1_p_queue_mapping_name
        if queue_scheduler_name is not UNSET:
            field_dict["queueSchedulerName"] = queue_scheduler_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        dscp_dot_1_p_mapping_id = d.pop("dscpDot1pMappingId")

        dot_1_p_queue_mapping_id = d.pop("dot1pQueueMappingId")

        queue_scheduler_id = d.pop("queueSchedulerId")

        dscp_dot_1_p_mapping_name = d.pop("dscpDot1pMappingName", UNSET)

        dot_1_p_queue_mapping_name = d.pop("dot1pQueueMappingName", UNSET)

        queue_scheduler_name = d.pop("queueSchedulerName", UNSET)

        osw_qos_config_vo = cls(
            dscp_dot_1_p_mapping_id=dscp_dot_1_p_mapping_id,
            dot_1_p_queue_mapping_id=dot_1_p_queue_mapping_id,
            queue_scheduler_id=queue_scheduler_id,
            dscp_dot_1_p_mapping_name=dscp_dot_1_p_mapping_name,
            dot_1_p_queue_mapping_name=dot_1_p_queue_mapping_name,
            queue_scheduler_name=queue_scheduler_name,
        )

        osw_qos_config_vo.additional_properties = d
        return osw_qos_config_vo

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
