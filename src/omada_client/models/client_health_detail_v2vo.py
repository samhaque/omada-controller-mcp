from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_sub_health_info_detail_vo import ChannelSubHealthInfoDetailVO
    from ..models.client_data_rate_sub_health_detail_vo import (
        ClientDataRateSubHealthDetailVO,
    )
    from ..models.common_sub_health_info_detail_vo import CommonSubHealthInfoDetailVO
    from ..models.connect_score_sub_health_info_detail_vo import (
        ConnectScoreSubHealthInfoDetailVO,
    )
    from ..models.incident_sub_health_info_detail_vo import (
        IncidentSubHealthInfoDetailVO,
    )
    from ..models.on_boarding_time_sub_health_detail_vo import (
        OnBoardingTimeSubHealthDetailVO,
    )


T = TypeVar("T", bound="ClientHealthDetailV2VO")


@_attrs_define
class ClientHealthDetailV2VO:
    """
    Attributes:
        score (int | Unset):
        onboarding_time (OnBoardingTimeSubHealthDetailVO | Unset): Onboarding time health info and score
        band_rssi (ChannelSubHealthInfoDetailVO | Unset): Rssi health info and score
        data_rate (ClientDataRateSubHealthDetailVO | Unset): Negotiation rate health info and score
        snr (CommonSubHealthInfoDetailVO | Unset): Link error score health info and score (wired clients only)
        connect_score (ConnectScoreSubHealthInfoDetailVO | Unset): Connect score and status (wired clients only)
        link_error_score (CommonSubHealthInfoDetailVO | Unset): Link error score health info and score (wired clients
            only)
        incident (IncidentSubHealthInfoDetailVO | Unset): Incident health info and score (wireless clients only)
    """

    score: int | Unset = UNSET
    onboarding_time: OnBoardingTimeSubHealthDetailVO | Unset = UNSET
    band_rssi: ChannelSubHealthInfoDetailVO | Unset = UNSET
    data_rate: ClientDataRateSubHealthDetailVO | Unset = UNSET
    snr: CommonSubHealthInfoDetailVO | Unset = UNSET
    connect_score: ConnectScoreSubHealthInfoDetailVO | Unset = UNSET
    link_error_score: CommonSubHealthInfoDetailVO | Unset = UNSET
    incident: IncidentSubHealthInfoDetailVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        score = self.score

        onboarding_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.onboarding_time, Unset):
            onboarding_time = self.onboarding_time.to_dict()

        band_rssi: dict[str, Any] | Unset = UNSET
        if not isinstance(self.band_rssi, Unset):
            band_rssi = self.band_rssi.to_dict()

        data_rate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_rate, Unset):
            data_rate = self.data_rate.to_dict()

        snr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snr, Unset):
            snr = self.snr.to_dict()

        connect_score: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connect_score, Unset):
            connect_score = self.connect_score.to_dict()

        link_error_score: dict[str, Any] | Unset = UNSET
        if not isinstance(self.link_error_score, Unset):
            link_error_score = self.link_error_score.to_dict()

        incident: dict[str, Any] | Unset = UNSET
        if not isinstance(self.incident, Unset):
            incident = self.incident.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if score is not UNSET:
            field_dict["score"] = score
        if onboarding_time is not UNSET:
            field_dict["onboardingTime"] = onboarding_time
        if band_rssi is not UNSET:
            field_dict["bandRssi"] = band_rssi
        if data_rate is not UNSET:
            field_dict["dataRate"] = data_rate
        if snr is not UNSET:
            field_dict["snr"] = snr
        if connect_score is not UNSET:
            field_dict["connectScore"] = connect_score
        if link_error_score is not UNSET:
            field_dict["linkErrorScore"] = link_error_score
        if incident is not UNSET:
            field_dict["incident"] = incident

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.channel_sub_health_info_detail_vo import (
            ChannelSubHealthInfoDetailVO,
        )
        from ..models.client_data_rate_sub_health_detail_vo import (
            ClientDataRateSubHealthDetailVO,
        )
        from ..models.common_sub_health_info_detail_vo import (
            CommonSubHealthInfoDetailVO,
        )
        from ..models.connect_score_sub_health_info_detail_vo import (
            ConnectScoreSubHealthInfoDetailVO,
        )
        from ..models.incident_sub_health_info_detail_vo import (
            IncidentSubHealthInfoDetailVO,
        )
        from ..models.on_boarding_time_sub_health_detail_vo import (
            OnBoardingTimeSubHealthDetailVO,
        )

        d = dict(src_dict)
        score = d.pop("score", UNSET)

        _onboarding_time = d.pop("onboardingTime", UNSET)
        onboarding_time: OnBoardingTimeSubHealthDetailVO | Unset
        if isinstance(_onboarding_time, Unset):
            onboarding_time = UNSET
        else:
            onboarding_time = OnBoardingTimeSubHealthDetailVO.from_dict(
                _onboarding_time
            )

        _band_rssi = d.pop("bandRssi", UNSET)
        band_rssi: ChannelSubHealthInfoDetailVO | Unset
        if isinstance(_band_rssi, Unset):
            band_rssi = UNSET
        else:
            band_rssi = ChannelSubHealthInfoDetailVO.from_dict(_band_rssi)

        _data_rate = d.pop("dataRate", UNSET)
        data_rate: ClientDataRateSubHealthDetailVO | Unset
        if isinstance(_data_rate, Unset):
            data_rate = UNSET
        else:
            data_rate = ClientDataRateSubHealthDetailVO.from_dict(_data_rate)

        _snr = d.pop("snr", UNSET)
        snr: CommonSubHealthInfoDetailVO | Unset
        if isinstance(_snr, Unset):
            snr = UNSET
        else:
            snr = CommonSubHealthInfoDetailVO.from_dict(_snr)

        _connect_score = d.pop("connectScore", UNSET)
        connect_score: ConnectScoreSubHealthInfoDetailVO | Unset
        if isinstance(_connect_score, Unset):
            connect_score = UNSET
        else:
            connect_score = ConnectScoreSubHealthInfoDetailVO.from_dict(_connect_score)

        _link_error_score = d.pop("linkErrorScore", UNSET)
        link_error_score: CommonSubHealthInfoDetailVO | Unset
        if isinstance(_link_error_score, Unset):
            link_error_score = UNSET
        else:
            link_error_score = CommonSubHealthInfoDetailVO.from_dict(_link_error_score)

        _incident = d.pop("incident", UNSET)
        incident: IncidentSubHealthInfoDetailVO | Unset
        if isinstance(_incident, Unset):
            incident = UNSET
        else:
            incident = IncidentSubHealthInfoDetailVO.from_dict(_incident)

        client_health_detail_v2vo = cls(
            score=score,
            onboarding_time=onboarding_time,
            band_rssi=band_rssi,
            data_rate=data_rate,
            snr=snr,
            connect_score=connect_score,
            link_error_score=link_error_score,
            incident=incident,
        )

        client_health_detail_v2vo.additional_properties = d
        return client_health_detail_v2vo

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
