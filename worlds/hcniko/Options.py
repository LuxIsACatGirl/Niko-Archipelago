from dataclasses import dataclass
from Options import Toggle, StartInventoryPool, DeathLink, PerGameCommonOptions, Choice, Range, DefaultOnToggle


def adjust_options(world):
    if world.options.max_kiosk_cost < world.options.min_kiosk_cost:
        world.options.max_kiosk_cost.value, world.options.min_kiosk_cost.value = \
         world.options.min_kiosk_cost.value, world.options.max_kiosk_cost.value

    if world.options.max_elevator_cost < world.options.min_elevator_cost:
        world.options.max_elevator_cost.value, world.options.min_elevator_cost.value = \
         world.options.min_elevator_cost.value, world.options.max_elevator_cost.value

    tot_coins: int = total_coins(world)
    if world.options.max_kiosk_cost > tot_coins - 6:
        world.options.max_kiosk_cost.value = min(70, tot_coins - 6)

    if world.options.min_kiosk_cost > tot_coins - 6:
        world.options.min_kiosk_cost.value = min(70, tot_coins - 6)

    if world.options.max_elevator_cost > tot_coins:
        world.options.max_elevator_cost.value = min(79, tot_coins)

    if world.options.min_elevator_cost > tot_coins:
        world.options.min_elevator_cost.value = min(79, tot_coins)

def total_coins(world) -> int:
    count: int = 76
    if world.options.shuffle_garys_garden.value:
        count += 3

    return count

class ShuffleKioskReward(DefaultOnToggle):
    """Choose whether to shuffle the Kiosk to NOT give the next Ticket but instead something else.
    Compatible with 'Start with Ticket'.
    Check the in-game Tracker for Kiosk Cost and if you bought it."""
    display_name = "Shuffle Kiosk Reward"


class StartWithTicket(DefaultOnToggle):
    """You'll start with a random Ticket. Highly recommended as there are only 3 checks at Home!"""
    display_name = "Start with Ticket"


class EnableAchievements(Choice):
    """Enables if Achievements should be a location.
    Frog Fan only needs 10 bumps & Volley Dreams only needs a highscore of 5 in every level."""
    display_name = "Enable Achievements"
    option_all_achievements = 0
    option_except_snail_fashion_show = 1
    option_disabled = 2
    default = 2


class ShuffleHandsomeFrog(Toggle):
    """Enables if talking to Handsome Frog should be a location."""
    display_name = "Shuffle Handsome Frog"


class ShuffleGarysGarden(DefaultOnToggle):
    """Choose whether Gary's Garden should have locations."""
    display_name = "Shuffle Gary's Garden"


class GarysGardenAccess(Choice):
    """Changes when Gary's Garden is accessible.
    Tadpole HQ: Gary's Garden will be accessible when Tadpole HQ is accessible.
    -----------------------------------------------------------
    Tadpole HQ & Gary's Garden: Gary's Garden won't be accessible until Tadpole HQ Ticket & Gary's Garden Ticket are obtained.
    -----------------------------------------------------------
    Gary's Garden: Gary's Garden will be accessible in 'Home' when Gary's Garden Ticket has been obtained."""
    display_name = "Gary's Garden Access"
    option_tadpole_hq = 0
    option_tadpole_and_garden = 1
    option_garden = 2
    default = 1


class KeysLevelBased(Toggle):
    """If this option is enabled, Keys will be specific to the level.
    Hairball City Keys only open Hairball City Locks, Turbine Town Keys only open Turbine Town Locks etc."""
    display_name = "Level Specific Keys"


class GoalCompletion(Choice):
    """Set your Completion Goal.
    Hired: Reach Pepper's Interview and get hired!
    Employee: Get 76 Coins and be the Employee Of The Month!"""
    display_name = "Completion Goal"
    option_hired = 0
    option_employee = 1
    default = 0


class MinKioskCost(Range):
    """Determines the lowest possible cost for a Kiosk.
    Disabled if 'Shuffle Kiosk Reward' is false"""
    display_name = "Minimum Kiosk Cost"
    range_start = 0
    range_end = 55
    default = 1


class MaxKioskCost(Range):
    """Determines the highest possible cost for a Kiosk.
    Disabled if 'Shuffle Kiosk Reward' is false"""
    display_name = "Maximum Kiosk Cost"
    range_start = 20
    range_end = 70
    default = 38


class MinElevatorCost(Range):
    """Determines the lowest possible cost for the elevator"""
    display_name = "Minimum Elevator Repair Cost"
    range_start = 0
    range_end = 79
    default = 46


class MaxElevatorCost(Range):
    """Determines the highest possible cost for the elevator"""
    display_name = "Maximum Elevator Repair Cost"
    range_start = 0
    range_end = 79
    default = 46


