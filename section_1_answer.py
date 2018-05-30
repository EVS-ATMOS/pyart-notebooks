radar = pyart.io.read('./data/nsaxsaprppiC1.a1.20140201.184802.nc')
display = pyart.graph.RadarMapDisplayCartopy(radar)
display.plot_ppi_map('relectivity_horizontal', sweep=0, vmin=-10, vmax=60,
                     cmap='pyart_HomeyerRainbow', resolution='10m')
