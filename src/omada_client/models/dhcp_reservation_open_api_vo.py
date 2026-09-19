from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_dhcp_options import CustomDHCPOptions
    from ..models.feature_info_vo import FeatureInfoVO


T = TypeVar("T", bound="DhcpReservationOpenApiVO")


@_attrs_define
class DhcpReservationOpenApiVO:
    """
    Attributes:
        id (str | Unset): DHCP reservation ID
        description (str | Unset): Description of DHCP reservation
        net_id (str | Unset): ID of the configured LAN Network
        net_name (str | Unset): Name of the configured LAN Network
        mac (str | Unset): Device MAC address
        ip (str | Unset): Reserved IP address
        options (list[CustomDHCPOptions] | Unset): Advanced DHCP options
        status (bool | Unset): DHCP reservation enable status
        export_to_ip_mac_binding (bool | Unset): Indicates whether DHCP reservation can be exported to the IP-MAC
            Binding list
        client_name (str | Unset): Client name
        name (str | Unset): Device Name
        exist_options (list[int] | Unset): Options configured in the current DHCP Reservation entry.
        type_ (int | Unset): Type should be a value as follows: 0: Device; 1: Client
        showing_type (str | Unset): Client Type or Device Type
        model (str | Unset): Device Model
        model_version (str | Unset): Device Model Version
        server_name (str | Unset): Dhcp Server Device Name
        server_type (str | Unset): Dhcp Server Device Type
        server_mac (str | Unset): Dhcp Server Device Mac
        server_stack_id (str | Unset): Dhcp Server Stack ID
        abnormal (int | Unset): Abnormal cause
        feature_description (list[FeatureInfoVO] | Unset): Gateway Feature Description.
    """

    id: str | Unset = UNSET
    description: str | Unset = UNSET
    net_id: str | Unset = UNSET
    net_name: str | Unset = UNSET
    mac: str | Unset = UNSET
    ip: str | Unset = UNSET
    options: list[CustomDHCPOptions] | Unset = UNSET
    status: bool | Unset = UNSET
    export_to_ip_mac_binding: bool | Unset = UNSET
    client_name: str | Unset = UNSET
    name: str | Unset = UNSET
    exist_options: list[int] | Unset = UNSET
    type_: int | Unset = UNSET
    showing_type: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    server_name: str | Unset = UNSET
    server_type: str | Unset = UNSET
    server_mac: str | Unset = UNSET
    server_stack_id: str | Unset = UNSET
    abnormal: int | Unset = UNSET
    feature_description: list[FeatureInfoVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        description = self.description

        net_id = self.net_id

        net_name = self.net_name

        mac = self.mac

        ip = self.ip

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        status = self.status

        export_to_ip_mac_binding = self.export_to_ip_mac_binding

        client_name = self.client_name

        name = self.name

        exist_options: list[int] | Unset = UNSET
        if not isinstance(self.exist_options, Unset):
            exist_options = self.exist_options

        type_ = self.type_

        showing_type = self.showing_type

        model = self.model

        model_version = self.model_version

        server_name = self.server_name

        server_type = self.server_type

        server_mac = self.server_mac

        server_stack_id = self.server_stack_id

        abnormal = self.abnormal

        feature_description: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.feature_description, Unset):
            feature_description = []
            for feature_description_item_data in self.feature_description:
                feature_description_item = feature_description_item_data.to_dict()
                feature_description.append(feature_description_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if net_id is not UNSET:
            field_dict["netId"] = net_id
        if net_name is not UNSET:
            field_dict["netName"] = net_name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if ip is not UNSET:
            field_dict["ip"] = ip
        if options is not UNSET:
            field_dict["options"] = options
        if status is not UNSET:
            field_dict["status"] = status
        if export_to_ip_mac_binding is not UNSET:
            field_dict["exportToIpMacBinding"] = export_to_ip_mac_binding
        if client_name is not UNSET:
            field_dict["clientName"] = client_name
        if name is not UNSET:
            field_dict["name"] = name
        if exist_options is not UNSET:
            field_dict["existOptions"] = exist_options
        if type_ is not UNSET:
            field_dict["type"] = type_
        if showing_type is not UNSET:
            field_dict["showingType"] = showing_type
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if server_name is not UNSET:
            field_dict["serverName"] = server_name
        if server_type is not UNSET:
            field_dict["serverType"] = server_type
        if server_mac is not UNSET:
            field_dict["serverMac"] = server_mac
        if server_stack_id is not UNSET:
            field_dict["serverStackId"] = server_stack_id
        if abnormal is not UNSET:
            field_dict["abnormal"] = abnormal
        if feature_description is not UNSET:
            field_dict["featureDescription"] = feature_description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.custom_dhcp_options import CustomDHCPOptions
        from ..models.feature_info_vo import FeatureInfoVO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        net_id = d.pop("netId", UNSET)

        net_name = d.pop("netName", UNSET)

        mac = d.pop("mac", UNSET)

        ip = d.pop("ip", UNSET)

        _options = d.pop("options", UNSET)
        options: list[CustomDHCPOptions] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = CustomDHCPOptions.from_dict(options_item_data)

                options.append(options_item)

        status = d.pop("status", UNSET)

        export_to_ip_mac_binding = d.pop("exportToIpMacBinding", UNSET)

        client_name = d.pop("clientName", UNSET)

        name = d.pop("name", UNSET)

        exist_options = cast(list[int], d.pop("existOptions", UNSET))

        type_ = d.pop("type", UNSET)

        showing_type = d.pop("showingType", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        server_name = d.pop("serverName", UNSET)

        server_type = d.pop("serverType", UNSET)

        server_mac = d.pop("serverMac", UNSET)

        server_stack_id = d.pop("serverStackId", UNSET)

        abnormal = d.pop("abnormal", UNSET)

        _feature_description = d.pop("featureDescription", UNSET)
        feature_description: list[FeatureInfoVO] | Unset = UNSET
        if _feature_description is not UNSET:
            feature_description = []
            for feature_description_item_data in _feature_description:
                feature_description_item = FeatureInfoVO.from_dict(
                    feature_description_item_data
                )

                feature_description.append(feature_description_item)

        dhcp_reservation_open_api_vo = cls(
            id=id,
            description=description,
            net_id=net_id,
            net_name=net_name,
            mac=mac,
            ip=ip,
            options=options,
            status=status,
            export_to_ip_mac_binding=export_to_ip_mac_binding,
            client_name=client_name,
            name=name,
            exist_options=exist_options,
            type_=type_,
            showing_type=showing_type,
            model=model,
            model_version=model_version,
            server_name=server_name,
            server_type=server_type,
            server_mac=server_mac,
            server_stack_id=server_stack_id,
            abnormal=abnormal,
            feature_description=feature_description,
        )

        dhcp_reservation_open_api_vo.additional_properties = d
        return dhcp_reservation_open_api_vo

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
