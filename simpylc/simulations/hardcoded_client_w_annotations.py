'''
====== Legal notices

Copyright (C) 2013 - 2021 GEATEC engineering

This program is free software.
You can use, redistribute and/or modify it, but only under the terms stated in the QQuickLicense.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY, without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the QQuickLicense for details.

The QQuickLicense can be accessed at: http://www.qquick.org/license.html

__________________________________________________________________________


 THIS PROGRAM IS FUNDAMENTALLY UNSUITABLE FOR CONTROLLING REAL SYSTEMS !!

__________________________________________________________________________

It is meant for training purposes only.

Removing this header ends your license.
'''

import time as tm                  # Voor 'time out', niet elke milliseconde rekenen
import traceback as tb             # Wordt niet gebruikt
import math as mt                  # Wordt niet gebruikt
import sys as ss                   # Systeem
import os                          # Operating system
import socket as sc                # Om tussen World en Car(= hardcoded_client)) te kunnen communiceren. 

ss.path +=  [os.path.abspath (relPath) for relPath in  ('..',)]        # Voegt toe aan directory waar info weggeschreven wordt

import socket_wrapper as sw        # Zie 'socket'
import parameters as pm            # Module parameters.py

class HardcodedClient:
    def __init__ (self):
        self.steeringAngle = 0

        with open (pm.sampleFileName, 'w') as self.sampleFile:        # Om data te loggen in default.samples-bestand
            with sc.socket (*sw.socketType) as self.clientSocket:     # Socket/Socketwrapper
                self.clientSocket.connect (sw.address)
                self.socketWrapper = sw.SocketWrapper (self.clientSocket)  # van World naar Car en vice versa, ontvangen en sturen van data, connection
                self.halfApertureAngle = False                        # halfApertureAngle wordt hier aangemaakt, lege plaats in het geheugen

                while True:                      # Zolang het True is wordt onderstaande uitgevoerd, in dit geval alleen handmatig te stoppen
                    self.input ()
                    self.sweep ()
                    self.output ()
                    self.logTraining ()
                    tm.sleep (0.02)              # neem even pauze, nieuwe stuurhoek wordt hier/nu steeds meegegeven

    def input (self):                            # Voeg hier Breakpoint toe en ga met debugging er door heen om te zien wat er gebeurt
        sensors = self.socketWrapper.recv ()     # info uit 'World', geeft aan waar de Car zich bevindt en wat er om hem heen gebeurt

        if not self.halfApertureAngle:           # Met deze 'if not (dus; False) zie voorgaand blok (self.halfApertureAngle = False) wordt onderstaand loopje geactiveerd
            self.halfApertureAngle = sensors ['halfApertureAngle']            # kijkhoek is totaal (120 graden), gedeeld door aantal sensoren. Helft geeft aan: wat is links, wat is rechts
            self.sectorAngle = 2 * self.halfApertureAngle / pm.lidarInputDim
            self.halfMiddleApertureAngle = sensors ['halfMiddleApertureAngle']
            
        if 'lidarDistances' in sensors:
            self.lidarDistances = sensors ['lidarDistances']    # lidarDistances aangemaakt
        else:
            self.sonarDistances = sensors ['sonarDistances']    # idem voor sonarDistances

    def lidarSweep (self):                                 # sweep is per graden > 120    ### Sweep doet bijna alles!!! Hiermee wordt de Car bestuurd
        nearestObstacleDistance = pm.finity                # Max. afstand, om het zicht enigzins te beperken. Met ook nog informatie van ver weg staande objecten wordt het te complex.
        nearestObstacleAngle = 0
        
        nextObstacleDistance = pm.finity                   ## we kijken in deze functie naar de 2 dichtsbijstaande pylonen
        nextObstacleAngle = 0

        for lidarAngle in range (-self.halfApertureAngle, self.halfApertureAngle):  # 120 graden/2 van -60 naar +60 sweepen, 0 is rechtdoor. Welke info vindt je in het bereik
            lidarDistance = self.lidarDistances [lidarAngle]   # doorloopt alle hoeken van -60 t/m +60 (dus -60, -59, - 58 etc.) en geeft de afstand tot de pylonen terug
            
            if lidarDistance < nearestObstacleDistance:               # dus afstand kleiner dan 20 
                nextObstacleDistance = nearestObstacleDistance        # Pylon die eerst het dichtbijzijnde was, wordt vervangen door pylon die nog dichterbij is.
                nextObstacleAngle = nearestObstacleAngle              # Maar, ex-dicthtbijzijnde pylon is nog steeds interessant, want als volgende aan de beurt
                
                nearestObstacleDistance = lidarDistance               # dichtbijzijnde krijgt de afstand mee    
                nearestObstacleAngle = lidarAngle

            elif lidarDistance < nextObstacleDistance:           # check anders de pylon die op één na dichtbijzijnde is
                nextObstacleDistance = lidarDistance
                nextObstacleAngle = lidarAngle
           
        targetObstacleDistance = (nearestObstacleDistance + nextObstacleDistance) / 2   # hiermee rijd je precies tussen 2 pylonen door
                                                                                        # gemiddelde hoek links en rechts 
        self.steeringAngle = (nearestObstacleAngle + nextObstacleAngle) / 2             
        self.targetVelocity = pm.getTargetVelocity (self.steeringAngle)                 # Snelheid is afhankelijk van stuurhoek, zie parameters

    def sonarSweep (self):
        obstacleDistances = [pm.finity for sectorIndex in range (3)]                    # niet doorgenomen met Frank #
        obstacleAngles = [0 for sectorIndex in range (3)]
        
        for sectorIndex in (-1, 0, 1):
            sonarDistance = self.sonarDistances [sectorIndex]
            sonarAngle = 2 * self.halfMiddleApertureAngle * sectorIndex
            
            if sonarDistance < obstacleDistances [sectorIndex]:
                obstacleDistances [sectorIndex] = sonarDistance
                obstacleAngles [sectorIndex] = sonarAngle

        if obstacleDistances [-1] > obstacleDistances [0]:
            leftIndex = -1
        else:
            leftIndex = 0
           
        if obstacleDistances [1] > obstacleDistances [0]:
            rightIndex = 1
        else:
            rightIndex = 0
           
        self.steeringAngle = (obstacleAngles [leftIndex] + obstacleAngles [rightIndex]) / 2
        self.targetVelocity = pm.getTargetVelocity (self.steeringAngle)

    def sweep (self):                             # Wordt meegegeven in World bij keuze 'l/s'
        if hasattr (self, 'lidarDistances'):      # hasattr (has attribute) is een standaardfunctie, hier is attribute 'lidarDistances'
            self.lidarSweep ()
        else:
            self.sonarSweep ()

    def output (self):                             # Copy/pasten naar eigen code
        actuators = {
            'steeringAngle': self.steeringAngle,
            'targetVelocity': self.targetVelocity
        }

        self.socketWrapper.send (actuators)        # Hier worden stuurhoek en snelheid doorgegeven aan Car

    def logLidarTraining (self):                           # Alleen om trainingsdata op te slaan, straks niet meer nodig.
        sample = [pm.finity for entryIndex in range (pm.lidarInputDim + 1)]

        for lidarAngle in range (-self.halfApertureAngle, self.halfApertureAngle):
            sectorIndex = round (lidarAngle / self.sectorAngle)
            sample [sectorIndex] = min (sample [sectorIndex], self.lidarDistances [lidarAngle])

        sample [-1] = self.steeringAngle
        print (*sample, file = self.sampleFile)

    def logSonarTraining (self):                    # Alleen om trainingsdata op te slaan, straks niet meer nodig.
        sample = [pm.finity for entryIndex in range (pm.sonarInputDim + 1)]

        for entryIndex, sectorIndex in ((2, -1), (0, 0), (1, 1)):
            sample [entryIndex] = self.sonarDistances [sectorIndex]

        sample [-1] = self.steeringAngle
        print (*sample, file = self.sampleFile)

    def logTraining (self):                         # Om keuze uit bovenstaande functies te maken
        if hasattr (self, 'lidarDistances'):
            self.logLidarTraining ()
        else:
            self.logSonarTraining ()

HardcodedClient ()
