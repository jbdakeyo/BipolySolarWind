# Importation required to run this code
import bipoly_solar_wind_solve_and_plot as bpsw
import streamline_calc_dakeyo2024a as stream 
import matplotlib.pyplot as plt
#########################################
# Inputs of the model : Isopoly 
#########################################

# Length of the output model
N = 5e4         # (Note : the number of points N has been inscreased compared to previous cases)
L = 1.496e11      # set to 1au by default

# Polytropic indexes
gamma_p_values = [0.905, 1.35] 
gamma_e_values = [1.040, 1.21]

# Coronal temperature
Tpc = 1.575e6
Tec = 1.070e6

# Isothermal radius (in solar radii)
r_poly_p = 4.5
r_poly_e = 3.5

# Expansion factor parameters
fm = 100
r_exp = 1.9          # in solar radii
sig_exp = 0.1       # in solar radii
#########################################
# Plotting option 
plot_f = False
plot_gamma = False

plot_unT = True
plot_energy = False
#########################################

###############################################################
# Running the main function
(r, n, u, Tp, Te, gamma_p, gamma_e, ind_rc, f, bol_super) = bpsw.solve_bipoly(
                                        N, L, gamma_p_values, gamma_e_values, 
                                        Tpc, Tec, r_poly_p, r_poly_e,
                                        fm, r_exp, sig_exp, plot_f, 
                                        plot_gamma, plot_unT, 
                                        plot_energy)
###############################################################



#########################################
# Streamline tracing 
#########################################
stream_calc = False
plot_streamline = False
# Probe location for streamline tracing
phi_sat = 10     # in degrees

# Streamline calculation
if(stream_calc):
    (r_phi, phi, v_alf, u_phi) = stream.streamline_calc(r, n, u, phi_sat, plot_streamline)  
###############################################################
plt.show()


