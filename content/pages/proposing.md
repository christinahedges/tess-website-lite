Title: Proposing to the TESS General Investigator program
template: slide
save_as: proposing.html

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

The primary purpose of the TESS General Investigator (GI) Program is to enhance and maximize the science return from the mission. Users can obtain both data and funding through the TESS GI Program. The program facilitates and supports short-cadence observations with TESS as well as research undertaken with the Full-Frame Images.
<br> Note that the TESS GI program is for new TESS data only (ZZZZTHIS MIGHT CHANGE IN THE FUTUREZZZ) </br>
<br> Below you can find more information on the TESS General Investigator (GI) Program and how to propose for TESS data and research funding. </br>

<button type="button" class="collapsible">Proposal Basics</button>
<div class="content">
    <button type="button" class="collapsible">Why submit a TESS GI proposal?</button>
    <div class="content">
      <br>Secure high-cadence observations (20 sec and 2 min) and mission-provided lightcurves for targets of interest</br>
      <br>Pursue joint observing programs with Fermi, Swift, and NICER</br>
      <br>Obtain funds for you and your collaborators, including support for ground-based observations supporting TESS science.</br>
      <br>Participate in wide-range of cutting-edge science investigations with a NASA mission</br>
    </div>
    <button type="button" class="collapsible">Who can submit a TESS GI proposal?</button>
    <div class="content">
        <ul style=“list-style-type:circle”>
            <br>Anyone is eligible to submit a TESS GI Program.</br>
            <br>To recieve funding through the TESS GI Program, you must be based at a US institution.</br>
        </ul>
    </div>
    <button type="button" class="collapsible">What should I include in my proposal?</button>
    <div class="content">
        <ul style=“list-style-type:circle”>
            <br>Proposals may utilize any combination of 2-minute cadence, 20-second cadence, and the Full-Frame Image data.</br>
            <br>The proposal should provide a compelling, timely, and relevant scientific and technical justification.</br>
            <br>The science justification may include, but is not limited to: exoplanet detection and characterization, stellar astrophysics, galactic and extragalactic astrophysics, and Solar System science.</br>
            <br>The technical justification should be clearly described and sufficiently detailed to support the science case.</br>
            <br>All except the mini proposals should also provide at least one paragraph for the work plan detailing how the proposed effort will be carried out.</br>
            <br>The work plan should include the allocation of effort amongst investigators. This should be expressed in terms of each participant's role in the investigation to preserve the anonymity of the document.</br>
        </ul>
    </div>
</div>

<button type="button" class="collapsible">Proposal Types</button>
<div class="content">
    <ul style=“list-style-type:circle”>
        <br>Type, Typical Duration, Budget, Targets, Length of science/technical section (References are not included in the page limit), Additional Comments</br>
        <br>Mini, One year, Not eligible, Up to fifty 20-sec cadence and up to 1000 2-min cadence, up to two pages, Not eligible for ground-based observations</br>
        <br>Small, One year, $70,000, No limit, up to four pages,Ground-based proposals allowed (~1FTE for a grad student) </br>
        <br>Large, One year, $250,000, No limit, up to six pages, Ground-based proposals allowed (~1FTE for a post doc)</br>
        <br>Key Programs, Max 3 years, $250,000, No limit, up to six pages, Ground-based proposals allowed. Not always solicited depending on the mission cycle (e.g. near the end of an extended mission). </br>
    </ul>
</div>

