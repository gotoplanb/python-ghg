subregions = {
	"AKGD": 1045.0,
	"AKMS": 527.0,
	"AZNM": 1027.5,
	"CAMX": 498.7,
	"ERCT": 936.1,
	"FRCC": 936.1,
	"HIMS": 1119.1,
	"HIOA": 1682.6,
	"MROE": 1689.7,
	"MROW": 1249.2,
	"NEWE": 527.6,
	"NWPP": 643.4,
	"NYCW": 597.8,
	"NYLI": 1193.1,
	"NYUP": 253.9,
	"RFCE": 720.0,
	"RFCM": 1321.2,
	"RFCW": 1174.0,
	"RMPA": 1281.9,
	"SPNO": 1171.6,
	"SPSO": 1172.8,
	"SRMV": 858.4,
	"SRMW": 1676.8,
	"SRSO": 1033.5,
	"SRTV": 1038.1,
	"SRVC": 747.5,
    "US": 952.9
}

def watts(mw, subregion):
    if subregion in subregions:
	    tco2e = subregions[subregion] * mw
    else:
    	tco2e = subregions["US"] * mw
	
    return tco2e
