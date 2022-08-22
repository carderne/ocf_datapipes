from ocf_datapipes.load import OpenSatellite
from ocf_datapipes.transform.xarray import ConvertSatelliteToInt8

def test_convert_satellite_to_int8():
    sat_dp = OpenSatellite(zarr_path="tests/data/hrv_sat_data.zarr")
    sat_dp = ConvertSatelliteToInt8(sat_dp)
    data = next(iter(sat_dp))
    print(data)

