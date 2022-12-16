'''
Neuron simulator export for:

Components:
    null (Type: notes)
    Ca_HVA (Type: ionChannelHH:  conductance=1.0E-11 (SI conductance))
    null (Type: notes)
    Ca_LVAst (Type: ionChannelHH:  conductance=1.0E-11 (SI conductance))
    null (Type: notes)
    CaDynamics_E2_NML2 (Type: concentrationModelHayEtAl:  gamma=0.05 (dimensionless) minCai=1.0E-4 (SI concentration) decay=0.08 (SI time) depth=1.0E-7 (SI length) Faraday=96485.3 (SI charge_per_mole))
    null (Type: notes)
    CaDynamics_E2_NML2__decay122__gamma5_09Emin4 (Type: concentrationModelHayEtAl:  gamma=5.09E-4 (dimensionless) minCai=1.0E-4 (SI concentration) decay=0.122 (SI time) depth=1.0E-7 (SI length) Faraday=96485.3 (SI charge_per_mole))
    null (Type: notes)
    CaDynamics_E2_NML2__decay460__gamma5_01Emin4 (Type: concentrationModelHayEtAl:  gamma=5.01E-4 (dimensionless) minCai=1.0E-4 (SI concentration) decay=0.46 (SI time) depth=1.0E-7 (SI length) Faraday=96485.3 (SI charge_per_mole))
    null (Type: notes)
    Ih (Type: ionChannelHH:  conductance=1.0E-11 (SI conductance))
    null (Type: notes)
    Im (Type: ionChannelHH:  conductance=1.0E-11 (SI conductance))
    null (Type: notes)
    K_Pst (Type: ionChannelHH:  conductance=1.0E-11 (SI conductance))
    null (Type: notes)
    K_Tst (Type: ionChannelHH:  conductance=1.0E-11 (SI conductance))
    null (Type: notes)
    Nap_Et2 (Type: ionChannelHH:  conductance=1.0E-11 (SI conductance))
    null (Type: notes)
    NaTa_t (Type: ionChannelHH:  conductance=1.0E-11 (SI conductance))
    null (Type: notes)
    pas (Type: ionChannelPassive:  conductance=1.0E-11 (SI conductance))
    null (Type: notes)
    SK_E2 (Type: ionChannelHH:  conductance=1.0E-11 (SI conductance))
    null (Type: notes)
    SKv3_1 (Type: ionChannelHH:  conductance=1.0E-11 (SI conductance))
    L5PC (Type: cell)
    null (Type: notes)
    Input_0 (Type: pulseGenerator:  delay=0.7 (SI time) duration=2.0 (SI time) amplitude=7.93E-10 (SI current))
    network_L5bPyrCellHayEtAl2011 (Type: networkWithTemperature:  temperature=279.45 (SI temperature))
    sim1 (Type: Simulation:  length=3.0 (SI time) step=2.5E-5 (SI time))


    This NEURON file has been generated by org.neuroml.export (see https://github.com/NeuroML/org.neuroml.export)
         org.neuroml.export  v1.9.0
         org.neuroml.model   v1.9.0
         jLEMS               v0.10.7

'''

import neuron

import time
import datetime
import sys

import hashlib
h = neuron.h
h.load_file("nrngui.hoc")

h("objref p")
h("p = new PythonObject()")

