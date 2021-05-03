import Projectile as pct 

pct = pct.Projectile(10,45,0,0,0.1,1.225,0.1,0.05)
pct.run_event_with_ar(0.01)
pct.plot_trajectory()
pct.return_to_start()