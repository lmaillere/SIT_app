import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib.image as image
from numpy.linalg import eig

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

# modele TIS
def model_SIT(etat, t, params):
    f, m = etat
    r, p, K, μ, m_s = params
    etatdot = [r*(1-p)*f*(m/(m+m_s))*(1-f/K) - μ*f,
               r*p*f*(m/(m+m_s))*(1-f/K) - μ*m]
    
    return etatdot    

# definition du modèle TIS en temps inverse pour separatrice
def model_SITinv(etat, t, params):
    f, m = etat
    r, p, K, μ, m_s = params
    etatdot = [-r*(1-p)*f*(m/(m+m_s))*(1-f/K) + μ*f,
               -r*p*f*(m/(m+m_s))*(1-f/K) + μ*m]
    
    return etatdot   

# fonction pour intégration et plot des dynamiques
@st.experimental_singleton
def plotSim(etat0, mS, params_sim, tspan = tspan):
    params = np.append(params_sim, mS)
    
    int_SIT = odeint(model_SIT, etat0, tspan, args=(params,), hmax=pas_t)
    
    # figure
    fig1, ax1 = plt.subplots(figsize=(8, 6))  

    # tracé des simulations par rapport au temps
    ax1.plot(tspan, int_SIT[:,0], color='C0', label='femelles', linewidth = 2)
    ax1.plot(tspan, int_SIT[:,1], color='C1', label='mâles', alpha = .4)

    # tracé des équilibres positifs
    fRoots, mRoots = getEqs(params)

    mycolors = ['C3', 'C2']
    mylabels = ['éq. instable (femelles)', 'éq. stable (femelles)']

    for i in range(fRoots.size):
        ax1.plot(tspan, np.ones(tspan.shape)*fRoots[-1-i], color = mycolors[-1-i], label = mylabels[-1-i], linestyle = (0, (3, 3)), linewidth = 2)

    # # tracé de l'équilibre nul
    if mS != 0:
        ax1.plot(tspan, np.ones(tspan.shape)*0, linestyle = (0, (3, 3)), linewidth = 2, color = mycolors[1])
    else:
        ax1.plot(tspan, np.ones(tspan.shape)*0, linestyle = (0, (3, 3)), linewidth = 2, color = mycolors[0])
    
    ax1.legend(fontsize='10', loc = 'upper right')
    ax1.set_xlabel('temps', fontsize='12')
    ax1.set_ylabel('densités', fontsize='12')
    fig1.suptitle(r'Dynamiques de populations TIS', va='top', fontsize='18')
    ax1.set_ylim(bottom = -.25, top=K)
    ax1.grid()

    # returns the figure object
    return fig1


################################
# calcul équilibres
def getEqs(params):
    r, p, K, μ, m_s = params
    
    R_0 = r*(1-p)/μ
    
    fP = P([0, 1]) # définition de monôme de polynôme

    # def polynôme définissant les équilibres f^* > 0
    polF = fP*(-R_0/K*fP+(R_0-1))-(1-p)/p*m_s

    # calcul des racines, recuperations des racines reelles, positives plus petites que K
    fRoots = polF.roots()[(np.isreal(polF.roots())) * (polF.roots() < K) * (polF.roots() > 0) ] # on récupère seulement les racines entre 0 et K
    mRoots = p/(1-p)*fRoots

    eqs = np.array([fRoots, mRoots])

    return eqs


