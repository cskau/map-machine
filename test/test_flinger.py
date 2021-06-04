"""
Test coordinates computation.
"""
import numpy as np

from roentgen.flinger import (
    pseudo_mercator,
    osm_zoom_level_to_pixels_per_meter,
)

__author__ = "Sergey Vartanov"
__email__ = "me@enzet.ru"


def test_pseudo_mercator() -> None:
    """
    Test pseudo-Mercator projection.
    """
    assert np.allclose(pseudo_mercator(np.array((0, 0))), np.array((0, 0)))
    assert np.allclose(pseudo_mercator(np.array((0, 10))), np.array((10, 0)))
    assert np.allclose(
        pseudo_mercator(np.array((10, 0))), np.array((0, 10.05115966))
    )


def test_osm_zoom_level_to_pixels_per_meter() -> None:
    """
    Test scale computation.
    """
    assert np.allclose(
        osm_zoom_level_to_pixels_per_meter(18), 1.6759517949045808
    )