<button type="button" class="collapsible">Selecting your TESS Targets</button>
<div class="content">
  <button type="button" class="collapsible">How do I find out if TESS can observe my targets?</button>
  <div class="content">
    <br>
     The <a href="https://heasarc.gsfc.nasa.gov/wsgi-scripts/TESS/TESS-point_Web_Tool/TESS-point_Web_Tool/wtv_v2.0.py/" target="_blank">TESS-point Web Tool</a> is provided by the TESS Science Support Center to assist the community in planning and proposing. It allows the user to find the TESS observability of single or multiple targets, as well as calculate the brightness of a source in the TESS bandpass and estimate the corresponding TESS. photometric error sigma. 
     <br>The user provides the name (or TIC ID, or RA/DEC) of an object, and the tool will output which sector and camera the object is expected to be observed with (or null results if it will not fall in the TESS FOV). For larger sets of targets, the TESS-point Web Tool will take an input file (csv) with RA and DEC (in decimal) and return the potential visibility (sector/camera) per object.
     </br>
    </br>
  </div>
  <button type="button" class="collapsible"> Creating target lists</button>
  <div class="content">
    <br>
    Proposers can follow <a href = "https://archive.stsci.edu/tess/"> MAST TESS </a> tutorials to learn how to access the Target Input Catalog (TIC) and Candidate Target List (CTL), crossmatch their targets with these catalogs, and create output files with relevant target information required for the GI call. The TESS GI program office requires that if a target is in the TIC, GI proposers must provide only the following columns from the TIC in comma separated value (csv) format:
    <ul style=“list-style-type:circle”>
      <li>TIC ID (if available)</li>
      <li>Right Ascension (decimal degrees)</li>
      <li>Declination (decimal degrees)</li>
      <li>Proper motion in Right Ascension (mas/yr)</li>
      <li>Proper motion in Declination (mas/yr) </li>
      <li>TESS mag</li>
    </ul>
    </br>
    Since adherence to this format is critical for target list uploads to the <a href = "https://heasarc.gsfc.nasa.gov/ark/rps/"> Remote Proposal System (RPS) website </a>, the MAST has provided a <a href = "https://archive.stsci.edu/tess/tutorials/goddard_format.html"> tutorial </a> to show GI proposers how to select and output these columns for their target lists. Please follow this tutorial to provide a compliant target list. 
    <br>
    In addition to the above six columns, the following additional columns can be provided as necessary (the columns order must not change):
    <ul style=“list-style-type:circle”>
    <li>Common name of target</li>
    <li>Extended flag</li>
    <li>Special handling flag</li>
    <li>20-second cadence flag</li>
    <li>Swift time request (ksec)</li>
    <li>Remarks</li>
    </br>
  </div>
</div>

<button type="button" class="collapsible">Writing your Proposal</button>
<div class="content">
    <ul style=“list-style-type:circle”>
        <br>How many proposals can I submit?</br>
        <ul style=“list-style-type:square>
          <br>As many as you want!</br>
          <br>Note that total amount of funding available is fixed. Thus if you submit multiple proposals you may be competing with yourself!</br>
        </ul>
        <br>How do I make my proposal dual-anonymous compliant?</br>
        <ul style=“list-style-type:square>
          <br>NSPIRES is a great resource for dual-anonymous compliance. You can consult the <a href="https://nspires.nasaprs.com/external/viewrepositorydocument/cmdocumentid=736703/solicitationId=%7B4B9CAAB3-D398-183A-B1F3-EF963DF415C7%7D/viewSolicitationDocument=1/Guidelines%20for%20Anonymous%20Proposals%20DAPR%20Doc%20Astro%20GO%20Programs.pdf" target="_blank">Guidelines for Anonymous Proposals</a> PDF document for specific instructions. Note that this link will automatically download the PDF to your machine.</br>
          <br>Note that the instructions provided in the "Guidelines for Anonymous Proposals" supersede the default instructions given in the NASA</br>
          <br>The "Guidelines for Anonymous Proposals" document also contains complete information on how to write the required "Expertise and Resources - Not Anonymized" document.</br>
          <br>When writing the anonymous part of your Phase-1 proposal, make sure to eliminate language that identifies you or your institution. For example, instead of using "...as we demonstrated in Smith et al. (2022)..." you can instead use "...as demonstrated by [1]...", and then put [1] into the reference list. Another example of compliance issue could be "...we have guaranteed time on our 1.5-m campus telescope at the University of Maryland...". Instead, you can say "...we have guaranteed time on a 1.5-m telescope..." and then describe the facility in the "Expertise and Resources - Not Anonymized" part of the Phase-1 proposal.</br>
          <br>Speaking of references, they should always be in a [1], [2], [3] format in the main body of the proposal.</br>
          <br>NASA understands that dual-anonymous peer review represents a major shift in the evaluation of proposals, and as such there may be occasional slips in writing anonymized proposals.</br>
          <br>However, NASA reserves the right to return without review proposals that are particularly egregious in terms of the identification of the proposing team.</br>
        </ul>
    </ul>
