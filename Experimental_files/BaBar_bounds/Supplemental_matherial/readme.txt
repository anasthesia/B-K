

Supplementary material for the "Search for Long-Lived Particles in e+e- Collisions" at BaBar.

--------------------------------------------------------------------------------------------
Usage
-----

Users may

1) evaluate the efficiency for any particular model using the efficiency_f.txt
file

2) potentially use the PT_distribution_m.txt file to obtain a more precise
value for the efficiency, accounting for the transverse-momentum distribution
of the generated events within each transverse-momentum bin.
In the case where the pT distribution of a signal differs significantly from
the provided one, a linear interpolation of the efficiency as a function of pT
will provide the user with a more accurate value for the efficiency than the
one provided in the efficiency_f.txt files.

3) divide the upper limits from the upperLimts_f_p.txt file by the efficiency
to obtain an upper limit on sigma(e+e- -> LX) B(L -> f).

--------------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------------
efficiency_f.txt
----------------

Contains the efficiency for long-lived particles L, in each of the final states f = ee, mumu, emu, pipi, KK and piK. The columns in each of the files are ordered as follows:

Mass_[GeV]    Minimal_pT_[GeV]    c*tau_[cm]    Efficiency    Efficiency_error.

The Minimal_pT_[GeV] column notes the lower end of the following transverse momentum regions: 

   0.1 < pT  < 0.2 GeV
   0.2 < pT  < 0.3 GeV
   0.3 < pT  < 0.4 GeV
   0.4 < pT  < 0.5 GeV
   0.5 < pT  < 0.6 GeV
   0.6 < pT  < 1.0 GeV
   1.0 < pT  < 2.0 GeV
   2.0 < pT  < 3.0 GeV
   3.0 < pT  < 4.0 GeV
         pT  > 4.0 GeV

Efficiencies of 10^-4 or below are set to 0. 
The Efficiency_error includes all the systematic uncertainties on the efficiency 
(a.k.a the multiplicative uncertainties) mentioned in the paper, including the luminosity error.
The systematic uncertainty that is correlated between the bins amounts to
2.5%. The remaining uncertainties are due to Monte Carlo statistics in each
bin, and are uncorrelated.

--------------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------------
upperLimits_f_p.txt
--------------------

The electronic version of Fig.2 of the paper. Contains the 90% confidence level upper limits on the product sigma(e+e- -> LX) B(L -> f) epsilon(f) of the cross section for production of the long-lived particle L along with any other particles (denoted X), the branching fraction for decay of L to the final state f, and the efficiency for f reconstruction. 
The final states f are noted as ee, mumu, emu, pipi, KK and piK, and p = Y4S, for the Y(4S)+continuum sample, or p = Y2SY3S, for the Y(2S,3S) sample.

The columns in each of the files are ordered as follows:

Mass [GeV]        UL [fb]
--------------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------------
PT_distribution_m.txt
---------------------

The transverse momentum distribution of the generated L particles used for the efficiency calculation, for each of the generated masses m = 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9 and 9.5 GeV.

The columns in each of the files are ordered as follows:

pT [GeV]      #entries

where pT marks the minimal pT value of each transverse-momentum bin, and #entries marks the number of entries in this bin.
--------------------------------------------------------------------------------------------

