Title: TESS Data Products Information
template: slide
save_as: data_products.html

<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.collapsible {
  background-color: #777;
  color: white;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
}

.active, .collapsible:hover {
  background-color: #555;
}

.content {
  padding: 0 18px;
  display: none;
  overflow: hidden;
  background-color: #f1f1f1;
}
</style>
</head>

<body>

The four cameras of TESS take consecutive images of a particular region of the sky every 2 seconds. Several data products are produced by the TESS mission from these images: <a href="https://archive.stsci.edu/missions-and-data/tess" target="_blank">Target Pixel Files (TPFs, also known as postage stamps) of selected targets, corresponding Light Curves (LCs), and Full Frame Images (FFIs)</a>. 

Each of these is created on-board the spacecraft by co-adding the individual 2-second exposures. These data products are provided in standard FITS format with multiple extensions which contain additional information on calibration, background removal, cosmic-ray rejection, and in the case of the TPFs aperture masks indicating the pixels used to extract the lightcurve. For more information, see the <a href = "https://archive.stsci.edu/missions-and-data/tess/data-products" target = "_blank"> TESS mission page at MAST </a>, the <a href="https://ui.adsabs.harvard.edu/abs/2016SPIE.9913E..3EJ/abstract" target="_blank"> TESS pipeline </a>, as well as the slideshow presented below.

<br></br>

<h2>Types of TESS Data Products</h2>

<button type="button" class="collapsible">Target Pixel Files [TPF]</button>
<div class="content">
    <br>The Target Pixel Files are the rawest form of target-specific data available at MAST. For each short-cadence target in an observing sector, TESS only acquires the pixels contained within a predefined mask. These pixels are used to create the data found in the light curve files.Each TPF packages these pixels as a time series of images in a binary FITS table. In this binary table, the pixel values are encoded as images. Each element in the binary table contains the pixels from a single cadence. The purpose of these files is to provide the data necessary to perform photometry on the raw or calibrated data when needed (or desired) to understand (or improve) the automated results of the TESS pipeline.
    </br>
    <br>
    If a target is observed in more than one sector, multiple TPFs will be created for that target. Note that they may be made available in separate deliveries to the MAST.
    </br>
    <br>
    The images in the TPF will have dimensions equal to the bounding box of the pixels that were collected for that target. Depending on the location of the target on a CCD, a TPF may therefore contain pixels that do not contain stored data.
    </br>
    <br>
    TPFs will have several HDUs: a primary header, a binary table of images header and data, the aperture mask image header and data, and the cosmic ray correction binary table header and data. The aperture mask image provided with each TPF file indicates the pixels that were collected for the target and which of those pixels were used for photometry.
    </br>
    <br>
    An example TPF is shown in the figure below for TIC 25375553. To learn more about TPFs and how to use them please see <a href = "https://github.com/spacetelescope/notebooks/blob/master/notebooks/MAST/TESS/beginner_how_to_use_tp/beginner_how_to_use_tp.ipynb" target = "_blank">this tutorial</a>
    <img src="images/data/tess_tpf.png" class="center"></img>
    </br>
</div>

<button type="button" class="collapsible">Light Curve Files [LCFs or LCs]</button>
<div class="content">
    <br>
    Lightcurves are flux time-series produced for each short-cadenced target (from the TPFs) using Simple Aperture Photometry (SAP). LCs are used to search for transiting planets and other astrophysical phenomena. TESS light curves are FITS format files that contain the output of the photometric extraction and subsequent systematics removal (cotrending) performed by the SPOC algorithms. The flux and respective uncertainties are provided at each cadence, with NaNs filling in any missing data values.
    </br>
    <br>
    A single Light Curve File contains the data for one target for on observing sector. Identical to the case for TPFs, if a target was observed in more than one TESS sector, multiple Light Curve Files will be created but they may be made available on the MAST in separate deliveries. Light Curve Files will also consist of several HDUs: a primary header, the light curve photometry binary table header and data, and the aperture mask image header and data. The aperture mask image provided with each light curve is the same as that provided with the corresponding target TPF file.
    </br>
    <br>
    An example LC is shown in the figure below for TIC 25375553, Sector 1. To learn more about LCFs and how to use them please see <a href = "https://github.com/spacetelescope/notebooks/blob/master/notebooks/MAST/TESS/beginner_how_to_use_lc/beginner_how_to_use_lc.ipynb" target = "_blank">this tutorial </a>
    <img src="images/data/TIC_25375553_S1.png" class="center"></img>
</div>

<button type="button" class="collapsible">Full Frame Images [FFIs]</button>
<div class="content">
    <br>
    FFIs are a collection of science and collateral pixels observed simultaneously. A single FFI is the full set of all science and collateral pixels across all CCDs of a given camera. Note that there are 16 CCDs on the spacecraft, each of which is supported by 4 output channels.
    </br>
    <br>
    FFIs are FITS format files containing all pixels on a single CCD. The FFI data is provided in three types: uncalibrated, calibrated, and uncertainty. The uncalibrated FFI data is provided in one file with two Header/Data Units (HDUs): a primary header and the CCD image header and data. The calibrated FFI data and its uncertainty are provided in a separate file with several HDUs: a primary header, the CCD calibrated image header and data, the CCD uncertainty image header and data, and the cosmic ray corrections binary table header and data.
    </br>
    <br>
    Note that Cosmic Ray Mitigated FFIs are the same as FFIs except they are collected with the onboard cosmic ray mitigation enabled.
    </br>
    <br>
    The FFIs have observational cadence of 30 minutes (Cycles 1 and 2), 10 minutes (Cycles 3 and 4), and 200 seconds (Cycles 5 and 6).
    </br>
    <br>
  To learn more about FFIs and how to use them please see <a href = "https://github.com/spacetelescope/notebooks/blob/master/notebooks/MAST/TESS/beginner_how_to_use_ffi/beginner_how_to_use_ffi.ipynb" target = "_blank">this tutorial </a>
