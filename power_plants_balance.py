# Module to calculate the balance between real generation and real physical guarantee of portfolio power plants

def getIndex(keyElements, array, e1, e2):
    """Get the index of arrays by matching the desired values or combination of values"""
    """My arrays only have 1 key value or combination of 2 key values"""

    if keyElements == 1: # key elements in may arrays can contain a key value, or a combination of 2 key values
        for i in range(len(array)):
            if array[i][0] == e1:
                return i
        return -1

    if keyElements == 2:
        for i in range(len(array)):
            if array[i][0] == e1 and array[i][1] == e2:
                return i
        return -1

monthsAnalysis = ['01-2021', '02-2021', '03-2021', '04-2021'] # Array that stores the month of analysis

powerPlants = ['plant1', 'plant2', 'plant3'] # Arrays with the power plants that are subject of analysis

# Array with the monthly generation of each plant
plantGener = [['plant1', '01-2021', 3500.05],\
              ['plant1', '02-2021', 3000.01],\
              ['plant1', '03-2021', 2000.05],\
              ['plant1', '04-2021', 4000.25], \
              ['plant2', '01-2021', 1000.00], \
              ['plant2', '02-2021', 1200.01], \
              ['plant2', '03-2021', 1300.05], \
              ['plant2', '04-2021', 1450.25], \
              ['plant3', '01-2021', 400.80], \
              ['plant3', '02-2021', 200.90], \
              ['plant3', '03-2021', 150.35], \
              ['plant3', '04-2021', 120.00]]

# Array with the nominal physical guarantee of each plant
plantPhysGrt = [['plant1', 3700.00],\
                ['plant2', 1800.00],\
                ['plant3', 380.00]]

# Array with the monthly system factor to adjust physical guarantee of plants
sysGrtFct = [['01-2021', 0.88],\
             ['02-2021', 0.93],\
             ['03-2021', 0.75],\
             ['04-2021', 1.06]]

# Array with the monthly system electrical losses to adjust generation of plants
sysElectloss = [['01-2021', 0.027],\
                ['02-2021', 0.032],\
                ['03-2021', 0.025],\
                ['04-2021', 0.021]]

# Array to store the results, in 2 dimensions [power plant][month]
plantExp = [[0 for i in range(len(monthsAnalysis))] for i in range(len(powerPlants))]

for i in range(len(powerPlants)):
    for j in range(len(monthsAnalysis)):

        iPGen = getIndex(2,plantGener,powerPlants[i],monthsAnalysis[j])
        iLoss = getIndex(1,sysElectloss,monthsAnalysis[j],0)
        adjGen = plantGener[iPGen][2] * (1 - sysElectloss[iLoss][1])

        iPGrt = getIndex(1, plantPhysGrt, powerPlants[i],0)
        iGFct = getIndex(1, sysGrtFct, monthsAnalysis[j],0)
        adjGrt = plantPhysGrt[iPGrt][1] * sysGrtFct[iGFct][1]

        plantExp[i][j] = adjGen - adjGrt

print('End.')