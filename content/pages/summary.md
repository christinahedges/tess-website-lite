Title: TESS Summary
template: slide
save_as: summary.html

The TESS mission provides the community with an opportunity to make ground-breaking discoveries in the field of exoplanets, astrophysics and planetary science. A summary of the technical details that proposers should be aware of can be found here.

A description of the overall mission can be found in Ricker et al. 2015. Brief descriptions of the mission operations, including the TESS orbit, field-of-view, time-sampling, and observing strategy, can be found on the objectives and primary mission pages.

This website as well as the TESS Instrument Handbook and Data Release Notes should be consulted for the latest information regarding observing with TESS.


<button type="button" class="btn btn-lg btn-secondary" data-bs-toggle="popover" data-bs-placement="bottom"
  data-bs-title="What's TESS doing right now?"
  data-bs-content="TESS is currently DOING SOMETHING for SECTOR, and is pointing towards A LOCATION. Click here to go SOMEWHERE ELSE.">Where's
  TESS now?</button>

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

<button type="button" class="collapsible">Mission objectives</button>
<div class="content">
  <br>
  The Transiting Exoplanet Survey Satellite (TESS) is a NASA-sponsored Astrophysics Explorer-class mission that is performing a photometric survey over 85% of the sky and searching for planets transiting nearby stars (within ~200 light years). The primary goal of TESS is to discover planets smaller than Neptune that transit stars bright enough to enable follow-up spectroscopic observations that can provide planet masses and atmospheric compositions.
  </br>
  <br>
  TESS covers an area of the sky ~400 times larger than covered by Kepler, and the observed stars are typically 30-100 times brighter than those surveyed by Kepler. Planets detected around these stars are thus easier to characterize with follow-up observations, resulting in refined measurements of planet masses, sizes, densities, and atmospheric properties.
  </br>
  <br>
  <img class="img-responsive" style="max-width:67%;" src="images/data/tess_bright_stars.png">
  *Image Credit: MIT*
  </br>
  <br>
  TESS is led by the [Massachusetts Institute of Technology](https://tess.mit.edu) (MIT), which is responsible for the overall direction of the mission. The TESS Science Office (TSO) is a partnership between MIT's Physics Department and Kavli Institute for Astrophysics and Space Research and the Smithsonian Astrophysical Observatory. The TESS Science Office analyzes the science data and organizes the co-investigators, collaborators, and working groups. The MIT Lincoln Laboratory led the science camera development and construction.
  </br>
  <br>
  NASA's Goddard Space Flight Center (GSFC) provides project management, systems engineering, and safety and mission assurance. The TESS Science Support Center (TSSC) at GSFC operates the Guest Investigator Program and supports the science community proposing for new science with TESS.
  </br>
  <br>
  The spacecraft is operated by Northrop Grumman Innovation Systems. This includes mission operations at the Mission Operation Center.
  </br>
  <br>
  The data are processed by the Science Processing Operations Center (SPOC) at [NASA Ames Research Center](https://www.nasa.gov/ames/tess-pipeline). For more information about the TESS data pipeline see the [data handling page](data-handel.html).
  </br>
</div>

<button type="button" class="collapsible">Launch and orbit</button>
<div class="content">
  <br>TESS launched on April 18, 2018 from Cape Canaveral Air Force Station aboard a SpaceX Falcon 9 rocket. TESS is the first NASA Astrophysics satellite mission to be launched under a contract with SpaceX.</br>
  <br>
  TESS observes from a unique elliptical high Earth orbit (HEO) that provides an unobstructed view of its field to obtain continuous light curves and a more stable platform for precise photometry than the low Earth orbit. The launch carried the observatory to parking orbit inclined by 28.5 degrees. The high Earth orbit was achieved through a series of propulsion system burns and a lunar flyby. Two burns raised the orbit apogee to 400,000 km, one at perigee of the first phasing orbit and another at perigee of the second phasing orbit. Another small adjustment was made before a lunar gravitational assist raised the ecliptic inclination to ~40 degrees. The final apogee and ~13.7 day orbital period were achieved through a final period-adjustment maneuver after the lunar flyby. Final orbit was achieved around 60 days after launch and regular science operations began July 25, 2018.
  </br>
  <br>
  The nominal perigee and apogee of of the elliptical orbit are 17 Earth radii and 59 Earth radii, respectively. The exact orbital period varies between 12-15 days. The orbit places the spacecraft in a 2:1 resonance with the Moon and is inclined with respect to the Ecliptic plane. This avoids lengthy eclipses of the Earth and Moon through the FOV. The large apogee and perigee keep the spacecraft above the Earth's radiation belts and provide a nearly constant thermal environment for the stable -75 degrees C operation of the CCDs. The orbit is operationally stable due to the Moon leading or lagging the apogee by about 90 degrees, effectively averaging out lunar perturbations. The period and semi-major axis are relatively stable, with long term inclination and eccentricity exchanges over periods of 8-12 years. There are additional short term perturbations caused by the Sun with a period of 6 months. The TESS high Earth orbit is stable for decades or longer and requires no propulsion for station-keeping.
  </br>
  <br>
  At the TESS orbit perigee (varies between 12-20 Earth radii), science operations are interrupted to point TESS's antenna toward Earth, downlink data, and resume observing. TESS will also use its hydrazine thrusters to unload angular momentum built up from solar photon pressure at perigee and throughout the orbit.
  </br>
  <br>
        <img class="img-responsive" style="max-width:75%;" src="images/data/tess_orbit_Winnpresentation.jpg"></img>
        *Schematic of maneuvers and encounters leading to the final TESS orbit (light blue). The observatory orbits with a period of ~13.7 days in a 2:1 resonance with the Moon. PLEA and PLEP are the post-lunar-encounter-apogee and -perigee, respectively. Image Credit: Ricker et al. (2015)*
  </br>
</div>

<button type="button" class="collapsible">Science operations</button>
<div class="content">
    <button type="button" class="collapsible">Primary Mission</button>
    <div class="content">
      <br>
      The TESS primary mission ran from July 25th 2018 until July 4th 2020 (note that ground-based follow up for the primary mission continued into 2021). During this time, TESS searched for planets outside of our solar system with a primary goal of finding nearby planets that are amenable to characterization with ground-based follow-up surveys.
      </br>
      <br>
      The TESS primary mission surveyed stars with spectral types ranging from F5 to M5 to searching for transiting exoplanets. In addition to its search for exoplanets, the TESS primary mission allowed scientists from the wider community to request targets for astrophysics research on approximately 10,000 additional objects through each cycle of its Guest Investigator program.
      </br>
      <br>
      Within the primary mission TESS imaged 26 individual sectors, 13 in the southern hemisphere and 13 in the northern hemisphere. Each hemisphere was observed for 1 year each, beginning in the south in July 2018. Each sector was observed for two orbits (27.4 days total), and once complete, TESS re-orientated to the next sector moving eastward until the hemisphere was tiled by 13 sectors.
      </br>
      <br>
      In the second year of the primary mission TESS observed the northern ecliptic hemisphere. The cameras were oriented along a line of ecliptic longitude (as they were in Year 1), with that longitude determined by the anti-solar longitude at the mid-point of the sector. For most of Year 2, the camera array was oriented such that Camera 4 was centered on the northern ecliptic pole: in this orientation, the southernmost edge of Camera 1 was ~6 degree from the ecliptic.
      </br>
      <br>
      However, for Sectors 14 and 15, scattered light from the Earth and Moon was a significant problem in Cameras 1 and 2, reducing the available observing time for exoplanet transits by as much as 75% in those cameras. To reduce the impact of scattered light, the field-of-view of the camera array was shifted north by 31 degrees with respect to its nominal pointing in Sectors 14 and 15.
      </br>
      <br>
      When the cameras were shifted north, the northern ecliptic pole was located 7 degrees from the center of Camera 3, and the southernmost edge of Camera 1 was at an ecliptic latitude of ~37 degrees. In addition, with this shift, the fields-of-view of Cameras 3 and 4 observed ``on the other side of the pole'', thereby providing additional observations of parts of the sky that would otherwise only be observed in Sectors 20-22.
      </br>
      <br>
      The scattered light performance in Sectors 14 and 15 was reviewed, and it was decided that Sector 16 would also have its pointing shifted north. In addition, it was decided that Sectors 24, 25, and 26 would benefit from having their pointings shifted north as well.
      </br>
      <br>
      The fraction of sky coverage for the  different time baselines that TESS had over the 2-year prime mission is listed below. Note this does not  take into account the shift in pointing in Sectors 14, 15, and 16 that are described below. 
      <br/>
      <img class="img-responsive" style="max-width:67%;" src="images/data/tess_sky_coverage.png">
      <br/>
      <br>
      [Additional details on TESS observations can be found at the MIT TESS website](https://tess.mit.edu/observations/).
      </br>
      <br>
      The sky coverage maps for Sectors 1-26 are given below in the ecliptic and celestial coordinate systems and show the shifted fields for Sectors 14, 15, 16 and 24, 25, 26.
      </br>
      <br>
      <img class="img-responsive" style="max-width:90%;" src="images/data/y1sec.png">
      <img class="img-responsive" style="max-width:90%;" src="images/data/y2sec.png">
      <br><img class="img-responsive" style="max-width:80%;" src="images/data/tess_first_light_quarter.jpg"></img>*The first light image from TESS, showing the combined view of all four of its cameras taken on August 7, 2018. Image Credit: NASA/MIT/TESS*</br>
    </div>
    <button type="button" class="collapsible">First Extended Mission</button>
    <div class="content">
      <br>
      After the completion of its prime mission, TESS entered its first extended mission which lasted approximately two years ending in September 2022. This first extension of the TESS mission involved an extensive Guest Investigator Program that was executed over two observing cycles.
      </br>
      <br>
      The first year of the the first extended mission (Cycle 3) comprised of Sectors 27 - 39, during which the Southern ecliptic hemisphere was re-observed. In these Sectors the instrument boresight was pointed at an ecliptic declination of -54 degrees.
      </br>
      <br>
      The TESS Cycle 3 coverage, dates, and camera information are shown below. <br/><img class="img-responsive" style="max-width:90%;" src="images/data/Cycle3sectors.png"><br/>*A depiction of the survey sectors for Cycle 3. Credit: Taken from the [TESS MIT Page](https://tess.mit.edu/observations/).*
      </br>
      <br>
      <img class="img-responsive" style="max-width:90%;" src="images/data/Cycle3table.png"><br/>*List of the sectors in Cycle 3. Details of the cameras, angles, and dates are provided. Credit: Taken from the [TESS MIT Page](https://tess.mit.edu/observations/).*
      </br>
      <br>
      The second year of the first extended mission (Cycle 4) comprised of 16 Sectors instead of 13, and as such lasted ~15 months running from Sectors 40-55. In this Cycle the Northern hemisphere was observed, with Sectors 40-41 sharing similar pointings to that of 14 and 15, at an ecliptic latitude of +85 degrees. Sectors 42-46 were ecliptic pointings and Sectors 47-55 Northern hemisphere pointings at an ecliptic latitude of +54 degrees. Sectors 52 and 53 then shifted north to +85 degrees to avoid scattered light in cameras 1 and 2.<br/><img class="img-responsive" style="max-width:90%;" src="images/data/Cycle4sectors.png"><br/>*A depiction of the survey sectors for Cycle 4. Credit: Taken from the [TESS MIT Page](https://tess.mit.edu/observations/).*<br/><img class="img-responsive" style="max-width:90%;" src="images/data/Cycle4table.png"><br/>*List of the sectors in Cycle 4. Details of the cameras, angles, and dates are provided. Credit: Taken from the [TESS MIT Page](https://tess.mit.edu/observations/).*
      </br>
      <br>
      In Cycles 3 and 4, the following data products changes were introduced: (i) 6 times increase in the number of 2-minute cadenced targets alloted in the GI program; (ii) new 20-second cadence mode data for ~600 targets per sector; (iii) full frame images cadence changed from 30-minute to 10-minute.
      </br>
      <br>
      More than 80% of the observing time was dedicated to GI proposals.
      </br>
    </div>
    <button type="button" class="collapsible">Second Extended Mission</button>
    <div class="content">
      <br>
      The first year of the second extended mission (Cycle 5) covered fields in both the Northern and Southern Ecliptic Hemispheres and ran from September 2022 until September 2023. It comprised of sectors 56 through 69. The second year (Cycle 6) covered fields along the ecliptic and in the Northern Hemispheres, runs from September 2023 until September 2024, and comprises of sectors 70 through 83.
      </br>
      <br>
      The location of the sectors is shown in the figures below.<br/><img class="img-responsive" style="max-width:45%;" src="images/data/Year5_cel.png"><br/><br><img class="img-responsive" style="max-width:45%;" src="images/data/Year5_ecl.png"></br>*A depiction of the survey sectors for Cycle 5.<br/><img class="img-responsive" style="max-width:45%;" src="images/data/Year6_cel.png"><br/><br><img class="img-responsive" style="max-width:45%;" src="images/data/Year6_ecl.png"></br>*A depiction of the survey sectors for Cycle 6. Credit: Provided by TESS MIT.*
      </br>
      <br>
      In Cycles 5 and 6, the following data products changes were introduced: (i) 2-min cadence mode data for ~8,000 targets per sector; (ii) 20-second cadence mode data for ~2,000 targets per sector; (iii) full frame images cadence changed from 10-minute to 200-sec.
      </br>
      <br>
      By the end of the second extended mission, TESS would cover at least 95% of the sky. 
      </br>
    </div>
</div>

<button type="button" class="collapsible">What can TESS observe? (Add cool images)</button>
<div class="content">
  As an all-sky survey, TESS measures the brightness as a function of time of tens of millions of bright objects, including:
  <button type="button" class="collapsible">Exoplanets</button>
  <div class="content">
    The primary exoplanet goal of TESS is to deliver 50 small transiting planets around bright nearby stars. These will be prime targets for follow-up observations aimed at mass measurements via Doppler spectroscopy, emission and transmission spectroscopy for atmospheric characterization with e.g. NASA's JWST, and for precise stellar characterization. Beyond these, TESS will discover thousands of transiting exoplanet systems with various planet sizes, orbital configurations, and multiplicity level, orbiting a wide range of stellar types, and residing in a diverse set of Galactic environments. 
  </div>

  <button type="button" class="collapsible">Stars</button>
  <div class="content">
    As the first all-sky, space-based photometric survey, TESS provides an excellent opportunity to dramatically expand our understanding of key aspects of stellar astrophysics. For example, the highest-cadence TESS observations are ideally-suited for detailed astreroseismology studies and analysis of stellar flares. The nearly-continuous, long-duration TESS observations provide critical information about the mechanisms responsible for intrinsic stellar variability due to e.g. stellar rotation or episodic/quasiperidoc dimming in young stellar objects. Other key contributions of TESS are in the realms of eclipsing binary stars, multiple stellar systems (eclipsing and non-eclipsing), pulsar timing, cataclysmic variables, etc.
  </div>

  <button type="button" class="collapsible">Supernovae</button>
  <div class="content">
    The discovery potential of TESS extends to late stages of stellar evolution as well, in particular to one of its most dramatic outcomes, supernovae explosions. Key component of our understanding of supernovae is the information contained in the shape and duration of the early-rise lightcurves, significantly before peak brightness. Catching these from the ground is challenging -- but TESS has already provided vital observations of dozens of Type Ia and II supernovae and many more are expected to follow suit. It is expected that the significance of TESS observations of supernovae will only increase with time as the sample of early-rise lightcurves grows. 
  </div>

  <button type="button" class="collapsible">Galaxies</button>
  <div class="content">
    Like their constituent stars, galaxies exhibit variability on multiple timescales and with a wide range of amplitudes. Active galactic nuclei,vary both photometrically and spectroscopically, and can exhibit extreme flaring events such as tidal disruptions, accretion rate changes, or ambiguous nuclear transients. The high-quality TESS data enables systematic studies of hours to weeks-long (and even longer) nuclear variability of galaxies at various distances and luminosities, and provides valuable constraints on the characteristic timescales observed in the corresponding lightcurves.
  </div>

  <button type="button" class="collapsible">Asteroids</button>
  <div class="content">
    While TESS excels at observing objects in the the distant Universe, it is an ideal platform to study our own Solar System as well. With its anti-Solar pointing, TESS is in the perfect position to observe these objects at opposition. Observations of comets, asteroids, and near-Earth objects are all within the capabilities of TESS, and the mission has already been highly successful at both their detection and characterization. For example, the observations have been used to measure rotation periods and constrain the shapes of thousands of objects, and more are expected to come. The impact and importance of these studies is not only on the astronomical community, but also on the entire human race as some of these objects can be considered an existential threat. 
  </div>
</div>




<button type="button" class="collapsible">Engage with TESS</button>
<div class="content">
  Here you can find more information on how to engage with TESS and the TESS community.
  <br>
  <img class="img-responsive" style="max-width:100%;" src="images/data/engage_with_tess.png">
  *Image Credit: MIT*
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