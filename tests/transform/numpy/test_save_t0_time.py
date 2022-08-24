from ocf_datapipes.transform.numpy import EncodeSpaceTime, AlignGSPto5Min, SaveT0Time
from ocf_datapipes.batch import MergeNumpyModalities
from ocf_datapipes.utils.consts import BatchKey

def test_save_t0_time(sat_hrv_np_dp, passiv_np_dp, gsp_np_dp):
    combined_dp = MergeNumpyModalities([sat_hrv_np_dp, gsp_np_dp, passiv_np_dp])
    combined_dp = AlignGSPto5Min(combined_dp, batch_key_for_5_min_datetimes=BatchKey.hrvsatellite_time_utc)
    combined_dp = EncodeSpaceTime(combined_dp)
    combined_dp = SaveT0Time(combined_dp)
    data = next(iter(combined_dp))