class NeuronSimulation():

    def __init__(self, tstop, dt, seed=123456789):

        print("\n    Starting simulation in NEURON of %sms generated from NeuroML2 model...\n"%tstop)

        self.setup_start = time.time()
        self.seed = seed
        import socket
        self.report_file = open('simulator.props','w')
        print('Simulator version:  %s'%h.nrnversion())
        self.report_file.write('# Report of running simulation with %s\n'%h.nrnversion())
        self.report_file.write('Simulator=NEURON\n')
        self.report_file.write('SimulatorVersion=%s\n'%h.nrnversion())

        self.report_file.write('SimulationFile=%s\n'%__file__)
        self.report_file.write('PythonVersion=%s\n'%sys.version.replace('\n',' '))
        print('Python version:     %s'%sys.version.replace('\n',' '))
        self.report_file.write('NeuroMLExportVersion=1.9.0\n')
        self.report_file.write('SimulationSeed=%s\n'%self.seed)
        self.report_file.write('Hostname=%s\n'%socket.gethostname())
        self.randoms = []
        self.next_global_id = 0  # Used in Random123 classes for elements using random(), etc. 

        self.next_spiking_input_id = 0  # Used in Random123 classes for elements using random(), etc. 

        '''
        Adding simulation Component(id=sim1 type=Simulation) of network/component: network_L5bPyrCellHayEtAl2011 (Type: networkWithTemperature:  temperature=279.45 (SI temperature))
        
        '''

        # Temperature used for network: 279.45 K
        h.celsius = 279.45 - 273.15

        # ######################   Population: CellGroup_1
        print("Population CellGroup_1 contains 1 instance(s) of component: L5PC of type: cell")

        print("Setting the default initial concentrations for ca (used in L5PC) to 5.0E-5 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 5.0E-5")
        h("cao0_ca_ion = 2.0")

        print("Setting the default initial concentrations for ca (used in L5PC) to 5.0E-5 mM (internal), 2.0 mM (external)")
        h("cai0_ca_ion = 5.0E-5")
        h("cao0_ca_ion = 2.0")

        h.load_file("L5PC.hoc")
        a_CellGroup_1 = []
        h("{ n_CellGroup_1 = 1 }")
        h("objectvar a_CellGroup_1[n_CellGroup_1]")
        for i in range(int(h.n_CellGroup_1)):
            h("a_CellGroup_1[%i] = new L5PC()"%i)
            h("access a_CellGroup_1[%i].soma_0"%i)

            self.next_global_id+=1

        h("{ a_CellGroup_1[0].position(0.0, 0.0, 0.0) }")

        h("proc initialiseV_CellGroup_1() { for i = 0, n_CellGroup_1-1 { a_CellGroup_1[i].set_initial_v() } }")
        h("objref fih_CellGroup_1")
        h('{fih_CellGroup_1 = new FInitializeHandler(0, "initialiseV_CellGroup_1()")}')

        h("proc initialiseIons_CellGroup_1() { for i = 0, n_CellGroup_1-1 { a_CellGroup_1[i].set_initial_ion_properties() } }")
        h("objref fih_ion_CellGroup_1")
        h('{fih_ion_CellGroup_1 = new FInitializeHandler(1, "initialiseIons_CellGroup_1()")}')

        print("Processing 1 input lists")

        # ######################   Input List: Input_0
        # Adding single input: Component(id=0 type=input)
        h("objref Input_0_0")
        h("a_CellGroup_1[0].soma_0 { Input_0_0 = new Input_0(0.024999658) } ")

        print("Finished processing 1 input lists")

        trec = h.Vector()
        trec.record(h._ref_t)

        h.tstop = tstop

        h.dt = dt

        h.steps_per_ms = 1/h.dt

        # ######################   Display: self.display_CellGroup_1_v
        self.display_CellGroup_1_v = h.Graph(0)
        self.display_CellGroup_1_v.size(0,h.tstop,-80.0,50.0)
        self.display_CellGroup_1_v.view(0, -80.0, h.tstop, 130.0, 80, 330, 330, 250)
        h.graphList[0].append(self.display_CellGroup_1_v)
        # Line, plotting: CellGroup_1/0/L5PC/0/v
        self.display_CellGroup_1_v.addexpr("a_CellGroup_1[0].soma_0.v(0.024999658)", "a_CellGroup_1[0].soma_0.v(0.024999658)", 1, 1, 0.8, 0.9, 2)
        # Line, plotting: CellGroup_1/0/L5PC/2363/v
        self.display_CellGroup_1_v.addexpr("a_CellGroup_1[0].apic_36.v(0.96349317)", "a_CellGroup_1[0].apic_36.v(0.96349317)", 2, 1, 0.8, 0.9, 2)
        # Line, plotting: CellGroup_1/0/L5PC/2313/v
        self.display_CellGroup_1_v.addexpr("a_CellGroup_1[0].apic_36.v(0.038759712)", "a_CellGroup_1[0].apic_36.v(0.038759712)", 3, 1, 0.8, 0.9, 2)



        # ######################   File to save: CellGroup_1_0.0.dat (CellGroup_1_v_OF)
        # Column: CellGroup_1/0/L5PC/0/v
        h(' objectvar v_v_CellGroup_1_v_OF ')
        h(' { v_v_CellGroup_1_v_OF = new Vector() } ')
        h(' { v_v_CellGroup_1_v_OF.record(&a_CellGroup_1[0].soma_0.v(0.024999658)) } ')
        h.v_v_CellGroup_1_v_OF.resize((h.tstop * h.steps_per_ms) + 1)

        # ######################   File to save: CellGroup_1_0.2313.dat (CellGroup_1_v_2_OF)
        # Column: CellGroup_1/0/L5PC/2313/v
        h(' objectvar v_v_CellGroup_1_v_2_OF ')
        h(' { v_v_CellGroup_1_v_2_OF = new Vector() } ')
        h(' { v_v_CellGroup_1_v_2_OF.record(&a_CellGroup_1[0].apic_36.v(0.038759712)) } ')
        h.v_v_CellGroup_1_v_2_OF.resize((h.tstop * h.steps_per_ms) + 1)

        # ######################   File to save: time.dat (time)
        # Column: time
        h(' objectvar v_time ')
        h(' { v_time = new Vector() } ')
        h(' { v_time.record(&t) } ')
        h.v_time.resize((h.tstop * h.steps_per_ms) + 1)

        # ######################   File to save: CellGroup_1_0.2363.dat (CellGroup_1_v_1_OF)
        # Column: CellGroup_1/0/L5PC/2363/v
        h(' objectvar v_v_CellGroup_1_v_1_OF ')
        h(' { v_v_CellGroup_1_v_1_OF = new Vector() } ')
        h(' { v_v_CellGroup_1_v_1_OF.record(&a_CellGroup_1[0].apic_36.v(0.96349317)) } ')
        h.v_v_CellGroup_1_v_1_OF.resize((h.tstop * h.steps_per_ms) + 1)

        self.initialized = False

        self.sim_end = -1 # will be overwritten

        setup_end = time.time()
        self.setup_time = setup_end - self.setup_start
        print("Setting up the network to simulate took %f seconds"%(self.setup_time))

        h.nrncontrolmenu()


    def run(self):

        self.initialized = True
        sim_start = time.time()
        print("Running a simulation of %sms (dt = %sms; seed=%s)" % (h.tstop, h.dt, self.seed))

        try:
            h.run()
        except Exception as e:
            print("Exception running NEURON: %s" % (e))
            return


        self.sim_end = time.time()
        self.sim_time = self.sim_end - sim_start
        print("Finished NEURON simulation in %f seconds (%f mins)..."%(self.sim_time, self.sim_time/60.0))

        try:
            self.save_results()
        except Exception as e:
            print("Exception saving results of NEURON simulation: %s" % (e))
            return


    def advance(self):

        if not self.initialized:
            h.finitialize()
            self.initialized = True

        h.fadvance()


    ###############################################################################
    # Hash function to use in generation of random value
    # This is copied from NetPyNE: https://github.com/Neurosim-lab/netpyne/blob/master/netpyne/simFuncs.py
    ###############################################################################
    def _id32 (self,obj): 
        return int(hashlib.md5(obj.encode('utf-8')).hexdigest()[0:8],16)  # convert 8 first chars of md5 hash in base 16 to int


    ###############################################################################
    # Initialize the stim randomizer
    # This is copied from NetPyNE: https://github.com/Neurosim-lab/netpyne/blob/master/netpyne/simFuncs.py
    ###############################################################################
    def _init_stim_randomizer(self,rand, stimType, gid, seed): 
        #print("INIT STIM  %s; %s; %s; %s"%(rand, stimType, gid, seed))
        rand.Random123(self._id32(stimType), gid, seed)


    def save_results(self):

        print("Saving results at t=%s..."%h.t)

        if self.sim_end < 0: self.sim_end = time.time()

        self.display_CellGroup_1_v.exec_menu("View = plot")

        # ######################   File to save: time.dat (time)
        py_v_time = [ t/1000 for t in h.v_time.to_python() ]  # Convert to Python list for speed...

        f_time_f2 = open('time.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_time_f2.write('%f'% py_v_time[i])  # Save in SI units...
        f_time_f2.close()
        print("Saved data to: time.dat")

        # ######################   File to save: CellGroup_1_0.0.dat (CellGroup_1_v_OF)
        py_v_v_CellGroup_1_v_OF = [ float(x  / 1000.0) for x in h.v_v_CellGroup_1_v_OF.to_python() ]  # Convert to Python list for speed, variable has dim: voltage

        f_CellGroup_1_v_OF_f2 = open('CellGroup_1_0.0.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_CellGroup_1_v_OF_f2.write('%e\t%e\t\n' % (py_v_time[i], py_v_v_CellGroup_1_v_OF[i], ))
        f_CellGroup_1_v_OF_f2.close()
        print("Saved data to: CellGroup_1_0.0.dat")

        # ######################   File to save: CellGroup_1_0.2313.dat (CellGroup_1_v_2_OF)
        py_v_v_CellGroup_1_v_2_OF = [ float(x  / 1000.0) for x in h.v_v_CellGroup_1_v_2_OF.to_python() ]  # Convert to Python list for speed, variable has dim: voltage

        f_CellGroup_1_v_2_OF_f2 = open('CellGroup_1_0.2313.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_CellGroup_1_v_2_OF_f2.write('%e\t%e\t\n' % (py_v_time[i], py_v_v_CellGroup_1_v_2_OF[i], ))
        f_CellGroup_1_v_2_OF_f2.close()
        print("Saved data to: CellGroup_1_0.2313.dat")

        # ######################   File to save: CellGroup_1_0.2363.dat (CellGroup_1_v_1_OF)
        py_v_v_CellGroup_1_v_1_OF = [ float(x  / 1000.0) for x in h.v_v_CellGroup_1_v_1_OF.to_python() ]  # Convert to Python list for speed, variable has dim: voltage

        f_CellGroup_1_v_1_OF_f2 = open('CellGroup_1_0.2363.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_CellGroup_1_v_1_OF_f2.write('%e\t%e\t\n' % (py_v_time[i], py_v_v_CellGroup_1_v_1_OF[i], ))
        f_CellGroup_1_v_1_OF_f2.close()
        print("Saved data to: CellGroup_1_0.2363.dat")

        save_end = time.time()
        save_time = save_end - self.sim_end
        print("Finished saving results in %f seconds"%(save_time))

        self.report_file.write('StartTime=%s\n'%datetime.datetime.fromtimestamp(self.setup_start).strftime('%Y-%m-%d %H:%M:%S'))
        self.report_file.write('SetupTime=%s\n'%self.setup_time)
        self.report_file.write('RealSimulationTime=%s\n'%self.sim_time)
        self.report_file.write('SimulationSaveTime=%s\n'%save_time)
        self.report_file.close()

        print("Saving report of simulation to %s"%('simulator.props'))

        print("Done")

if __name__ == '__main__':

    ns = NeuronSimulation(tstop=3000.0, dt=0.025, seed=123456789)

    ns.run()

