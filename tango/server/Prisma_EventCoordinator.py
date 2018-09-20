#!/usr/bin/env python
# -*- coding:utf-8 -*-


# ############################################################################
#  license :
# ============================================================================
#
#  File :        Prisma_EventCoordinator.py
#
#  Project :     
#
# This file is part of Tango device class.
# 
# Tango is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Tango is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Tango.  If not, see <http://www.gnu.org/licenses/>.
# 
#
#  $Author :      cosimo.volpicelli$
#
#  $Revision :    $
#
#  $Date :        $
#
#  $HeadUrl :     $
# ============================================================================
#            This file is generated by POGO
#     (Program Obviously used to Generate tango Object)
# ############################################################################

__all__ = ["Prisma_EventCoordinator", "Prisma_EventCoordinatorClass", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
# Add additional import
#----- PROTECTED REGION ID(Prisma_EventCoordinator.additionnal_import) ENABLED START -----#

#----- PROTECTED REGION END -----#	//	Prisma_EventCoordinator.additionnal_import

# Device States Description
# No states for this device


class Prisma_EventCoordinator (PyTango.Device_4Impl):
    """"""
    
    # -------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(Prisma_EventCoordinator.global_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	Prisma_EventCoordinator.global_variables

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        Prisma_EventCoordinator.init_device(self)
        #----- PROTECTED REGION ID(Prisma_EventCoordinator.__init__) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Prisma_EventCoordinator.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(Prisma_EventCoordinator.delete_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Prisma_EventCoordinator.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        #----- PROTECTED REGION ID(Prisma_EventCoordinator.init_device) ENABLED START -----#
        db = PyTango.Database()
        dict = db.get_device_property(self.get_name(), "ManagedDeviceList")
        cameraCount = db.get_device_property(self.get_name(), "CameraCount")
        print(cameraCount)
        timeBetweenEvents = db.get_device_property(self.get_name(), "TimeBetweenEvents")
        print(timeBetweenEvents)
        dict = db.get_device_property(self.get_name(), "ManagedDeviceList")
        self.ManagedDeviceList = dict["ManagedDeviceList"]
        print("DEVICE LIST", self.ManagedDeviceList)
        #dev = PyTango.DeviceProxy('prisma/event/it01001')
        #print(dev.state)
        for device in self.ManagedDeviceList:
            print("DEVICE",device)
            try:
                dev = PyTango.DeviceProxy(device)  # .split('\n')[0])
                print("AAAAAAA")#, dev.state)
                dev.subscribe_event("NewEvent", PyTango.EventType.CHANGE_EVENT, self.HandleEvent)
            except Exception  :
                print("str(e)")
        #----- PROTECTED REGION END -----#	//	Prisma_EventCoordinator.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(Prisma_EventCoordinator.always_executed_hook) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Prisma_EventCoordinator.always_executed_hook

    # -------------------------------------------------------------------------
    #    Prisma_EventCoordinator read/write attribute methods
    # -------------------------------------------------------------------------
    
    
    
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(Prisma_EventCoordinator.read_attr_hardware) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Prisma_EventCoordinator.read_attr_hardware


    # -------------------------------------------------------------------------
    #    Prisma_EventCoordinator command methods
    # -------------------------------------------------------------------------
    
    def HandleEvent(self, argin):
        """ 
        :param argin: 
        :type argin: PyTango.DevString
        """
        self.debug_stream("In HandleEvent()")
        #----- PROTECTED REGION ID(Prisma_EventCoordinator.HandleEvent) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Prisma_EventCoordinator.HandleEvent
        

    #----- PROTECTED REGION ID(Prisma_EventCoordinator.programmer_methods) ENABLED START -----#
        #db = PyTango.Database()
        #dict = db.get_device_property(self.get_name(), "ManagedDeviceList")
        #self.ManagedDeviceList = dict["ManagedDeviceList"]
        #print("DEVICE LIST", self.ManagedDeviceList)
#        print("PPPP")
        if not argin.attr_value is None:
#              print("POLLO" ,argin)
#        print(type(argin))
#              print(argin.attr_value)
              print("EVENT",argin.attr_value.value)
              print("DEVICE",argin.device)
    #----- PROTECTED REGION END -----#	//	Prisma_EventCoordinator.programmer_methods

class Prisma_EventCoordinatorClass(PyTango.DeviceClass):
    # -------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(Prisma_EventCoordinator.global_class_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	Prisma_EventCoordinator.global_class_variables


    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
        'CameraCount':
            [PyTango.DevLong, 
            "Minimum number of cameras in order to detect meteor event",
            [2]],
        'TimeBetweenEvents':
            [PyTango.DevLong, 
            "Time in seconds between events detected from different cameras",
            [5]],
        'WaitingTimeToAnalisys':
            [PyTango.DevLong, 
            "How much time, in minutes, have to wait before start with analisys if there are more then CameraCounter value",
            [10]],
        'ManagedDeviceList':
            [PyTango.DevVarStringArray, 
            "List of all Managed device handle from this coordinator device",
            [] ],
        }


    #    Command definitions
    cmd_list = {
        'HandleEvent':
            [[PyTango.DevString, "none"],
            [PyTango.DevVoid, "none"]],
        }


    #    Attribute definitions
    attr_list = {
        }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(Prisma_EventCoordinatorClass, Prisma_EventCoordinator, 'Prisma_EventCoordinator')
        #----- PROTECTED REGION ID(Prisma_EventCoordinator.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Prisma_EventCoordinator.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

if __name__ == '__main__':
    main()
