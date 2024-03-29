Title: TESS Instrument Information TEST
template: slide
save_as: instrument_information.html

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

<p>Here you can find information on the photometric performance of TESS, including major sources of noise, saturation, systematic effects, pixel-response-function, etc. Additional information can be found in the <a href = "https://archive.stsci.edu/missions/tess/doc/TESS_Instrument_Handbook_v0.1.pdf" target = "_blank"> TESS Instrument Handbook </a> and in the <a href = "https://archive.stsci.edu/tess/tess_drn.html" target = "_blank"> Data Release Notes </a>.</p>

<button type="button" class="collapsible">Typical noise levels</button>
<div class="content">
  <table>
    <tr>
      <th colspan="2" style="font-size: 28px;"></th>
    </tr>
    <tr>
      <td width="50%">
        <ul style=“list-style-type:circle”>
          <li>The typical photometric uncertainties are dominated by pointing jitter, which are at the level of 60 ppm on hourly timescales</li>
          <li>The best light curves are well below the mission requirements of (1) a systematic error floor at 50 ppm for stars with Tmag = 9-15 and (2) 230 ppm at Tmag = 10 mag, which is sufficient to detect super-Earths around bright stars.</li>
          <li>For fainter stars with Tmag = 16, the photometric precision drops to about 1%, which is still sufficient for many astrophysical studies such as supernovae and stellar variability. </li>
          <li>The figure on the right shows the 1-hour Combined Differential Photometric Precision (CDPP) measured from TESS Sector 1. The typical noise achieved in each individual TESS sector is described in the <a href = "https://archive.stsci.edu/tess/tess_drn.html" target = "_blank"> Data Release Notes </a>.</li>
          <ul style=“list-style-type:square”>
            <li>The red points represent the RMS CDPP measurements for the 15,889 light curves from Sector 1 plotted as a function of TESS magnitude. </li>
            <li>The blue x's represent the uncertainties, scaled to a 1-hour timescale. </li>
            <li>The purple curve represents a moving 10th percentile of the RMS CDPP measurements, and the gold curve represetns a moving median of the 1-hour uncertainties.</li>
          </ul>
        </ul>
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
        <ul style=“list-style-type:circle”>
            <li>For bright stars the amount of charge generated by photons can exceed the full well capacity of a pixel. When this occurs, electrons begin to spill over into adjacent pixels along the same column, i.e. "blooming" (the charge barrier in the CCD is much lower along the columns). In many cases, the distribution of charge along the column that has a bright star, causing blooming, has humps at both ends of the bloomed part of the image (See figure on the right).</li>
            <li>The amount of charge deposited by a star of magnitude Tmag into the peak pixel depends on the fraction of the total charge in the peak pixel: this value generally ranges from 0.2 to 0.4 in the TESS images. The TESS cameras create 15,000 e-/s for a star of Tmag = 10. Thus, a star of Tmag = 5 will create 3 x 10<sup>6</sup> electrons in a two-second exposure.</li>
            <li>For a flux fraction of 0.3, the charge in the peak pixel is 9 x 10<sup>5</sup> electrons, leading to a bloom length of 5 rows; similarly, a star of Tmag = 2.5 will create a bloom of 50 rows. A key feature of the CCID-80 CCDs used on TESS is their ability to conserve charge even from very saturated stars. Charge will be conserved for stars at least as bright I<sub>c</sub> = 4 mag.</li>
            <li>Saturation is anticipated in the central pixel at I<sub>c</sub> = 7.5 mag. This, however, does not represent the bright limit for precise photometry. Excess charge from saturated pixels is conserved and spread across adjacent pixels in a CCD column until the excess reaches a CCD boundary. This leads to "bleed trails" extending above and below a saturated pixel, similar to what is seen for bright stars in Kepler/K2 photometry. Precision photometry can still be achieved by creating a photometric aperture that is large enough to encompass all excess charge.</li>
            <li>Cadences with bad calibrations due to saturation are explicitly marked with bit 15 from Sector 68 (value 16384, "Bad Calibration Exclude")</li>
        </ul>
      </td>
      <td width="50%"><img src="images/data/saturation.png"></img></td>
    </tr>
  </table>