class CassetteLogic(Choice):
    """This changes how Mitch & Mai work

    LevelBased: Cassettes have been split up into level specific variants.
    So you need 'Hairball City Cassette' 5x/10x to trade with Mitch/Mai in Hairball City.
    -----------------------------------------------------------
    Progressive: Mitch and Mai require increasing numbers of cassettes to unlock their locations.
    Unlock order is fixed: The number of cassettes needed progresses incrementally -> 5 -> 10 -> 15 -> 20 -> 25.
    The in-game Cassette Tracker shows from left to right your progress.
    When you buy the first progressive unlock, the first Mitch/Mai icon will be marked as purchased.
    If Gary's Garden is shuffled -> The tracker starts at Gary's Garden. If not shuffled -> The tracker starts at Hairball City.
    -----------------------------------------------------------
    Scattered: Prices are randomly shuffled between all Mitch & Mai Locations."""
    display_name = "Cassette Logic"
    option_Level_Based = 0
    option_progressive = 1
    option_scattered = 2
    default = 2


class ProgressiveContactList(DefaultOnToggle):
    """If this option is enabled, the Contact Lists will not be separate, so you cannot get Contact List 2 before Contact List 1."""
    display_name = "Progressive Contact List"


class SnailShopLocations(Toggle):
    """When enabled the clothes shop from the Tamagotchi Snail will contain AP Items."""
    display_name = "Snail Shop"


class Fishsanity(Choice):
    """Need more checks or are you just insane?
    Vanilla: Normal Here Comes Niko! behaviour
    -----------------------------------------------------------
    Location: Every single fish you can fish with Fischer is a unique location
    -----------------------------------------------------------
    Insanity: Same as location with the change that Fischer won't give you the 'Fish with Fischer' item until you have all 5 fish for that level obtained.
    So you need the item 'Hairball City Fish' 5x before being able to obtain Fischer's reward in Hairball City.
    Check the in-game menu, to see if you have enough fish and obtained the reward from Fischer."""
    display_name = "Fishsanity"
    option_vanilla = 0
    option_location = 1
    option_insanity = 2
    default = 0


class Seedsanity(Choice):
    """Need more checks or are you just insane?
    Vanilla: Normal Here Comes Niko! behaviour
    -----------------------------------------------------------
    Location: Every single seed you can collect with the hamster ball is a unique location
    -----------------------------------------------------------
    Insanity: Same as location with the change that Moomy won't give you the reward for collecting all seeds until you have been sent all 10 seeds for that level.
    So you need the item 'Hairball City Seed' 10x before being able to obtain Moomy's reward in Hairball City.
    Check the in-game menu, to see if you have enough seeds and obtained the reward from Moomy."""
    display_name = "Seedsanity"
    option_vanilla = 0
    option_location = 1
    option_insanity = 2
    default = 0


class Flowerbedsanity(Choice):
    """Need more checks or are you just insane?
    Vanilla: Normal Here Comes Niko! behaviour
    -----------------------------------------------------------
    Location: Every single flower bed is a unique location
    -----------------------------------------------------------
    Insanity: Same as location with the change that Little Gabi won't give you the reward for completing all flower beds until you have been sent all flowers for that level.
    So you need the item 'Hairball City Flower' 3x before being able to obtain Little Gabi's reward in Hairball City.
    Check the in-game menu, to see if you have enough flowers and obtained the reward from Little Gabi."""
    display_name = "Flowersanity"
    option_vanilla = 0
    option_location = 1
    option_insanity = 2
    default = 0


class Applesanity(Toggle):
    """Need more checks or are you just insane?
    When enabled, freestanding apples will be randomized.
    This adds ~290 locations."""
    display_name = "Applesanity"


# class NPCsanity(Toggle):
#     """Need more checks or are you just insane?
#     When enabled, NPCs will be randomized, and will contain items, but you will need to unlock them with the corresponding item.
#     So you need the item 'Hairball City NPCs' to unlock them and be able to talk to them."""
#     display_name = "NPCsanity"


class HCNDeathLink(DeathLink):
    """When somebody dies the level will be reloaded"""

@dataclass
class HereComesNikoOptions(PerGameCommonOptions):
    shuffle_kiosk_reward: ShuffleKioskReward
    start_with_ticket: StartWithTicket
    enable_achievements: EnableAchievements
    shuffle_handsome_frog: ShuffleHandsomeFrog
    shuffle_garys_garden: ShuffleGarysGarden
    access_garys_garden: GarysGardenAccess
    level_based_keys: KeysLevelBased
    cassette_logic: CassetteLogic
    progressive_contact_list: ProgressiveContactList
    snail_shop: SnailShopLocations
    fishsanity: Fishsanity
    seedsanity: Seedsanity
    flowersanity: Flowerbedsanity
    applesanity: Applesanity
#    npcsanity: NPCsanity
    goal_completion: GoalCompletion
    min_kiosk_cost: MinKioskCost
    max_kiosk_cost: MaxKioskCost
    min_elevator_cost: MinElevatorCost
    max_elevator_cost: MaxElevatorCost
    start_inventory_from_pool: StartInventoryPool
    death_link: HCNDeathLink