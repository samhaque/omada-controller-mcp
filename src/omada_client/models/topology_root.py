from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopologyRoot")


@_attrs_define
class TopologyRoot:
    """Root Node In Topology.

    Attributes:
        type_ (str | Unset): Root Node Type, which can only be one of the following three types: switch, olt and other.
        specific_type (int | Unset): MultiSwitch Node SpecificType, which can only be one of the following two types:
            0:Mlag and 1:Vrrp.
        name (str | Unset): Root Node name.
        name_list (list[str] | Unset): MultiSwitch Node name list.
        mac (str | Unset): Root Node MAC address, like AA-BB-CC-DD-EE-FF.
        mac_list (list[str] | Unset): MultiSwitch Node MAC list.
        model (str | Unset): Root Node Model.
        model_version (str | Unset): Root Node ModelVersion.
        show_model (str | Unset): Root Node ShowModel.
        is_root (bool | Unset): Whether the Node is root.
        stack_group (bool | Unset): Whether the Node is stackGroup.
        client_type (str | Unset): Specific type of other node when it is a client.
        omada_device_type (str | Unset): Specific type of other node when it is a omada device.
    """

    type_: str | Unset = UNSET
    specific_type: int | Unset = UNSET
    name: str | Unset = UNSET
    name_list: list[str] | Unset = UNSET
    mac: str | Unset = UNSET
    mac_list: list[str] | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    show_model: str | Unset = UNSET
    is_root: bool | Unset = UNSET
    stack_group: bool | Unset = UNSET
    client_type: str | Unset = UNSET
    omada_device_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        specific_type = self.specific_type

        name = self.name

        name_list: list[str] | Unset = UNSET
        if not isinstance(self.name_list, Unset):
            name_list = self.name_list

        mac = self.mac

        mac_list: list[str] | Unset = UNSET
        if not isinstance(self.mac_list, Unset):
            mac_list = self.mac_list

        model = self.model

        model_version = self.model_version

        show_model = self.show_model

        is_root = self.is_root

        stack_group = self.stack_group

        client_type = self.client_type

        omada_device_type = self.omada_device_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if specific_type is not UNSET:
            field_dict["specificType"] = specific_type
        if name is not UNSET:
            field_dict["name"] = name
        if name_list is not UNSET:
            field_dict["nameList"] = name_list
        if mac is not UNSET:
            field_dict["mac"] = mac
        if mac_list is not UNSET:
            field_dict["macList"] = mac_list
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if is_root is not UNSET:
            field_dict["isRoot"] = is_root
        if stack_group is not UNSET:
            field_dict["stackGroup"] = stack_group
        if client_type is not UNSET:
            field_dict["clientType"] = client_type
        if omada_device_type is not UNSET:
            field_dict["omadaDeviceType"] = omada_device_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        specific_type = d.pop("specificType", UNSET)

        name = d.pop("name", UNSET)

        name_list = cast(list[str], d.pop("nameList", UNSET))

        mac = d.pop("mac", UNSET)

        mac_list = cast(list[str], d.pop("macList", UNSET))

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        show_model = d.pop("showModel", UNSET)

        is_root = d.pop("isRoot", UNSET)

        stack_group = d.pop("stackGroup", UNSET)

        client_type = d.pop("clientType", UNSET)

        omada_device_type = d.pop("omadaDeviceType", UNSET)

        topology_root = cls(
            type_=type_,
            specific_type=specific_type,
            name=name,
            name_list=name_list,
            mac=mac,
            mac_list=mac_list,
            model=model,
            model_version=model_version,
            show_model=show_model,
            is_root=is_root,
            stack_group=stack_group,
            client_type=client_type,
            omada_device_type=omada_device_type,
        )

        topology_root.additional_properties = d
        return topology_root

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
