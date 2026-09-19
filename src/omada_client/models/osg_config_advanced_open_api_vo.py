from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_load_balance_open_api_vo import ApLoadBalanceOpenApiVO
    from ..models.ap_qos_open_api_vo import ApQosOpenApiVO
    from ..models.ap_rssi_threshold_open_api_vo import ApRssiThresholdOpenApiVO
    from ..models.osg_port_poe_open_api_vo import OsgPortPoeOpenApiVO


T = TypeVar("T", bound="OsgConfigAdvancedOpenApiVO")


@_attrs_define
class OsgConfigAdvancedOpenApiVO:
    """
    Attributes:
        hw_offload_enable (bool | Unset): Hardware Offload enabled or not.
        lldp_enable (bool | Unset): LLDP enabled or not. Deprecated, filed lldpSetting is recommended
        lldp_setting (int | Unset): LLDP setting. 0: Off, 1: On, 2: Follow site.
        poe_settings (list[OsgPortPoeOpenApiVO] | Unset): Port Poe setting list.
        echo_server (str | Unset): Echo Server should be a domain name or IP address.
        lb_setting_2_g (ApLoadBalanceOpenApiVO | Unset): Load Balance setting of 6 GHz.
        lb_setting_5_g (ApLoadBalanceOpenApiVO | Unset): Load Balance setting of 6 GHz.
        lb_setting_5_g_1 (ApLoadBalanceOpenApiVO | Unset): Load Balance setting of 6 GHz.
        lb_setting_5_g_2 (ApLoadBalanceOpenApiVO | Unset): Load Balance setting of 6 GHz.
        lb_setting_6_g (ApLoadBalanceOpenApiVO | Unset): Load Balance setting of 6 GHz.
        rssi_setting_2_g (ApRssiThresholdOpenApiVO | Unset): Rssi Threshold setting of 6 GHz.
        rssi_setting_5_g (ApRssiThresholdOpenApiVO | Unset): Rssi Threshold setting of 6 GHz.
        rssi_setting_5_g_1 (ApRssiThresholdOpenApiVO | Unset): Rssi Threshold setting of 6 GHz.
        rssi_setting_5_g_2 (ApRssiThresholdOpenApiVO | Unset): Rssi Threshold setting of 6 GHz.
        rssi_setting_6_g (ApRssiThresholdOpenApiVO | Unset): Rssi Threshold setting of 6 GHz.
        qos_setting_2_g (ApQosOpenApiVO | Unset): Qos setting of 6 GHz.
        qos_setting_5_g (ApQosOpenApiVO | Unset): Qos setting of 6 GHz.
        qos_setting_5_g_1 (ApQosOpenApiVO | Unset): Qos setting of 6 GHz.
        qos_setting_5_g_2 (ApQosOpenApiVO | Unset): Qos setting of 6 GHz.
        qos_setting_6_g (ApQosOpenApiVO | Unset): Qos setting of 6 GHz.
        ofdma_enable_2_g (bool | Unset): Enable or disable OFDMA of 2.4 GHz.
        ofdma_enable_5_g (bool | Unset): Enable or disable OFDMA of 5 GHz.
        ofdma_enable_5_g_1 (bool | Unset): Enable or disable OFDMA of 5 GHz-1.
        ofdma_enable_5_g_2 (bool | Unset): Enable or disable OFDMA of 5 GHz-2.
        ofdma_enable_6_g (bool | Unset): Enable or disable OFDMA of 6 GHz.
    """

    hw_offload_enable: bool | Unset = UNSET
    lldp_enable: bool | Unset = UNSET
    lldp_setting: int | Unset = UNSET
    poe_settings: list[OsgPortPoeOpenApiVO] | Unset = UNSET
    echo_server: str | Unset = UNSET
    lb_setting_2_g: ApLoadBalanceOpenApiVO | Unset = UNSET
    lb_setting_5_g: ApLoadBalanceOpenApiVO | Unset = UNSET
    lb_setting_5_g_1: ApLoadBalanceOpenApiVO | Unset = UNSET
    lb_setting_5_g_2: ApLoadBalanceOpenApiVO | Unset = UNSET
    lb_setting_6_g: ApLoadBalanceOpenApiVO | Unset = UNSET
    rssi_setting_2_g: ApRssiThresholdOpenApiVO | Unset = UNSET
    rssi_setting_5_g: ApRssiThresholdOpenApiVO | Unset = UNSET
    rssi_setting_5_g_1: ApRssiThresholdOpenApiVO | Unset = UNSET
    rssi_setting_5_g_2: ApRssiThresholdOpenApiVO | Unset = UNSET
    rssi_setting_6_g: ApRssiThresholdOpenApiVO | Unset = UNSET
    qos_setting_2_g: ApQosOpenApiVO | Unset = UNSET
    qos_setting_5_g: ApQosOpenApiVO | Unset = UNSET
    qos_setting_5_g_1: ApQosOpenApiVO | Unset = UNSET
    qos_setting_5_g_2: ApQosOpenApiVO | Unset = UNSET
    qos_setting_6_g: ApQosOpenApiVO | Unset = UNSET
    ofdma_enable_2_g: bool | Unset = UNSET
    ofdma_enable_5_g: bool | Unset = UNSET
    ofdma_enable_5_g_1: bool | Unset = UNSET
    ofdma_enable_5_g_2: bool | Unset = UNSET
    ofdma_enable_6_g: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hw_offload_enable = self.hw_offload_enable

        lldp_enable = self.lldp_enable

        lldp_setting = self.lldp_setting

        poe_settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.poe_settings, Unset):
            poe_settings = []
            for poe_settings_item_data in self.poe_settings:
                poe_settings_item = poe_settings_item_data.to_dict()
                poe_settings.append(poe_settings_item)

        echo_server = self.echo_server

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
        if hw_offload_enable is not UNSET:
            field_dict["hwOffloadEnable"] = hw_offload_enable
        if lldp_enable is not UNSET:
            field_dict["lldpEnable"] = lldp_enable
        if lldp_setting is not UNSET:
            field_dict["lldpSetting"] = lldp_setting
        if poe_settings is not UNSET:
            field_dict["poeSettings"] = poe_settings
        if echo_server is not UNSET:
            field_dict["echoServer"] = echo_server
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
        from ..models.ap_load_balance_open_api_vo import (
            ApLoadBalanceOpenApiVO,
        )
        from ..models.ap_qos_open_api_vo import ApQosOpenApiVO
        from ..models.ap_rssi_threshold_open_api_vo import (
            ApRssiThresholdOpenApiVO,
        )
        from ..models.osg_port_poe_open_api_vo import (
            OsgPortPoeOpenApiVO,
        )

        d = dict(src_dict)
        hw_offload_enable = d.pop("hwOffloadEnable", UNSET)

        lldp_enable = d.pop("lldpEnable", UNSET)

        lldp_setting = d.pop("lldpSetting", UNSET)

        _poe_settings = d.pop("poeSettings", UNSET)
        poe_settings: list[OsgPortPoeOpenApiVO] | Unset = UNSET
        if _poe_settings is not UNSET:
            poe_settings = []
            for poe_settings_item_data in _poe_settings:
                poe_settings_item = OsgPortPoeOpenApiVO.from_dict(
                    poe_settings_item_data
                )

                poe_settings.append(poe_settings_item)

        echo_server = d.pop("echoServer", UNSET)

        _lb_setting_2_g = d.pop("lbSetting2g", UNSET)
        lb_setting_2_g: ApLoadBalanceOpenApiVO | Unset
        if isinstance(_lb_setting_2_g, Unset):
            lb_setting_2_g = UNSET
        else:
            lb_setting_2_g = ApLoadBalanceOpenApiVO.from_dict(_lb_setting_2_g)

        _lb_setting_5_g = d.pop("lbSetting5g", UNSET)
        lb_setting_5_g: ApLoadBalanceOpenApiVO | Unset
        if isinstance(_lb_setting_5_g, Unset):
            lb_setting_5_g = UNSET
        else:
            lb_setting_5_g = ApLoadBalanceOpenApiVO.from_dict(_lb_setting_5_g)

        _lb_setting_5_g_1 = d.pop("lbSetting5g1", UNSET)
        lb_setting_5_g_1: ApLoadBalanceOpenApiVO | Unset
        if isinstance(_lb_setting_5_g_1, Unset):
            lb_setting_5_g_1 = UNSET
        else:
            lb_setting_5_g_1 = ApLoadBalanceOpenApiVO.from_dict(_lb_setting_5_g_1)

        _lb_setting_5_g_2 = d.pop("lbSetting5g2", UNSET)
        lb_setting_5_g_2: ApLoadBalanceOpenApiVO | Unset
        if isinstance(_lb_setting_5_g_2, Unset):
            lb_setting_5_g_2 = UNSET
        else:
            lb_setting_5_g_2 = ApLoadBalanceOpenApiVO.from_dict(_lb_setting_5_g_2)

        _lb_setting_6_g = d.pop("lbSetting6g", UNSET)
        lb_setting_6_g: ApLoadBalanceOpenApiVO | Unset
        if isinstance(_lb_setting_6_g, Unset):
            lb_setting_6_g = UNSET
        else:
            lb_setting_6_g = ApLoadBalanceOpenApiVO.from_dict(_lb_setting_6_g)

        _rssi_setting_2_g = d.pop("rssiSetting2g", UNSET)
        rssi_setting_2_g: ApRssiThresholdOpenApiVO | Unset
        if isinstance(_rssi_setting_2_g, Unset):
            rssi_setting_2_g = UNSET
        else:
            rssi_setting_2_g = ApRssiThresholdOpenApiVO.from_dict(_rssi_setting_2_g)

        _rssi_setting_5_g = d.pop("rssiSetting5g", UNSET)
        rssi_setting_5_g: ApRssiThresholdOpenApiVO | Unset
        if isinstance(_rssi_setting_5_g, Unset):
            rssi_setting_5_g = UNSET
        else:
            rssi_setting_5_g = ApRssiThresholdOpenApiVO.from_dict(_rssi_setting_5_g)

        _rssi_setting_5_g_1 = d.pop("rssiSetting5g1", UNSET)
        rssi_setting_5_g_1: ApRssiThresholdOpenApiVO | Unset
        if isinstance(_rssi_setting_5_g_1, Unset):
            rssi_setting_5_g_1 = UNSET
        else:
            rssi_setting_5_g_1 = ApRssiThresholdOpenApiVO.from_dict(_rssi_setting_5_g_1)

        _rssi_setting_5_g_2 = d.pop("rssiSetting5g2", UNSET)
        rssi_setting_5_g_2: ApRssiThresholdOpenApiVO | Unset
        if isinstance(_rssi_setting_5_g_2, Unset):
            rssi_setting_5_g_2 = UNSET
        else:
            rssi_setting_5_g_2 = ApRssiThresholdOpenApiVO.from_dict(_rssi_setting_5_g_2)

        _rssi_setting_6_g = d.pop("rssiSetting6g", UNSET)
        rssi_setting_6_g: ApRssiThresholdOpenApiVO | Unset
        if isinstance(_rssi_setting_6_g, Unset):
            rssi_setting_6_g = UNSET
        else:
            rssi_setting_6_g = ApRssiThresholdOpenApiVO.from_dict(_rssi_setting_6_g)

        _qos_setting_2_g = d.pop("qosSetting2g", UNSET)
        qos_setting_2_g: ApQosOpenApiVO | Unset
        if isinstance(_qos_setting_2_g, Unset):
            qos_setting_2_g = UNSET
        else:
            qos_setting_2_g = ApQosOpenApiVO.from_dict(_qos_setting_2_g)

        _qos_setting_5_g = d.pop("qosSetting5g", UNSET)
        qos_setting_5_g: ApQosOpenApiVO | Unset
        if isinstance(_qos_setting_5_g, Unset):
            qos_setting_5_g = UNSET
        else:
            qos_setting_5_g = ApQosOpenApiVO.from_dict(_qos_setting_5_g)

        _qos_setting_5_g_1 = d.pop("qosSetting5g1", UNSET)
        qos_setting_5_g_1: ApQosOpenApiVO | Unset
        if isinstance(_qos_setting_5_g_1, Unset):
            qos_setting_5_g_1 = UNSET
        else:
            qos_setting_5_g_1 = ApQosOpenApiVO.from_dict(_qos_setting_5_g_1)

        _qos_setting_5_g_2 = d.pop("qosSetting5g2", UNSET)
        qos_setting_5_g_2: ApQosOpenApiVO | Unset
        if isinstance(_qos_setting_5_g_2, Unset):
            qos_setting_5_g_2 = UNSET
        else:
            qos_setting_5_g_2 = ApQosOpenApiVO.from_dict(_qos_setting_5_g_2)

        _qos_setting_6_g = d.pop("qosSetting6g", UNSET)
        qos_setting_6_g: ApQosOpenApiVO | Unset
        if isinstance(_qos_setting_6_g, Unset):
            qos_setting_6_g = UNSET
        else:
            qos_setting_6_g = ApQosOpenApiVO.from_dict(_qos_setting_6_g)

        ofdma_enable_2_g = d.pop("ofdmaEnable2g", UNSET)

        ofdma_enable_5_g = d.pop("ofdmaEnable5g", UNSET)

        ofdma_enable_5_g_1 = d.pop("ofdmaEnable5g1", UNSET)

        ofdma_enable_5_g_2 = d.pop("ofdmaEnable5g2", UNSET)

        ofdma_enable_6_g = d.pop("ofdmaEnable6g", UNSET)

        osg_config_advanced_open_api_vo = cls(
            hw_offload_enable=hw_offload_enable,
            lldp_enable=lldp_enable,
            lldp_setting=lldp_setting,
            poe_settings=poe_settings,
            echo_server=echo_server,
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

        osg_config_advanced_open_api_vo.additional_properties = d
        return osg_config_advanced_open_api_vo

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
