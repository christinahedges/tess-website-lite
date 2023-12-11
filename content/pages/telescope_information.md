Title: TESS Telescope Information TEST
template: slide
save_as: telescope_information.html

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

<p>The TESS observatory consists of the spacecraft and the payload. The TESS payload has a single instrument, a camera suite composed of 4 wide field-of-view optical cameras and their associated hoods, mount, sun shield, and Data Handling Unit (DHU). The payload is coupled to the spacecraft, an NGIS LEOStar-2/750 satellite bus. The spacecraft provides power (via two deployable solar arrays), attitude control, data storage, and communications/transmission. </p>


<button type="button" class="collapsible"> Spacecraft </button>
<div class="content">
  <br>The TESS spacecraft is an NGIS LEOStar-2/750 satellite bus which provides power, attitude control, data storage, and communications/transmission. The spacecraft was built by <a href = "https://www.northropgrumman.com/"> Northrop Grumman Innovation Systems </a> in Dulles, VA, where the Mission Operations Center (MOC) is located.</br>
  <br>Power is supplied by two deployable solar array wings that are capable of providing 415 W of total power. The estimated requirement of the observatory is 290 W. The bus is equipped with a Ka-band transmitter coupled to an 0.7m body-fixed high-gain antenna. The transmitter operates on 2 W of power and transfers data at a rate of at 100 Mb/s, sufficient to downlink science data during 4-h intervals at each orbit perigee. Spacecraft attitude is controlled through a zero-momentum attitude control system with a three-axis hydrazine monopropellent propulsion system and 2 star trackers. The fine pointing of the observatory is achieved through four reaction wheels and high-precision quaternions produced by the science cameras.</br>
  <br/><img class="img-responsive" style="max-width:67%;" src="images/data/TESS_alone_high_res.jpg"><br/>*The TESS spacecraft and payload ready for launch. Image Credit: MIT*
  <br/><img class="img-responsive" style="max-width:67%;" src="images/data/spacecraft_orbital.png"><br/>*Image Credit: Northrop Grumman Innovation Systems*
</div>

