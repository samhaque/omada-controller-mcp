from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_load_balance_vo import ApLoadBalanceVO
    from ..models.ap_qos_vo import ApQosVO
    from ..models.ap_rssi_threshold_vo import ApRssiThresholdVO


T = TypeVar("T", bound="OsgConfigWirelessAdvancedOpenApiVO")


@_attrs_define
class OsgConfigWirelessAdvancedOpenApiVO:
    """
    Attributes:
        lb_setting_2_g (ApLoadBalanceVO | Unset):
        lb_setting_5_g (ApLoadBalanceVO | Unset):
        lb_setting_5_g_1 (ApLoadBalanceVO | Unset):
        lb_setting_5_g_2 (ApLoadBalanceVO | Unset):
        lb_setting_6_g (ApLoadBalanceVO | Unset):
        rssi_setting_2_g (ApRssiThresholdVO | Unset):
        rssi_setting_5_g (ApRssiThresholdVO | Unset):
        rssi_setting_5_g_1 (ApRssiThresholdVO | Unset):
        rssi_setting_5_g_2 (ApRssiThresholdVO | Unset):
        rssi_setting_6_g (ApRssiThresholdVO | Unset):
        qos_setting_2_g (ApQosVO | Unset):
        qos_setting_5_g (ApQosVO | Unset):
        qos_setting_5_g_1 (ApQosVO | Unset):
        qos_setting_5_g_2 (ApQosVO | Unset):
        qos_setting_6_g (ApQosVO | Unset):
        ofdma_enable_2_g (bool | Unset):
        ofdma_enable_5_g (bool | Unset):
        ofdma_enable_5_g_1 (bool | Unset):
        ofdma_enable_5_g_2 (bool | Unset):
        ofdma_enable_6_g (bool | Unset):
    """

    lb_setting_2_g: ApLoadBalanceVO | Unset = UNSET
    lb_setting_5_g: ApLoadBalanceVO | Unset = UNSET
    lb_setting_5_g_1: ApLoadBalanceVO | Unset = UNSET
    lb_setting_5_g_2: ApLoadBalanceVO | Unset = UNSET
    lb_setting_6_g: ApLoadBalanceVO | Unset = UNSET
    rssi_setting_2_g: ApRssiThresholdVO | Unset = UNSET
    rssi_setting_5_g: ApRssiThresholdVO | Unset = UNSET
    rssi_setting_5_g_1: ApRssiThresholdVO | Unset = UNSET
    rssi_setting_5_g_2: ApRssiThresholdVO | Unset = UNSET
    rssi_setting_6_g: ApRssiThresholdVO | Unset = UNSET
    qos_setting_2_g: ApQosVO | Unset = UNSET
    qos_setting_5_g: ApQosVO | Unset = UNSET
    qos_setting_5_g_1: ApQosVO | Unset = UNSET
    qos_setting_5_g_2: ApQosVO | Unset = UNSET
    qos_setting_6_g: ApQosVO | Unset = UNSET
    ofdma_enable_2_g: bool | Unset = UNSET
    ofdma_enable_5_g: bool | Unset = UNSET
    ofdma_enable_5_g_1: bool | Unset = UNSET
    ofdma_enable_5_g_2: bool | Unset = UNSET
    ofdma_enable_6_g: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lb_setting_2_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lb_setting_2_g, Unset):
            lb_setting_2_g = self.lb_setting_2_g.to_dict()

        lb_setting_5_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lb_setting_5_g, Unset):
            lb_setting_5_g = self.lb_setting_5_g.to_dict()

        lb_setting_5_g_1: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lb_setting_5_g_1, Unset):
            lb_setting_5_g_1 = self.lb_setting_5_g_1.to_dict()

        lb_setting_5_g_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lb_setting_5_g_2, Unset):
            lb_setting_5_g_2 = self.lb_setting_5_g_2.to_dict()

        lb_setting_6_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lb_setting_6_g, Unset):
            lb_setting_6_g = self.lb_setting_6_g.to_dict()

        rssi_setting_2_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rssi_setting_2_g, Unset):
            rssi_setting_2_g = self.rssi_setting_2_g.to_dict()

        rssi_setting_5_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rssi_setting_5_g, Unset):
            rssi_setting_5_g = self.rssi_setting_5_g.to_dict()

        rssi_setting_5_g_1: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rssi_setting_5_g_1, Unset):
            rssi_setting_5_g_1 = self.rssi_setting_5_g_1.to_dict()

        rssi_setting_5_g_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rssi_setting_5_g_2, Unset):
            rssi_setting_5_g_2 = self.rssi_setting_5_g_2.to_dict()

        rssi_setting_6_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rssi_setting_6_g, Unset):
            rssi_setting_6_g = self.rssi_setting_6_g.to_dict()

        qos_setting_2_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qos_setting_2_g, Unset):
            qos_setting_2_g = self.qos_setting_2_g.to_dict()

        qos_setting_5_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qos_setting_5_g, Unset):
            qos_setting_5_g = self.qos_setting_5_g.to_dict()

        qos_setting_5_g_1: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qos_setting_5_g_1, Unset):
            qos_setting_5_g_1 = self.qos_setting_5_g_1.to_dict()

        qos_setting_5_g_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qos_setting_5_g_2, Unset):
            qos_setting_5_g_2 = self.qos_setting_5_g_2.to_dict()

        qos_setting_6_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qos_setting_6_g, Unset):
            qos_setting_6_g = self.qos_setting_6_g.to_dict()

        ofdma_enable_2_g = self.ofdma_enable_2_g

        ofdma_enable_5_g = self.ofdma_enable_5_g

        ofdma_enable_5_g_1 = self.ofdma_enable_5_g_1

        ofdma_enable_5_g_2 = self.ofdma_enable_5_g_2

        ofdma_enable_6_g = self.ofdma_enable_6_g

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lb_setting_2_g is not UNSET:
            field_dict["lbSetting2g"] = lb_setting_2_g
        if lb_setting_5_g is not UNSET:
            field_dict["lbSetting5g"] = lb_setting_5_g
        if lb_setting_5_g_1 is not UNSET:
            field_dict["lbSetting5g1"] = lb_setting_5_g_1
        if lb_setting_5_g_2 is not UNSET:
            field_dict["lbSetting5g2"] = lb_setting_5_g_2
        if lb_setting_6_g is not UNSET:
            field_dict["lbSetting6g"] = lb_setting_6_g
        if rssi_setting_2_g is not UNSET:
            field_dict["rssiSetting2g"] = rssi_setting_2_g
        if rssi_setting_5_g is not UNSET:
            field_dict["rssiSetting5g"] = rssi_setting_5_g
        if rssi_setting_5_g_1 is not UNSET:
            field_dict["rssiSetting5g1"] = rssi_setting_5_g_1
        if rssi_setting_5_g_2 is not UNSET:
            field_dict["rssiSetting5g2"] = rssi_setting_5_g_2
        if rssi_setting_6_g is not UNSET:
            field_dict["rssiSetting6g"] = rssi_setting_6_g
        if qos_setting_2_g is not UNSET:
            field_dict["qosSetting2g"] = qos_setting_2_g
        if qos_setting_5_g is not UNSET:
            field_dict["qosSetting5g"] = qos_setting_5_g
        if qos_setting_5_g_1 is not UNSET:
            field_dict["qosSetting5g1"] = qos_setting_5_g_1
        if qos_setting_5_g_2 is not UNSET:
            field_dict["qosSetting5g2"] = qos_setting_5_g_2
        if qos_setting_6_g is not UNSET:
            field_dict["qosSetting6g"] = qos_setting_6_g
        if ofdma_enable_2_g is not UNSET:
            field_dict["ofdmaEnable2g"] = ofdma_enable_2_g
        if ofdma_enable_5_g is not UNSET:
            field_dict["ofdmaEnable5g"] = ofdma_enable_5_g
        if ofdma_enable_5_g_1 is not UNSET:
            field_dict["ofdmaEnable5g1"] = ofdma_enable_5_g_1
        if ofdma_enable_5_g_2 is not UNSET:
            field_dict["ofdmaEnable5g2"] = ofdma_enable_5_g_2
        if ofdma_enable_6_g is not UNSET:
            field_dict["ofdmaEnable6g"] = ofdma_enable_6_g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_load_balance_vo import ApLoadBalanceVO
        from ..models.ap_qos_vo import ApQosVO
        from ..models.ap_rssi_threshold_vo import ApRssiThresholdVO

        d = dict(src_dict)
        _lb_setting_2_g = d.pop("lbSetting2g", UNSET)
        lb_setting_2_g: ApLoadBalanceVO | Unset
        if isinstance(_lb_setting_2_g, Unset):
            lb_setting_2_g = UNSET
        else:
            lb_setting_2_g = ApLoadBalanceVO.from_dict(_lb_setting_2_g)

        _lb_setting_5_g = d.pop("lbSetting5g", UNSET)
        lb_setting_5_g: ApLoadBalanceVO | Unset
        if isinstance(_lb_setting_5_g, Unset):
            lb_setting_5_g = UNSET
        else:
            lb_setting_5_g = ApLoadBalanceVO.from_dict(_lb_setting_5_g)

        _lb_setting_5_g_1 = d.pop("lbSetting5g1", UNSET)
        lb_setting_5_g_1: ApLoadBalanceVO | Unset
        if isinstance(_lb_setting_5_g_1, Unset):
            lb_setting_5_g_1 = UNSET
        else:
            lb_setting_5_g_1 = ApLoadBalanceVO.from_dict(_lb_setting_5_g_1)

        _lb_setting_5_g_2 = d.pop("lbSetting5g2", UNSET)
        lb_setting_5_g_2: ApLoadBalanceVO | Unset
        if isinstance(_lb_setting_5_g_2, Unset):
            lb_setting_5_g_2 = UNSET
        else:
            lb_setting_5_g_2 = ApLoadBalanceVO.from_dict(_lb_setting_5_g_2)

        _lb_setting_6_g = d.pop("lbSetting6g", UNSET)
        lb_setting_6_g: ApLoadBalanceVO | Unset
        if isinstance(_lb_setting_6_g, Unset):
            lb_setting_6_g = UNSET
        else:
            lb_setting_6_g = ApLoadBalanceVO.from_dict(_lb_setting_6_g)

        _rssi_setting_2_g = d.pop("rssiSetting2g", UNSET)
        rssi_setting_2_g: ApRssiThresholdVO | Unset
        if isinstance(_rssi_setting_2_g, Unset):
            rssi_setting_2_g = UNSET
        else:
            rssi_setting_2_g = ApRssiThresholdVO.from_dict(_rssi_setting_2_g)

        _rssi_setting_5_g = d.pop("rssiSetting5g", UNSET)
        rssi_setting_5_g: ApRssiThresholdVO | Unset
        if isinstance(_rssi_setting_5_g, Unset):
            rssi_setting_5_g = UNSET
        else:
            rssi_setting_5_g = ApRssiThresholdVO.from_dict(_rssi_setting_5_g)

        _rssi_setting_5_g_1 = d.pop("rssiSetting5g1", UNSET)
        rssi_setting_5_g_1: ApRssiThresholdVO | Unset
        if isinstance(_rssi_setting_5_g_1, Unset):
            rssi_setting_5_g_1 = UNSET
        else:
            rssi_setting_5_g_1 = ApRssiThresholdVO.from_dict(_rssi_setting_5_g_1)

        _rssi_setting_5_g_2 = d.pop("rssiSetting5g2", UNSET)
        rssi_setting_5_g_2: ApRssiThresholdVO | Unset
        if isinstance(_rssi_setting_5_g_2, Unset):
            rssi_setting_5_g_2 = UNSET
        else:
            rssi_setting_5_g_2 = ApRssiThresholdVO.from_dict(_rssi_setting_5_g_2)

        _rssi_setting_6_g = d.pop("rssiSetting6g", UNSET)
        rssi_setting_6_g: ApRssiThresholdVO | Unset
        if isinstance(_rssi_setting_6_g, Unset):
            rssi_setting_6_g = UNSET
        else:
            rssi_setting_6_g = ApRssiThresholdVO.from_dict(_rssi_setting_6_g)

        _qos_setting_2_g = d.pop("qosSetting2g", UNSET)
        qos_setting_2_g: ApQosVO | Unset
        if isinstance(_qos_setting_2_g, Unset):
            qos_setting_2_g = UNSET
        else:
            qos_setting_2_g = ApQosVO.from_dict(_qos_setting_2_g)

        _qos_setting_5_g = d.pop("qosSetting5g", UNSET)
        qos_setting_5_g: ApQosVO | Unset
        if isinstance(_qos_setting_5_g, Unset):
            qos_setting_5_g = UNSET
        else:
            qos_setting_5_g = ApQosVO.from_dict(_qos_setting_5_g)

        _qos_setting_5_g_1 = d.pop("qosSetting5g1", UNSET)
        qos_setting_5_g_1: ApQosVO | Unset
        if isinstance(_qos_setting_5_g_1, Unset):
            qos_setting_5_g_1 = UNSET
        else:
            qos_setting_5_g_1 = ApQosVO.from_dict(_qos_setting_5_g_1)

        _qos_setting_5_g_2 = d.pop("qosSetting5g2", UNSET)
        qos_setting_5_g_2: ApQosVO | Unset
        if isinstance(_qos_setting_5_g_2, Unset):
            qos_setting_5_g_2 = UNSET
        else:
            qos_setting_5_g_2 = ApQosVO.from_dict(_qos_setting_5_g_2)

        _qos_setting_6_g = d.pop("qosSetting6g", UNSET)
        qos_setting_6_g: ApQosVO | Unset
        if isinstance(_qos_setting_6_g, Unset):
            qos_setting_6_g = UNSET
        else:
            qos_setting_6_g = ApQosVO.from_dict(_qos_setting_6_g)

        ofdma_enable_2_g = d.pop("ofdmaEnable2g", UNSET)

        ofdma_enable_5_g = d.pop("ofdmaEnable5g", UNSET)

        ofdma_enable_5_g_1 = d.pop("ofdmaEnable5g1", UNSET)

        ofdma_enable_5_g_2 = d.pop("ofdmaEnable5g2", UNSET)

        ofdma_enable_6_g = d.pop("ofdmaEnable6g", UNSET)

        osg_config_wireless_advanced_open_api_vo = cls(
            lb_setting_2_g=lb_setting_2_g,
            lb_setting_5_g=lb_setting_5_g,
            lb_setting_5_g_1=lb_setting_5_g_1,
            lb_setting_5_g_2=lb_setting_5_g_2,
            lb_setting_6_g=lb_setting_6_g,
            rssi_setting_2_g=rssi_setting_2_g,
            rssi_setting_5_g=rssi_setting_5_g,
            rssi_setting_5_g_1=rssi_setting_5_g_1,
            rssi_setting_5_g_2=rssi_setting_5_g_2,
            rssi_setting_6_g=rssi_setting_6_g,
            qos_setting_2_g=qos_setting_2_g,
            qos_setting_5_g=qos_setting_5_g,
            qos_setting_5_g_1=qos_setting_5_g_1,
            qos_setting_5_g_2=qos_setting_5_g_2,
            qos_setting_6_g=qos_setting_6_g,
            ofdma_enable_2_g=ofdma_enable_2_g,
            ofdma_enable_5_g=ofdma_enable_5_g,
            ofdma_enable_5_g_1=ofdma_enable_5_g_1,
            ofdma_enable_5_g_2=ofdma_enable_5_g_2,
            ofdma_enable_6_g=ofdma_enable_6_g,
        )

        osg_config_wireless_advanced_open_api_vo.additional_properties = d
        return osg_config_wireless_advanced_open_api_vo

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
