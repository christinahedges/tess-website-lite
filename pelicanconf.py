import datetime
import os
from datetime import date, timedelta
from datetime import datetime as dt
import pandas as pd

AUTHOR = 'TESS GI'
SITEURL = ''
PATH = 'content'
STATIC_PATHS = ['images']
SITELOGO = 'images/logos/NASA_logo_vector_lg.png'
SITELOGO_SIZE = 32
SITEURL = "https://heasarc.gsfc.nasa.gov/docs/tess"	
FULLURL = "https://heasarc.gsfc.nasa.gov/docs/tess"


#Get the latest stats for the planet counter. Note the planet and paper counts are generated with a python script to be added in a future commit (consider them static at the moment)
stats = pd.read_csv('htmlcontent/statistics/data/planet_counter_stats.csv', index_col=0)

#Get the sectors and orbits by date. 
today_split = dt.strptime(str(date.today()), "%Y-%m-%d")
today_date_decimal = today_split.year + (today_split.timetuple().tm_yday - 1) / 365.2425

current_working_directory = os.getcwd()
print(current_working_directory)

# import scripts.make-approved-programs#TESS_button_func
#from scripts.TESS_button_func import main_func as main_func
#sector_today, orbit_today = main_func(today_date_decimal)


PLANETCOUNT = stats['planetcount'].values[0]
PAPERCOUNT = stats['papercount'].values[0]

SCIENCE_DAYS = (date.today() - date.fromisoformat('2018-07-18')).days #days since start of TESS science operations

SITENAME = "TESS"
HIDE_SITENAME = False


THEME = "themes/pelican-bootstrap3-kepler"
BOOTSTRAP_THEME = 'cosmo'
BOOTSTRAP_FLUID = False
FAVICON = 'images/logos/favicon.png'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

HIDE_SIDEBAR = True

# Defines the "related websites" listing in the footer of all pages
RELATEDSITES = (
            ('NASA News, Media, and Education Resources',
             'https://nasa.gov/tess'),
            ('TESS @ MIT',
             'http://tess.mit.edu/'), 
            ('TESS @ MAST',
             'http://archive.stsci.edu/tess'),
            ('High Energy Astrophysics Science Archive Research Center',
             'https://heasarc.gsfc.nasa.gov/'),
            ('NASA Exoplanet Archive @ IPAC',
             'http://exoplanetarchive.ipac.caltech.edu'),
            )


MENUITEMS = (
          ('Education Resources', (
            ('What is TESS?', 'summary.html'),
            ('Outreach Materials', 'outreach.html'),
            ('Citizen Science', 'citizen_science.html'),
            ('Frequently Asked Questions', 'faq.html'),
                    )
        ),

        ('Science Resources', (
            ('TESS Statistics', 'statistics.html'),
            ('TESS Telescope Information', 'telescope_information.html'),
            ('TESS Sector Information', 'sector.html'),
            ('TESS Data Pipeline Information', 'data_pipeline.html'),
            ('TESS Data Product Information', 'data_products.html'),
            ('TESS Users Committee', 'tuc.html'),
            ('Data Release Notes', 'drn.html'),
            ('Documentation Library', 'documentation.html'),
             )
        ),
        ('Propose for Observations', (
            ('Proposing Basics', 'proposing.html'),
            ('Propose for Upcoming Cycle 7', 'new_proposing.html'),
            ('Approved Programs', 'approved-programs.html'),
                    )
        ),
        ('Tools', (
            ('TESS Data Analysis and Community Tools', 'community.html'),
            ('Prepare a TESS Proposal with TPT', 'new_proposing.html'),
            ('Work with TESS Data online with TiKE', 'new_proposing.html'),
                    )
        ),
        ('Tutorials', (
            ('Tutorial 1', 'tutorial1.html'),
            ('Tutorial 2', 'tutorial2.html'),
            ('Tutorial 3', 'new_proposing.html'),
                    )
        ),
        # For press

        )


MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.toc': {},
    'mdx_include': {
            'base_path': "htmlcontent",
            'recursive_relative_path': True,
            'allow_local': True,
            'allow_remote': True,
            'recurs_local': True,
            'recurs_remote': True
        }
  }
}

SHOW_ARTICLE_AUTHOR = True
DEFAULT_PAGINATION = 10

RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True

DATE_MODIFIED = datetime.datetime.now().strftime('%Y-%m-%d')
# Defines the "important dates" box on the front page
IMPORTANT_DATES = (
    ('<b>11th June 2022</b>',
             'AAS Workshop: Engaging the Public in Exoplanet Science Through the Legacy of TESS',
             'https://submissions.mirasmart.com/AAS240/itinerary/EventDetail.aspx?evt=6',),
    ('<b>13th June 2022</b>',
     'AAS Splinter Session: Future Science with TESS',
     'https://submissions.mirasmart.com/AAS240/itinerary/EventDetail.aspx?evt=76'),
     )

DISPLAY_ALERT = True
ALERT_TYPE = 'warning'
ALERT_TITLE = 'TESS Cycle 6 Proposal Deadline.'
ALERT_TEXT = "The TESS Cycle 6 Proposal Deadline is set for DATE. If you are interested in obtaining processed data products or NASA grant funding from TESS, please consider proposing. Click the Proposing tab to learn more."