</div>

<button type="button" class="collapsible">Pixel Response Function</button>
<div class="content">
    <ul style=“list-style-type:circle”>
        <li>Instead of a point-spread-function, TESS has a pixel response function (PRF). The PRF gives the 2-D distribution of light from a point source in the focal plane convolved with the pixel response non-uniformity of the detector and the jitter profile of the spacecraft over a 2 minute exposure.</li>
        <li>The PRF changes substantially over each camera’s field of view, is slightly chromatic and varies with temperature.</li>
        <li>The TESS PRF was created by the SPOC and PRF models for each sector can be found on <a href = "https://archive.stsci.edu/missions-and-data/tess/data-products" target = "_blank"> MAST </a>.</li>
        <li>-Physical WCS solutions can be used to convert the PRF image coordinates into the corresponding TESS CCD's. </li>
        <li>Given the unusual nature of the TESS PRF, photometry of an object is typically obtained through the summation of all pixels within a given region. This region is referred to as an "aperture mask" and can be determined through the pipeline or can be selected by the user.</li>
        <li>The figure below shows the TESS PRF from Sector 1, Camera 1.</li>
    </ul>
    <img src="https://heasarc.gsfc.nasa.gov/docs/tess/images/tess_psf.png"></img>
</div>

<button type="button" class="collapsible">Crowding</button>
<div class="content">
    <ul style=“list-style-type:circle”>
        <li>Due to the relatively large pixels (~21 arcsec), the TESS photometry can be contaminated by nearby objects. </li>
        <li>To address this, the <a href = "https://iopscience.iop.org/article/10.3847/1538-3881/ab3467" target = "_blank"> TESS Input Catalog (TIC) </a> provides information needed to estimate the contamination in the TESS band. </li>
        <li>This cannot be determined accurately ahead of time because it will depend on the pixels selected for the aperture photometry of each target and the exact position of the target in the aperture. However, it is possible for the TIC to provide guidance on the expected contamination, for example by providing the number of known objects and their total brightness in the TESS band for some suitable standard aperture and photometer Pixel Response Function (PRF)</li>
    </ul>
</div>

<button type="button" class="collapsible">Scattered Light</button>
<div class="content">
     <ul style=“list-style-type:circle”>
        <li>The effect of the scattered light on the CCD's is typically 2-6 times that of the nominal sky background and covers approximately 10-15% of the FoV. </li>
        <li>When the Earth is below the level of the sun shade there is no scattered light. </li>
        <li>When the Earth or Moon is directly in the FoV of a camera the data is no longer viable.</li>
        <li>An example of the effects of scattered light can be seen <a href="https://www.youtube.com/watch?v=SP4QSF9G6FA" title="Scattered Light" target = "_blank"> here <img alt="scatter.png" src="https://heasarc.gsfc.nasa.gov/docs/tess/images/scatter.png"></a>.</li>
     </ul>
</div>

<button type="button" class="collapsible">Cosmic rays</button>
<div class="content">
  <ul style=“list-style-type:circle”>
    <li>Nearly half of the TESS pixels in the 30 min FFIs are affected by cosmic ray hits</li>
    <li>Within the DHU a tools was developed to help mitigate the effect of the Cosmic-rays, images are stacked and pixels are examined in groups of N. The highest and lowest values of the stack are removed, and the remaining sum are used to create the stack. </li>
    <li>Although this method of cosmic-ray rejection reduces contamination by a factor of 100, some low level outliers still exist and can be seen within the data. These outliers can be removed via TESS-zap.</li>
    <li>Note that for the 20 second cadenced data produced in Cycles 3+, cosmic-ray mitigation is turned off.</li>
    <li>For more information about cosmic-ray mitigation please see section 5.1 of the <a href="https://archive.stsci.edu/files/live/sites/mast/files/home/missions-and-data/active-missions/tess/_documents/TESS_Instrument_Handbook_v0.1.pdf" target = "_blank"> instrument handbook </a></li>
  </ul>
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