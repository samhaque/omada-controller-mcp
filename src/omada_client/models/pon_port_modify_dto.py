from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.pon_port_modify_dto_dba_calculate_mode import (
    PonPortModifyDTODbaCalculateMode,
)
from ..models.pon_port_modify_dto_downstream_fec import PonPortModifyDTODownstreamFEC
from ..models.pon_port_modify_dto_long_laser_onu_auto_detect import (
    PonPortModifyDTOLongLaserOnuAutoDetect,
)
from ..models.pon_port_modify_dto_long_laser_onu_auto_isolate import (
    PonPortModifyDTOLongLaserOnuAutoIsolate,
)
from ..models.pon_port_modify_dto_status import PonPortModifyDTOStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PonPortModifyDTO")


@_attrs_define
class PonPortModifyDTO:
    """
    Attributes:
        port_id (str): Port ID
        key_exchange_period (int): Configure the downstream encryption ONT key update time. KeyExchangePeriod should be
            within the range of 0 to 60 minutes, where 0 means key update is disabled.
        max_distance (int): The maximum logical distance of the ONT.MaxDistance should be within the range of 1 to 60
            (km). The difference between the maximum logical distance and the minimum logical distance must not exceed 40
            km.
        min_distance (int): The minimum logical distance of the ONT.MinDistance should be within the range of 1 to 40
            (km). The difference between the maximum logical distance and the minimum logical distance must not exceed 40
            km.
        auto_detect_interval (int): Set the interval time for port traffic ONU detection, unit:
            minutes.AutoDetectInternal should be within the range of 1 to 100.Default value:15
        status (PonPortModifyDTOStatus | Unset): Whether to enable the laser for the PON port.Status should be a value
            as follows:DISABLE,ENABLE.
        downstream_fec (PonPortModifyDTODownstreamFEC | Unset): Whether to start downstream FEC function of the
            port.DownstreamFEC should be a value as follows:DISABLE,ENABLE.
        dba_calculate_mode (PonPortModifyDTODbaCalculateMode | Unset): Configure the DBA calculation cycle mode.
            DbaCalculateMode should be a value as follows: MIN_DELAY:In minimum delay mode, the DBA calculation cycle is
            related to the number of T-CONTs. The more T-CONTs there are, the longer the calculation cycle. Under the
            premise that the bandwidth can complete the calculation, it is advisable to use as few calculation cycles as
            possible. When dealing with TDM services, the minimum delay mode must be selected; MAX_BW:In maximum bandwidth
            utilization mode, the DBA calculation cycle is allocated over multiple frames, with each frame lasting 125 µs.
            This method is suitable when the service does not have high delay requirements.
        long_laser_onu_auto_detect (PonPortModifyDTOLongLaserOnuAutoDetect | Unset): Whether to enable port rogue ONU
            automatic detection function.LongLaserOnuAutoDetect should be a value as follows:DISABLE,ENABLE.Default
            value:DISABLE
        long_laser_onu_auto_isolate (PonPortModifyDTOLongLaserOnuAutoIsolate | Unset): Whether to enable port rogue ONU
            automatic isolation function.LongLaserOnuAutoIsolate should be a value as follows:DISABLE,ENABLE.Default
            value:DISABLE
    """

    port_id: str
    key_exchange_period: int
    max_distance: int
    min_distance: int
    auto_detect_interval: int
    status: PonPortModifyDTOStatus | Unset = UNSET
    downstream_fec: PonPortModifyDTODownstreamFEC | Unset = UNSET
    dba_calculate_mode: PonPortModifyDTODbaCalculateMode | Unset = UNSET
    long_laser_onu_auto_detect: PonPortModifyDTOLongLaserOnuAutoDetect | Unset = UNSET
    long_laser_onu_auto_isolate: PonPortModifyDTOLongLaserOnuAutoIsolate | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_id = self.port_id

        key_exchange_period = self.key_exchange_period

        max_distance = self.max_distance

        min_distance = self.min_distance

        auto_detect_interval = self.auto_detect_interval

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        downstream_fec: str | Unset = UNSET
        if not isinstance(self.downstream_fec, Unset):
            downstream_fec = self.downstream_fec.value

        dba_calculate_mode: str | Unset = UNSET
        if not isinstance(self.dba_calculate_mode, Unset):
            dba_calculate_mode = self.dba_calculate_mode.value

        long_laser_onu_auto_detect: str | Unset = UNSET
        if not isinstance(self.long_laser_onu_auto_detect, Unset):
            long_laser_onu_auto_detect = self.long_laser_onu_auto_detect.value

        long_laser_onu_auto_isolate: str | Unset = UNSET
        if not isinstance(self.long_laser_onu_auto_isolate, Unset):
            long_laser_onu_auto_isolate = self.long_laser_onu_auto_isolate.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portId": port_id,
                "keyExchangePeriod": key_exchange_period,
                "maxDistance": max_distance,
                "minDistance": min_distance,
                "autoDetectInterval": auto_detect_interval,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if downstream_fec is not UNSET:
            field_dict["downstreamFEC"] = downstream_fec
        if dba_calculate_mode is not UNSET:
            field_dict["dbaCalculateMode"] = dba_calculate_mode
        if long_laser_onu_auto_detect is not UNSET:
            field_dict["longLaserOnuAutoDetect"] = long_laser_onu_auto_detect
        if long_laser_onu_auto_isolate is not UNSET:
            field_dict["longLaserOnuAutoIsolate"] = long_laser_onu_auto_isolate

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_id = d.pop("portId")

        key_exchange_period = d.pop("keyExchangePeriod")

        max_distance = d.pop("maxDistance")

        min_distance = d.pop("minDistance")

        auto_detect_interval = d.pop("autoDetectInterval")

        _status = d.pop("status", UNSET)
        status: PonPortModifyDTOStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PonPortModifyDTOStatus(_status)

        _downstream_fec = d.pop("downstreamFEC", UNSET)
        downstream_fec: PonPortModifyDTODownstreamFEC | Unset
        if isinstance(_downstream_fec, Unset):
            downstream_fec = UNSET
        else:
            downstream_fec = PonPortModifyDTODownstreamFEC(_downstream_fec)

        _dba_calculate_mode = d.pop("dbaCalculateMode", UNSET)
        dba_calculate_mode: PonPortModifyDTODbaCalculateMode | Unset
        if isinstance(_dba_calculate_mode, Unset):
            dba_calculate_mode = UNSET
        else:
            dba_calculate_mode = PonPortModifyDTODbaCalculateMode(_dba_calculate_mode)

        _long_laser_onu_auto_detect = d.pop("longLaserOnuAutoDetect", UNSET)
        long_laser_onu_auto_detect: PonPortModifyDTOLongLaserOnuAutoDetect | Unset
        if isinstance(_long_laser_onu_auto_detect, Unset):
            long_laser_onu_auto_detect = UNSET
        else:
            long_laser_onu_auto_detect = PonPortModifyDTOLongLaserOnuAutoDetect(
                _long_laser_onu_auto_detect
            )

        _long_laser_onu_auto_isolate = d.pop("longLaserOnuAutoIsolate", UNSET)
        long_laser_onu_auto_isolate: PonPortModifyDTOLongLaserOnuAutoIsolate | Unset
        if isinstance(_long_laser_onu_auto_isolate, Unset):
            long_laser_onu_auto_isolate = UNSET
        else:
            long_laser_onu_auto_isolate = PonPortModifyDTOLongLaserOnuAutoIsolate(
                _long_laser_onu_auto_isolate
            )

        pon_port_modify_dto = cls(
            port_id=port_id,
            key_exchange_period=key_exchange_period,
            max_distance=max_distance,
            min_distance=min_distance,
            auto_detect_interval=auto_detect_interval,
            status=status,
            downstream_fec=downstream_fec,
            dba_calculate_mode=dba_calculate_mode,
            long_laser_onu_auto_detect=long_laser_onu_auto_detect,
            long_laser_onu_auto_isolate=long_laser_onu_auto_isolate,
        )

        pon_port_modify_dto.additional_properties = d
        return pon_port_modify_dto

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
