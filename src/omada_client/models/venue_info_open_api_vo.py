from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VenueInfoOpenApiVO")


@_attrs_define
class VenueInfoOpenApiVO:
    """Indicates the venue information using the combination of the network's venue group and venue type (using the
    international building code).

        Attributes:
            group (int): Venue Group.Parameter group should be a value as follows: [0: Unspecified; 1: Assembly; 2:
                Business; 3: Educational; 4: Factory and Industrial; 5: Institutional; 6: Mercantile; 7: Residential; 8:
                Storage; 9: Utility and Miscellaneous; 10: Vehicular; 11: Outdoor]
            type_ (int): Venue Type.When Venue Group = 0, type should be a value as follows:[0: Unspecified]When Venue Group
                = 1, type should be a value as follows:[0: Unspecified Assembly;1: Arena;2: Stadium;3: Passenger Terminal (e.g.,
                airport, bus, ferry, train station);4: Amphitheater;5: Amusement Park;6: Place of Worship;7: Convention
                Center;8: Library;9: Museum;10: Restaurant;11: Theater;12: Bar;13: Coffee Shop;14: Zoo or Aquarium;15: Emergency
                Coordination Center]When Venue Group = 2, type should be a value as follows:[0: Unspecified Business;1: Doctor
                or Dentist office;2: Bank;3: Fire Station;4: Police Station;5: Post Office;6: Professional Office;7: Research
                and Development Facility;8: Attorney Office]When Venue Group = 3, type should be a value as follows:[0:
                Unspecified Educational;1: School,Primary;2: School, Secondary;3: University or College;]When Venue Group = 4,
                type should be a value as follows:[0: Unspecified Factory and Industrial;1: Factory]When Venue Group = 5, type
                should be a value as follows:[0: Unspecified Institutional;1: Hospital;2: Long-Term Care Facility (e.g. Nursing
                home, Hospice, etc.);3: Alchohol and Drug Re-habilitation Center;4: Group Home;5: Prison or Jail;]When Venue
                Group = 6, type should be a value as follows:[0: Unspecified Mercantile;1: Retail Store;2: Grocery Market;3:
                Automotive Service Station;4: Shopping Mall;5: Gas Station;]When Venue Group = 7, type should be a value as
                follows:[0: Unspecified Residential;1: Private Residence;2: Hotel or Motel;3: Dormitory;4: Boarding House;]When
                Venue Group = 8, type should be a value as follows:[0: Unspecified Storage]When Venue Group = 9, type should be
                a value as follows:[0: Unspecified Utility and Miscellaneous]When Venue Group = 10, type should be a value as
                follows:[0: Unspecified Vehicular;1: Automobile or Truck;2: Airplane;3: Bus;4: Ferry;5: Ship or Boat;6: Train;7:
                Motor Bike;]When Venue Group = 11, type should be a value as follows:[0: Unspecified Outdoor;1: Muni-mesh
                Network;2: City Park;3: Rest Area;4: Traffic Control;5: Bus Stop;6: Kiosk]
            name (str | Unset): Network’s venue name, identifying the physical location of the network.<br />Note: It should
                contain between 1 and 64 visible ASCII characters, with no Spaces at the beginning and end, and Spaces in
                between.
    """

    group: int
    type_: int
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group = self.group

        type_ = self.type_

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group": group,
                "type": type_,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        group = d.pop("group")

        type_ = d.pop("type")

        name = d.pop("name", UNSET)

        venue_info_open_api_vo = cls(
            group=group,
            type_=type_,
            name=name,
        )

        venue_info_open_api_vo.additional_properties = d
        return venue_info_open_api_vo

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