###############################
# tracer toutes les dynamiques
@st.experimental_singleton
def plotSimAll(mS, params_sim, tspan = tspan):
    params = np.append(params_sim, mS)

    # figure
    figS, axS = plt.subplots(figsize=(8, 6))  

    # équilibres positifs
    fRoots, mRoots = getEqs(params)

    # generation de conditions initiales aléatoires, intégration et plot
    np.random.seed(12)
    if fRoots.size > 1:
        etat0Bundle = np.random.rand(30,2)*.75 * fRoots[1]
    else:
        etat0Bundle = np.random.rand(30,2)*.4 * K

    etat0Bundle = etat0Bundle[etat0Bundle[:, 0].argsort()] # permet de trier le tableau selon la 1e coordonnée en conservant les vecteurs générés

    # labels
    labSimAll = np.full(etat0Bundle[:,0].shape, '')
    labSimAll = np.append(labSimAll, "femelles")
    labSimAll = np.delete(labSimAll, 0)

    # redéfinition du cycle des couleurs pour un dégradé de bleu
    colorSimAll = plt.cm.Blues(np.linspace(.3, .8, etat0Bundle.shape[0]))
    axS.set_prop_cycle(color = colorSimAll)

    for i in range(etat0Bundle.shape[0]):
        int_SIT = odeint(model_SIT, etat0Bundle[i], tspan, args=(params,), hmax=pas_t)
        axS.plot(tspan, int_SIT[:,0], label=labSimAll[i])

    # tracé des équilibres positifs
    mycolors = ['C3', 'C2']
    mylabels = ['éq. instable (femelles)', 'éq. stable (femelles)']

    for i in range(fRoots.size):
        axS.plot(tspan, np.ones(tspan.shape)*fRoots[-1-i], color = mycolors[-1-i], label = mylabels[-1-i], linestyle = (0, (3, 3)), linewidth = 2)

    # # tracé de l'équilibre nul
    if mS != 0:
        axS.plot(tspan, np.ones(tspan.shape)*0, linestyle = (0, (3, 3)), linewidth = 2, color = mycolors[1])
    else:
        axS.plot(tspan, np.ones(tspan.shape)*0, linestyle = (0, (3, 3)), linewidth = 2, color = mycolors[0])

    # enluminures
    axS.legend(fontsize='10', loc = 'center right')
    axS.set_xlabel('temps', fontsize='12')
    axS.set_ylabel('densités', fontsize='12')
    figS.suptitle(r'Dynamiques de populations TIS', va='top', fontsize='18')
    axS.set_ylim(bottom = -.25, top = 1.1*fRoots[1])
    axS.grid()

    return figS

################################
# plot plan de phase
@st.experimental_singleton
def plotPlane(mS, params_sim, tspan = tspan):
    params = np.append(params_sim, mS)

    # équilibres positifs
    fRoots, mRoots = getEqs(params)

    # generation de conditions initiales aléatoires, intégration et plot
    np.random.seed(12)
    if fRoots.size > 1:
        etat0Bundle = np.random.rand(30,2)*.75 * fRoots[1]
    else:
        etat0Bundle = np.random.rand(30,2)*.4 * K
    
    etat0Bundle = etat0Bundle[etat0Bundle[:, 0].argsort()] # permet de trier le tableau selon la 1e coordonnée en conservant les vecteurs générés

    # labels
    labSimAll = np.full(etat0Bundle[:,0].shape, '')
    labSimAll = np.append(labSimAll, "femelles")
    labSimAll = np.delete(labSimAll, 0)

    # figure
    figP, axP = plt.subplots(figsize=(8, 6))  

    # redéfinition du cycle des couleurs pour un dégradé de bleu
    colorSimAll = plt.cm.Blues(np.linspace(.3, .8, etat0Bundle.shape[0]))
    axP.set_prop_cycle(color = colorSimAll)

    for i in range(etat0Bundle.shape[0]):
        int_SIT = odeint(model_SIT, etat0Bundle[i], tspan, args=(params,), hmax=pas_t)
        axP.plot(int_SIT[:,1], int_SIT[:,0], label=labSimAll[i])

    # pour plotter le streamplot 
    # définition de l'échantillonnage selon $x$ et $y$
    f_grid = np.linspace(0.5, 7, 9)   # au passage on change un peu de np.arange()
    m_grid = np.linspace(0.5, 7, 9)

    # grille X,Y selon x_grid et y_grid
    M, F = np.meshgrid(m_grid, f_grid)

    # dérivées sur la grille
    df, dm = model_SIT([F, M], 0, params)

    # streamplot
    #axP.streamplot(M, F, dm, df, density = 0.4, maxlength = 0.5, color = "grey")

    # dot f = 0
    mStep = .01
    mPlot = np.arange(mStep, K, mStep)
    fNull = K*(1-μ/(r*(1-p))*(1+mS/mPlot))

    # dot m = 0
    fStep = .01
    fPlot = np.arange(fStep, K, fStep)
    mNull = r*p/μ*fPlot*(1-fPlot/K) - mS

    # nulclines
    axP.plot(mPlot, fNull, label = "$\\dot f = 0$", color = "C4")
    axP.plot(fPlot, np.zeros_like(fPlot), color = "C4")
    axP.plot(mNull, fPlot, label = "$\\dot m = 0$", color = "C6")
    axP.plot(np.zeros_like(mPlot), mPlot, color = "C6")

    # équilibres   
    if mS !=0:
        axP.plot(0, 0, marker = '.', markersize = 14, color = 'C2')
    else:
        axP.plot(0, 0, marker = '.', markersize = 14, color = 'C3')

    if fRoots.size > 0 :
        axP.plot(max(mRoots), max(fRoots), color = "C2", marker = '.', markersize = 14)
        axP.plot(min(mRoots), min(fRoots), color = "C3", marker = '.', markersize = 14)

    # separatrix
    λ, V = eig(Jac([min(fRoots), min(mRoots)], params))

    tspan_sep = np.arange(0, 13, .1)

    initSep1 = [min(fRoots), min(mRoots)] + .01* V[:,1]
    initSep2 = [min(fRoots), min(mRoots)] - .01* V[:,1]

    intSep1 = odeint(model_SITinv, initSep1, tspan, args=(params,), hmax = pas_t)
    intSep2 = odeint(model_SITinv, initSep2, tspan_sep, args=(params,), hmax = pas_t)

    axP.plot(intSep1[:,1], intSep1[:,0], color = "C3", label="séparatrice")
    axP.plot(intSep2[:,1], intSep2[:,0], color = "C3")

    # enluminures
    axP.set_ylim(bottom = -.1, top = 1.2*fRoots[1])
    axP.set_xlim(left = -.1, right = 1.2*mRoots[1])
    axP.set_xlabel('densité de mâles', fontsize='12')
    axP.set_ylabel('densité de femelles', fontsize='12')
    figP.suptitle('Plan de phase', va='top', fontsize='18')

    axP.grid()
    axP.legend(loc = 'upper left')

    return figP

