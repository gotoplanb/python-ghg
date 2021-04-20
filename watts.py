def watts(mw, subregion):
    if subregion == "AKGD":
        co2 = 1045.0 * mw
    elif subregion == "FRCC":
        co2 = 936.1 * mw
    else:
        co2 = 952.9 * mw

    return co2
