from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSsidRateControlOpenApiVO")


@_attrs_define
class UpdateSsidRateControlOpenApiVO:
    """
    Attributes:
        rate_2_g_ctrl_enable (bool): Whether to enable 2.4GHz Data Rate Control
        rate_5_g_ctrl_enable (bool): Whether to enable 5GHz Data Rate Control.
        lower_density_2_g (float | Unset): 2.4GHz Data Rate Control lower density value(Unit: Mbps); It should be a
            value as follows: [1, 2, 5.5, 6, 9, 11, 12, 18, 24, 36, 48, 54].
        higher_density_2_g (int | Unset): 2.4GHz Data Rate Control higher density value(Unit: Mbps); It should be a
            value as follows: [54].
        cck_rates_disable (bool | Unset): Whether to disable 2G CCK Rates. If this field is true, Parameter
            [lowerDensity2g] can not enter the following values: [1, 2, 5.5, 11].
        client_rates_require_2_g (bool | Unset): Whether to require clients to use rates at or above the specified value
            of 2.4GHz Data Rate Control.
        send_beacons_2_g (bool | Unset): Whether to enable send beacons at 1Mbps of 2.4GHz Data Rate Control.
        lower_density_5_g (int | Unset): 5GHz Data Rate Control lower density value(Unit: Mbps); It should be a value as
            follows: [6, 9, 12, 18, 24, 36, 48, 54].
        higher_density_5_g (int | Unset): 5GHz Data Rate Control higher density value(Unit: Mbps); It should be a value
            as follows: [54].
        client_rates_require_5_g (bool | Unset): Whether to require clients to use rates at or above the specified value
            of 5GHz Data Rate Control.
        send_beacons_5_g (bool | Unset): Whether to enable send beacons at 6Mbps of 5GHz Data Rate Control.
        rate_6_g_ctrl_enable (bool | Unset): Whether to enable 6GHz Data Rate Control. Note: This field will no longer
            be supported since Omada Controller V5.14.30.
        lower_density_6_g (int | Unset): 6GHz Data Rate Control lower density value(Unit: Mbps); It should be a value as
            follows: [6, 9, 12, 18, 24, 36, 48, 54].Note: This field will no longer be supported since Omada Controller
            V5.14.30.
        higher_density_6_g (int | Unset): 6GHz Data Rate Control higher density value(Unit: Mbps); It should be a value
            as follows: [54].Note: This field will no longer be supported since Omada Controller V5.14.30.
        client_rates_require_6_g (bool | Unset): Whether to require clients to use rates at or above the specified value
            of 6GHz Data Rate Control. Note: This field will no longer be supported since Omada Controller V5.14.30.
        send_beacons_6_g (bool | Unset): Whether to enable send beacons at 6Mbps of 6GHz Data Rate Control. Note: This
            field will no longer be supported since Omada Controller V5.14.30.
        manage_rate_control_2_g_enable (bool | Unset): Whether to enable 2GHz Manage Rate Control.
        manage_rate_control_2_g (float | Unset): 2.4GHz Manage Rate Control lower density value(Unit: Mbps); It should
            be a value as follows: [1, 2, 5.5, 6, 9, 11, 12, 18, 24, 36, 48, 54]. The higher density value is fixed at 54.
        manage_rate_control_5_g_enable (bool | Unset): Whether to enable 5GHz Manage Rate Control.
        manage_rate_control_5_g (int | Unset): 5GHz Manage Rate Control lower density value(Unit: Mbps); It should be a
            value as follows: [6, 9, 12, 18, 24, 36, 48, 54]. The higher density value is fixed at 54.
    """

    rate_2_g_ctrl_enable: bool
    rate_5_g_ctrl_enable: bool
    lower_density_2_g: float | Unset = UNSET
    higher_density_2_g: int | Unset = UNSET
    cck_rates_disable: bool | Unset = UNSET
    client_rates_require_2_g: bool | Unset = UNSET
    send_beacons_2_g: bool | Unset = UNSET
    lower_density_5_g: int | Unset = UNSET
    higher_density_5_g: int | Unset = UNSET
    client_rates_require_5_g: bool | Unset = UNSET
    send_beacons_5_g: bool | Unset = UNSET
    rate_6_g_ctrl_enable: bool | Unset = UNSET
    lower_density_6_g: int | Unset = UNSET
    higher_density_6_g: int | Unset = UNSET
    client_rates_require_6_g: bool | Unset = UNSET
    send_beacons_6_g: bool | Unset = UNSET
    manage_rate_control_2_g_enable: bool | Unset = UNSET
    manage_rate_control_2_g: float | Unset = UNSET
    manage_rate_control_5_g_enable: bool | Unset = UNSET
    manage_rate_control_5_g: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rate_2_g_ctrl_enable = self.rate_2_g_ctrl_enable

        rate_5_g_ctrl_enable = self.rate_5_g_ctrl_enable

        lower_density_2_g = self.lower_density_2_g

        higher_density_2_g = self.higher_density_2_g

        cck_rates_disable = self.cck_rates_disable

        client_rates_require_2_g = self.client_rates_require_2_g

        send_beacons_2_g = self.send_beacons_2_g

        lower_density_5_g = self.lower_density_5_g

        higher_density_5_g = self.higher_density_5_g

        client_rates_require_5_g = self.client_rates_require_5_g

        send_beacons_5_g = self.send_beacons_5_g

        rate_6_g_ctrl_enable = self.rate_6_g_ctrl_enable

        lower_density_6_g = self.lower_density_6_g

        higher_density_6_g = self.higher_density_6_g

        client_rates_require_6_g = self.client_rates_require_6_g

        send_beacons_6_g = self.send_beacons_6_g

        manage_rate_control_2_g_enable = self.manage_rate_control_2_g_enable

        manage_rate_control_2_g = self.manage_rate_control_2_g

        manage_rate_control_5_g_enable = self.manage_rate_control_5_g_enable

        manage_rate_control_5_g = self.manage_rate_control_5_g

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rate2gCtrlEnable": rate_2_g_ctrl_enable,
                "rate5gCtrlEnable": rate_5_g_ctrl_enable,
            }
        )
        if lower_density_2_g is not UNSET:
            field_dict["lowerDensity2g"] = lower_density_2_g
        if higher_density_2_g is not UNSET:
            field_dict["higherDensity2g"] = higher_density_2_g
        if cck_rates_disable is not UNSET:
            field_dict["cckRatesDisable"] = cck_rates_disable
        if client_rates_require_2_g is not UNSET:
            field_dict["clientRatesRequire2g"] = client_rates_require_2_g
        if send_beacons_2_g is not UNSET:
            field_dict["sendBeacons2g"] = send_beacons_2_g
        if lower_density_5_g is not UNSET:
            field_dict["lowerDensity5g"] = lower_density_5_g
        if higher_density_5_g is not UNSET:
            field_dict["higherDensity5g"] = higher_density_5_g
        if client_rates_require_5_g is not UNSET:
            field_dict["clientRatesRequire5g"] = client_rates_require_5_g
        if send_beacons_5_g is not UNSET:
            field_dict["sendBeacons5g"] = send_beacons_5_g
        if rate_6_g_ctrl_enable is not UNSET:
            field_dict["rate6gCtrlEnable"] = rate_6_g_ctrl_enable
        if lower_density_6_g is not UNSET:
            field_dict["lowerDensity6g"] = lower_density_6_g
        if higher_density_6_g is not UNSET:
            field_dict["higherDensity6g"] = higher_density_6_g
        if client_rates_require_6_g is not UNSET:
            field_dict["clientRatesRequire6g"] = client_rates_require_6_g
        if send_beacons_6_g is not UNSET:
            field_dict["sendBeacons6g"] = send_beacons_6_g
        if manage_rate_control_2_g_enable is not UNSET:
            field_dict["manageRateControl2gEnable"] = manage_rate_control_2_g_enable
        if manage_rate_control_2_g is not UNSET:
            field_dict["manageRateControl2g"] = manage_rate_control_2_g
        if manage_rate_control_5_g_enable is not UNSET:
            field_dict["manageRateControl5gEnable"] = manage_rate_control_5_g_enable
        if manage_rate_control_5_g is not UNSET:
            field_dict["manageRateControl5g"] = manage_rate_control_5_g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        rate_2_g_ctrl_enable = d.pop("rate2gCtrlEnable")

        rate_5_g_ctrl_enable = d.pop("rate5gCtrlEnable")

        lower_density_2_g = d.pop("lowerDensity2g", UNSET)

        higher_density_2_g = d.pop("higherDensity2g", UNSET)

        cck_rates_disable = d.pop("cckRatesDisable", UNSET)

        client_rates_require_2_g = d.pop("clientRatesRequire2g", UNSET)

        send_beacons_2_g = d.pop("sendBeacons2g", UNSET)

        lower_density_5_g = d.pop("lowerDensity5g", UNSET)

        higher_density_5_g = d.pop("higherDensity5g", UNSET)

        client_rates_require_5_g = d.pop("clientRatesRequire5g", UNSET)

        send_beacons_5_g = d.pop("sendBeacons5g", UNSET)

        rate_6_g_ctrl_enable = d.pop("rate6gCtrlEnable", UNSET)

        lower_density_6_g = d.pop("lowerDensity6g", UNSET)

        higher_density_6_g = d.pop("higherDensity6g", UNSET)

        client_rates_require_6_g = d.pop("clientRatesRequire6g", UNSET)

        send_beacons_6_g = d.pop("sendBeacons6g", UNSET)

        manage_rate_control_2_g_enable = d.pop("manageRateControl2gEnable", UNSET)

        manage_rate_control_2_g = d.pop("manageRateControl2g", UNSET)

        manage_rate_control_5_g_enable = d.pop("manageRateControl5gEnable", UNSET)

        manage_rate_control_5_g = d.pop("manageRateControl5g", UNSET)

        update_ssid_rate_control_open_api_vo = cls(
            rate_2_g_ctrl_enable=rate_2_g_ctrl_enable,
            rate_5_g_ctrl_enable=rate_5_g_ctrl_enable,
            lower_density_2_g=lower_density_2_g,
            higher_density_2_g=higher_density_2_g,
            cck_rates_disable=cck_rates_disable,
            client_rates_require_2_g=client_rates_require_2_g,
            send_beacons_2_g=send_beacons_2_g,
            lower_density_5_g=lower_density_5_g,
            higher_density_5_g=higher_density_5_g,
            client_rates_require_5_g=client_rates_require_5_g,
            send_beacons_5_g=send_beacons_5_g,
            rate_6_g_ctrl_enable=rate_6_g_ctrl_enable,
            lower_density_6_g=lower_density_6_g,
            higher_density_6_g=higher_density_6_g,
            client_rates_require_6_g=client_rates_require_6_g,
            send_beacons_6_g=send_beacons_6_g,
            manage_rate_control_2_g_enable=manage_rate_control_2_g_enable,
            manage_rate_control_2_g=manage_rate_control_2_g,
            manage_rate_control_5_g_enable=manage_rate_control_5_g_enable,
            manage_rate_control_5_g=manage_rate_control_5_g,
        )

        update_ssid_rate_control_open_api_vo.additional_properties = d
        return update_ssid_rate_control_open_api_vo

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