</div>


<button type="button" class="collapsible">Submitting your Proposal</button>
<div class="content">
    <ul style=“list-style-type:circle”>
        <br>How do I submit a proposal?</br>
        <ul style=“list-style-type:square>
          <br>The TESS GI program uses a two-step proposal process. Phase-1 presents the scientific/technical justification. If a Phase-1 proposal is accepted and requests funding, a Phase-2 budget justification is required. All proposal materials are submitted electronically through the <a href="https://heasarc.gsfc.nasa.gov/ark/rps/" target="_blank">ARK/RPS portal </a>.</br>
          <br>The <a href="https://heasarc.gsfc.nasa.gov/ark/rps/" target="_blank">ARK/RPS portal </a> has two pages: a cover page for general information and a second page for uploading the science justification and other files. The uploaded files can be updated as many times as needed before the deadline.</br>
          <br>The TESS Science Support Center provides provides a number of freely-available tools, tutorials, guidelines, examples, and other materials to facilitate the preparation and submission process. You can find more information here.</br>
        </ul>
        <br>When are the proposals due?</br>
        <ul style=“list-style-type:square>
          <br>Proposals are solicited once a year, typically in the spring. You can find more details on <a href="https://nspires.nasaprs.com/external/" target="_blank">NSPIRES</a></br>
        </ul>
    </ul>
</div>

<button type="button" class="collapsible">Proposal Evaluations</button>
<div class="content">
    <ul style=“list-style-type:circle”>
        <br>NASA recognizes and supports the benefits of having diverse and inclusive scientific, engineering, and technology communities and fully expects that such values will be reflected in the composition of the peer review panels and the proposal teams.</br>
        <br>All proposals are peer-reviewed and ranked by a panel of professional volunteers through a double-blind process, followed by ratification from NASA Headquarters.</br>
        <br>The members of the peer-review panel will not be disclosed.</br>
        <br>The deliberations of the panel will be disclosed to PIs only after ratification by the selecting official.</br>
        <br>The review panels will evaluate the anonymized proposals based on their scientific merit, without initially taking into account the proposing team qualifications.</br>
        <br>Only after the scientific evaluation is finalized for all proposals, the panel will review the "Expertise and Resources - Not Anonymized" documents.</br>
        <br>The panel will validate the qualifications of the team in order to allow the reviewers to assess the team capabilities required to execute a given proposed science investigation.</br>
        <br>Is there a specific type of proposals and/or science areas that are more likely to be successful? The TESS GI program supports a wide variety of scientific proposals covering multiple aspects of astrophysics. All proposal are evaluated equally.</br>
    </ul>
</div>

