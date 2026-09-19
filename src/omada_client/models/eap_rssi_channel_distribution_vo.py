from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eap_rssi_channel_vo import EapRssiChannelVO


T = TypeVar("T", bound="EapRssiChannelDistributionVO")


@_attrs_define
class EapRssiChannelDistributionVO:
    """
    Attributes:
        exist_ap (bool | Unset):
        exist_ap_client (bool | Unset):
        less_than_90 (list[EapRssiChannelVO] | Unset):
        from_90_to_85 (list[EapRssiChannelVO] | Unset):
        from_85_to_80 (list[EapRssiChannelVO] | Unset):
        from_80_to_75 (list[EapRssiChannelVO] | Unset):
        from_75_to_70 (list[EapRssiChannelVO] | Unset):
        from_70_to_65 (list[EapRssiChannelVO] | Unset):
        from_65_to_60 (list[EapRssiChannelVO] | Unset):
        from_60_to_55 (list[EapRssiChannelVO] | Unset):
        from_55_to_50 (list[EapRssiChannelVO] | Unset):
        from_50_to_45 (list[EapRssiChannelVO] | Unset):
        from_45_to_40 (list[EapRssiChannelVO] | Unset):
        from_40_to_35 (list[EapRssiChannelVO] | Unset):
        from_35_to_30 (list[EapRssiChannelVO] | Unset):
        more_than_30 (list[EapRssiChannelVO] | Unset):
    """

    exist_ap: bool | Unset = UNSET
    exist_ap_client: bool | Unset = UNSET
    less_than_90: list[EapRssiChannelVO] | Unset = UNSET
    from_90_to_85: list[EapRssiChannelVO] | Unset = UNSET
    from_85_to_80: list[EapRssiChannelVO] | Unset = UNSET
    from_80_to_75: list[EapRssiChannelVO] | Unset = UNSET
    from_75_to_70: list[EapRssiChannelVO] | Unset = UNSET
    from_70_to_65: list[EapRssiChannelVO] | Unset = UNSET
    from_65_to_60: list[EapRssiChannelVO] | Unset = UNSET
    from_60_to_55: list[EapRssiChannelVO] | Unset = UNSET
    from_55_to_50: list[EapRssiChannelVO] | Unset = UNSET
    from_50_to_45: list[EapRssiChannelVO] | Unset = UNSET
    from_45_to_40: list[EapRssiChannelVO] | Unset = UNSET
    from_40_to_35: list[EapRssiChannelVO] | Unset = UNSET
    from_35_to_30: list[EapRssiChannelVO] | Unset = UNSET
    more_than_30: list[EapRssiChannelVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exist_ap = self.exist_ap

        exist_ap_client = self.exist_ap_client

        less_than_90: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.less_than_90, Unset):
            less_than_90 = []
            for less_than_90_item_data in self.less_than_90:
                less_than_90_item = less_than_90_item_data.to_dict()
                less_than_90.append(less_than_90_item)

        from_90_to_85: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.from_90_to_85, Unset):
            from_90_to_85 = []
            for from_90_to_85_item_data in self.from_90_to_85:
                from_90_to_85_item = from_90_to_85_item_data.to_dict()
                from_90_to_85.append(from_90_to_85_item)

        from_85_to_80: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.from_85_to_80, Unset):
            from_85_to_80 = []
            for from_85_to_80_item_data in self.from_85_to_80:
                from_85_to_80_item = from_85_to_80_item_data.to_dict()
                from_85_to_80.append(from_85_to_80_item)

        from_80_to_75: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.from_80_to_75, Unset):
            from_80_to_75 = []
            for from_80_to_75_item_data in self.from_80_to_75:
                from_80_to_75_item = from_80_to_75_item_data.to_dict()
                from_80_to_75.append(from_80_to_75_item)

        from_75_to_70: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.from_75_to_70, Unset):
            from_75_to_70 = []
            for from_75_to_70_item_data in self.from_75_to_70:
                from_75_to_70_item = from_75_to_70_item_data.to_dict()
                from_75_to_70.append(from_75_to_70_item)

        from_70_to_65: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.from_70_to_65, Unset):
            from_70_to_65 = []
            for from_70_to_65_item_data in self.from_70_to_65:
                from_70_to_65_item = from_70_to_65_item_data.to_dict()
                from_70_to_65.append(from_70_to_65_item)

        from_65_to_60: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.from_65_to_60, Unset):
            from_65_to_60 = []
            for from_65_to_60_item_data in self.from_65_to_60:
                from_65_to_60_item = from_65_to_60_item_data.to_dict()
                from_65_to_60.append(from_65_to_60_item)

        from_60_to_55: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.from_60_to_55, Unset):
            from_60_to_55 = []
            for from_60_to_55_item_data in self.from_60_to_55:
                from_60_to_55_item = from_60_to_55_item_data.to_dict()
                from_60_to_55.append(from_60_to_55_item)

        from_55_to_50: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.from_55_to_50, Unset):
            from_55_to_50 = []
            for from_55_to_50_item_data in self.from_55_to_50:
                from_55_to_50_item = from_55_to_50_item_data.to_dict()
                from_55_to_50.append(from_55_to_50_item)

        from_50_to_45: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.from_50_to_45, Unset):
            from_50_to_45 = []
            for from_50_to_45_item_data in self.from_50_to_45:
                from_50_to_45_item = from_50_to_45_item_data.to_dict()
                from_50_to_45.append(from_50_to_45_item)

        from_45_to_40: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.from_45_to_40, Unset):
            from_45_to_40 = []
            for from_45_to_40_item_data in self.from_45_to_40:
                from_45_to_40_item = from_45_to_40_item_data.to_dict()
                from_45_to_40.append(from_45_to_40_item)

        from_40_to_35: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.from_40_to_35, Unset):
            from_40_to_35 = []
            for from_40_to_35_item_data in self.from_40_to_35:
                from_40_to_35_item = from_40_to_35_item_data.to_dict()
                from_40_to_35.append(from_40_to_35_item)

        from_35_to_30: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.from_35_to_30, Unset):
            from_35_to_30 = []
            for from_35_to_30_item_data in self.from_35_to_30:
                from_35_to_30_item = from_35_to_30_item_data.to_dict()
                from_35_to_30.append(from_35_to_30_item)

        more_than_30: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.more_than_30, Unset):
            more_than_30 = []
            for more_than_30_item_data in self.more_than_30:
                more_than_30_item = more_than_30_item_data.to_dict()
                more_than_30.append(more_than_30_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exist_ap is not UNSET:
            field_dict["existAp"] = exist_ap
        if exist_ap_client is not UNSET:
            field_dict["existApClient"] = exist_ap_client
        if less_than_90 is not UNSET:
            field_dict["lessThan90"] = less_than_90
        if from_90_to_85 is not UNSET:
            field_dict["from90To85"] = from_90_to_85
        if from_85_to_80 is not UNSET:
            field_dict["from85To80"] = from_85_to_80
        if from_80_to_75 is not UNSET:
            field_dict["from80To75"] = from_80_to_75
        if from_75_to_70 is not UNSET:
            field_dict["from75To70"] = from_75_to_70
        if from_70_to_65 is not UNSET:
            field_dict["from70To65"] = from_70_to_65
        if from_65_to_60 is not UNSET:
            field_dict["from65To60"] = from_65_to_60
        if from_60_to_55 is not UNSET:
            field_dict["from60To55"] = from_60_to_55
        if from_55_to_50 is not UNSET:
            field_dict["from55To50"] = from_55_to_50
        if from_50_to_45 is not UNSET:
            field_dict["from50To45"] = from_50_to_45
        if from_45_to_40 is not UNSET:
            field_dict["from45To40"] = from_45_to_40
        if from_40_to_35 is not UNSET:
            field_dict["from40To35"] = from_40_to_35
        if from_35_to_30 is not UNSET:
            field_dict["from35To30"] = from_35_to_30
        if more_than_30 is not UNSET:
            field_dict["moreThan30"] = more_than_30

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.eap_rssi_channel_vo import EapRssiChannelVO

        d = dict(src_dict)
        exist_ap = d.pop("existAp", UNSET)

        exist_ap_client = d.pop("existApClient", UNSET)

        _less_than_90 = d.pop("lessThan90", UNSET)
        less_than_90: list[EapRssiChannelVO] | Unset = UNSET
        if _less_than_90 is not UNSET:
            less_than_90 = []
            for less_than_90_item_data in _less_than_90:
                less_than_90_item = EapRssiChannelVO.from_dict(less_than_90_item_data)

                less_than_90.append(less_than_90_item)

        _from_90_to_85 = d.pop("from90To85", UNSET)
        from_90_to_85: list[EapRssiChannelVO] | Unset = UNSET
        if _from_90_to_85 is not UNSET:
            from_90_to_85 = []
            for from_90_to_85_item_data in _from_90_to_85:
                from_90_to_85_item = EapRssiChannelVO.from_dict(from_90_to_85_item_data)

                from_90_to_85.append(from_90_to_85_item)

        _from_85_to_80 = d.pop("from85To80", UNSET)
        from_85_to_80: list[EapRssiChannelVO] | Unset = UNSET
        if _from_85_to_80 is not UNSET:
            from_85_to_80 = []
            for from_85_to_80_item_data in _from_85_to_80:
                from_85_to_80_item = EapRssiChannelVO.from_dict(from_85_to_80_item_data)

                from_85_to_80.append(from_85_to_80_item)

        _from_80_to_75 = d.pop("from80To75", UNSET)
        from_80_to_75: list[EapRssiChannelVO] | Unset = UNSET
        if _from_80_to_75 is not UNSET:
            from_80_to_75 = []
            for from_80_to_75_item_data in _from_80_to_75:
                from_80_to_75_item = EapRssiChannelVO.from_dict(from_80_to_75_item_data)

                from_80_to_75.append(from_80_to_75_item)

        _from_75_to_70 = d.pop("from75To70", UNSET)
        from_75_to_70: list[EapRssiChannelVO] | Unset = UNSET
        if _from_75_to_70 is not UNSET:
            from_75_to_70 = []
            for from_75_to_70_item_data in _from_75_to_70:
                from_75_to_70_item = EapRssiChannelVO.from_dict(from_75_to_70_item_data)

                from_75_to_70.append(from_75_to_70_item)

        _from_70_to_65 = d.pop("from70To65", UNSET)
        from_70_to_65: list[EapRssiChannelVO] | Unset = UNSET
        if _from_70_to_65 is not UNSET:
            from_70_to_65 = []
            for from_70_to_65_item_data in _from_70_to_65:
                from_70_to_65_item = EapRssiChannelVO.from_dict(from_70_to_65_item_data)

                from_70_to_65.append(from_70_to_65_item)

        _from_65_to_60 = d.pop("from65To60", UNSET)
        from_65_to_60: list[EapRssiChannelVO] | Unset = UNSET
        if _from_65_to_60 is not UNSET:
            from_65_to_60 = []
            for from_65_to_60_item_data in _from_65_to_60:
                from_65_to_60_item = EapRssiChannelVO.from_dict(from_65_to_60_item_data)

                from_65_to_60.append(from_65_to_60_item)

        _from_60_to_55 = d.pop("from60To55", UNSET)
        from_60_to_55: list[EapRssiChannelVO] | Unset = UNSET
        if _from_60_to_55 is not UNSET:
            from_60_to_55 = []
            for from_60_to_55_item_data in _from_60_to_55:
                from_60_to_55_item = EapRssiChannelVO.from_dict(from_60_to_55_item_data)

                from_60_to_55.append(from_60_to_55_item)

        _from_55_to_50 = d.pop("from55To50", UNSET)
        from_55_to_50: list[EapRssiChannelVO] | Unset = UNSET
        if _from_55_to_50 is not UNSET:
            from_55_to_50 = []
            for from_55_to_50_item_data in _from_55_to_50:
                from_55_to_50_item = EapRssiChannelVO.from_dict(from_55_to_50_item_data)

                from_55_to_50.append(from_55_to_50_item)

        _from_50_to_45 = d.pop("from50To45", UNSET)
        from_50_to_45: list[EapRssiChannelVO] | Unset = UNSET
        if _from_50_to_45 is not UNSET:
            from_50_to_45 = []
            for from_50_to_45_item_data in _from_50_to_45:
                from_50_to_45_item = EapRssiChannelVO.from_dict(from_50_to_45_item_data)

                from_50_to_45.append(from_50_to_45_item)

        _from_45_to_40 = d.pop("from45To40", UNSET)
        from_45_to_40: list[EapRssiChannelVO] | Unset = UNSET
        if _from_45_to_40 is not UNSET:
            from_45_to_40 = []
            for from_45_to_40_item_data in _from_45_to_40:
                from_45_to_40_item = EapRssiChannelVO.from_dict(from_45_to_40_item_data)

                from_45_to_40.append(from_45_to_40_item)

        _from_40_to_35 = d.pop("from40To35", UNSET)
        from_40_to_35: list[EapRssiChannelVO] | Unset = UNSET
        if _from_40_to_35 is not UNSET:
            from_40_to_35 = []
            for from_40_to_35_item_data in _from_40_to_35:
                from_40_to_35_item = EapRssiChannelVO.from_dict(from_40_to_35_item_data)

                from_40_to_35.append(from_40_to_35_item)

        _from_35_to_30 = d.pop("from35To30", UNSET)
        from_35_to_30: list[EapRssiChannelVO] | Unset = UNSET
        if _from_35_to_30 is not UNSET:
            from_35_to_30 = []
            for from_35_to_30_item_data in _from_35_to_30:
                from_35_to_30_item = EapRssiChannelVO.from_dict(from_35_to_30_item_data)

                from_35_to_30.append(from_35_to_30_item)

        _more_than_30 = d.pop("moreThan30", UNSET)
        more_than_30: list[EapRssiChannelVO] | Unset = UNSET
        if _more_than_30 is not UNSET:
            more_than_30 = []
            for more_than_30_item_data in _more_than_30:
                more_than_30_item = EapRssiChannelVO.from_dict(more_than_30_item_data)

                more_than_30.append(more_than_30_item)

        eap_rssi_channel_distribution_vo = cls(
            exist_ap=exist_ap,
            exist_ap_client=exist_ap_client,
            less_than_90=less_than_90,
            from_90_to_85=from_90_to_85,
            from_85_to_80=from_85_to_80,
            from_80_to_75=from_80_to_75,
            from_75_to_70=from_75_to_70,
            from_70_to_65=from_70_to_65,
            from_65_to_60=from_65_to_60,
            from_60_to_55=from_60_to_55,
            from_55_to_50=from_55_to_50,
            from_50_to_45=from_50_to_45,
            from_45_to_40=from_45_to_40,
            from_40_to_35=from_40_to_35,
            from_35_to_30=from_35_to_30,
            more_than_30=more_than_30,
        )

        eap_rssi_channel_distribution_vo.additional_properties = d
        return eap_rssi_channel_distribution_vo

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
