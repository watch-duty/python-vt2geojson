import os
from unittest import TestCase

from vt2geojson.tools import vt_bytes_to_geojson

DIRPATH = os.path.dirname(os.path.realpath(__file__))
SAMPLE_FILEPATH = os.path.join(DIRPATH, "sample_14_8185_5449.pbf")
RIVERGAUGES_FILEPATH = os.path.join(DIRPATH, "rivergauges_10_164_394.pbf")

with open(SAMPLE_FILEPATH, "rb") as f:
    sample_content = f.read()

with open(RIVERGAUGES_FILEPATH, "rb") as f:
    rivergauges_content = f.read()


class TestConversions(TestCase):
    def test_bytes_to_geojson_sample(self):
        result = vt_bytes_to_geojson(sample_content, 8185, 5449, 14)
        assert result["features"][0]["properties"] == {
            "left_hand_traffic": True,
            "road_type": "Major road",
            "traffic_level": 0.30000001192092896,
            "traffic_road_coverage": "full",
        }
        assert result["features"][0]["id"] == 0
        assert result["features"][1]["id"] == 0

    def test_bytes_to_geojson_rivergauges(self):
        result = vt_bytes_to_geojson(rivergauges_content, 8185, 5449, 14)
        assert len(result["features"][0]["properties"]) == 8
        assert result["features"][0]["id"] == 50
        assert result["features"][1]["id"] == 2735