######################
# jacobian for separatrix

def Jac(etat, params):
    f, m = etat
    r, p, K, μ, m_s = params
    J = np.array([[r*(1-p)*m/(m+m_s)*(1-2*f/K)-μ, r*(1-p)*f*(1-f/K)*m_s/(m+m_s)**2],
                 [r*p*m/(m+m_s)*(1-2*f/K),        r*p*f*(1-f/K)*m_s/(m+m_s)**2-μ]])
    
    return J
   
###########################
# birfurcations

def plotBif(params_sim):
    r, p, K, μ = params_sim

    R_0 = r*(1-p)/μ

    fPlotInst = np.arange(0, K*(R_0-1)/R_0/2, .01)
    fPlotSta = np.arange(K*(R_0-1)/R_0/2, K*(R_0-1)/R_0, .01)

    msBifInst = p/(1-p)*(-R_0*fPlotInst**2/K + (R_0-1)*fPlotInst)
    msBifSta = p/(1-p)*(-R_0*fPlotSta**2/K + (R_0-1)*fPlotSta)

    msPlot = np.arange (0, 2, .1)

    # création d'une figure, et d'un système d'axe
    fig3, ax3 = plt.subplots(figsize=(8, 6))  

    # titre de la figure
    fig3.suptitle("Diagramme de bifurcations", va='top', fontsize='18')

    ax3.plot(msBifInst, fPlotInst, color = "C3", label = "équilibre instable")
    ax3.plot(msBifSta, fPlotSta, color = "C2", label = "équilibres stables")
    ax3.plot(msBifInst[-1], fPlotInst[-1], 'D', markersize = 5, color = "C4", label = "bifurcation pli")
    ax3.plot(msPlot, np.zeros_like(msPlot), color = "C2")

    ax3.grid()
    ax3.legend()

    ax3.set_ylabel("densité de femelles", fontsize = 14)
    ax3.set_xlabel("densité de mâles stériles $m_s$", fontsize = 14);

    return fig3
