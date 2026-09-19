from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.common_sub_health_info_detail_vo_integer import (
        CommonSubHealthInfoDetailVOInteger,
    )
    from ..models.common_sub_health_info_detail_vo_long import (
        CommonSubHealthInfoDetailVOLong,
    )
    from ..models.incident_sub_health_info_detail_vo import (
        IncidentSubHealthInfoDetailVO,
    )


T = TypeVar("T", bound="ClientHealthDetailVO")


@_attrs_define
class ClientHealthDetailVO:
    """
    Attributes:
        score (int | Unset):
        association_time (CommonSubHealthInfoDetailVOInteger | Unset): Link error score info (wired clients only)
        rssi (CommonSubHealthInfoDetailVOInteger | Unset): Link error score info (wired clients only)
        rate (CommonSubHealthInfoDetailVOLong | Unset): Negotiation rate health info and score
        snr (CommonSubHealthInfoDetailVOInteger | Unset): Link error score info (wired clients only)
        incident (IncidentSubHealthInfoDetailVO | Unset): Incident health info and score (wireless clients only)
        connect_score (CommonSubHealthInfoDetailVOInteger | Unset): Link error score info (wired clients only)
        link_error_score (CommonSubHealthInfoDetailVOInteger | Unset): Link error score info (wired clients only)
    """

    score: int | Unset = UNSET
    association_time: CommonSubHealthInfoDetailVOInteger | Unset = UNSET
    rssi: CommonSubHealthInfoDetailVOInteger | Unset = UNSET
    rate: CommonSubHealthInfoDetailVOLong | Unset = UNSET
    snr: CommonSubHealthInfoDetailVOInteger | Unset = UNSET
    incident: IncidentSubHealthInfoDetailVO | Unset = UNSET
    connect_score: CommonSubHealthInfoDetailVOInteger | Unset = UNSET
    link_error_score: CommonSubHealthInfoDetailVOInteger | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        score = self.score

        association_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.association_time, Unset):
            association_time = self.association_time.to_dict()

        rssi: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rssi, Unset):
            rssi = self.rssi.to_dict()

        rate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rate, Unset):
            rate = self.rate.to_dict()

        snr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snr, Unset):
            snr = self.snr.to_dict()

        incident: dict[str, Any] | Unset = UNSET
        if not isinstance(self.incident, Unset):
            incident = self.incident.to_dict()

        connect_score: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connect_score, Unset):
            connect_score = self.connect_score.to_dict()

        link_error_score: dict[str, Any] | Unset = UNSET
        if not isinstance(self.link_error_score, Unset):
            link_error_score = self.link_error_score.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if score is not UNSET:
            field_dict["score"] = score
        if association_time is not UNSET:
            field_dict["associationTime"] = association_time
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if rate is not UNSET:
            field_dict["rate"] = rate
        if snr is not UNSET:
            field_dict["snr"] = snr
        if incident is not UNSET:
            field_dict["incident"] = incident
        if connect_score is not UNSET:
            field_dict["connectScore"] = connect_score
        if link_error_score is not UNSET:
            field_dict["linkErrorScore"] = link_error_score

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.common_sub_health_info_detail_vo_integer import (
            CommonSubHealthInfoDetailVOInteger,
        )
        from ..models.common_sub_health_info_detail_vo_long import (
            CommonSubHealthInfoDetailVOLong,
        )
        from ..models.incident_sub_health_info_detail_vo import (
            IncidentSubHealthInfoDetailVO,
        )

        d = dict(src_dict)
        score = d.pop("score", UNSET)

        _association_time = d.pop("associationTime", UNSET)
        association_time: CommonSubHealthInfoDetailVOInteger | Unset
        if isinstance(_association_time, Unset):
            association_time = UNSET
        else:
            association_time = CommonSubHealthInfoDetailVOInteger.from_dict(
                _association_time
            )

        _rssi = d.pop("rssi", UNSET)
        rssi: CommonSubHealthInfoDetailVOInteger | Unset
        if isinstance(_rssi, Unset):
            rssi = UNSET
        else:
            rssi = CommonSubHealthInfoDetailVOInteger.from_dict(_rssi)

        _rate = d.pop("rate", UNSET)
        rate: CommonSubHealthInfoDetailVOLong | Unset
        if isinstance(_rate, Unset):
            rate = UNSET
        else:
            rate = CommonSubHealthInfoDetailVOLong.from_dict(_rate)

        _snr = d.pop("snr", UNSET)
        snr: CommonSubHealthInfoDetailVOInteger | Unset
        if isinstance(_snr, Unset):
            snr = UNSET
        else:
            snr = CommonSubHealthInfoDetailVOInteger.from_dict(_snr)

        _incident = d.pop("incident", UNSET)
        incident: IncidentSubHealthInfoDetailVO | Unset
        if isinstance(_incident, Unset):
            incident = UNSET
        else:
            incident = IncidentSubHealthInfoDetailVO.from_dict(_incident)

        _connect_score = d.pop("connectScore", UNSET)
        connect_score: CommonSubHealthInfoDetailVOInteger | Unset
        if isinstance(_connect_score, Unset):
            connect_score = UNSET
        else:
            connect_score = CommonSubHealthInfoDetailVOInteger.from_dict(_connect_score)

        _link_error_score = d.pop("linkErrorScore", UNSET)
        link_error_score: CommonSubHealthInfoDetailVOInteger | Unset
        if isinstance(_link_error_score, Unset):
            link_error_score = UNSET
        else:
            link_error_score = CommonSubHealthInfoDetailVOInteger.from_dict(
                _link_error_score
            )

        client_health_detail_vo = cls(
            score=score,
            association_time=association_time,
            rssi=rssi,
            rate=rate,
            snr=snr,
            incident=incident,
            connect_score=connect_score,
            link_error_score=link_error_score,
        )

        client_health_detail_vo.additional_properties = d
        return client_health_detail_vo

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
