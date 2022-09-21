import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib.image as image

# nickname for Polynomial function
P = np.polynomial.Polynomial

#######################################
# parameters
r = 2.0
p = .4
K = 10.
μ = .5

params_sim = np.array([r, p, K, μ])


#########################################################
# partie intégration du modèle / dynamiques

# définition d'un vecteur tspan 
t_0 = 0             # temps initial
t_fin = 30.0        # temps final
pas_t = 0.01        # pas de temps de récupération des variables entre t_0 et t_fin
tspan = np.arange(t_0, t_fin, pas_t)

#######################################
# modele TIS
def model_SIT(etat, t, params):
    f, m = etat
    r, p, K, μ, m_s = params
    etatdot = [r*(1-p)*f*(m/(m+m_s))*(1-f/K) - μ*f,
               r*p*f*(m/(m+m_s))*(1-f/K) - μ*m]
    
    return etatdot    

# fonction pour intégration et plot des dynamiques
@st.experimental_singleton
def plotSim(etat0, mS, params_sim, tspan = tspan):
    params = np.append(params_sim, mS)
    
    int_SIT = odeint(model_SIT, etat0, tspan, args=(params,), hmax=pas_t)
    
    # figure
    fig1, ax1 = plt.subplots(figsize=(8, 6))  

    # tracé des simulations par rapport au temps
    ax1.plot(tspan, int_SIT[:,0], color='C0', label='femelles')
    ax1.plot(tspan, int_SIT[:,1], color='C1', label='mâles')

    # tracé des équilibres positifs
    fRoots, mRoots = getEqs(params)

    #mycolors = ['C3', 'C2']
    #mylabels = ['équilibre instable', 'équilibre stable']

    #for i in range(fRoots.size):
        #ax1.plot(tspan, np.ones(tspan.shape)*v_roots[-1-i], color = mycolors[-1-i], label = mylabels[-1-i], linestyle = (0, (3, 7)))

    # # tracé de l'équilibre nul
    # col0, lab0 = 'C2', ''
    # if v_roots.size == 1: col0, lab0 ='C3', "équilibre instable" 
    # if v_roots.size == 0: lab0 = "équilibre stable"
    # ax1.plot(tspan, np.ones(tspan.shape)*0, linestyle = (0, (3, 7)), color = col0, label = lab0)
    
    # # ajout de petites imagettes
    # im1 = image.imread("img/forest.png") 
    # im2 = image.imread("img/desert.png") 
    
    # if v_roots.size > 0:
    #     # put a new axes where you want the image to appear
    #     # (x, y, width, height)
    #     imax1 = fig1.add_axes([.77, (69+384*v_roots[-1])/510+.01, 0.1, 0.1])
    #     # remove ticks & the box from imax 
    #     imax1.set_axis_off()
    #     # print the logo with aspect="equal" to avoid distorting the logo
    #     imax1.imshow(im1, aspect="equal")
    
    # imax2 = fig1.add_axes([.78, 0.17, 0.08, 0.08])
    # imax2.set_axis_off()
    # imax2.imshow(im2, aspect="equal")

    ax1.legend(fontsize='10', loc = 'upper right')
    ax1.set_xlabel('temps', fontsize='12')
    ax1.set_ylabel('densités', fontsize='12')
    fig1.suptitle(r'Dynamiques de populations TIS', va='top', fontsize='14')
    ax1.set_ylim(bottom = -.05, top=K)
    ax1.grid()

    # returns the figure object
    return fig1


################################
# calcul équilibres

def getEqs(params):
    r, p, K, μ, m_s = params

    fP = P([0, 1]) # définition de monôme

    # def polynôme définissant les équilibres f^* > 0
    polF = fP*(-R_0/K*fP+(R_0-1))-(1-p)/p*m_s

    # calcul des racines, recuperations des racines reelles, positives plus petites que K
    fRoots = polF.roots()[(np.isreal(polF.roots())) * (polF.roots() < K) * (polF.roots() > 0) ] # on récupère seulement les racines entre 0 et K
    mRoots = p/(1-p)*fRoots

    eqs = np.array([fRoots, mRoots])

    return eqs
