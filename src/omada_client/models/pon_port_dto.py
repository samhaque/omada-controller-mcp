from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.pon_port_dto_dba_calculate_mode import PonPortDTODbaCalculateMode
from ..models.pon_port_dto_downstream_fec import PonPortDTODownstreamFEC
from ..models.pon_port_dto_duplex_link import PonPortDTODuplexLink
from ..models.pon_port_dto_link_status import PonPortDTOLinkStatus
from ..models.pon_port_dto_long_laser_onu_auto_detect import (
    PonPortDTOLongLaserOnuAutoDetect,
)
from ..models.pon_port_dto_long_laser_onu_auto_isolate import (
    PonPortDTOLongLaserOnuAutoIsolate,
)
from ..models.pon_port_dto_onu_isolate import PonPortDTOOnuIsolate
from ..models.pon_port_dto_port_isolate import PonPortDTOPortIsolate
from ..models.pon_port_dto_speed import PonPortDTOSpeed
from ..models.pon_port_dto_status import PonPortDTOStatus
from ..models.pon_port_dto_type import PonPortDTOType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_vo import DeviceVO


T = TypeVar("T", bound="PonPortDTO")


@_attrs_define
class PonPortDTO:
    """Content

    Attributes:
        port_id (str | Unset): Port ID
        status (PonPortDTOStatus | Unset): Whether to enable the laser for the PON port.Status should be a value as
            follows:DISABLE,ENABLE.
        downstream_fec (PonPortDTODownstreamFEC | Unset): Whether to start downstream FEC function of the
            port.DownstreamFEC should be a value as follows:DISABLE,ENABLE.
        key_exchange_period (int | Unset): Configure the downstream encryption ONT key update time. KeyExchangePeriod
            should be a value between 0 to 60 minutes, where 0 means key update is disabled.
        dba_calculate_mode (PonPortDTODbaCalculateMode | Unset): Configure the DBA calculation cycle mode.
            DbaCalculateMode should be a value as follows: MIN_DELAY:In minimum delay mode, the DBA calculation cycle is
            related to the number of T-CONTs. The more T-CONTs there are, the longer the calculation cycle. Under the
            premise that the bandwidth can complete the calculation, it is advisable to use as few calculation cycles as
            possible. When dealing with TDM services, the minimum delay mode must be selected; MAX_BW:In maximum bandwidth
            utilization mode, the DBA calculation cycle is allocated over multiple frames, with each frame lasting 125 µs.
            This method is suitable when the service does not have high delay requirements.
        max_distance (int | Unset): The maximum logical distance of the ONT.MaxDistance should be within the range of 1
            to 60 (km). The difference between the maximum logical distance and the minimum logical distance must not exceed
            40 km.
        min_distance (int | Unset): The minimum logical distance of the ONT.MinDistance should be within the range of 1
            to 40 (km). The difference between the maximum logical distance and the minimum logical distance must not exceed
            40 km.
        port_isolate (PonPortDTOPortIsolate | Unset): Set port isolation function.(only DS-P7001-04、DS-P7001-08 OLT
            support this function,other olts should not provide or display this field)When enabled, the port cannot
            communicate with other ports, and the ONU on this port cannot communicate with ONUs on other ports.PortIsolation
            should be a value as follows:DISABLE,ENABLE.
        onu_isolate (PonPortDTOOnuIsolate | Unset): Set ONU isolation function.(only DS-P7001-04、DS-P7001-08 OLT support
            this function,other olts should not provide or display this field)When enabled, different ONUs on the same port
            cannot communicate with each other.OnuIsolate should be a value as follows:DISABLE,ENABLE.
        long_laser_onu_auto_detect (PonPortDTOLongLaserOnuAutoDetect | Unset): Whether to enable port rogue ONU
            automatic detection function.LongLaserOnuAutoDetect should be a value as follows:DISABLE,ENABLE.Default
            value:DISABLE
        auto_detect_interval (int | Unset): Set the interval time for port traffic ONU detection, unit:
            minutes.AutoDetectInternal should be within the range of 1 to 100.Default value:15
        type_ (PonPortDTOType | Unset): Pon port type,type should be a value as follows:COPPER,COMBO,SFP
        link_status (PonPortDTOLinkStatus | Unset): Pon port link status.LinkStatus should be a value as
            follows:INACTIVE,ACTIVE_WORKING,ACTIVE_WORKING_NONE,ACTIVE_STANDBY
        duplex_link (PonPortDTODuplexLink | Unset): Duplex mode.DuplexLink should be a value as follows:FULL
        speed (PonPortDTOSpeed | Unset): Speed configured by customer.Speed should be a value as
            follows:GPON,XG_PON,XGS_PON,NONE
        up_link_speed (int | Unset): The upstream rate of the PON port, unit: M. The range of values varies by model.
        down_link_speed (int | Unset): The downstream rate of the PON port. The range of values varies by model.
        long_laser_onu_auto_isolate (PonPortDTOLongLaserOnuAutoIsolate | Unset): Whether to enable port rogue ONU
            automatic isolation function.LongLaserOnuAutoIsolate should be a value as follows:DISABLE,ENABLE.Default
            value:DISABLE
        downlink_list (list[DeviceVO] | Unset): Down link device list
        onu_num (int | Unset): Online ONU number
    """

    port_id: str | Unset = UNSET
    status: PonPortDTOStatus | Unset = UNSET
    downstream_fec: PonPortDTODownstreamFEC | Unset = UNSET
    key_exchange_period: int | Unset = UNSET
    dba_calculate_mode: PonPortDTODbaCalculateMode | Unset = UNSET
    max_distance: int | Unset = UNSET
    min_distance: int | Unset = UNSET
    port_isolate: PonPortDTOPortIsolate | Unset = UNSET
    onu_isolate: PonPortDTOOnuIsolate | Unset = UNSET
    long_laser_onu_auto_detect: PonPortDTOLongLaserOnuAutoDetect | Unset = UNSET
    auto_detect_interval: int | Unset = UNSET
    type_: PonPortDTOType | Unset = UNSET
    link_status: PonPortDTOLinkStatus | Unset = UNSET
    duplex_link: PonPortDTODuplexLink | Unset = UNSET
    speed: PonPortDTOSpeed | Unset = UNSET
    up_link_speed: int | Unset = UNSET
    down_link_speed: int | Unset = UNSET
    long_laser_onu_auto_isolate: PonPortDTOLongLaserOnuAutoIsolate | Unset = UNSET
    downlink_list: list[DeviceVO] | Unset = UNSET
    onu_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_id = self.port_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        downstream_fec: str | Unset = UNSET
        if not isinstance(self.downstream_fec, Unset):
            downstream_fec = self.downstream_fec.value

        key_exchange_period = self.key_exchange_period

        dba_calculate_mode: str | Unset = UNSET
        if not isinstance(self.dba_calculate_mode, Unset):
            dba_calculate_mode = self.dba_calculate_mode.value

        max_distance = self.max_distance

        min_distance = self.min_distance

        port_isolate: str | Unset = UNSET
        if not isinstance(self.port_isolate, Unset):
            port_isolate = self.port_isolate.value

        onu_isolate: str | Unset = UNSET
        if not isinstance(self.onu_isolate, Unset):
            onu_isolate = self.onu_isolate.value

        long_laser_onu_auto_detect: str | Unset = UNSET
        if not isinstance(self.long_laser_onu_auto_detect, Unset):
            long_laser_onu_auto_detect = self.long_laser_onu_auto_detect.value

        auto_detect_interval = self.auto_detect_interval

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        link_status: str | Unset = UNSET
        if not isinstance(self.link_status, Unset):
            link_status = self.link_status.value

        duplex_link: str | Unset = UNSET
        if not isinstance(self.duplex_link, Unset):
            duplex_link = self.duplex_link.value

        speed: str | Unset = UNSET
        if not isinstance(self.speed, Unset):
            speed = self.speed.value

        up_link_speed = self.up_link_speed

        down_link_speed = self.down_link_speed

        long_laser_onu_auto_isolate: str | Unset = UNSET
        if not isinstance(self.long_laser_onu_auto_isolate, Unset):
            long_laser_onu_auto_isolate = self.long_laser_onu_auto_isolate.value

        downlink_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.downlink_list, Unset):
            downlink_list = []
            for downlink_list_item_data in self.downlink_list:
                downlink_list_item = downlink_list_item_data.to_dict()
                downlink_list.append(downlink_list_item)

        onu_num = self.onu_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_id is not UNSET:
            field_dict["portId"] = port_id
        if status is not UNSET:
            field_dict["status"] = status
        if downstream_fec is not UNSET:
            field_dict["downstreamFEC"] = downstream_fec
        if key_exchange_period is not UNSET:
            field_dict["keyExchangePeriod"] = key_exchange_period
        if dba_calculate_mode is not UNSET:
            field_dict["dbaCalculateMode"] = dba_calculate_mode
        if max_distance is not UNSET:
            field_dict["maxDistance"] = max_distance
        if min_distance is not UNSET:
            field_dict["minDistance"] = min_distance
        if port_isolate is not UNSET:
            field_dict["portIsolate"] = port_isolate
        if onu_isolate is not UNSET:
            field_dict["onuIsolate"] = onu_isolate
        if long_laser_onu_auto_detect is not UNSET:
            field_dict["longLaserOnuAutoDetect"] = long_laser_onu_auto_detect
        if auto_detect_interval is not UNSET:
            field_dict["autoDetectInterval"] = auto_detect_interval
        if type_ is not UNSET:
            field_dict["type"] = type_
        if link_status is not UNSET:
            field_dict["linkStatus"] = link_status
        if duplex_link is not UNSET:
            field_dict["duplexLink"] = duplex_link
        if speed is not UNSET:
            field_dict["speed"] = speed
        if up_link_speed is not UNSET:
            field_dict["upLinkSpeed"] = up_link_speed
        if down_link_speed is not UNSET:
            field_dict["downLinkSpeed"] = down_link_speed
        if long_laser_onu_auto_isolate is not UNSET:
            field_dict["longLaserOnuAutoIsolate"] = long_laser_onu_auto_isolate
        if downlink_list is not UNSET:
            field_dict["downlinkList"] = downlink_list
        if onu_num is not UNSET:
            field_dict["onuNum"] = onu_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_vo import DeviceVO

        d = dict(src_dict)
        port_id = d.pop("portId", UNSET)

        _status = d.pop("status", UNSET)
        status: PonPortDTOStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PonPortDTOStatus(_status)

        _downstream_fec = d.pop("downstreamFEC", UNSET)
        downstream_fec: PonPortDTODownstreamFEC | Unset
        if isinstance(_downstream_fec, Unset):
            downstream_fec = UNSET
        else:
            downstream_fec = PonPortDTODownstreamFEC(_downstream_fec)

        key_exchange_period = d.pop("keyExchangePeriod", UNSET)

        _dba_calculate_mode = d.pop("dbaCalculateMode", UNSET)
        dba_calculate_mode: PonPortDTODbaCalculateMode | Unset
        if isinstance(_dba_calculate_mode, Unset):
            dba_calculate_mode = UNSET
        else:
            dba_calculate_mode = PonPortDTODbaCalculateMode(_dba_calculate_mode)

        max_distance = d.pop("maxDistance", UNSET)

        min_distance = d.pop("minDistance", UNSET)

        _port_isolate = d.pop("portIsolate", UNSET)
        port_isolate: PonPortDTOPortIsolate | Unset
        if isinstance(_port_isolate, Unset):
            port_isolate = UNSET
        else:
            port_isolate = PonPortDTOPortIsolate(_port_isolate)

        _onu_isolate = d.pop("onuIsolate", UNSET)
        onu_isolate: PonPortDTOOnuIsolate | Unset
        if isinstance(_onu_isolate, Unset):
            onu_isolate = UNSET
        else:
            onu_isolate = PonPortDTOOnuIsolate(_onu_isolate)

        _long_laser_onu_auto_detect = d.pop("longLaserOnuAutoDetect", UNSET)
        long_laser_onu_auto_detect: PonPortDTOLongLaserOnuAutoDetect | Unset
        if isinstance(_long_laser_onu_auto_detect, Unset):
            long_laser_onu_auto_detect = UNSET
        else:
            long_laser_onu_auto_detect = PonPortDTOLongLaserOnuAutoDetect(
                _long_laser_onu_auto_detect
            )

        auto_detect_interval = d.pop("autoDetectInterval", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: PonPortDTOType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PonPortDTOType(_type_)

        _link_status = d.pop("linkStatus", UNSET)
        link_status: PonPortDTOLinkStatus | Unset
        if isinstance(_link_status, Unset):
            link_status = UNSET
        else:
            link_status = PonPortDTOLinkStatus(_link_status)

        _duplex_link = d.pop("duplexLink", UNSET)
        duplex_link: PonPortDTODuplexLink | Unset
        if isinstance(_duplex_link, Unset):
            duplex_link = UNSET
        else:
            duplex_link = PonPortDTODuplexLink(_duplex_link)

        _speed = d.pop("speed", UNSET)
        speed: PonPortDTOSpeed | Unset
        if isinstance(_speed, Unset):
            speed = UNSET
        else:
            speed = PonPortDTOSpeed(_speed)

        up_link_speed = d.pop("upLinkSpeed", UNSET)

        down_link_speed = d.pop("downLinkSpeed", UNSET)

        _long_laser_onu_auto_isolate = d.pop("longLaserOnuAutoIsolate", UNSET)
        long_laser_onu_auto_isolate: PonPortDTOLongLaserOnuAutoIsolate | Unset
        if isinstance(_long_laser_onu_auto_isolate, Unset):
            long_laser_onu_auto_isolate = UNSET
        else:
            long_laser_onu_auto_isolate = PonPortDTOLongLaserOnuAutoIsolate(
                _long_laser_onu_auto_isolate
            )

        _downlink_list = d.pop("downlinkList", UNSET)
        downlink_list: list[DeviceVO] | Unset = UNSET
        if _downlink_list is not UNSET:
            downlink_list = []
            for downlink_list_item_data in _downlink_list:
                downlink_list_item = DeviceVO.from_dict(downlink_list_item_data)

                downlink_list.append(downlink_list_item)

        onu_num = d.pop("onuNum", UNSET)

        pon_port_dto = cls(
            port_id=port_id,
            status=status,
            downstream_fec=downstream_fec,
            key_exchange_period=key_exchange_period,
            dba_calculate_mode=dba_calculate_mode,
            max_distance=max_distance,
            min_distance=min_distance,
            port_isolate=port_isolate,
            onu_isolate=onu_isolate,
            long_laser_onu_auto_detect=long_laser_onu_auto_detect,
            auto_detect_interval=auto_detect_interval,
            type_=type_,
            link_status=link_status,
            duplex_link=duplex_link,
            speed=speed,
            up_link_speed=up_link_speed,
            down_link_speed=down_link_speed,
            long_laser_onu_auto_isolate=long_laser_onu_auto_isolate,
            downlink_list=downlink_list,
            onu_num=onu_num,
        )

        pon_port_dto.additional_properties = d
        return pon_port_dto

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
