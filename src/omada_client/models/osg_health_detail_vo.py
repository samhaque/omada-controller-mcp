from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_sub_health_info_detail_vo import ChannelSubHealthInfoDetailVO
    from ..models.common_sub_health_info_detail_vo import CommonSubHealthInfoDetailVO
    from ..models.incident_sub_health_info_detail_vo import (
        IncidentSubHealthInfoDetailVO,
    )
    from ..models.link_error_health_info_detail_vo import LinkErrorHealthInfoDetailVO
    from ..models.transmission_sub_health_info_detail_vo import (
        TransmissionSubHealthInfoDetailVO,
    )
    from ..models.wan_sub_health_info_detail_vo import WanSubHealthInfoDetailVO


T = TypeVar("T", bound="OsgHealthDetailVO")


@_attrs_define
class OsgHealthDetailVO:
    """
    Attributes:
        score (int | Unset): Device health score.
        cpu (CommonSubHealthInfoDetailVO | Unset): Link error score health info and score (wired clients only)
        memory (CommonSubHealthInfoDetailVO | Unset): Link error score health info and score (wired clients only)
        incident (IncidentSubHealthInfoDetailVO | Unset): Incident health info and score (wireless clients only)
        temperature (CommonSubHealthInfoDetailVO | Unset): Link error score health info and score (wired clients only)
        wan_latency (CommonSubHealthInfoDetailVO | Unset): Link error score health info and score (wired clients only)
        channel_util (ChannelSubHealthInfoDetailVO | Unset): Rssi health info and score
        supported_channel_util (ChannelSubHealthInfoDetailVO | Unset): Rssi health info and score
        transmission (TransmissionSubHealthInfoDetailVO | Unset): wireless transmission quality health info and score
        wan_status (WanSubHealthInfoDetailVO | Unset): WAN health info and score
        link_error (LinkErrorHealthInfoDetailVO | Unset): Port link error info and score
    """

    score: int | Unset = UNSET
    cpu: CommonSubHealthInfoDetailVO | Unset = UNSET
    memory: CommonSubHealthInfoDetailVO | Unset = UNSET
    incident: IncidentSubHealthInfoDetailVO | Unset = UNSET
    temperature: CommonSubHealthInfoDetailVO | Unset = UNSET
    wan_latency: CommonSubHealthInfoDetailVO | Unset = UNSET
    channel_util: ChannelSubHealthInfoDetailVO | Unset = UNSET
    supported_channel_util: ChannelSubHealthInfoDetailVO | Unset = UNSET
    transmission: TransmissionSubHealthInfoDetailVO | Unset = UNSET
    wan_status: WanSubHealthInfoDetailVO | Unset = UNSET
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

        wan_latency: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wan_latency, Unset):
            wan_latency = self.wan_latency.to_dict()

        channel_util: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channel_util, Unset):
            channel_util = self.channel_util.to_dict()

        supported_channel_util: dict[str, Any] | Unset = UNSET
        if not isinstance(self.supported_channel_util, Unset):
            supported_channel_util = self.supported_channel_util.to_dict()

        transmission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transmission, Unset):
            transmission = self.transmission.to_dict()

        wan_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wan_status, Unset):
            wan_status = self.wan_status.to_dict()

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
        if wan_latency is not UNSET:
            field_dict["wanLatency"] = wan_latency
        if channel_util is not UNSET:
            field_dict["channelUtil"] = channel_util
        if supported_channel_util is not UNSET:
            field_dict["supportedChannelUtil"] = supported_channel_util
        if transmission is not UNSET:
            field_dict["transmission"] = transmission
        if wan_status is not UNSET:
            field_dict["wanStatus"] = wan_status
        if link_error is not UNSET:
            field_dict["linkError"] = link_error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.channel_sub_health_info_detail_vo import (
            ChannelSubHealthInfoDetailVO,
        )
        from ..models.common_sub_health_info_detail_vo import (
            CommonSubHealthInfoDetailVO,
        )
        from ..models.incident_sub_health_info_detail_vo import (
            IncidentSubHealthInfoDetailVO,
        )
        from ..models.link_error_health_info_detail_vo import (
            LinkErrorHealthInfoDetailVO,
        )
        from ..models.transmission_sub_health_info_detail_vo import (
            TransmissionSubHealthInfoDetailVO,
        )
        from ..models.wan_sub_health_info_detail_vo import (
            WanSubHealthInfoDetailVO,
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

        _wan_latency = d.pop("wanLatency", UNSET)
        wan_latency: CommonSubHealthInfoDetailVO | Unset
        if isinstance(_wan_latency, Unset):
            wan_latency = UNSET
        else:
            wan_latency = CommonSubHealthInfoDetailVO.from_dict(_wan_latency)

        _channel_util = d.pop("channelUtil", UNSET)
        channel_util: ChannelSubHealthInfoDetailVO | Unset
        if isinstance(_channel_util, Unset):
            channel_util = UNSET
        else:
            channel_util = ChannelSubHealthInfoDetailVO.from_dict(_channel_util)

        _supported_channel_util = d.pop("supportedChannelUtil", UNSET)
        supported_channel_util: ChannelSubHealthInfoDetailVO | Unset
        if isinstance(_supported_channel_util, Unset):
            supported_channel_util = UNSET
        else:
            supported_channel_util = ChannelSubHealthInfoDetailVO.from_dict(
                _supported_channel_util
            )

        _transmission = d.pop("transmission", UNSET)
        transmission: TransmissionSubHealthInfoDetailVO | Unset
        if isinstance(_transmission, Unset):
            transmission = UNSET
        else:
            transmission = TransmissionSubHealthInfoDetailVO.from_dict(_transmission)

        _wan_status = d.pop("wanStatus", UNSET)
        wan_status: WanSubHealthInfoDetailVO | Unset
        if isinstance(_wan_status, Unset):
            wan_status = UNSET
        else:
            wan_status = WanSubHealthInfoDetailVO.from_dict(_wan_status)

        _link_error = d.pop("linkError", UNSET)
        link_error: LinkErrorHealthInfoDetailVO | Unset
        if isinstance(_link_error, Unset):
            link_error = UNSET
        else:
            link_error = LinkErrorHealthInfoDetailVO.from_dict(_link_error)

        osg_health_detail_vo = cls(
            score=score,
            cpu=cpu,
            memory=memory,
            incident=incident,
            temperature=temperature,
            wan_latency=wan_latency,
            channel_util=channel_util,
            supported_channel_util=supported_channel_util,
            transmission=transmission,
            wan_status=wan_status,
            link_error=link_error,
        )

        osg_health_detail_vo.additional_properties = d
        return osg_health_detail_vo

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