<button type="button" class="collapsible"> Payload </button>
<div class="content">
  <br>The TESS payload is coupled to the spacecraft and has a single instrument -- a camera suite composed of 4 identical wide field-of-view optical cameras and their associated hoods, mount, sun shield, and Data Handling Unit (DHU). The four cameras cover a combined field-of-view (FOV) of 24x96 degrees (known as an observing sector). Each camera consists of a CCD detector assembly, a lens assembly, and a lens hood. An overview of the FOV coverage is shown below.</br>
  <br/><img class="img-responsive" style="max-width:48%;" src="images/data/tess_observingsectorschematic_Winnpresentation.jpg"><br/>
  <br/><img class="img-responsive" style="max-width:48%;" src="images/data/tess_cameraFOVschematic_Winnpresentation.png"><br/>

  <button type="button" class="collapsible"> Lens Assembly </button>
  <div class="content">
    The lens assembly is a custom design housing seven lenses mounted into two separate aluminum barrels that are fastened together. The lens assembly has a 10.5 cm diameter entrance pupil and a focal ratio  f/1.4. All optical elements have antireflection coatings and one element has a long-pass filter coating to enforce a short-wavelength cutoff at 600 nm in the  TESS  bandpass. Each camera forms a 24x24 un-vignetted image on the detector in its focal plane. The lens assemblies were designed for consistent image spot size across the field-of-view (FOV) and to produce under-sampled images similar to  Kepler. Operating at nominal focus and a flight temperature of -75 degrees C, the 50% ensquared-energy half-width is 15 micron averaged over the FOV. This corresponds to 1 detector pixel or 21 arcseconds (approx. 0.35 arcmin) on sky. Along with an internal stray light baffle, each lens assembly aperture is equipped with a hood to reduce scattered light from the Earth and Moon.
    <img class="img-responsive" style="max-width:67%;" src="images/data/tess_camera.png">*Image Credit: MIT*
    <img class="img-responsive" style="max-width:75%;" src="images/data/tess_lens_assembly.png">  *The TESS Payload. Image Credit: MIT*
  </div>

  <button type="button" class="collapsible"> CCD detector assembly </button>
  <div class="content">
    The detector assembly in each camera consists of a focal plane CCD array and associated electronics. Each CCD array contains four back-illuminated MIT/Lincoln Laboratory CCID-80 devices. The deep-depletion, frame-transfer CCDs consist of a 2048 x 2048 imaging array and a 2048 x 2048 frame-store region (for rapid shutterless readout 4 ms) with 15 x 15 micron pixels. The four CCDs in each array are separated by 2mm and create an effective 4096 x 4096 pixel detector that is operated at -75 degrees C to reduce dark current. The detectors are read out at 625 kHz with < 10 e- read noise. The detector electronics consist of two compact double-sided printed circuit boards seated beneath the CCD focal plane. The electronics transmit digitized data over a serial LVDS link to the Data Handling Unit. The four TESS cameras are bolted to a common plate such that their FOV's are aligned to form a total simultaneous FOV of 24x96 degrees.</br>
    <br/><img class="img-responsive" style="max-width:90%;" src="images/data/tess_detector_assembly.png">
    <br/> *TESS CCD mosaic in mounting bracket (left). TESS CCD mosaic and focal plane electronics with frame store regions covered (right). Image credit: MIT*
    <br>Here you can see a schematic diagram of one TESS CCD.</br>
    <br><img src="https://heasarc.gsfc.nasa.gov/docs/tess/images/data/tess_ccd.png" width="60%;" class="center"></img></br>  
  </div>

  <button type="button" class="collapsible"> Data Handling Unit (DHU) </button>
  <div class="content">
    The TESS Data Handling Unit (DHU) provides the hardware, software, and firmware for camera control, on-board data processing, data storage, spacecraft avionics, and ground communications. The DHU is manufactured by SEAKR Engineering, Inc. and consists of an Athena-3 Single Board Computer, an RCC5 module, an FMC-Gen3 192 gigabyte solid state recorder (SSR), a low voltage power supply, and other ancillary components. During science operations, the four TESS cameras produce a continuous stream of images with an exposure time of 2 s. The DHU performs real time processing on these data to convert raw CCD images into data products responsible for ground post-processing. This includes cosmic ray mitigation and collecting pixel sub-arrays for postage stamp targets and image stacks for the FFIs. The DHU also calculates photometric centroids from around 200 photometric guide stars from each 2 s image from each camera. These data are used to calculate offset quaternions for fine attitude pointing control by the Master Avionics Unit (MAU). Data downlink via the Ka-band antenna is also controlled by the DHU. Data stored on the SSR are downlinked every 13.7 days at orbit perigee.
  </div>

  <button type="button" class="collapsible"> Summary specifications </button>
  <div class="content">
    <img class="img-responsive" style="max-width:90%;" src="images/data/tess_camera_specs.png"><br/>*Characteristics of the TESS cameras. Ensquared energy is the fraction of the total energy of the point-spread function (PSF) that is within a square of the given dimensions centered on the peak. Image Credit: MIT*
  </div>

  <button type="button" class="collapsible"> Bandpass </button>
  <div class="content">
    <br>The TESS detector bandpass spans from 600 - 1000 nm and is centered on the traditional Cousins I-band (I_C, central wavelength  = 786.5 nm). This wide, red-optical bandpass is preferred to reduce photon-counting noise and increase sensitivity to small planets transiting cool, red stars.</br>
    <br>
    The long wavelength end represents the red-limit of the CCD detectors and is set by their quantum efficiency. The short wavelength end is set by a long-pass filter coating on one of the camera lenses.</br> <br/><img class="img-responsive" style="max-width:67%;" src="images/data/tess_bandpass.png">*The TESS spectral response function (black line), defined as the product of the long-pass filter transmission curve and the detector quantum efficiency curve. Also plotted, for comparison, are the Johnson-Cousins V, RC, and I_C filter curves and the Sloan Digital Sky Survey z filter curve. Each of the functions has been scaled to have a maximum value of unity. Image Credit: Ricker et al. (2015)*<br/>
    <br>
    In contrast to Kepler, the TESS bandpass is comparably wide but covers redder wavelengths, reflecting the differing target priorities of the two missions (Sun-like stars for Kepler; small, cool stars for TESS). The width of 400 nm was the largest practical choice for the optical design. A comma separated variable file with the bandpass response function is available <a href="https://heasarc.gsfc.nasa.gov/docs/tess/data/tess-response-function-v2.0.csv" target="_blank"> here </a>. <br/><img class="img-responsive" style="max-width:67%;" src="images/data/tess_vs_kepler_bandpass.png"><br/>TESS monitors a much larger sample of M stars compared to Kepler, thus the bandpass extends further to red wavelengths. Image Credit: Zach Berta-Thompson with data from Sullivan at al. (2015). 
    </br>
  </div>

  <p>Below you can find information on the photometric performance of TESS, including major sources of noise, saturation, systematic effects, pixel-response-function, etc. Additional information can be found in the <a href = "https://archive.stsci.edu/missions/tess/doc/TESS_Instrument_Handbook_v0.1.pdf" target = "_blank"> TESS Instrument Handbook </a> and in the <a href = "https://archive.stsci.edu/tess/tess_drn.html" target = "_blank"> Data Release Notes </a>.</p>

  <button type="button" class="collapsible">Typical noise levels</button>
  <div class="content">
  <table>
    <tr>
      <th colspan="2" style="font-size: 28px;"></th>
    </tr>
    <tr>
      <td width="50%">
          <br>The typical photometric uncertainties are dominated by pointing jitter, which are at the level of 60 ppm on hourly timescales</br>
          <br>The best light curves are well below the mission requirements of (1) a systematic error floor at 50 ppm for stars with Tmag = 9-15 and (2) 230 ppm at Tmag = 10 mag, which is sufficient to detect super-Earths around bright stars.</br>
          <br>For fainter stars with Tmag = 16, the photometric precision drops to about 1%, which is still sufficient for many astrophysical studies such as supernovae and stellar variability. </br>
          <br>The figure on the right shows the 1-hour Combined Differential Photometric Precision (CDPP) measured from TESS Sector 1. The typical noise achieved in each individual TESS sector is described in the <a href = "https://archive.stsci.edu/tess/tess_drn.html" target = "_blank"> Data Release Notes </a>.</br>
            <br>The red points represent the RMS CDPP measurements for the 15,889 light curves from Sector 1 plotted as a function of TESS magnitude. </br>
            <br>The blue x's represent the uncertainties, scaled to a 1-hour timescale. </br>
            <br>The purple curve represents a moving 10th percentile of the RMS CDPP measurements, and the gold curve represetns a moving median of the 1-hour uncertainties.</br>
      </td>
      <td width="50%"><img src="https://heasarc.gsfc.nasa.gov/docs/tess/images/giprogram/cdpp_sector1.png"></img></td>
    </tr>
  </table>
  </div>

  <button type="button" class="collapsible">Saturation</button>
  <div class="content">
  <table>
    <tr>
      <th colspan="2" style="font-size: 28px;"></th>
    </tr>
    <tr>
      <td width="50%">
            <br>For bright stars the amount of charge generated by photons can exceed the full well capacity of a pixel. When this occurs, electrons begin to spill over into adjacent pixels along the same column, i.e. "blooming" (the charge barrier in the CCD is much lower along the columns). In many cases, the distribution of charge along the column that has a bright star, causing blooming, has humps at both ends of the bloomed part of the image (See figure on the right).</br>
            <br>The amount of charge deposited by a star of magnitude Tmag into the peak pixel depends on the fraction of the total charge in the peak pixel: this value generally ranges from 0.2 to 0.4 in the TESS images. The TESS cameras create 15,000 e-/s for a star of Tmag = 10. Thus, a star of Tmag = 5 will create 3 x 10<sup>6</sup> electrons in a two-second exposure.</br>
            <br>For a flux fraction of 0.3, the charge in the peak pixel is 9 x 10<sup>5</sup> electrons, leading to a bloom length of 5 rows; similarly, a star of Tmag = 2.5 will create a bloom of 50 rows. A key feature of the CCID-80 CCDs used on TESS is their ability to conserve charge even from very saturated stars. Charge will be conserved for stars at least as bright I<sub>c</sub> = 4 mag.</br>
            <br>Saturation is anticipated in the central pixel at I<sub>c</sub> = 7.5 mag. This, however, does not represent the bright limit for precise photometry. Excess charge from saturated pixels is conserved and spread across adjacent pixels in a CCD column until the excess reaches a CCD boundary. This leads to "bleed trails" extending above and below a saturated pixel, similar to what is seen for bright stars in Kepler/K2 photometry. Precision photometry can still be achieved by creating a photometric aperture that is large enough to encompass all excess charge.</br>
            <br>Cadences with bad calibrations due to saturation are explicitly marked with bit 15 from Sector 68 (value 16384, "Bad Calibration Exclude")</br>
      </td>
      <td width="50%"><img src="images/data/saturation.png"></img></td>
    </tr>
  </table>
  </div>

  <button type="button" class="collapsible">Pixel Response Function</button>
  <div class="content">
        <br>Instead of a point-spread-function, TESS has a pixel response function (PRF). The PRF gives the 2-D distribution of light from a point source in the focal plane convolved with the pixel response non-uniformity of the detector and the jitter profile of the spacecraft over a 2 minute exposure.</br>
        <br>The PRF changes substantially over each camera’s field of view, is slightly chromatic and varies with temperature.</br>
        <br>The TESS PRF was created by the SPOC and PRF models for each sector can be found on <a href = "https://archive.stsci.edu/missions-and-data/tess/data-products" target = "_blank"> MAST </a>.</br>
        <br>-Physical WCS solutions can be used to convert the PRF image coordinates into the corresponding TESS CCD's. </br>
        <br>Given the unusual nature of the TESS PRF, photometry of an object is typically obtained through the summation of all pixels within a given region. This region is referred to as an "aperture mask" and can be determined through the pipeline or can be selected by the user.</br>
        <br>The figure below shows the TESS PRF from Sector 1, Camera 1.</br>
    <img src="https://heasarc.gsfc.nasa.gov/docs/tess/images/tess_psf.png"></img>
  </div>

  <button type="button" class="collapsible">Crowding</button>
  <div class="content">
        <br>Due to the relatively large pixels (~21 arcsec), the TESS photometry can be contaminated by nearby objects. </br>
        <br>To address this, the <a href = "https://iopscience.iop.org/article/10.3847/1538-3881/ab3467" target = "_blank"> TESS Input Catalog (TIC) </a> provides information needed to estimate the contamination in the TESS band. </br>
        <br>This cannot be determined accurately ahead of time because it will depend on the pixels selected for the aperture photometry of each target and the exact position of the target in the aperture. However, it is possible for the TIC to provide guidance on the expected contamination, for example by providing the number of known objects and their total brightness in the TESS band for some suitable standard aperture and photometer Pixel Response Function (PRF)</br>
  </div>

  <button type="button" class="collapsible">Scattered Light</button>
  <div class="content">
        <br>The effect of the scattered light on the CCD's is typically 2-6 times that of the nominal sky background and covers approximately 10-15% of the FoV. </br>
        <br>When the Earth is below the level of the sun shade there is no scattered light. </br>
        <br>When the Earth or Moon is directly in the FoV of a camera the data is no longer viable.</br>
        <br>An example of the effects of scattered light can be seen <a href="https://www.youtube.com/watch?v=SP4QSF9G6FA" title="Scattered Light" target = "_blank"> here <img alt="scatter.png" src="https://heasarc.gsfc.nasa.gov/docs/tess/images/scatter.png"></a>.</br>
    </div>

  <button type="button" class="collapsible">Cosmic rays</button>
  <div class="content">
    <br>Nearly half of the TESS pixels in the 30 min FFIs are affected by cosmic ray hits</br>
    <br>Within the DHU a tools was developed to help mitigate the effect of the Cosmic-rays, images are stacked and pixels are examined in groups of N. The highest and lowest values of the stack are removed, and the remaining sum are used to create the stack. </br>
    <br>Although this method of cosmic-ray rejection reduces contamination by a factor of 100, some low level outliers still exist and can be seen within the data. These outliers can be removed via TESS-zap.</br>
    <br>Note that for the 20 second cadenced data produced in Cycles 3+, cosmic-ray mitigation is turned off.</br>
    <br>For more information about cosmic-ray mitigation please see section 5.1 of the <a href="https://archive.stsci.edu/files/live/sites/mast/files/home/missions-and-data/active-missions/tess/_documents/TESS_Instrument_Handbook_v0.1.pdf" target = "_blank"> instrument handbook </a></br>
  </div>
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