<button type="button" class="collapsible">Additional Resources</button>
<div class="content">
    <ul style=“list-style-type:circle”>
        <br>Are there proposal templates available?</br>
        <ul style=“list-style-type:square>
          <br>Yes! You can find templates in the table below. Note that use of these templates is not required.</br>
          <table class="table table-striped table-hover" style="max-width:55em;">
            <tr>
              <td>
              <td>Template for small, large, and key proposals</td>
              <td><a href="https://heasarc.gsfc.nasa.gov/docs/proposal-templates/tessgi_smalllargekey_template_cycle6.tex" download>Latex</a></td>
              <td><a href="https://heasarc.gsfc.nasa.gov/docs/proposal-templates/tessgi_smalllargekey_template_cycle6.docx" download>Word</a></td>
              <td><a href="https://heasarc.gsfc.nasa.gov/docs/proposal-templates/tessgi_smalllargekey_template_cycle6.pdf" download>PDF</a></td>
            </tr>
            <tr>
              <td>
              <td>Template for mini proposals</td>
              <td><a href="https://heasarc.gsfc.nasa.gov/docs/proposal-templates/tessgi_mini_template_cycle6.tex" download>Latex</a></td>
              <td><a href="https://heasarc.gsfc.nasa.gov/docs/proposal-templates/tessgi_mini_template_cycle6.docx" download>Word</a></td>
              <td><a href="https://heasarc.gsfc.nasa.gov/docs/proposal-templates/tessgi_mini_template_cycle6.pdf" download>PDF</a></td>
            </tr>
            <tr>
              <td>
              <td>Template for team expertise</td>
              <td><a href="https://heasarc.gsfc.nasa.gov/docs/proposal-templates/tessgi_teamexpertise_template_cycle6.tex" download>Latex</a></td>
              <td><a href="https://heasarc.gsfc.nasa.gov/docs/proposal-templates/tessgi_teamexpertise_template_cycle6.docx" download>Word</a></td>
              <td><a href="https://heasarc.gsfc.nasa.gov/docs/proposal-templates/tessgi_teamexpertise_template_cycle6.pdf" download>PDF</a></td>
            </tr>
          </table>
        </ul>
        <br>Can I see examples of successful proposals?</br>
        <ul style=“list-style-type:square>
          <br>The titles and abstracts of all accepted GI proposals can be found here and additional links therein.</br>
        </ul>
        <br>Are there examples on how to analyze TESS data?</br>
        <ul style=“list-style-type:square>
          <br>Yes! You can check out the following tutorials and additional links therein.</br>
        </ul>
        <br>Are there any additional resources I can use?</br>
        <ul style=“list-style-type:square>
          <br>You can keep an eye on the <a href="https://twitter.com/tesshelp?lang=en" target="_blank">TESS Science Support Center X</a>. </br>
        </ul>
        <br>Where can I request a no cost extension for my grant?</br>
        <ul>
          You can make this request by filling out <a href = 'https://www.nasa.gov/centers/nssc/forms/grantcooperative-agreement-no-cost-extension-request'> this form </a>.
        </ul>
        <br>Can I propose to use archival data?</br>
          <ul>
            Proposals to use archival TESS data or to perform other TESS-related investigations could be submitted through the following solicitations:
            <li> Investigations dominated by theoretical effort should respond to the Appendix D.4 Astrophysics Theory Program (ATP) solicitation, or Appendix E.3 the Exoplanet Research Program (XRP). </li>
            <li> Investigations dominated by archival data analysis effort should respond to the Appendix D.2 Astrophysics Data Archive Program (ADAP) solicitation. </li>
            <li> Investigations dominated by ground-based data collection and/or analysis efforts should respond to the Appendix E.3 the Exoplanet Research Program (XRP), or the NSF Astronomy and Astrophysics Research Grants program (AAG). </li>
            <li> More information can be found <a href = 'https://heasarc.gsfc.nasa.gov/docs/tess/proposing-investigations.html'> here </a>.</li>
          </ul>
        <br>Director's Discretionary Target (DDT) program</br>
          <ul>
            The <a href = "https://tess.mit.edu/science/ddt/">DDT and out-of-cycle Target of Opportunity </a> processes for TESS draws on those used successfully for the NuStar Explorer mission. Proposals for DDT and the corresponding targets will be submitted through a form on the <a href = "https://tess.mit.edu/science/ddt/">MIT TESS website </a>. The requests will be reviewed by the TESS PI, a science expert selected by the TESS PI, and the TESS operations team. Approved targets will be posted on the MIT TESS website, along with the expected time(s) of observation.  There is no proprietary period for approved DDT observations. Data from a DDT observation will be delivered to the TESS archives concurrently with the non-DDT data from the sector in which the DDT is observed.
            Note that a number of targets per sector have been reserved for targets which are not covered in the GI target lists, yet may warrant inclusion as targets. 
          </ul>
        <br>If in doubt, reach out to <a href="https://heasarc.gsfc.nasa.gov/docs/tess/helpdesk.html" target="_blank"> TESS GI Helpdesk</a> at tesshelp@bigbang.gsfc.nasa.gov. We are happy to help answer any TESS-related questions!</br>
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