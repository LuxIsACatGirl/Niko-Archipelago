from . import HereComesNikoTestBase


class TestDefault(HereComesNikoTestBase):
    options = {}


class TestHiredGoal(HereComesNikoTestBase):
    options = {
        "GoalCompletion": 0
    }


class TestEmployeeGoal(HereComesNikoTestBase):
    options = {
        "GoalCompletion": 1
    }


# class TestGardenAccess(HereComesNikoTestBase):
#     options = {
#         "GarysGardenAccess": 0
#     }
#
#     def test_garden_access(self) -> None:
#         """Test access to Gary's Garden"""
#         locations = ["Gary's Garden - Cassette 1",
#                      "Gary's Garden - Cassette 2",
#                      "Gary's Garden - Cassette 3",
#                      "Gary's Garden - Cassette 4",
#                      "Gary's Garden - Cassette 5",
#                      "Gary's Garden - Cassette 6",
#                      "Gary's Garden - Cassette 7",
#                      "Gary's Garden - Cassette 8",
#                      "Gary's Garden - Cassette 9",
#                      "Gary's Garden - Cassette 10"]
#         items = [["Tadpole HQ Ticket"]]
#         self.assertAccessDependency(locations, items, True)


class TestFischerAccess(HereComesNikoTestBase):
    options = {
        "Fishsanity": 1
    }

#     def test_hcfish(self) -> None:
#         """Test locations that require fish"""
#         locations = ["Hairball City - Fish with Fischer"]
#         items = [["Hairball City fish"]]
#         self.assertAccessDependency(locations, items)
#
#     def test_ttfish(self) -> None:
#         """Test locations that require fish"""
#         locations = ["Turbine Town - Fish with Fischer"]
#         items = [["Turbine Town fish"]]
#         self.assertAccessDependency(locations, items)
#
# def test_sfcfish(self) -> None:
#     """Test locations that require fish"""
#     locations = ["Salmon Creek Forest - Fish with Fischer"]
#     items = [["Salmon Creek Forest - Bass",
#      "Salmon Creek Forest - Catfish",
#      "Salmon Creek Forest - Pike",
#      "Salmon Creek Forest - Salmon",
#      "Salmon Creek Forest - Trout",]]
#     self.assertAccessDependency(locations, items)
#
#     def test_ppfish(self) -> None:
#         """Test locations that require fish"""
#         locations = ["Public Pool - Fish with Fischer"]
#         items = [["Public Pool fish"]]
#         self.assertAccessDependency(locations, items)
#
#     def test_bathfish(self) -> None:
#         """Test locations that require fish"""
#         locations = ["Bathhouse - Fish with Fischer"]
#         items = [["Bathhouse fish"]]
#         self.assertAccessDependency(locations, items)
#
#     def test_hqfish(self) -> None:
#         """Test locations that require fish"""
#         locations = ["Tadpole HQ - Fish with Fischer"]
#         items = [["Tadpole HQ fish"]]
#         self.assertAccessDependency(locations, items)
