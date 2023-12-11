Title: TESS Data Analysis and Community Tools
template: slide
save_as: community.html

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

<p>Here you can find information on the various community products, software tools, and efforts developed specifically for TESS data, or can be used or modified for TESS data. Note that tools and utilities are continuously under development by the community, and some can be more robust than others. The TESS Science Support Center periodically updates this list as new tools, software, and tutorials become available. 

If you have any tools you would like us to include or highlight, please contact us at <a href="https://heasarc.gsfc.nasa.gov/docs/tess/helpdesk.html" target="_blank"> TESS GI Helpdesk</a> or tesshelp@bigbang.gsfc.nasa.gov</p>

<button type="button" class="collapsible"> <a href = 'https://docs.lightkurve.org'>Lightkurve </a></button>
<div class="content">
  Lightkurve is a Python-based package developed by the Kepler/K2 Guest Observer (GO) Office for use by the community to work with Kepler and K2 data. The TESS GI Office has partnered with the Kepler/K2 GO Office to adapt Lightkurve for use with TESS data. 
  <ul>Lightkurve functionality:
    <li>Reading, writing, and interacting with pipeline products (TPFs, LightCurve files, etc) </li>
    <li>Extracting light curves from pixels using custom aperture photometry or custom PSF fitting.</li>
    <li>Removing trends or correcting systematics using widely-used, non-controversial methods (SavGol, CBVs, SFF, ...</li>
  </ul>
  The lightkurve git repository can be found <a href = 'https://github.com/lightkurve/lightkurve'> here </a>.
</div>

<button type="button" class="collapsible"> <a href = 'https://tess.mit.edu/followup/'>TESS Follow-Up Observing Program </a></button>
<div class="content">
  The TESS Follow-Up Observing Program (TFOP) is a large international working group of astronomers brought together to primarily provide follow-up observations to support the TESS Mission's primary goal of measuring the masses for 50 planets smaller than 4 Earth radii. Stars hosting high priority planet candidates are observed to establish reliable stellar parameters, confirm the existence of planets, refine their radii, and measure planet masses.
  The TFOP is led by the <a href = "https://www.cfa.harvard.edu"> Smithsonian Astrophysical Observatory (SAO) </a>, in coordination with MIT, as part of the TESS Science Office. A goal of TFOP is to foster communication and coordination among the TESS Science Team members and the community in order to maximize scientific output and minimize duplication of effort. 
  The TFOP is organized into five sub-groups: Seeing-Limited Photometry (SG1), Recon Spectroscopy (SG2), High-Resolution Imaging (SG3), Precise Radial Velocities (SG4), and Space-Based Photometry (SG5). TFOP observations are performed with committed time on the [Las Cumbres Observatory Network](https://lco.global) (for photometry and spectroscopy), the MEarth (photometry) and TRES (spectroscopy) facilities, and numerous other facilities through the usual telescope time allocation processes. There are currently dozens of working groups (each representing a team and facility from around the world) involved in TFOP and additional participation and follow-up programs are welcome. For more information and to apply to join TFOP, [check out the MIT website here](https://tess.mit.edu/followup/).
  Observations acquired via the TFOP are uploaded to the ExoFOP Repository, described in further detail below.
</div>

<button type="button" class="collapsible"> <a href = 'https://exofop.ipac.caltech.edu/'> ExoFOP Repository </a></button>
<div class="content">
  ExoFOP is a web-based service developed and operated by the <a href = 'http://nexsci.caltech.edu'> NASA Exoplanet Science Institute (NExScI) </a> originally for the Kepler and K2 Follow-Up Observation Programs. ExoFOP plays a key role in coordinating TESS Follow-Up Observing Program (TFOP) activities and hosting observations and tools. ExoFOP is a 'sand-box' for the community to share data and information regarding follow-up observations to help facilitate the efficient and effective use of community telescope resources. ExoFOP is connected to and integrated with the <a href = 'https://exoplanetarchive.ipac.caltech.edu'> NASA Exoplanet Archive </a>.
  ExoFOP hosts a dedicated page for TESS, <a href = 'https://exofop.ipac.caltech.edu/tess/'> ExoFOP-TESS </a>, with a format similar to the Kepler/K2 pages. ExoFOP-TESS contains overview pages for everything in TIC V8 (~1.7 billion targets).
  <ul>ExoFOP-TESS includes:
    <li>Summaries of TESS-observed targets</li>
    <li>TOI/CTOI lists with candidate planet parameters</li>
    <li>Overviews of individual targets</li>
    <li>Summaries of observations</li>
    <li>Observing notes</li>
    <li>Links to outside services (NASA Exoplanet Archive tools, MAST data and documentation, Simbad and other host star resources, community-produced light curves and products, and more)</li>
    <li>Telescope resource calendar</li>
  </ul> 
  All files (data/image/notes) can be uploaded in any format, in single or bulk-uploads. Attached notes can be html to enable linking within ExoFOP or outside. ExoFOP-TESS products will be searchable and available to sort and download. A tool to follow specific targets, or sets of targets, can be enabled via a "My Targets" feature with an option for email updates.
  <br/><img class="img-responsive" style="max-width:67%;" src="https://heasarc.gsfc.nasa.gov/docs/tess/images/data/exoFOP_figures.png">*Examples of supporting follow-up observation results that can be uploaded to ExoFOP. Image Credit: D. Ciardi/NexScI*<br/>
</div>

<button type="button" class="collapsible"> High Level Science Products </button>
<div class="content">
  High level science products (HLSP) created by the community (e.g., full-frame image light curves) can be found at the MAST. If you are interested in creating a HLSP and having it hosted on MAST, we encourage you to <a href = 'https://archive.stsci.edu/contacts.html'> contact MAST </a>. A list of currently available HLSP for TESS can be found <a href = 'https://archive.stsci.edu/hlsp/'> here at MAST </a>, including:
  <ul>
    <li>[TESS-HERMES Spectroscopic Survey](https://archive.stsci.edu/prepds/tess-hermes/) (PI: Sanjib Sharma)</li>
    <li>[Data Products From TESS Data Alerts](https://archive.stsci.edu/prepds/tess-data-alerts/) (PI: Roland Vanderspek)</li>
    <li>[TESS Data For Asteroseismology Lightcurves](http://archive.stsci.edu/hlsp/tasoc) (PI: Rasmus Handberg)</li>
    <li>[Cluster Difference Imaging Photometric Survey](http://archive.stsci.edu/hlsp/cdips) (PI: Luke Bouma)</li>
    <li>[eleanor FFI Light Curves From TESS ](http://archive.stsci.edu/prepds/eleanor) (PI: Benjamin Montet)</li>
    <li>[A PSF-Based Approach to TESS High Quality Data Of Stellar Clusters](http://archive.stsci.edu/hlsp/pathos) (PI: Domenico Nardiello)</li>
    <li>[TESS Light Curves From Full Frame Images](https://archive.stsci.edu/hlsp/tess-spoc) (PI: Douglas A. Caldwell)</li>
    <li>[TESS Lightcurves From The MIT Quick-Look Pipeline](https://archive.stsci.edu/hlsp/qlp) (PI: Chelsea X. Huang)</li>
    <li>[Multi-Sector Light Curves From TESS Full Frame Imaes (DIAMANTE)](https://archive.stsci.edu/hlsp/diamante) (PI: Marco Montalto)</li>
    <li>[Convolution Neural Networks for Flare Identification in TESS 2-minute Data (STELLA)](https://archive.stsci.edu/hlsp/stella) (PI: Adina Feinstein)</li>
    <li>[TESS Image CAlibrator Full Frame Images (TICA)](https://archive.stsci.edu/hlsp/tica) (PI: Michael Fausnaugh)</li>
    <li>[The TESS Stellar Variability Catalog (TESS-SVC)](https://archive.stsci.edu/hlsp/tess-svc) (PI: Tara Fetherolf)</li>
    <li>[TESS-Gaia Light Curve ("TGLC")](https://archive.stsci.edu/hlsp/tglc) (PI: Timothy D. Brandt)</li>
    <li>[TESS Eclipsing Binaries ("TESS-EBs")](https://archive.stsci.edu/hlsp/tess-ebs) (PI: Andrej Prsa)/li>
    <li>[TESS FFI-Based Light Curves from the GSFC Team (GSFC-ELEANOR-LITE)](https://archive.stsci.edu/hlsp/gsfc-eleanor-lite) (PI: Brian P. Powell)</li>
    <li>[Simulated TESS Light Curves for Measuring Rotation with Deep Learning ("SMARTS")](https://archive.stsci.edu/hlsp/smarts) (PI: Zachary R. Claytor)</li>
    <li>[Cutouts from Wide-area TESS Coadded Images ("TESS-COADD-CUTOUTS")](https://archive.stsci.edu/hlsp/tess-coadd-cutouts) (PI: G. Bruce Berriman)</li>
  </ul>
</div>

<button type="button" class="collapsible"> Detrending and analysis </button>
<div class="content">
  <table class="table table-striped table-hover" style="max-width:55em;">
  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/waqasbhatti/astrobase'>astrobase</a></td>
    <td> Light curve tools and analysis <a href='github.com/waqasbhatti/astrobase-notebooks'>A tutorial can be found here</a>.
    </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/hvidy/halophot/'>halophot</a></td>
    <td> K2 Halo Photometry for very bright stars. Can be applied to TESS data.</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/saigrain/k2scTess'>k2scTess</a></td>
    <td>TESS systematics correction via simultaneous modeling of stellar variability and jitter-dependent systematics using Gaussian Process regression.</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://docs.lightkurve.org/'> Lightkurve</a></td>
    <td> A user-friendly package for supporting science and performing lightcurve analysis with data from Kepler, K2, and TESS. <a href='https://docs.lightkurve.org/tutorials/index.html#tutorials'> Tutorials can be found here</a>.
    </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/stephtdouglas/PySysRem'>PySysRem</a></td>
    <td>Correct systematic effects in large sets of photometric light curves.</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/nksaunders/skope'>skope</a></td>
    <td>scope creates a forward model of telescope detectors with pixel sensitivity variation, and synthetic stellar targets with motion relative to the CCD. It allows for the creation of light curves and as simulations of Kepler/K2/TESS data.</td>
  </tr>
  </table>
</div>

<button type="button" class="collapsible"> Full frame image analysis </button>
<div class="content">
  <table class="table table-striped table-hover" style="max-width:55em;">

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/ryanoelkers/DIA'>DIA</a></td>
    <td>Difference Imaging Analysis to extract a light curve from FFIs.</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a href='http://adina.feinste.in/eleanor/index.html'>eleanor</a></td>
    <td>eleanor is an open-source python framework for downloading, analyzing, and visualizing data from the TESS Full Frame Images.</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://filtergraph.com/tess_ffi/'>Filtergraph</a></td>
    <td>This is the TESS full-frame-image (FFI) portal which hosts the
    data products from the pipeline of <a href='http://adsabs.harvard.edu/abs/2018AJ....156..132O'>Oelkers & Stassun (2018).</a>
    </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a href='http://www2.iap.fr/users/alard/package.html'>ISIS</a></td>
    <td>Process CCD images using image subtraction.
    </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://docs.lightkurve.org'>Lightkurve</a></td>
    <td> Extract light curves from FFIs, and package into TPFs.
    </td>
  </tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/zkbt/spyffi'>SpyFFI</a></td>
    <td>Tools for simulating TESS imaging at multiple cadences, including light curves, jitter, focus drifts, cosmic rays.
    </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://mast.stsci.edu/tesscut/ '>TESSCut</a></td>
    <td> Create time series pixel cutouts from the TESS FFIs. Find out what sectors/cameras/detectors a target was observed in.
    </td>
  </tr>
  
  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/keatonb/TESS_PRF'>TESS_PRF</a></td>
    <td>Tools to display the TESS pixel response function (PRF) at any location on the detector.
    </td>
  </tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/CheerfulUser/TESSreduce'>TESSreduce</a></td>
    <td>This builds on lightkurve, allowing the user to reduce TESS data while preserving transient signals. The user can supply a TPF or give coordinates and sector to construct a TPF with TESScut. The background subtraction accounts for the smooth background and detector straps. Alongside background subtraction TESSreduce also aligns images, performs difference imaging, and can even detect transient events!
    </td>
  </tr>
  </table>
</div>

<button type="button" class="collapsible">Positional tools</button>
<div class="content">
  <table class="table table-striped table-hover" style="max-width:55em;">
  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/christopherburke/tess-point'>tess-point</a></td>
    <td> Provides the target ecliptic coordinates, TESS sector number, camera number, detector number, and pixel column and row.
    </td>
  </tr>
  <tr>
    <td style="width: 15em;"><a
    href='https://heasarc.gsfc.nasa.gov/wsgi-scripts/TESS/TESS-point_Web_Tool/TESS-point_Web_Tool/wtv_v2.0.py/'>TESS-point Web Tool</a></td>
    <td>A tool which uses tess-point for determining whether stars and galaxies are observable by TESS, and in which sector.
    </td>
    </tr>
  
   <tr>
    <td style="width: 15em;"><a
    href='https://github.com/tessgi/toco'>toco</a></td>
    <td>A way to quickly see some info about a star based on it's TICID.
    </td>
    </tr>
  </table>
</div>

<button type="button" class="collapsible">Data handling</button>
<div class="content">
  <table class="table table-striped table-hover" style="max-width:55em;">
  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/barentsen/k2flix'>k2flix</a></td>
    <td>Create quicklook movies from the pixel data observed by Kepler/K2/TESS.
    </td>
  </tr>
  </table>
</div>

<button type="button" class="collapsible">Planet search, modeling, and vetting</button>
<div class="content">
  <table class="table table-striped table-hover" style="max-width:55em;">
  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/lkreidberg/batman'>batman</a></td>
    <td>Fast transit light curve models in Python.
    </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://exogram.vercel.app'>Exogram</a></td>
    <td>Online toolkit for vetting and validation of TESS data. </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/exoplanet-dev/exoplanet'>exoplanet</a></td>
    <td> Toolkit for probabilistic modeling of time series data in astronomy with a focus on observations of exoplanets
    </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/3fon3fonov/exostriker'>ExoStriker</a></td>
    <td>Performs N-body simulations, and models the RV stellar reflex motion caused by dynamically interacting planets in multi-planetary systems.
    </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/hpparvi/k2ps'>k2ps</a></td>
    <td>K2 planet search.
    </td>
  </tr>
  
  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/mrtommyb/ktransit'>ktransit</a></td>
    <td>A simple exoplanet transit modeling tool in Python.
    </td>
  </tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/matiscke/lcps'>lcps</a></td>
    <td>A tool for pre-selecting light curves with possible transit signatures.
    </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/rodluger/planetplanet'>planetplanet</a></td>
    <td>A general photodynamical code for exoplanet light curves.
    </td>
  </tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/rodluger/pysyzygy'>pysyzygy</a></td>
    <td>A fast and general planet transit (syzygy) code written in C and in Python.
    </td>
  </tr>


 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/hpparvi/PyTransit'>PyTransit</a></td>
    <td>Fast and easy transit light curve modeling using Python and Fortran.
    </td>
  </tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/petigura/terra'>terra</a></td>
    <td>Transit detection code.
    </td>
  </tr>

 <tr>
    <td style="width: 15em;"><a
    href='https://github.com/mindriot101/ttvfast-python'>ttvfast-python</a></td>
    <td>Python interface to the TTVFast library.
    </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/exoplanetvetting/DAVE'>DAVE</a></td>
    <td> Find and vetting planets using data from K2 and TESS.
    </td>
  </tr>
 
  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/timothydmorton/VESPA'>VESPA</a></td>
    <td>Calculating false positive probabilities for transit signals.
    </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/stevengiacalone/triceratops'>Triceratops</a></td>
    <td> Vetting and validating TESS Objects of Interest.
    </td>
  </tr>

  </table>
</div>

<button type="button" class="collapsible">Miscellaneous science tools</button>
<div class="content">
  <table class="table table-striped table-hover" style="max-width:55em;">
  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/stephtdouglas/animate_spots'>animate_spots</a></td>
    <td>Make frames for animated gifs/movies showing a rotating spotted star.
    </td>
  </tr>
  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/ekaterinailin/AltaiPony'>AltaiPony</a></td>
    <td>Python-based flare finding code for Kepler/K2/TESS light curves.
    </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://emac.gsfc.nasa.gov/'>EMAC</a></td>
    <td>The NASA Goddard Space Flight Center Exoplanet Modeling and
    Analysis Center (EMAC) serves as a repository and integration platform for modeling and analysis resources focused on the study of exoplanet characteristics and environments.
    </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://fast-lightcurve-inspector.osc-fr1.scalingo.io'>FLI</a></td>
    <td>Online toolkit for visual inspection of TESS data. </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/skgrunblatt/FoFreeAST'>FoFreeAST</a></td>
    <td>Fourier-Free Asteroseismology: uses celerite to model granulation and oscillations of stars.
    </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/timothydmorton/isochrones'>isochrones</a></td>
    <td>Pythonic stellar model grid access; easy MCMC fitting of stellar properties.
    </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/danxhuber/isoclassify'>isoclassify</a></td>
    <td>Perform stellar classifications using isochrone grids.
    </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='http://latte-online.flatironinstitute.org/app'>LATTE</a></td>
    <td>Online toolkit for visual inspection of TESS data. </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/hpparvi/ldtk'>ldtk</a></td>
    <td>Python toolkit for calculating stellar limb darkening profiles. </td>
  </tr>


  <tr>
    <td style="width: 15em;"><a
    href='https://arxiv.org/abs/1804.10295'>limb darkening</a></td>
    <td>Limb-darkening and gravity-darkening coefficients for TESS.</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/rpoleski/MulensModel'>MulensModel</a></td>
    <td>Microlensing Modelling package.</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/natashabatalha/PandExo'>PandExo</a></td>
    <td>A community tool for transiting exoplanets with HST & JWST. </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/timothydmorton/pymacula'>pymacula</a></td>
    <td>Python wrapper for Macula analytic starspot code.</td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/LucaMalavolta/PyORBIT'>PyOrbit</a></td>
    <td>General toolkit for modeling radial velocity data. </td>
  </tr>

  <tr>
    <td style="width: 15em;"><a
    href='https://github.com/California-Planet-Search/radvel'>radvel</a></td>
    <td>Simultaneously characterize the orbits of exoplanets and the noise induced by stellar activity.</td>
  </tr>
  </table>
</div>


<button type="button" class="collapsible">Kepler/K2 tools REMOVE?</button>
<div class="content">
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