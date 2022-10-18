from ocf_datapipes.transform.xarray import CreatePVImage
import numpy as np

def test_create_pv_image(passiv_datapipe, sat_datapipe):
    pv_image_datapipe = CreatePVImage(passiv_datapipe, sat_datapipe)
    data = next(iter(pv_image_datapipe))
    print(data)
    assert np.max(data) > 0
