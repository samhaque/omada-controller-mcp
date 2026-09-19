from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.common_sub_health_info_detail_vo import CommonSubHealthInfoDetailVO
    from ..models.float_sub_health_info_detail_vo import FloatSubHealthInfoDetailVO
    from ..models.incident_sub_health_info_detail_vo import (
        IncidentSubHealthInfoDetailVO,
    )
    from ..models.link_error_health_info_detail_vo import LinkErrorHealthInfoDetailVO


T = TypeVar("T", bound="OswHealthDetailVO")


@_attrs_define
class OswHealthDetailVO:
    """
    Attributes:
        score (int | Unset): Device health score.
        cpu (CommonSubHealthInfoDetailVO | Unset): Link error score health info and score (wired clients only)
        memory (CommonSubHealthInfoDetailVO | Unset): Link error score health info and score (wired clients only)
        incident (IncidentSubHealthInfoDetailVO | Unset): Incident health info and score (wireless clients only)
        temperature (CommonSubHealthInfoDetailVO | Unset): Link error score health info and score (wired clients only)
        packet_loss (FloatSubHealthInfoDetailVO | Unset): Error frame health info and score
        error_frame (FloatSubHealthInfoDetailVO | Unset): Error frame health info and score
        link_error (LinkErrorHealthInfoDetailVO | Unset): Port link error info and score
    """

    score: int | Unset = UNSET
    cpu: CommonSubHealthInfoDetailVO | Unset = UNSET
    memory: CommonSubHealthInfoDetailVO | Unset = UNSET
    incident: IncidentSubHealthInfoDetailVO | Unset = UNSET
    temperature: CommonSubHealthInfoDetailVO | Unset = UNSET
    packet_loss: FloatSubHealthInfoDetailVO | Unset = UNSET
    error_frame: FloatSubHealthInfoDetailVO | Unset = UNSET
    link_error: LinkErrorHealthInfoDetailVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        score = self.score

        cpu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cpu, Unset):
            cpu = self.cpu.to_dict()

        memory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.memory, Unset):
            memory = self.memory.to_dict()

        incident: dict[str, Any] | Unset = UNSET
        if not isinstance(self.incident, Unset):
            incident = self.incident.to_dict()

        temperature: dict[str, Any] | Unset = UNSET
        if not isinstance(self.temperature, Unset):
            temperature = self.temperature.to_dict()

        packet_loss: dict[str, Any] | Unset = UNSET
        if not isinstance(self.packet_loss, Unset):
            packet_loss = self.packet_loss.to_dict()

        error_frame: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error_frame, Unset):
            error_frame = self.error_frame.to_dict()

        link_error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.link_error, Unset):
            link_error = self.link_error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if score is not UNSET:
            field_dict["score"] = score
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if memory is not UNSET:
            field_dict["memory"] = memory
        if incident is not UNSET:
            field_dict["incident"] = incident
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if packet_loss is not UNSET:
            field_dict["packetLoss"] = packet_loss
        if error_frame is not UNSET:
            field_dict["errorFrame"] = error_frame
        if link_error is not UNSET:
            field_dict["linkError"] = link_error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.common_sub_health_info_detail_vo import (
            CommonSubHealthInfoDetailVO,
        )
        from ..models.float_sub_health_info_detail_vo import (
            FloatSubHealthInfoDetailVO,
        )
        from ..models.incident_sub_health_info_detail_vo import (
            IncidentSubHealthInfoDetailVO,
        )
        from ..models.link_error_health_info_detail_vo import (
            LinkErrorHealthInfoDetailVO,
        )

        d = dict(src_dict)
        score = d.pop("score", UNSET)

        _cpu = d.pop("cpu", UNSET)
        cpu: CommonSubHealthInfoDetailVO | Unset
        if isinstance(_cpu, Unset):
            cpu = UNSET
        else:
            cpu = CommonSubHealthInfoDetailVO.from_dict(_cpu)

        _memory = d.pop("memory", UNSET)
        memory: CommonSubHealthInfoDetailVO | Unset
        if isinstance(_memory, Unset):
            memory = UNSET
        else:
            memory = CommonSubHealthInfoDetailVO.from_dict(_memory)

        _incident = d.pop("incident", UNSET)
        incident: IncidentSubHealthInfoDetailVO | Unset
        if isinstance(_incident, Unset):
            incident = UNSET
        else:
            incident = IncidentSubHealthInfoDetailVO.from_dict(_incident)

        _temperature = d.pop("temperature", UNSET)
        temperature: CommonSubHealthInfoDetailVO | Unset
        if isinstance(_temperature, Unset):
            temperature = UNSET
        else:
            temperature = CommonSubHealthInfoDetailVO.from_dict(_temperature)

        _packet_loss = d.pop("packetLoss", UNSET)
        packet_loss: FloatSubHealthInfoDetailVO | Unset
        if isinstance(_packet_loss, Unset):
            packet_loss = UNSET
        else:
            packet_loss = FloatSubHealthInfoDetailVO.from_dict(_packet_loss)

        _error_frame = d.pop("errorFrame", UNSET)
        error_frame: FloatSubHealthInfoDetailVO | Unset
        if isinstance(_error_frame, Unset):
            error_frame = UNSET
        else:
            error_frame = FloatSubHealthInfoDetailVO.from_dict(_error_frame)

        _link_error = d.pop("linkError", UNSET)
        link_error: LinkErrorHealthInfoDetailVO | Unset
        if isinstance(_link_error, Unset):
            link_error = UNSET
        else:
            link_error = LinkErrorHealthInfoDetailVO.from_dict(_link_error)

        osw_health_detail_vo = cls(
            score=score,
            cpu=cpu,
            memory=memory,
            incident=incident,
            temperature=temperature,
            packet_loss=packet_loss,
            error_frame=error_frame,
            link_error=link_error,
        )

        osw_health_detail_vo.additional_properties = d
        return osw_health_detail_vo

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
