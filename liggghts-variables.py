Rho1 = 5000
Dp1 = 100
Poros1 = 100
Rp1 = 100
YM1 = 100
PR1 = 100
Dp2 = 100
Poros2 = 100
Rp2 = 100
YM2 = 100
PR2 = 100
YM = 0.1
PR = 0.1
eP1P1 = 0.1
eP1P2 = 0.1
eP1W = 0.1
eP2P2 = 0.1
eP2W = 0.1
eWW = 0.5
msP1P1 = 0.1
msP1P2 = 0.1
msP1W = 0.1
msP2P2 = 0.1
msP2W = 0.1
msWW = 0.5
mrP1P1 = 0.1
mrP1P2 = 0.1
mrP1W = 0.1
mrP2P2 = 0.1
mrP2W = 0.1
mrWW = 0.5
G1 = 1
Rayleigh = 100
writeInterval = 1
MyDt = 1
bkpInterval = 1
tempo = 10
print(f'#ALL UNITS IN SI' '\n'
        f'echo both' '\n'
        f'units si' '\n'
        f'#particle 1 data' '\n'
        f'variable Rho1           universe {Rho1}' '\n'
        f'variable Dp1            universe 0.006' '\n'
        f'variable Rp1            equal 0.5*${Dp1}' '\n'
        f'variable Poros1         universe 0.39' '\n'
        f'variable PartFrac1      equal 1.0-${Poros1}' '\n'
        f'variable VolP1          equal 4.0/3.0*PI*(${Rp1})^3.0' '\n'
        f'variable YM1		universe 5.0e6' '\n'
        f'variable PR1         	universe 0.2' '\n'
        f'variable G1		equal (${YM1}/2.0*(${PR1}+1.0))' '\n'
        f'#particle 2 data' '\n'
        f'variable Rho2           universe 5000.0' '\n'
        f'variable Dp2            universe 0.006' '\n'
        f'variable Rp2            equal 0.5*${Dp2}' '\n'
        f'variable Poros2         universe 0.39' '\n'
        f'variable PartFrac2      equal 1.0-${Poros2}' '\n'
        f'variable VolP2          equal 4.0/3.0*PI*(${Rp2})^3.0' '\n'
        f'variable YM2		universe 5.0e6' '\n'
        f'variable PR2        	universe 0.2' '\n'
        f'variable G2		equal (${YM2}/2.0*(${PR2}+1.0))' '\n'
        f'#equipmentdata' '\n'
        f'variable Rho            universe 7000.0' '\n'
        f'variable YM		universe 5.0e6' '\n'
        f'variable PR         	universe 0.3' '\n'
        f'variable G		equal (${YM}/2.0*(${PR}+1.0))' '\n'
        f'#interacions' '\n'
        f'#restitution coefficient' '\n'
        f'variable eP1P1    	universe 0.3' '\n'
        f'variable eP1P2    	universe 0.3' '\n'
        f'variable eP1W    	universe 0.5' '\n'
        f'variable eP2P1    	equal 1.0*${eP1P2}' '\n'
        f'variable eP2P2    	universe 0.3' '\n'
        f'variable eP2W    	universe 0.5' '\n'
        f'variable eWP1    	equal 1.0*${eP1W}' '\n'
        f'variable eWP2    	equal 1.0*${eP2W}' '\n'
        f'variable eWW   		universe 0.5' '\n'
        f'#friction coefficient' '\n'
        f'variable msP1P1    	universe 0.3' '\n'
        f'variable msP1P2    	universe 0.3' '\n'
        f'variable msP1W    	universe 0.5' '\n'
        f'variable msP2P1    	equal 1.0*${msP1P2}' '\n'
        f'variable msP2P2    	universe 0.3' '\n'
        f'variable msP2W    	universe 0.5' '\n'
        f'variable msWP1    	equal 1.0*${msP1W}' '\n'
        f'variable msWP2    	equal 1.0*${msP2W}' '\n'
        f'variable msWW   	universe 0.5' '\n'
        f'#rolling coefficcient' '\n'
        f'variable mrP1P1    	universe 0.3' '\n'
        f'variable mrP1P2    	universe 0.3' '\n'
        f'variable mrP1W    	universe 0.5' '\n'
        f'variable mrP2P1    	equal 1.0*${mrP1P2}' '\n'
        f'variable mrP2P2    	universe 0.3' '\n'
        f'variable mrP2W    	universe 0.5' '\n'
        f'variable mrWP1    	equal 1.0*${mrP1W}' '\n'
        f'variable mrWP2    	equal 1.0*${mrP2W}' '\n'
        f'variable mrWW   	universe 0.5' '\n'
        f'## Neighbor listing' '\n'
        f'variable binsize	 equal 2.0*${Dp1}' '\n'
        f'#time-related variables' '\n'
       f'variable timecreation    universe 5.0' '\n'
        f'variable tempo		 universe 50.0' '\n'
        f'variable Rayleigh	 equal ((PI*${Rp1}/(0.163*${PR1}+0.8166))*(${Rho1}/${G1})^0.5)' '\n'
        f'variable MyDt            equal ((5.0/100.0)*${Rayleigh})' '\n'
        f'variable writeInterval   universe 0.1' '\n'
        f'variable bkpInterval     universe 1.0' '\n'
        f'variable saveEvery       equal round(${writeInterval}/${MyDt})' '\n'
        f'variable bkpEvery        equal round(${bkpInterval}/${MyDt})' '\n'
        f'variable nTimeStep	 equal round(${tempo}/${MyDt})' '\n'
        f'#Particles number' '\n'
        f'variable nP1      	 universe 100.0' '\n'
        f'variable nP2       	 universe 100.0' '\n'
        f'#rotation speed' '\n'
        f'variable omega 		 equal 1.0')