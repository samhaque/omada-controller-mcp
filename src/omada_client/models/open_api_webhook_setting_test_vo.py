from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenApiWebhookSettingTestVO")


@_attrs_define
class OpenApiWebhookSettingTestVO:
    """
    Attributes:
        name (str): Webhook name. It should contain 1 to 128 characters.
        url_list (list[str]): Webhook URL List. Up to 3 entries are allowed for the URL list Example:
            [http(s)://webhook.site/4a566f9e-0b77-42e2-9a34-a78].
        template (int): Webhook template, it should be a value as follow: 0:Omada template, 1:Google chat template.
            Example: 0.
        sharded_secret (str | Unset): Webhook Sharded Secret. It should contain 0 to 128 characters.
    """

    name: str
    url_list: list[str]
    template: int
    sharded_secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        url_list = self.url_list

        template = self.template

        sharded_secret = self.sharded_secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "urlList": url_list,
                "template": template,
            }
        )
        if sharded_secret is not UNSET:
            field_dict["shardedSecret"] = sharded_secret

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        url_list = cast(list[str], d.pop("urlList"))

        template = d.pop("template")

        sharded_secret = d.pop("shardedSecret", UNSET)

        open_api_webhook_setting_test_vo = cls(
            name=name,
            url_list=url_list,
            template=template,
            sharded_secret=sharded_secret,
        )

        open_api_webhook_setting_test_vo.additional_properties = d
        return open_api_webhook_setting_test_vo

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
