def find_tess_today(today_decimal):
    from datetime import date, datetime
    import pandas as pd

    fn_ = 'https://tess.mit.edu/public/files/TESS_orbit_times.csv'
    df = pd.read_csv(fn_, header = 0, delimiter=",", engine='python', na_filter=True).values
    sector = df[0:-1,0]
    orbit = df[0:-1,1]
    start_sector = df[0:-1,2]
    end_sector = df[0:-1,3]
    
    for ii in zip(start_sector, end_sector, sector, orbit):     
        start_date = datetime.strptime(str(ii[0][0:10]), "%Y-%m-%d")
        end_date = datetime.strptime(str(ii[1][0:10]), "%Y-%m-%d")
        
        start_date_decimal = start_date.year + (start_date.timetuple().tm_yday - 1) / 365.2425
        end_date_decimal = end_date.year + (end_date.timetuple().tm_yday - 1) / 365.2425

        if (today_decimal >= start_date_decimal) & (today_decimal <= end_date_decimal):
            return int(ii[2]), int(ii[3])

def plot_tess_today(sector_, orbit_):
    from tesswcs import WCS
    from tesswcs import pointings
    from tesswcs.utils import footprint
    from astropy.coordinates import SkyCoord
    import numpy as np

    import astropy.units as u
    import io
    import base64
    import matplotlib
    matplotlib.use('Agg')  # Use a non-interactive backend
    import matplotlib.pyplot as plt

    ecliptic_plane = SkyCoord(np.arange(0, 360, 1), np.arange(0, 360, 1)*0, unit='deg', frame='geocentricmeanecliptic').transform_to('icrs')
    ra, dec, roll = np.asarray(pointings[pointings['Sector'] == sector_][['RA', 'Dec', 'Roll']])[0]

    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(111, projection="mollweide")
    ax.grid(True)
    ax.set(
    title=f"TESS is currently observing Sector {sector_}\n(Orbit {orbit_})",#RA: {ra}, Dec: {dec}, Roll: {roll}\n[i.e. Sector {sector} Pointing]",
    xlabel="RA",
    ylabel="Dec",
    )

    s = np.argsort(ecliptic_plane.ra.wrap_at(180 * u.deg).rad)
    plt.plot(ecliptic_plane.ra.wrap_at(180 * u.deg).rad[s], ecliptic_plane.dec.rad[s], color='grey', zorder=-10, alpha=0.5, lw=10, label = 'Ecliptic Plane')

    # iterate over camera, CCD
    for camera in np.arange(1, 5):
        for ccd in np.arange(1, 5):
            # predict the WCS
            wcs = WCS.predict(ra, dec, roll, camera=camera, ccd=ccd)
            # create world coordinates from a pixel footprint
            c = wcs.pixel_to_world(*footprint().T)

            # Plot each camera/CCD
            ax.scatter(
                c.ra.wrap_at(180 * u.deg).rad,
                c.dec.rad,
                lw=1.,
                s=0.1,
                c=f"C{camera - 1}",
            )
        ax.text(0.9, 0.99 - (camera-1)*0.1, 'Camera ' + str(camera), 
                color = f"C{camera - 1}", size = 14, transform = ax.transAxes)
    #ax.legend()