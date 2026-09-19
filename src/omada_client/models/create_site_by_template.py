from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_account_setting_open_api_vo import (
        DeviceAccountSettingOpenApiVO,
    )


T = TypeVar("T", bound="CreateSiteByTemplate")


@_attrs_define
class CreateSiteByTemplate:
    """
    Attributes:
        site_template_id (str): Site template ID.
        name (str): Name of the site should contain 1 to 64 characters.
        region (str): Country/Region of the site; For the values of region, refer to the abbreviation of the ISO country
            code; For example, you need to input "United States" for the United States of America.
        scenario (str): For the values of the scenario of the site, refer to result of the interface for Get scenario
            list.
        device_account_setting (DeviceAccountSettingOpenApiVO):
        tag_ids (list[str] | Unset): Site tag ID, Site tag ID can be created using "Create new site tag" interface, and
            site tag ID can be obtained from "Get site tag list" interface
        longitude (float | Unset): Longitude of the site should be within the range of -180 - 180.
        latitude (float | Unset): Latitude of the site should be within the range of -90 - 90.
        address (str | Unset): Address of the site
        support_es (bool | Unset): Whether the site supports adopting Agile Series switches
        support_l2 (bool | Unset): Whether the site supports adopting Non-Agile Series switches
    """

    site_template_id: str
    name: str
    region: str
    scenario: str
    device_account_setting: DeviceAccountSettingOpenApiVO
    tag_ids: list[str] | Unset = UNSET
    longitude: float | Unset = UNSET
    latitude: float | Unset = UNSET
    address: str | Unset = UNSET
    support_es: bool | Unset = UNSET
    support_l2: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_template_id = self.site_template_id

        name = self.name

        region = self.region

        scenario = self.scenario

        device_account_setting = self.device_account_setting.to_dict()

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        longitude = self.longitude

        latitude = self.latitude

        address = self.address

        support_es = self.support_es

        support_l2 = self.support_l2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "siteTemplateId": site_template_id,
                "name": name,
                "region": region,
                "scenario": scenario,
                "deviceAccountSetting": device_account_setting,
            }
        )
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if address is not UNSET:
            field_dict["address"] = address
        if support_es is not UNSET:
            field_dict["supportES"] = support_es
        if support_l2 is not UNSET:
            field_dict["supportL2"] = support_l2

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_account_setting_open_api_vo import (
            DeviceAccountSettingOpenApiVO,
        )

        d = dict(src_dict)
        site_template_id = d.pop("siteTemplateId")

        name = d.pop("name")

        region = d.pop("region")

        scenario = d.pop("scenario")

        device_account_setting = DeviceAccountSettingOpenApiVO.from_dict(
            d.pop("deviceAccountSetting")
        )

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        longitude = d.pop("longitude", UNSET)

        latitude = d.pop("latitude", UNSET)

        address = d.pop("address", UNSET)

        support_es = d.pop("supportES", UNSET)

        support_l2 = d.pop("supportL2", UNSET)

        create_site_by_template = cls(
            site_template_id=site_template_id,
            name=name,
            region=region,
            scenario=scenario,
            device_account_setting=device_account_setting,
            tag_ids=tag_ids,
            longitude=longitude,
            latitude=latitude,
            address=address,
            support_es=support_es,
            support_l2=support_l2,
        )

        create_site_by_template.additional_properties = d
        return create_site_by_template

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
