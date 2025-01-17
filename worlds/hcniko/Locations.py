from typing import Dict, NamedTuple, Callable, Optional, Set

from BaseClasses import Location


class HereComesNikoLocation(Location):
    game = "Here Comes Niko!"


class HereComesNikoLocationData(NamedTuple):
    region: str
    id: Optional[int] = None
    can_create: Callable = lambda options: True
    locked_item: Optional[str] = None
    location_group: Optional[str] = None

base_id = 598_145_444_000

location_data_table: Dict[str, HereComesNikoLocationData] = {
    # Coins
    "Home - Give High Frog Lunchbox": HereComesNikoLocationData(region="Home",id=base_id + 0),
    # ~ Hairball City
    "Hairball City - BIG VOLLEY": HereComesNikoLocationData(region="Hairball City", id=base_id + 3, location_group="Volley"),
    "Hairball City - Dustan on Lighthouse": HereComesNikoLocationData(region="Hairball City",id=base_id + 4, location_group="Dustan"),
    "Hairball City - Little Gabi's Flowers": HereComesNikoLocationData(region="Hairball City",id=base_id + 5, location_group="Little Gabi"),
    "Hairball City - Gunter on Skyscraper": HereComesNikoLocationData(region="Hairball City",id=base_id + 6),
    "Hairball City - Fish with Fischer": HereComesNikoLocationData(region="Hairball City",id=base_id + 7, location_group="Fischer"),
    "Hairball City - Blessley": HereComesNikoLocationData(region="Hairball City",id=base_id + 8, location_group="Blessley"),
    "Hairball City - Nina": HereComesNikoLocationData(region="Hairball City",id=base_id + 9),
    "Hairball City - Moomy": HereComesNikoLocationData(region="Hairball City",id=base_id + 10),
    "Hairball City - Mitch": HereComesNikoLocationData(region="Hairball City",id=base_id + 11, location_group="Mitch & Mai"),
    "Hairball City - Mai": HereComesNikoLocationData(region="Hairball City",id=base_id + 12, location_group="Mitch & Mai"),
    "Hairball City - Game Kid": HereComesNikoLocationData(region="Hairball City",id=base_id + 13),
    "Hairball City - Blippy Dog": HereComesNikoLocationData(region="Hairball City",id=base_id + 14, location_group="Blippy"),
    "Hairball City - Blippy": HereComesNikoLocationData(region="Hairball City",id=base_id + 15, location_group="Blippy"),
    "Hairball City - Serschel & Louist": HereComesNikoLocationData(region="Hairball City",id=base_id + 16, location_group="Serschel & Louist"),
    # ~ Turbine Town
    "Turbine Town - Fish with Fischer": HereComesNikoLocationData(region="Turbine Town",id=base_id + 17, location_group="Fischer"),
    "Turbine Town - AIR VOLLEY": HereComesNikoLocationData(region="Turbine Town",id=base_id + 18, location_group="Volley"),
    "Turbine Town - Little Gabi's Flowers": HereComesNikoLocationData(region="Turbine Town",id=base_id + 19, location_group="Little Gabi"),
    "Turbine Town - Pelly the Engineer": HereComesNikoLocationData(region="Turbine Town",id=base_id + 20),
    "Turbine Town - Blessley": HereComesNikoLocationData(region="Turbine Town",id=base_id + 21, location_group="Blessley"),
    "Turbine Town - Dustan on Wind Turbine": HereComesNikoLocationData(region="Turbine Town",id=base_id + 22, location_group="Dustan"),
    "Turbine Town - Mitch": HereComesNikoLocationData(region="Turbine Town",id=base_id + 23, location_group="Mitch & Mai"),
    "Turbine Town - Mai": HereComesNikoLocationData(region="Turbine Town",id=base_id + 24, location_group="Mitch & Mai"),
    "Turbine Town - Blippy Dog": HereComesNikoLocationData(region="Turbine Town",id=base_id + 25, location_group="Blippy"),
    "Turbine Town - Blippy": HereComesNikoLocationData(region="Turbine Town",id=base_id + 26, location_group="Blippy"),
    "Turbine Town - Serschel & Louist": HereComesNikoLocationData(region="Turbine Town",id=base_id + 27, location_group="Serschel & Louist"),
    # ~ Salmon Creek Forest
    "Salmon Creek Forest - Stijn & Melissa": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 28),
    "Salmon Creek Forest - Mitch": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 29, location_group="Mitch & Mai"),
    "Salmon Creek Forest - Dustan on Mountain": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 30, location_group="Dustan"),
    "Salmon Creek Forest - Moomy": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 31),
    "Salmon Creek Forest - Blippy Dog": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 32, location_group="Blippy"),
    "Salmon Creek Forest - Treeman": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 33),
    "Salmon Creek Forest - Blessley": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 34, location_group="Blessley"),
    "Salmon Creek Forest - Secret of the Forest (Waterfall Cave)": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 35),
    "Salmon Creek Forest - SPORTVIVAL": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 36, location_group="Volley"),
    "Salmon Creek Forest - Little Gabi's Flowers": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 37, location_group="Little Gabi"),
    "Salmon Creek Forest - Nina": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 38),
    "Salmon Creek Forest - Mai": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 39, location_group="Mitch & Mai"),
    "Salmon Creek Forest - Fish with Fischer": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 40, location_group="Fischer"),
    "Salmon Creek Forest - Game Kid": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 41),
    "Salmon Creek Forest - Blippy": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 42, location_group="Blippy"),
    "Salmon Creek Forest - Serschel & Louist": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 43, location_group="Serschel & Louist"),
    # ~ Public Pool
    "Public Pool - Far Away Island": HereComesNikoLocationData(region="Public Pool",id=base_id + 44),
    "Public Pool - Mai": HereComesNikoLocationData(region="Public Pool",id=base_id + 45, location_group="Mitch & Mai"),
    "Public Pool - Blippy Dog": HereComesNikoLocationData(region="Public Pool",id=base_id + 46, location_group="Blippy"),
    "Public Pool - Blippy": HereComesNikoLocationData(region="Public Pool",id=base_id + 47, location_group="Blippy"),
    "Public Pool - Fish with Fischer": HereComesNikoLocationData(region="Public Pool",id=base_id + 48),
    "Public Pool - Frogtective": HereComesNikoLocationData(region="Public Pool",id=base_id + 49),
    "Public Pool - SPORTVIVAL VOLLEY": HereComesNikoLocationData(region="Public Pool",id=base_id + 50, location_group="Volley"),
    "Public Pool - Blessley": HereComesNikoLocationData(region="Public Pool",id=base_id + 51, location_group="Blessley"),
    "Public Pool - Mitch": HereComesNikoLocationData(region="Public Pool",id=base_id + 52, location_group="Mitch & Mai"),
    "Public Pool - Little Gabi's Flowers": HereComesNikoLocationData(region="Public Pool",id=base_id + 53, location_group="Little Gabi"),
    # ~ Bathhouse
    "Bathhouse - Serschel & Louist": HereComesNikoLocationData(region="Bathhouse",id=base_id + 54, location_group="Serschel & Louist"),
    "Bathhouse - Moomy": HereComesNikoLocationData(region="Bathhouse",id=base_id + 55),
    "Bathhouse - Poppy": HereComesNikoLocationData(region="Bathhouse",id=base_id + 56),
    "Bathhouse - Nina": HereComesNikoLocationData(region="Bathhouse",id=base_id + 57),
    "Bathhouse - Mitch": HereComesNikoLocationData(region="Bathhouse",id=base_id + 58, location_group="Mitch & Mai"),
    "Bathhouse - Mai": HereComesNikoLocationData(region="Bathhouse",id=base_id + 59, location_group="Mitch & Mai"),
    "Bathhouse - Dustan on Bathhouse": HereComesNikoLocationData(region="Bathhouse",id=base_id + 60, location_group="Dustan"),
    "Bathhouse - LONG VOLLEY": HereComesNikoLocationData(region="Bathhouse",id=base_id + 61, location_group="Volley"),
    "Bathhouse - Game Kid": HereComesNikoLocationData(region="Bathhouse",id=base_id + 62),
    "Bathhouse - Fish with Fischer": HereComesNikoLocationData(region="Bathhouse",id=base_id + 63, location_group="Fischer"),
    "Bathhouse - Blessley": HereComesNikoLocationData(region="Bathhouse",id=base_id + 64, location_group="Blessley"),
    "Bathhouse - Little Gabi's Flowers": HereComesNikoLocationData(region="Bathhouse",id=base_id + 65, location_group="Little Gabi"),
    "Bathhouse - Blippy Dog": HereComesNikoLocationData(region="Bathhouse",id=base_id + 66, location_group="Blippy"),
    "Bathhouse - Blippy": HereComesNikoLocationData(region="Bathhouse",id=base_id + 67, location_group="Blippy"),
    # ~ Tadpole HQ
    "Tadpole HQ - Mai": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 68, location_group="Mitch & Mai"),
    "Tadpole HQ - Mitch": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 69, location_group="Mitch & Mai"),
    "Tadpole HQ - Frog King": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 70),
    "Tadpole HQ - HUGE VOLLEY": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 71, location_group="Volley"),
    "Tadpole HQ - Fish with Fischer": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 72, location_group="Fischer"),
    "Tadpole HQ - Little Gabi's Flowers": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 73, location_group="Little Gabi"),
    "Tadpole HQ - Blippy": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 74, location_group="Blippy"),
    "Tadpole HQ - Blessley": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 75, location_group="Blessley"),
    "Tadpole HQ - Serschel & Louist": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 76, location_group="Serschel & Louist"),
    "Tadpole HQ - Blippy Dog": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 77, location_group="Blippy"),

    # Letters
    "Home - Next To Crane": HereComesNikoLocationData(region="Home",id=base_id + 80, location_group="Letter"),
    "Hairball City - Above Tree Near Gabi": HereComesNikoLocationData(region="Hairball City",id=base_id + 81, location_group="Letter"),
    "Hairball City - Behind The Train": HereComesNikoLocationData(region="Hairball City",id=base_id + 82, location_group="Letter"),
    "Turbine Town - Behind Wind Dragon": HereComesNikoLocationData(region="Turbine Town",id=base_id + 83, location_group="Letter"),
    "Turbine Town - Above Partially Sunken Shipping Container": HereComesNikoLocationData(region="Turbine Town",id=base_id + 84, location_group="Letter"),
    "Salmon Creek Forest - Inside Locked Cave": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 85, location_group="Letter"),
    "Salmon Creek Forest - Inside Secret of the Forest (Waterfall Cave)": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 86, location_group="Letter"),
    "Public Pool - Far Away Island Left Side": HereComesNikoLocationData(region="Public Pool",id=base_id + 87, location_group="Letter"),
    "Public Pool - Far Away Island Right Side": HereComesNikoLocationData(region="Public Pool",id=base_id + 88, location_group="Letter"),
    "Bathhouse - Behind Axolotl Family": HereComesNikoLocationData(region="Bathhouse",id=base_id + 89, location_group="Letter"),
    "Bathhouse - Near Game Kid": HereComesNikoLocationData(region="Bathhouse",id=base_id + 90, location_group="Letter"),
    "Tadpole HQ - Ledge Above Elevator": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 250, location_group="Letter"),

    # Keys
    "Turbine Town - Shipping Container With Breakable Boxes": HereComesNikoLocationData(region="Turbine Town",id=base_id + 91),
    "Turbine Town - Stone Pillar Behind Wind Turbine": HereComesNikoLocationData(region="Turbine Town",id=base_id + 92),
    "Salmon Creek Forest - Large Rock In Ocean": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 93),
    "Salmon Creek Forest - Beneath Pond": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 94),
    "Salmon Creek Forest - Behind Frog Statue": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 95),
    "Public Pool - Above Small Island": HereComesNikoLocationData(region="Public Pool",id=base_id + 96),
    "Bathhouse - On Top Of A Torii": HereComesNikoLocationData(region="Bathhouse",id=base_id + 97),
    "Bathhouse - Breakable Box Inside Bathhouse Box": HereComesNikoLocationData(region="Bathhouse",id=base_id + 98),
    "Bathhouse - Beneath Moomy": HereComesNikoLocationData(region="Bathhouse",id=base_id + 99),

    # Cassettes
    "Hairball City - Behind Pepper": HereComesNikoLocationData(region="Hairball City",id=base_id+100),
    "Hairball City - Frog Statue Crown": HereComesNikoLocationData(region="Hairball City",id=base_id + 101),
    "Hairball City - Big Umbrella": HereComesNikoLocationData(region="Hairball City",id=base_id + 102),
    "Hairball City - Lighthouse Front Door": HereComesNikoLocationData(region="Hairball City",id=base_id + 103),
    "Hairball City - Palm Tree": HereComesNikoLocationData(region="Hairball City",id=base_id + 104),
    "Hairball City - Inside Tunnel": HereComesNikoLocationData(region="Hairball City",id=base_id + 105),
    "Hairball City - Breakable Boxes Near Frog Of Destruction": HereComesNikoLocationData(region="Hairball City",id=base_id + 106),
    "Hairball City - Behind Lighthouse": HereComesNikoLocationData(region="Hairball City",id=base_id + 107),
    "Hairball City - Next to Breakable Boxes Under Ramp": HereComesNikoLocationData(region="Hairball City",id=base_id + 108),
    "Hairball City - Above Frog Statue": HereComesNikoLocationData(region="Hairball City",id=base_id + 109),
    #  ~ Turbine Town
    "Turbine Town - Inside Partially Sunken Shipping Container": HereComesNikoLocationData(region="Turbine Town",id=base_id + 111),
    "Turbine Town - Cube Rocks Behind Gabi's Garden": HereComesNikoLocationData(region="Turbine Town",id=base_id + 112),
    "Turbine Town - Above Handsome Frog Container": HereComesNikoLocationData(region="Turbine Town",id=base_id + 113),
    "Turbine Town - Behind Blessley": HereComesNikoLocationData(region="Turbine Town",id=base_id + 114),
    "Turbine Town - Inside Container With Buttons": HereComesNikoLocationData(region="Turbine Town",id=base_id + 115),
    "Turbine Town - Inside Container Behind Pepper": HereComesNikoLocationData(region="Turbine Town",id=base_id + 116),
    "Turbine Town - In Front Of Wind Turbine": HereComesNikoLocationData(region="Turbine Town",id=base_id + 117),
    "Turbine Town - Next To Torii Gates": HereComesNikoLocationData(region="Turbine Town",id=base_id + 118),
    "Turbine Town - Near Fishing Containers": HereComesNikoLocationData(region="Turbine Town",id=base_id + 119),
    "Turbine Town - Near AIR VOLLEY On Zip Line": HereComesNikoLocationData(region="Turbine Town",id=base_id + 120),
    #  ~ Salmon Creek Forest
    "Salmon Creek Forest - Behind Train": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 122),
    "Salmon Creek Forest - Wooden Bridge": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 123),
    "Salmon Creek Forest - Treehouse": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 124),
    "Salmon Creek Forest - Rocks Behind Mountain": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 125),
    "Salmon Creek Forest - Near Breakable Boxes (Waterfall Cave)": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 126),
    "Salmon Creek Forest - Inside Boxes (Waterfall Cave)": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 127),
    "Salmon Creek Forest - Next To Treehouse": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 128),
    "Salmon Creek Forest - Next To Flowers Near Stijn": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 129),
    "Salmon Creek Forest - Behind Mountain": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 130),
    "Salmon Creek Forest - Fallen Tree": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 131),
    "Salmon Creek Forest - Behind A Tent Near Moomy": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 132),
    #  ~ Public Pool
    "Public Pool - Frog Statue": HereComesNikoLocationData(region="Public Pool",id=base_id + 134),
    "Public Pool - On Springboard": HereComesNikoLocationData(region="Public Pool",id=base_id + 135),
    "Public Pool - Behind Palm Tree On Small Island": HereComesNikoLocationData(region="Public Pool",id=base_id + 136),
    "Public Pool - Cassette Rocks in Ocean": HereComesNikoLocationData(region="Public Pool",id=base_id + 137),
    "Public Pool - Inside Pool": HereComesNikoLocationData(region="Public Pool",id=base_id + 138),
    "Public Pool - Inside BIG Pool": HereComesNikoLocationData(region="Public Pool",id=base_id + 139),
    "Public Pool - Behind Frog Statue": HereComesNikoLocationData(region="Public Pool",id=base_id + 140),
    "Public Pool - On A Palm Tree": HereComesNikoLocationData(region="Public Pool",id=base_id + 141),
    "Public Pool - Breakable Boxes Near Frogtective": HereComesNikoLocationData(region="Public Pool",id=base_id + 142),
    "Public Pool - Above BIG Pool": HereComesNikoLocationData(region="Public Pool",id=base_id + 143),
    #  ~ Bathhouse
    "Bathhouse - Behind Frog Statue": HereComesNikoLocationData(region="Bathhouse",id=base_id + 145),
    "Bathhouse - In Water Next To Elizabeth IV": HereComesNikoLocationData(region="Bathhouse",id=base_id + 146),
    "Bathhouse - Hut in Water": HereComesNikoLocationData(region="Bathhouse",id=base_id + 147),
    "Bathhouse - Giant Frog Statue Crown": HereComesNikoLocationData(region="Bathhouse",id=base_id + 148),
    "Bathhouse - Lamp near Moomy": HereComesNikoLocationData(region="Bathhouse",id=base_id + 149),
    "Bathhouse - Behind LONG VOLLEY": HereComesNikoLocationData(region="Bathhouse",id=base_id + 150),
    "Bathhouse - Behind Waterfall": HereComesNikoLocationData(region="Bathhouse",id=base_id + 151),
    "Bathhouse - Fan to Fan": HereComesNikoLocationData(region="Bathhouse",id=base_id + 152),
    "Bathhouse - Pipe Under Wooden Bridge": HereComesNikoLocationData(region="Bathhouse",id=base_id + 153),
    "Bathhouse - Mahjong Hideout": HereComesNikoLocationData(region="Bathhouse",id=base_id + 154),
    # ~ Tadpole HQ
    "Tadpole HQ - Inbetween Four Skyscrapers": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 156),
    "Tadpole HQ - Next To Four Skyscrapers": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 157),
    "Tadpole HQ - Behind Bench In Bushes": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 158),
    "Tadpole HQ - Cannon Next To Elevator": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 159),
    "Tadpole HQ - Big Tree Next To Louist": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 160),
    "Tadpole HQ - Golden Frog Statue Crown": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 161),
    "Tadpole HQ - Breakable Boxes near Blessley": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 162),
    "Tadpole HQ - Behind Fischer On A Rock": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 163),
    "Tadpole HQ - Under Giant Umbrella": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 164),
    "Tadpole HQ - Wall Jump Near Breakable Boxes": HereComesNikoLocationData(region="Tadpole HQ",id=base_id + 165),

    # Misc
    "Tadpole HQ - Dojo Guy": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 166),
    "Salmon Creek Forest - Contact List": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 167),
    "Tadpole HQ - Contact List": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 168),

    # Achievements
    "Achievement - Frog Fan": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 176, can_create=lambda options: options.enable_achievements.value != 2),
    "Achievement - Employee Of The Month!": HereComesNikoLocationData(region="Home", id=base_id + 177, can_create=lambda options: options.enable_achievements.value != 2 and options.goal_completion.value != 1),
    "Achievement - Bottled Up": HereComesNikoLocationData(region="Bathhouse", id=base_id + 178, can_create=lambda options: options.enable_achievements.value != 2),
    "Achievement - Snail Fashion Show": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 179, can_create=lambda options: options.enable_achievements.value == 0),
    "Achievement - Volley Dreams": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 180, can_create=lambda options: options.enable_achievements.value != 2),
    "Achievement - Hopeless Romantic": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 181, can_create=lambda options: options.enable_achievements.value != 2),
    "Achievement - Lost at Sea": HereComesNikoLocationData(region="Home", id=base_id + 182, can_create=lambda options: options.enable_achievements.value != 2),

    # DLC Garden
    "Gary's Garden - Tree Branch Near The Top": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 183, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - On Tree Branch": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 184, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Tree Branch Near Gold Scissor Row": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 185, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Next Garden Seed On Rocks": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 186, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Next To Smaller Tree": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 187, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Near End Of Giant Gold Scissor": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 188, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Beginning Of Giant Gold Scissor": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 189, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Behind Large Rock": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 190, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Small Rocks In Water": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 191, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Next To Train": HereComesNikoLocationData(region="Gary's Garden",id=base_id + 192, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Gunter & Little Gabi": HereComesNikoLocationData(region="Gary's Garden", id=base_id + 198, can_create=lambda options: options.shuffle_garys_garden.value),
    "Gary's Garden - Mai": HereComesNikoLocationData(region="Gary's Garden", id=base_id + 199, can_create=lambda options: options.shuffle_garys_garden.value, location_group="Mitch & Mai"),
    "Gary's Garden - Mitch": HereComesNikoLocationData(region="Gary's Garden", id=base_id + 200, can_create=lambda options: options.shuffle_garys_garden.value, location_group="Mitch & Mai"),
    #"Gary's Garden - Handsome Frog": HereComesNikoLocationData(region="Gary's Garden", id=base_id + 201, can_create=lambda options: options.shuffle_garys_garden.value and options.shuffle_handsome_frog.value),

    # Handsome Frog
    "Hairball City - Handsome Frog": HereComesNikoLocationData(region="Hairball City",id=base_id + 193, can_create=lambda options: options.shuffle_handsome_frog.value, location_group="Handsome Frog"),
    "Turbine Town - Handsome Frog": HereComesNikoLocationData(region="Turbine Town",id=base_id + 194, can_create=lambda options: options.shuffle_handsome_frog.value, location_group="Handsome Frog"),
    "Salmon Creek Forest - Handsome Frog": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 195, can_create=lambda options: options.shuffle_handsome_frog.value, location_group="Handsome Frog"),
    "Public Pool - Handsome Frog": HereComesNikoLocationData(region="Public Pool",id=base_id + 196, can_create=lambda options: options.shuffle_handsome_frog.value, location_group="Handsome Frog"),
    "Bathhouse - Handsome Frog": HereComesNikoLocationData(region="Bathhouse",id=base_id + 197, can_create=lambda options: options.shuffle_handsome_frog.value, location_group="Handsome Frog"),

    # Kiosk
    "Home - Kiosk": HereComesNikoLocationData(region="Home",id=base_id + 170, location_group="Kiosk"),
    "Hairball City - Kiosk": HereComesNikoLocationData(region="Hairball City",id=base_id + 171, location_group="Kiosk"),
    "Turbine Town - Kiosk": HereComesNikoLocationData(region="Turbine Town",id=base_id + 172, location_group="Kiosk"),
    "Salmon Creek Forest - Kiosk": HereComesNikoLocationData(region="Salmon Creek Forest",id=base_id + 173, location_group="Kiosk"),
    "Public Pool - Kiosk": HereComesNikoLocationData(region="Public Pool",id=base_id + 174, location_group="Kiosk"),
    "Bathhouse - Kiosk": HereComesNikoLocationData(region="Bathhouse",id=base_id + 175, location_group="Kiosk"),

    #Dustan
    "Dustan - Meeting First Time": HereComesNikoLocationData(region="Home", id=base_id + 202, location_group="Dustan"),

    #Fishsanity
    "Hairball City - Moorish Idol": HereComesNikoLocationData(region="Hairball City", id=base_id + 203, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Hairball City - Not Nemo": HereComesNikoLocationData(region="Hairball City", id=base_id + 204, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Hairball City - Eel": HereComesNikoLocationData(region="Hairball City", id=base_id + 205, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Hairball City - Flying Fish": HereComesNikoLocationData(region="Hairball City", id=base_id + 206, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Hairball City - Orange Fish": HereComesNikoLocationData(region="Hairball City", id=base_id + 207, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Turbine Town - Albino Corydoras": HereComesNikoLocationData(region="Turbine Town", id=base_id + 208, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Turbine Town - Axolotl": HereComesNikoLocationData(region="Turbine Town", id=base_id + 209, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Turbine Town - Prianha": HereComesNikoLocationData(region="Turbine Town", id=base_id + 210, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Turbine Town - Mantaray": HereComesNikoLocationData(region="Turbine Town", id=base_id + 211, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Turbine Town - Sand Shrimp": HereComesNikoLocationData(region="Turbine Town", id=base_id + 212, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Salmon Creek Forest - Bass": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 213, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Salmon Creek Forest - Catfish": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 214, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Salmon Creek Forest - Pike": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 215, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Salmon Creek Forest - Salmon": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 216, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Salmon Creek Forest - Trout": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 217, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Public Pool - Baby Crocodile": HereComesNikoLocationData(region="Public Pool", id=base_id + 218, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Public Pool - Gramma Loreto": HereComesNikoLocationData(region="Public Pool", id=base_id + 219, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Public Pool - Shark": HereComesNikoLocationData(region="Public Pool", id=base_id + 220, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Public Pool - Squid": HereComesNikoLocationData(region="Public Pool", id=base_id + 221, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Public Pool - Turtle": HereComesNikoLocationData(region="Public Pool", id=base_id + 222, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Bathhouse - Anglerfish": HereComesNikoLocationData(region="Bathhouse", id=base_id + 223, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Bathhouse - Clione": HereComesNikoLocationData(region="Bathhouse", id=base_id + 224, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Bathhouse - Little Wiggly Guy": HereComesNikoLocationData(region="Bathhouse", id=base_id + 225, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Bathhouse - Jellyfish": HereComesNikoLocationData(region="Bathhouse", id=base_id + 226, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Bathhouse - Pufferfish": HereComesNikoLocationData(region="Bathhouse", id=base_id + 227, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Tadpole HQ - Blue Fairy Shrimp": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 228, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Tadpole HQ - Bluestreak Cleaner Wrasse": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 229, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Tadpole HQ - Honey Gourami": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 230, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Tadpole HQ - Loach": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 231, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),
    "Tadpole HQ - Neon Tetra": HereComesNikoLocationData(region="Tadpole HQ", id=base_id + 232, can_create=lambda options: options.fishsanity.value, location_group="Fischer"),

    # Snail Shop
    "Snail Shop - Bowtie": HereComesNikoLocationData(region="Home",id=base_id + 233, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Motorcycle": HereComesNikoLocationData(region="Home",id=base_id + 234, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Sunglasses": HereComesNikoLocationData(region="Home",id=base_id + 235, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Mahjong": HereComesNikoLocationData(region="Home",id=base_id + 236, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Cap": HereComesNikoLocationData(region="Home",id=base_id + 237, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - King Staff": HereComesNikoLocationData(region="Home",id=base_id + 238, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Mouse": HereComesNikoLocationData(region="Home",id=base_id + 239, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Clown Face": HereComesNikoLocationData(region="Home",id=base_id + 240, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Cat": HereComesNikoLocationData(region="Home",id=base_id + 241, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Bandanna": HereComesNikoLocationData(region="Home",id=base_id + 242, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Stars": HereComesNikoLocationData(region="Home",id=base_id + 243, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Sword": HereComesNikoLocationData(region="Home",id=base_id + 244, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Top hat": HereComesNikoLocationData(region="Home",id=base_id + 245, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Glasses": HereComesNikoLocationData(region="Home",id=base_id + 246, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Flower": HereComesNikoLocationData(region="Home",id=base_id + 247, can_create=lambda options: options.snail_shop.value),
    "Snail Shop - Small Hat": HereComesNikoLocationData(region="Home",id=base_id + 248, can_create=lambda options: options.snail_shop.value),

    #Seedsanity
    "Hairball City - Seed 1": HereComesNikoLocationData(region="Hairball City", id=base_id + 260, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Hairball City - Seed 2": HereComesNikoLocationData(region="Hairball City", id=base_id + 261, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Hairball City - Seed 3": HereComesNikoLocationData(region="Hairball City", id=base_id + 262, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Hairball City - Seed 4": HereComesNikoLocationData(region="Hairball City", id=base_id + 263, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Hairball City - Seed 5": HereComesNikoLocationData(region="Hairball City", id=base_id + 264, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Hairball City - Seed 6": HereComesNikoLocationData(region="Hairball City", id=base_id + 265, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Hairball City - Seed 7": HereComesNikoLocationData(region="Hairball City", id=base_id + 266, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Hairball City - Seed 8": HereComesNikoLocationData(region="Hairball City", id=base_id + 267, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Hairball City - Seed 9": HereComesNikoLocationData(region="Hairball City", id=base_id + 268, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Hairball City - Seed 10": HereComesNikoLocationData(region="Hairball City", id=base_id + 269, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Salmon Creek Forest - Seed 1": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 270, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Salmon Creek Forest - Seed 2": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 271, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Salmon Creek Forest - Seed 3": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 272, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Salmon Creek Forest - Seed 4": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 273, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Salmon Creek Forest - Seed 5": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 274, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Salmon Creek Forest - Seed 6": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 275, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Salmon Creek Forest - Seed 7": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 276, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Salmon Creek Forest - Seed 8": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 277, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Salmon Creek Forest - Seed 9": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 278, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Salmon Creek Forest - Seed 10": HereComesNikoLocationData(region="Salmon Creek Forest", id=base_id + 279, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Bathhouse - Seed 1": HereComesNikoLocationData(region="Bathhouse", id=base_id + 280, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Bathhouse - Seed 2": HereComesNikoLocationData(region="Bathhouse", id=base_id + 281, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Bathhouse - Seed 3": HereComesNikoLocationData(region="Bathhouse", id=base_id + 282, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Bathhouse - Seed 4": HereComesNikoLocationData(region="Bathhouse", id=base_id + 283, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Bathhouse - Seed 5": HereComesNikoLocationData(region="Bathhouse", id=base_id + 284, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Bathhouse - Seed 6": HereComesNikoLocationData(region="Bathhouse", id=base_id + 285, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Bathhouse - Seed 7": HereComesNikoLocationData(region="Bathhouse", id=base_id + 286, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Bathhouse - Seed 8": HereComesNikoLocationData(region="Bathhouse", id=base_id + 287, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Bathhouse - Seed 9": HereComesNikoLocationData(region="Bathhouse", id=base_id + 288, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),
    "Bathhouse - Seed 10": HereComesNikoLocationData(region="Bathhouse", id=base_id + 289, can_create=lambda options: options.seedsanity.value, location_group="Moomy"),

    # Victory
    "You're Hired!": HereComesNikoLocationData(region="Home Party", locked_item="Victory", can_create=lambda options: options.goal_completion.value == 0),
    "Best Employee!": HereComesNikoLocationData(region="Home", locked_item="Victory", can_create=lambda options: options.goal_completion.value == 1)
}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_data_table.items():
    if loc_data.locked_item:
        continue
    loc_group_name = loc_name.split(" - ", 1)[0]
    location_name_groups.setdefault(loc_group_name, set()).add(loc_name)
    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)

location_table = {name: data.id for name, data in location_data_table.items() if data.id is not None}
id_to_location_table = {data.id: name for name, data in location_data_table.items() if data.id is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}



