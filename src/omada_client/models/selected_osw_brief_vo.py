from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_dev_cap_vo import OswDevCapVO
    from ..models.osw_lag_vo import OswLagVO
    from ..models.osw_port_vo import OswPortVO
    from ..models.osw_stack_data_vo import OswStackDataVO


T = TypeVar("T", bound="SelectedOswBriefVO")


@_attrs_define
class SelectedOswBriefVO:
    """
    Attributes:
        name (str | Unset): Switch name.
        mac (str | Unset): Switch mac address.
        model (str | Unset): Switch model.
        model_version (str | Unset): Switch model version.
        show_model (str | Unset): Switch show model.
        status_category (int | Unset): Switch status category.
        status (int | Unset): Switch status.
        stack_device (bool | Unset): Indicate whether this device is a stacked device.
        dev_cap (OswDevCapVO | Unset): Capability of device
        ports (list[OswPortVO] | Unset): Switch port List.
        lags (list[OswLagVO] | Unset): Switch lag List.
        osw_stack_data (OswStackDataVO | Unset): oswStackData
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    show_model: str | Unset = UNSET
    status_category: int | Unset = UNSET
    status: int | Unset = UNSET
    stack_device: bool | Unset = UNSET
    dev_cap: OswDevCapVO | Unset = UNSET
    ports: list[OswPortVO] | Unset = UNSET
    lags: list[OswLagVO] | Unset = UNSET
    osw_stack_data: OswStackDataVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        model = self.model

        model_version = self.model_version

        show_model = self.show_model

        status_category = self.status_category

        status = self.status

        stack_device = self.stack_device

        dev_cap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dev_cap, Unset):
            dev_cap = self.dev_cap.to_dict()

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        lags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lags, Unset):
            lags = []
            for lags_item_data in self.lags:
                lags_item = lags_item_data.to_dict()
                lags.append(lags_item)

        osw_stack_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.osw_stack_data, Unset):
            osw_stack_data = self.osw_stack_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if status is not UNSET:
            field_dict["status"] = status
        if stack_device is not UNSET:
            field_dict["stackDevice"] = stack_device
        if dev_cap is not UNSET:
            field_dict["devCap"] = dev_cap
        if ports is not UNSET:
            field_dict["ports"] = ports
        if lags is not UNSET:
            field_dict["lags"] = lags
        if osw_stack_data is not UNSET:
            field_dict["oswStackData"] = osw_stack_data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_dev_cap_vo import OswDevCapVO
        from ..models.osw_lag_vo import OswLagVO
        from ..models.osw_port_vo import OswPortVO
        from ..models.osw_stack_data_vo import OswStackDataVO

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        show_model = d.pop("showModel", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        status = d.pop("status", UNSET)

        stack_device = d.pop("stackDevice", UNSET)

        _dev_cap = d.pop("devCap", UNSET)
        dev_cap: OswDevCapVO | Unset
        if isinstance(_dev_cap, Unset):
            dev_cap = UNSET
        else:
            dev_cap = OswDevCapVO.from_dict(_dev_cap)

        _ports = d.pop("ports", UNSET)
        ports: list[OswPortVO] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = OswPortVO.from_dict(ports_item_data)

                ports.append(ports_item)

        _lags = d.pop("lags", UNSET)
        lags: list[OswLagVO] | Unset = UNSET
        if _lags is not UNSET:
            lags = []
            for lags_item_data in _lags:
                lags_item = OswLagVO.from_dict(lags_item_data)

                lags.append(lags_item)

        _osw_stack_data = d.pop("oswStackData", UNSET)
        osw_stack_data: OswStackDataVO | Unset
        if isinstance(_osw_stack_data, Unset):
            osw_stack_data = UNSET
        else:
            osw_stack_data = OswStackDataVO.from_dict(_osw_stack_data)

        selected_osw_brief_vo = cls(
            name=name,
            mac=mac,
            model=model,
            model_version=model_version,
            show_model=show_model,
            status_category=status_category,
            status=status,
            stack_device=stack_device,
            dev_cap=dev_cap,
            ports=ports,
            lags=lags,
            osw_stack_data=osw_stack_data,
        )

        selected_osw_brief_vo.additional_properties = d
        return selected_osw_brief_vo

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
