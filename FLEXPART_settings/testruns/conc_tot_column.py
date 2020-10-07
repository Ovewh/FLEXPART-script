from params import *

"""
DESCRIPTION
===========
    Define flexpart simulation settings.

AUTHOR
======
    Ove Haugvaldstad

"""

#Path to parent directory where the output of the simulation is stored
#abs_path = '/cluster/projects/nn2806k/ovewh/flexpart/RUNFLEXPART/Test'
abs_path = '/cluster/work/users/ovewh/may_10th-14th_200hpa_20micron_conc'

#Path to where the forcing AVAILABLE file is
path_to_forcing='/cluster/work/users/ovewh/AVAILABLE_WINDFIELDS'

#Path to where the landuse and surface data is stored
flexpart_input_path = '/cluster/projects/nn2806k/ovewh/flexpart/FLEXPART-script/FLEXPART_input'

#Path to flexpart src

flexpart_src = '/cluster/projects/nn2806k/ovewh/flexpart/flexpart/src'

#Parameters in jobscript submited to the jobqueue

JOBSCRIPT = Job_params(
    time = '00:30:00',
    mem_per_cpu = '4G'
)
#Time of first simulation
start_date = '2019-05-10'
start_time = '00:00:00'

#Time of last simulation
end_date = '2019-05-14'
end_time = '00:00:00'

# The time intervall between each simulation
time_step = '10800s'

# Duration of simulation, Remember backward simulation start and the end!
lenght_of_simulation = '-5d'

# Release Intervall
release_intervall = '0s'

# Which locations to simulate , if location is set to 'ALL', then all locations is used
locations = ('SACOL', 'SHAPOTOU')

#Settings in Command file, name of settings is the same as in the reference file
COMMAND = Command(
LDIRECT = '-1',
IOUT = '9', # NetCDF output 9 + 4 gives both central plume trajectories and emission sensitvities
IND_SOURCE = '1', # 1 Mass, corresponds to mass units 2, mixing ratio
IND_RECEPTOR = '1', # 3 Wet Deposition, 4 Dry depostion

LOUTSTEP= '10800',
LOUTAVER= '10800',
IOUTPUTFOREACHRELEASE= '1' # 1 -> seperate output for each release in the release file, HAS TO BE 1 in bw runs

)
#Set parameters for outgrid
OUTGRID = Outgrid()
#Parameters for flexpart particles, SPEC001_mr ile
SPEC = Species_Params(
    # Dry depositon parameter
    PSPECIES = 'COARSE-SILT',
    PDQUER = '2.0E-05', # Particle size, mean diameter
    PDENSITY  =  '1400.000', # Density of the aerosol, negative -> no dry depostion
    PDSIGMA  = '1.250', # Measure of variation

    # In cloud scavaenging parameter
    PCCN_AERO = '0.1500000', #Cloud Condensation nuclei efficency (suggested value 0.9)
    PIN_AERO  = '0.0200000', #Ice Nuclei efficency, (suggested value 0.1)

)

RELEASES = Releases(
    ZKIND = '3',
    Z1 = '200',
    Z2 = '200',
    COMMENT = 'COARSE-SILT')

