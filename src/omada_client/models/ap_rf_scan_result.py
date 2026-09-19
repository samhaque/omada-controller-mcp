from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rf_scan_radio_2g import RFScanRadio2G
    from ..models.rf_scan_radio_5g import RFScanRadio5G
    from ..models.rf_scan_radio_5g2 import RFScanRadio5G2
    from ..models.rf_scan_radio_6g import RFScanRadio6G


T = TypeVar("T", bound="ApRFScanResult")


@_attrs_define
class ApRFScanResult:
    """
    Attributes:
        channel2g (list[RFScanRadio2G] | Unset): Channel 2g
        channel5g (list[RFScanRadio5G] | Unset): Channel 5g
        channel5g2 (list[RFScanRadio5G2] | Unset): Channel 5g2
        channel6g (list[RFScanRadio6G] | Unset): Channel 6g
        current_chan_2_g (str | Unset): The 2G channel of AP, such as 1,6,11,13. It should be within the range of 1–13.
        current_chan_5_g (str | Unset): The 5G channel of AP, such as 36,161. It should be within the range of 36–161.
        current_chan_5_g_2 (str | Unset): The 5G2 channel of AP,such as 36,161. It should be within the range of 36–161.
        current_chan_6_g (str | Unset): The 6G channel of AP,such as 36,161. It should be within the range of 36–161.
        current_chan_w2_g (int | Unset): The 2g channel bandwidth of the AP. It should be a value as follows: 2:20MHz,
            3: 40MHz
        current_chan_w5_g (int | Unset): The 5g channel bandwidth of the AP. It should be a value as follows: 2:20MHz,
            3: 40MHz, 5: 80MHz2 menas 20MHz, 3 means 40MHz, 5 means 80MHz
        current_chan_w5_g_2 (int | Unset): The 5g2 channel bandwidth of the AP. It should be a value as follows:
            2:20MHz, 3: 40MHz, 5: 80MHz
        current_chan_w6_g (int | Unset): The 6g channel bandwidth of the AP. It should be a value as follows: 2:20MHz,
            3: 40MHz, 5: 80MHz
        time (int | Unset): The scan time(13 bits), Unit: ms
        time2g (int | Unset): The scan time(13 bits) of 5GHz-2 band, Unit: ms
        time5g (int | Unset): The scan time(13 bits) of 5GHz band, Unit: ms
        time6g (int | Unset): The scan time(13 bits) of 6GHz band, Unit: ms
        status (int | Unset): Status should be a value as follows: 0: the scan result is displayed; 1: no scan result;
            2: Scanning
        status2g (int | Unset): Status of 2.4GHz band should be a value as follows: 0: the scan result is displayed; 1:
            no scan result; 2: Scanning
        status5g (int | Unset): Status of 5GHz band should be a value as follows: 0: the scan result is displayed; 1: no
            scan result; 2: Scanning
        status5g2 (int | Unset): Status of 5GHz-2 band should be a value as follows: 0: the scan result is displayed; 1:
            no scan result; 2: Scanning
        status6g (int | Unset): Status of 6GHz band should be a value as follows: 0: the scan result is displayed; 1: no
            scan result; 2: Scanning
    """

    channel2g: list[RFScanRadio2G] | Unset = UNSET
    channel5g: list[RFScanRadio5G] | Unset = UNSET
    channel5g2: list[RFScanRadio5G2] | Unset = UNSET
    channel6g: list[RFScanRadio6G] | Unset = UNSET
    current_chan_2_g: str | Unset = UNSET
    current_chan_5_g: str | Unset = UNSET
    current_chan_5_g_2: str | Unset = UNSET
    current_chan_6_g: str | Unset = UNSET
    current_chan_w2_g: int | Unset = UNSET
    current_chan_w5_g: int | Unset = UNSET
    current_chan_w5_g_2: int | Unset = UNSET
    current_chan_w6_g: int | Unset = UNSET
    time: int | Unset = UNSET
    time2g: int | Unset = UNSET
    time5g: int | Unset = UNSET
    time6g: int | Unset = UNSET
    status: int | Unset = UNSET
    status2g: int | Unset = UNSET
    status5g: int | Unset = UNSET
    status5g2: int | Unset = UNSET
    status6g: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel2g: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channel2g, Unset):
            channel2g = []
            for channel2g_item_data in self.channel2g:
                channel2g_item = channel2g_item_data.to_dict()
                channel2g.append(channel2g_item)

        channel5g: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channel5g, Unset):
            channel5g = []
            for channel5g_item_data in self.channel5g:
                channel5g_item = channel5g_item_data.to_dict()
                channel5g.append(channel5g_item)

        channel5g2: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channel5g2, Unset):
            channel5g2 = []
            for channel5g2_item_data in self.channel5g2:
                channel5g2_item = channel5g2_item_data.to_dict()
                channel5g2.append(channel5g2_item)

        channel6g: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channel6g, Unset):
            channel6g = []
            for channel6g_item_data in self.channel6g:
                channel6g_item = channel6g_item_data.to_dict()
                channel6g.append(channel6g_item)

        current_chan_2_g = self.current_chan_2_g

        current_chan_5_g = self.current_chan_5_g

        current_chan_5_g_2 = self.current_chan_5_g_2

        current_chan_6_g = self.current_chan_6_g

        current_chan_w2_g = self.current_chan_w2_g

        current_chan_w5_g = self.current_chan_w5_g

        current_chan_w5_g_2 = self.current_chan_w5_g_2

        current_chan_w6_g = self.current_chan_w6_g

        time = self.time

        time2g = self.time2g

        time5g = self.time5g

        time6g = self.time6g

        status = self.status

        status2g = self.status2g

        status5g = self.status5g

        status5g2 = self.status5g2

        status6g = self.status6g

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel2g is not UNSET:
            field_dict["channel2g"] = channel2g
        if channel5g is not UNSET:
            field_dict["channel5g"] = channel5g
        if channel5g2 is not UNSET:
            field_dict["channel5g2"] = channel5g2
        if channel6g is not UNSET:
            field_dict["channel6g"] = channel6g
        if current_chan_2_g is not UNSET:
            field_dict["currentChan2g"] = current_chan_2_g
        if current_chan_5_g is not UNSET:
            field_dict["currentChan5g"] = current_chan_5_g
        if current_chan_5_g_2 is not UNSET:
            field_dict["currentChan5g2"] = current_chan_5_g_2
        if current_chan_6_g is not UNSET:
            field_dict["currentChan6g"] = current_chan_6_g
        if current_chan_w2_g is not UNSET:
            field_dict["currentChanW2g"] = current_chan_w2_g
        if current_chan_w5_g is not UNSET:
            field_dict["currentChanW5g"] = current_chan_w5_g
        if current_chan_w5_g_2 is not UNSET:
            field_dict["currentChanW5g2"] = current_chan_w5_g_2
        if current_chan_w6_g is not UNSET:
            field_dict["currentChanW6g"] = current_chan_w6_g
        if time is not UNSET:
            field_dict["time"] = time
        if time2g is not UNSET:
            field_dict["time2g"] = time2g
        if time5g is not UNSET:
            field_dict["time5g"] = time5g
        if time6g is not UNSET:
            field_dict["time6g"] = time6g
        if status is not UNSET:
            field_dict["status"] = status
        if status2g is not UNSET:
            field_dict["status2g"] = status2g
        if status5g is not UNSET:
            field_dict["status5g"] = status5g
        if status5g2 is not UNSET:
            field_dict["status5g2"] = status5g2
        if status6g is not UNSET:
            field_dict["status6g"] = status6g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.rf_scan_radio_2g import RFScanRadio2G
        from ..models.rf_scan_radio_5g import RFScanRadio5G
        from ..models.rf_scan_radio_5g2 import RFScanRadio5G2
        from ..models.rf_scan_radio_6g import RFScanRadio6G

        d = dict(src_dict)
        _channel2g = d.pop("channel2g", UNSET)
        channel2g: list[RFScanRadio2G] | Unset = UNSET
        if _channel2g is not UNSET:
            channel2g = []
            for channel2g_item_data in _channel2g:
                channel2g_item = RFScanRadio2G.from_dict(channel2g_item_data)

                channel2g.append(channel2g_item)

        _channel5g = d.pop("channel5g", UNSET)
        channel5g: list[RFScanRadio5G] | Unset = UNSET
        if _channel5g is not UNSET:
            channel5g = []
            for channel5g_item_data in _channel5g:
                channel5g_item = RFScanRadio5G.from_dict(channel5g_item_data)

                channel5g.append(channel5g_item)

        _channel5g2 = d.pop("channel5g2", UNSET)
        channel5g2: list[RFScanRadio5G2] | Unset = UNSET
        if _channel5g2 is not UNSET:
            channel5g2 = []
            for channel5g2_item_data in _channel5g2:
                channel5g2_item = RFScanRadio5G2.from_dict(channel5g2_item_data)

                channel5g2.append(channel5g2_item)

        _channel6g = d.pop("channel6g", UNSET)
        channel6g: list[RFScanRadio6G] | Unset = UNSET
        if _channel6g is not UNSET:
            channel6g = []
            for channel6g_item_data in _channel6g:
                channel6g_item = RFScanRadio6G.from_dict(channel6g_item_data)

                channel6g.append(channel6g_item)

        current_chan_2_g = d.pop("currentChan2g", UNSET)

        current_chan_5_g = d.pop("currentChan5g", UNSET)

        current_chan_5_g_2 = d.pop("currentChan5g2", UNSET)

        current_chan_6_g = d.pop("currentChan6g", UNSET)

        current_chan_w2_g = d.pop("currentChanW2g", UNSET)

        current_chan_w5_g = d.pop("currentChanW5g", UNSET)

        current_chan_w5_g_2 = d.pop("currentChanW5g2", UNSET)

        current_chan_w6_g = d.pop("currentChanW6g", UNSET)

        time = d.pop("time", UNSET)

        time2g = d.pop("time2g", UNSET)

        time5g = d.pop("time5g", UNSET)

        time6g = d.pop("time6g", UNSET)

        status = d.pop("status", UNSET)

        status2g = d.pop("status2g", UNSET)

        status5g = d.pop("status5g", UNSET)

        status5g2 = d.pop("status5g2", UNSET)

        status6g = d.pop("status6g", UNSET)

        ap_rf_scan_result = cls(
            channel2g=channel2g,
            channel5g=channel5g,
            channel5g2=channel5g2,
            channel6g=channel6g,
            current_chan_2_g=current_chan_2_g,
            current_chan_5_g=current_chan_5_g,
            current_chan_5_g_2=current_chan_5_g_2,
            current_chan_6_g=current_chan_6_g,
            current_chan_w2_g=current_chan_w2_g,
            current_chan_w5_g=current_chan_w5_g,
            current_chan_w5_g_2=current_chan_w5_g_2,
            current_chan_w6_g=current_chan_w6_g,
            time=time,
            time2g=time2g,
            time5g=time5g,
            time6g=time6g,
            status=status,
            status2g=status2g,
            status5g=status5g,
            status5g2=status5g2,
            status6g=status6g,
        )

        ap_rf_scan_result.additional_properties = d
        return ap_rf_scan_result

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
