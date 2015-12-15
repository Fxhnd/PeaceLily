"""
@Author Robert Powell
@Module PeaceLily
@Class Stats
"""

def calculate_ttnm(moisture):
    """
    Utility function to calculate days until next watering. Based on a linear
    regression model involving soil moisture and time. Other models do suggest a
    correlation between temp, lux, and humidity but there wasn't enough data to
    get anything really better than the lm.

    :param int moisture
    :return Time till next watering
    :rtype float
    """

    return (m - 875) / 0.0725
