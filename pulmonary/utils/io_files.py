"""
   Copyright 2015 University of Auckland

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import os


def get_default_geometry_path(filename, patientid, protocal):
    """
    Return the default geometry path. This path is expected to be
    a sibling directory of the the main files directory.
    :param filename:
    :return: the absolute path to the geometry file.
    """
    #file_location = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    #full_path = os.path.abspath(os.path.join(file_location, '..', 'geometries', filename))
    full_path = '/home/ydon868/Desktop/VentilationStudy'
    full_path = os.path.join(full_path, patientid, protocal, filename)
    return full_path


def get_default_output_path(filename, patientid, protocal):
    """
    Return the default output path for the given filename, this is the current working directory.
    :param filename:
    :return: the absolute path to the output file
    """
    #full_path = os.path.abspath(os.path.join(os.getcwd(), filename))
    full_path = '/home/ydon868/Desktop/VentilationStudy'
    folder_path = os.path.join(full_path,patientid,protocal,'Output_test')
    full_path = os.path.join(full_path, patientid, protocal, 'Output_test', filename)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return full_path

def getFinalNumber(lineString, numType):
    if numType == "int":
        intNum = int(lineString.split(":",1)[1]);
        return intNum;
    elif numType == "2int":
        intString = lineString.split(":",1)[1];
        a,b = intString.split();
        node1 = int(a);
        node2 = int(b);
        return node1,node2;
    elif numType == "float":
        floatNum = float(lineString.split(":",1)[1])
        return floatNum