</div>

<button type="button" class="collapsible">Engineering Data</button>
<div class="content">
    <button type="button" class="collapsible"><i>Cotrending Basis Vectors [CBVs]</i></button>
    <div class="content">
        <br>
        Co-trending basis vectors (CBVs) represent the set of systematic trends present in the ensemble flux data.CBVs are provided for each operational sector of the mission.
        </br>
        <br>
        CBVs are calcualted by the TESS pipeline from a Principle Component Analysis and used to mitigate systematic artifacts within the target light curves. CBVs can be utilized for manual photometric correction more tailored towards the user's science.
        </br>
    </div>
    <button type="button" class="collapsible"><i>Auxiliary Data Products</i></button>
    <div class="content">
        <br>
        Focal plane characterization files, engineering and telemetry data used to calibrate the images and determine the status of the spacecraft.
        </br>
        <br>
        Black level: the mean correction estimated from the virtual black pixel values. There is one metric value per cadence for each CCD readout.
        </br>
        <br>
        2-D black model: the expected readout of a given CCD, in counts, which is observed when no light is incident upon the detector. The model is subtracted from the raw pixel values as part of the calibration process. The model also incorporates the expected black values of collateral pixels. Each CCD has a separate 2-D black model. The size of the model is 2078 x 2136 for each CCD.
        </br>
        <br>
        Smear: correction for shutterless operation. The smear will be less critical for TESS than was needed for Kepler due to the use of frame-transfer in TESS.
        </br>
        <br>
        Gain model: linear approximation to the CCD digitizer performance, in units of photoelectrons per digitizer count. Each TESS CCD has its own gain model containing separate values for each of the 4 readouts on the CCD.
        </br>
        <br>
        Flat field: a model describing the pixel-to-pixel variation in response to photons. This allows the variations in individual pixel response to be removed during calibration. The flat field model is 2048 x 2048 for each CCDs.
        </br>
        <br>
        Linearity: a model describing the deviations from linearity of the CCD digitizers. Each CCD has its own linearity model with separate values for each of the 4 readouts on the CCD. The linearity model is used in conjunction with the gain model of each CCD to convert from a measured number of counts to a flux in photoelectrons.
        </br>
        <br>
        Read noise: an estimate of the variation in pixel values caused by the digitization process itself. This is separate from the noise due to Poisson variation in the number of photons collected from a target (``shot noise''). The read noise model is used in the calibration process to estimate the uncertainty in pixel values, which is incorporated into the uncertainty propagation process. Each CCD has its own read noise model with separate values for each of the 4 readouts on the CCD.
        </br>
        <br>
        Dark current: the mean dark current calculated from the virtual row pixel values. There is one metric value per cadence for each readout. 
        </br>
        <br>
        See MAST for a full list is available auxiliary products.
        </br>
    </div>
    <button type="button" class="collapsible"><i>Collateral Data</i></button>
    <div class="content">
        <br>
        Includes pixels from leading and trailing virtual columns, leading and trailing masked rows, and trailing virtual rows (in units of ADC counts).
        </br>
        <br>
        Additional collateral data includes auxiliary instrument models which describe the calibration effects.
        </br>
        <br>
        Pixel calibration is performed on both the cadence pixels and Full Frame Image (FFI) pixels, and calibrated science pixel values, in photoelectrons, along with their uncertainties are archived at the MAST.            
        </br>
    </div>
    <button type="button" class="collapsible"><i>Simulated Data</i></button>
    <div class="content">
        <br>
        During the development of a space mission, several End-to-End tests are conducted, which include testing the pipeline and the data transfer between different institutions. To do this various data products are simulated, these data can be very useful to the community, and aid potential TESS users in the development of tools and in assessing the feasibility of an investigation.
        </br>
        <br>
        Data for the "End-To-End 6" can be found <a href = "https://archive.stsci.edu/missions-and-data/tess/data-products/ete-6" target = "_blank">here.</a>              
        </br>
    </div>
</div>

<button type="button" class="collapsible">TESS Data Product Workflow</button>
<div class="content">
    <br>The TESS pixel size is 21 arcsec. Below you can see a comparison between TESS pixels and those from several larger telescopes.
    <img src="https://heasarc.gsfc.nasa.gov/docs/tess/images/data/ciardi_target_pixels.png" width="60%;" class="center"></img>
    </br>
    <br>
    TESS identifies targets from a target list onboard the computer, and selects small pixel cut outs around those regions. The FFIs and pixel cut outs are downlinked. The FFIs are then sent to the MAST archive; the pixel cut outs are processed by SPOC into TPFs, and then LCFS. The process is illustrated below.
    <img src="https://heasarc.gsfc.nasa.gov/docs/tess/images/tess_ffi_phot.png" class="center"></img>
    </br>  
</div>


<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
</script>

</body>
</html>