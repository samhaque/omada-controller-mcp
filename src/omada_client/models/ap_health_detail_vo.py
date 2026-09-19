from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_interference_sub_health_detail_vo import (
        ChannelInterferenceSubHealthDetailVO,
    )
    from ..models.channel_sub_health_info_detail_vo import ChannelSubHealthInfoDetailVO
    from ..models.common_sub_health_info_detail_vo import CommonSubHealthInfoDetailVO
    from ..models.incident_sub_health_info_detail_vo import (
        IncidentSubHealthInfoDetailVO,
    )
    from ..models.transmission_sub_health_info_detail_vo import (
        TransmissionSubHealthInfoDetailVO,
    )


T = TypeVar("T", bound="ApHealthDetailVO")


@_attrs_define
class ApHealthDetailVO:
    """
    Attributes:
        score (int | Unset): Device health score.
        cpu (CommonSubHealthInfoDetailVO | Unset): Link error score health info and score (wired clients only)
        memory (CommonSubHealthInfoDetailVO | Unset): Link error score health info and score (wired clients only)
        incident (IncidentSubHealthInfoDetailVO | Unset): Incident health info and score (wireless clients only)
        channel_util (ChannelSubHealthInfoDetailVO | Unset): Rssi health info and score
        supported_channel_util (ChannelSubHealthInfoDetailVO | Unset): Rssi health info and score
        channel_interf (ChannelSubHealthInfoDetailVO | Unset): Rssi health info and score
        supported_channel_interf (ChannelInterferenceSubHealthDetailVO | Unset): Channel interference rate health info
            and score of supported channel
        transmission (TransmissionSubHealthInfoDetailVO | Unset): wireless transmission quality health info and score
    """

    score: int | Unset = UNSET
    cpu: CommonSubHealthInfoDetailVO | Unset = UNSET
    memory: CommonSubHealthInfoDetailVO | Unset = UNSET
    incident: IncidentSubHealthInfoDetailVO | Unset = UNSET
    channel_util: ChannelSubHealthInfoDetailVO | Unset = UNSET
    supported_channel_util: ChannelSubHealthInfoDetailVO | Unset = UNSET
    channel_interf: ChannelSubHealthInfoDetailVO | Unset = UNSET
    supported_channel_interf: ChannelInterferenceSubHealthDetailVO | Unset = UNSET
    transmission: TransmissionSubHealthInfoDetailVO | Unset = UNSET
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

        channel_util: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channel_util, Unset):
            channel_util = self.channel_util.to_dict()

        supported_channel_util: dict[str, Any] | Unset = UNSET
        if not isinstance(self.supported_channel_util, Unset):
            supported_channel_util = self.supported_channel_util.to_dict()

        channel_interf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channel_interf, Unset):
            channel_interf = self.channel_interf.to_dict()

        supported_channel_interf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.supported_channel_interf, Unset):
            supported_channel_interf = self.supported_channel_interf.to_dict()

        transmission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transmission, Unset):
            transmission = self.transmission.to_dict()

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
        if channel_util is not UNSET:
            field_dict["channelUtil"] = channel_util
        if supported_channel_util is not UNSET:
            field_dict["supportedChannelUtil"] = supported_channel_util
        if channel_interf is not UNSET:
            field_dict["channelInterf"] = channel_interf
        if supported_channel_interf is not UNSET:
            field_dict["supportedChannelInterf"] = supported_channel_interf
        if transmission is not UNSET:
            field_dict["transmission"] = transmission

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.channel_interference_sub_health_detail_vo import (
            ChannelInterferenceSubHealthDetailVO,
        )
        from ..models.channel_sub_health_info_detail_vo import (
            ChannelSubHealthInfoDetailVO,
        )
        from ..models.common_sub_health_info_detail_vo import (
            CommonSubHealthInfoDetailVO,
        )
        from ..models.incident_sub_health_info_detail_vo import (
            IncidentSubHealthInfoDetailVO,
        )
        from ..models.transmission_sub_health_info_detail_vo import (
            TransmissionSubHealthInfoDetailVO,
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

        _channel_interf = d.pop("channelInterf", UNSET)
        channel_interf: ChannelSubHealthInfoDetailVO | Unset
        if isinstance(_channel_interf, Unset):
            channel_interf = UNSET
        else:
            channel_interf = ChannelSubHealthInfoDetailVO.from_dict(_channel_interf)

        _supported_channel_interf = d.pop("supportedChannelInterf", UNSET)
        supported_channel_interf: ChannelInterferenceSubHealthDetailVO | Unset
        if isinstance(_supported_channel_interf, Unset):
            supported_channel_interf = UNSET
        else:
            supported_channel_interf = ChannelInterferenceSubHealthDetailVO.from_dict(
                _supported_channel_interf
            )

        _transmission = d.pop("transmission", UNSET)
        transmission: TransmissionSubHealthInfoDetailVO | Unset
        if isinstance(_transmission, Unset):
            transmission = UNSET
        else:
            transmission = TransmissionSubHealthInfoDetailVO.from_dict(_transmission)

        ap_health_detail_vo = cls(
            score=score,
            cpu=cpu,
            memory=memory,
            incident=incident,
            channel_util=channel_util,
            supported_channel_util=supported_channel_util,
            channel_interf=channel_interf,
            supported_channel_interf=supported_channel_interf,
            transmission=transmission,
        )

        ap_health_detail_vo.additional_properties = d
        return ap_health_detail_vo

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
