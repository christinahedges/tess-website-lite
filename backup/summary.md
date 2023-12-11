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
    <ul style=“list-style-type:circle”>
        <li>The Transiting Exoplanet Survey Satellite (TESS) is a NASA-sponsored Astrophysics Explorer-class mission that is performing a photometric survey over 85% of the sky and searching for planets transiting nearby stars (within ~200 light years). The primary goal of TESS is to discover planets smaller than Neptune that transit stars bright enough to enable follow-up spectroscopic observations that can provide planet masses and atmospheric compositions. </li>
        <li>TESS covers an area of the sky ~400 times larger than covered by Kepler, and the observed stars are typically 30-100 times brighter than those surveyed by Kepler. </li>
        <br/>
        <img class="img-responsive" style="max-width:67%;" src="images/data/tess_bright_stars.png">
        <br/>
        *Image Credit: MIT*
        <li> TESS is led by the [Massachusetts Institute of Technology](https://tess.mit.edu) (MIT), which is responsible for the overall direction of the mission. The TESS Science Office (TSO) is a partnership between MIT's Physics Department and Kavli Institute for Astrophysics and Space Research and the Smithsonian Astrophysical Observatory. The TESS Science Office analyzes the science data and organizes the co-investigators, collaborators, and working groups. The MIT Lincoln Laboratory led the science camera development and construction.</li>
        <li>NASA's Goddard Space Flight Center (GSFC) provides project management, systems engineering, and safety and mission assurance. The TESS Science Support Center (TSSC) at GSFC operates the Guest Investigator Program and supports the science community proposing for new science with TESS.</li>
        <li>The spacecraft is operated by Northrop Grumman Innovation Systems. This includes mission operations at the Mission Operation Center. </li>
        <li>The data are processed by the Science Processing Operations Center (SPOC) at [NASA Ames Research Center](https://www.nasa.gov/ames/tess-pipeline). For more information about the TESS data pipeline see the [data handling page](data-handel.html).</li>  
    </ul>
</div>

<button type="button" class="collapsible">Observatory Characteristics</button>
<div class="content">
    The TESS observatory consists of the spacecraft and the payload. The TESS payload has a single instrument, a camera suite composed of 4 identical wide field-of-view optical cameras and their associated hoods, mount, sun shield, and Data Handling Unit (DHU). The payload is coupled to the spacecraft, an NGIS LEOStar-2/750 satellite bus. The spacecraft provides power (via two deployable solar arrays), attitude control, data storage, and communications/transmission. 
    <br>
    The four cameras cover a combined field-of-view (FOV) of 24x96 degrees (known as an observing sector). An overview of the FOV coverage and observing strategy for the mission can be found in the Operations page. Each camera consists of a CCD detector assembly, a lens assembly, and a lens hood
</div>

<button type="button" class="collapsible">Launch and orbit</button>
<div class="content">
    <ul style=“list-style-type:circle”>
        <li>TESS launched on April 18, 2018 from Cape Canaveral Air Force Station aboard a SpaceX Falcon 9 rocket. TESS is the first NASA Astrophysics satellite mission to be launched under a contract with SpaceX.</li>
        <li>TESS observes from a unique elliptical high Earth orbit (HEO) that provides an unobstructed view of its field to obtain continuous light curves and a more stable platform for precise photometry than the low Earth orbit. The launch carried the observatory to parking orbit inclined by 28.5 degrees. The high Earth orbit was achieved through a series of propulsion system burns and a lunar flyby. Two burns raised the orbit apogee to 400,000 km, one at perigee of the first phasing orbit and another at perigee of the second phasing orbit. Another small adjustment was made before a lunar gravitational assist raised the ecliptic inclination to ~40 degrees. The final apogee and ~13.7 day orbital period were achieved through a final period-adjustment maneuver after the lunar flyby. Final orbit was achieved around 60 days after launch and regular science operations began July 25, 2018.</li>
        <li>The nominal perigee and apogee of of the elliptical orbit are 17 Earth radii and 59 Earth radii, respectively. The exact orbital period varies between 12-15 days. The orbit places the spacecraft in a 2:1 resonance with the Moon and is inclined with respect to the Ecliptic plane. This avoids lengthy eclipses of the Earth and Moon through the FOV. The large apogee and perigee keep the spacecraft above the Earth's radiation belts and provide a nearly constant thermal environment for the stable -75 degrees C operation of the CCDs. The orbit is operationally stable due to the Moon leading or lagging the apogee by about 90 degrees, effectively averaging out lunar perturbations. The period and semi-major axis are relatively stable, with long term inclination and eccentricity exchanges over periods of 8-12 years. There are additional short term perturbations caused by the Sun with a period of 6 months. The TESS high Earth orbit is stable for decades or longer and requires no propulsion for station-keeping.</li>
        <li>At the TESS orbit perigee (varies between 12-20 Earth radii), science operations are interrupted to point TESS's antenna toward Earth, downlink data, and resume observing. TESS will also use its hydrazine thrusters to unload angular momentum built up from solar photon pressure at perigee and throughout the orbit.</li>
        <br>
        <img class="img-responsive" style="max-width:75%;" src="images/data/tess_orbit_Winnpresentation.jpg"></img>
        *Schematic of maneuvers and encounters leading to the final TESS orbit (light blue). The observatory orbits with a period of ~13.7 days in a 2:1 resonance with the Moon. PLEA and PLEP are the post-lunar-encounter-apogee and -perigee, respectively. Image Credit: Ricker et al. (2015)*
        </br>
    </ul>
</div>

<button type="button" class="collapsible">Science operations</button>
<div class="content">
    <button type="button" class="collapsible">Primary Mission</button>
    <div class="content">
    <ul style=“list-style-type:circle”>
        <li>The TESS primary mission ran from July 25th 2018 until July 4th 2020 (note that ground-based follow up for the primary mission continued into 2021). During this time, TESS searched for planets outside of our solar system with a primary goal of finding nearby planets that are amenable to characterization with ground-based follow-up surveys.</li>
        <li>The TESS primary mission surveyed stars with spectral types ranging from F5 to M5 to searching for transiting exoplanets. In addition to its search for exoplanets, the TESS primary mission allowed scientists from the wider community to request targets for astrophysics research on approximately 10,000 additional objects through each cycle of its Guest Investigator program.</li>
        <li>Within the primary mission TESS imaged 26 individual sectors, 13 in the southern hemisphere and 13 in the northern hemisphere. Each hemisphere was observed for 1 year each, beginning in the south in July 2018. Each sector was observed for two orbits (27.4 days total), and once complete, TESS re-orientated to the next sector moving eastward until the hemisphere was tiled by 13 sectors.</li>
        <li>In the second year of the primary mission TESS observed the northern ecliptic hemisphere. The cameras were oriented along a line of ecliptic longitude (as they were in Year 1), with that longitude determined by the anti-solar longitude at the mid-point of the sector. For most of Year 2, the camera array was oriented such that Camera 4 was centered on the northern ecliptic pole: in this orientation, the southernmost edge of Camera 1 was ~6 degree from the ecliptic.</li>
        <li>However, for Sectors 14 and 15, scattered light from the Earth and Moon was a significant problem in Cameras 1 and 2, reducing the available observing time for exoplanet transits by as much as 75% in those cameras. To reduce the impact of scattered light, the field-of-view of the camera array was shifted north by 31 degrees with respect to its nominal pointing in Sectors 14 and 15.</li>
        <li>When the cameras were shifted north, the northern ecliptic pole was located 7 degrees from the center of Camera 3, and the southernmost edge of Camera 1 was at an ecliptic latitude of ~37 degrees. In addition, with this shift, the fields-of-view of Cameras 3 and 4 observed ``on the other side of the pole'', thereby providing additional observations of parts of the sky that would otherwise only be observed in Sectors 20-22.</li>
        <li>The scattered light performance in Sectors 14 and 15 was reviewed, and it was decided that Sector 16 would also have its pointing shifted north. In addition, it was decided that Sectors 24, 25, and 26 would benefit from having their pointings shifted north as well.</li>
        <li>[Additional details on TESS observations can be found at the MIT TESS website](https://tess.mit.edu/observations/).</li>
        <li>The sky coverage maps for Sectors 1-26 are given below in the ecliptic and celestial coordinate systems and show the shifted fields for Sectors 14, 15, 16 and 24, 25, 26. </li>
    </ul>
    *Sectors 14, 15, and 16 shifted north:*
    <img class="img-responsive" style="max-width:90%;" src="images/data/y1sec.png">
    <img class="img-responsive" style="max-width:90%;" src="images/data/y2sec.png">
    <br><img class="img-responsive" style="max-width:80%;" src="images/data/tess_first_light_quarter.jpg"></img>*The first light image from TESS, showing the combined view of all four of its cameras taken on August 7, 2018. Image Credit: NASA/MIT/TESS*</br>
    </div>
    <button type="button" class="collapsible">First Extended Mission</button>
    <div class="content">
    <ul style=“list-style-type:circle”>
        <li>After the completion of its prime mission, TESS entered its first extended mission which lasted approximately two years ending in September 2022. This first extension of the TESS mission involved an extensive Guest Investigator Program that was executed over two observing cycles</li>
        <li>The first year of the the first extended mission (Cycle 3) comprised of Sectors 27 - 39, during which the Southern ecliptic hemisphere was re-observed. In these Sectors the instrument boresight was pointed at an ecliptic declination of -54 degrees.</li>
        <li>The TESS Cycle 3 coverage, dates, and camera information are shown below. <br/><img class="img-responsive" style="max-width:90%;" src="images/data/Cycle3sectors.png"><br/>*A depiction of the survey sectors for Cycle 3. Credit: Taken from the [TESS MIT Page](https://tess.mit.edu/observations/).*
        <li><img class="img-responsive" style="max-width:90%;" src="images/data/Cycle3table.png"><br/>*List of the sectors in Cycle 3. Details of the cameras, angles, and dates are provided. Credit: Taken from the [TESS MIT Page](https://tess.mit.edu/observations/).*</li>
        <li>The second year of the first extended mission (Cycle 4) comprised of 16 Sectors instead of 13, and as such lasted ~15 months running from Sectors 40-55. In this Cycle the Northern hemisphere was observed, with Sectors 40-41 sharing similar pointings to that of 14 and 15, at an ecliptic latitude of +85 degrees. Sectors 42-46 were ecliptic pointings and Sectors 47-55 Northern hemisphere pointings at an ecliptic latitude of +54 degrees. Sectors 52 and 53 then shifted north to +85 degrees to avoid scattered light in cameras 1 and 2.<br/><img class="img-responsive" style="max-width:90%;" src="images/data/Cycle4sectors.png"><br/>*A depiction of the survey sectors for Cycle 4. Credit: Taken from the [TESS MIT Page](https://tess.mit.edu/observations/).*<br/><img class="img-responsive" style="max-width:90%;" src="images/data/Cycle4table.png"><br/>*List of the sectors in Cycle 4. Details of the cameras, angles, and dates are provided. Credit: Taken from the [TESS MIT Page](https://tess.mit.edu/observations/).*</li>
        <li>In Cycles 3 and 4, the following data products changes were introduced: (i) 6 times increase in the number of 2-minute cadenced targets alloted in the GI program; (ii) new 20-second cadence mode data for ~600 targets per sector; (iii) full frame images cadence changed from 30-minute to 10-minute.</li>
        <li>more than 80% of the osberving time was dedicated to GI proposals. </li>
    </ul>
    </div>
    <button type="button" class="collapsible">Second Extended Mission</button>
    <div class="content">
    <ul style=“list-style-type:circle”>
        <li>The first year of the second extended mission (Cycle 5) covered fields in both the Northern and Southern Ecliptic Hemispheres and ran from September 2022 until September 2023. It comprised of sectors 56 through 69. The second year (Cycle 6) covered fields along the ecliptic and in the Northern Hemispheres, runs from September 2023 until September 2024, and comprises of sectors 70 through 83.</li>
        <li>In Cycles 3 and 4, the following data products changes were introduced: (i) 6 times increase in the number of 2-minute cadenced targets alloted in the GI program; (ii) new 20-second cadence mode data for ~600 targets per sector; (iii) full frame images cadence changed from 30-minute to 10-minute.</li>
        <li>The location of the sectors is shown in the figures below.<br/><img class="img-responsive" style="max-width:45%;" src="images/data/Year5_cel.png"><br/><br><img class="img-responsive" style="max-width:45%;" src="images/data/Year5_ecl.png"></br>*A depiction of the survey sectors for Cycle 5.<br/><img class="img-responsive" style="max-width:45%;" src="images/data/Year6_cel.png"><br/><br><img class="img-responsive" style="max-width:45%;" src="images/data/Year6_ecl.png"></br>*A depiction of the survey sectors for Cycle 6. Credit: Provided by TESS MIT.*</li>
        <li>In Cycles 5 and 6, the following data products changes were introduced: (i) 2-min cadence mode data for ~8,000 targets per sector; (ii) 20-second cadence mode data for ~2,000 targets per sector; (iii) full frame images cadence changed from 10-minute to 200-sec.</li>
    </ul>
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